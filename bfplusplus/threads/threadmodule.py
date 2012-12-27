#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of Bfplusplus
#
# Bfplusplus is a graphical interface to the Betfair Betting Exchange
# Copyright (C) 2010 Daniel Rodriguez (aka Daniel Rodriksson)
# Copyright (C) 2011 Sensible Odds Ltd.
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/bfplusplus/
#
# Bfplusplus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Bfplusplus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Bfplusplus. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import Queue
import threading
import time

import wx

from threadbase import ThreadPyEvent, EmptyMessage
from util import Message

printMessages = True

class ThreadModule(threading.Thread):
    prioExit = 0
    prioHeartBeat = 1
    prioPlayPause = 2
    prioTimeout = 3
    prioParams = 4
    prioRunners = 5
    prioMessage = 6
    prioOnPlaceBets = 7
    prioOnCancelBets = 8
    prioOnUpdateBets = 9
    prioOnGetAccountFunds = 10
    prioAction = 11

    def __init__(self, modId, mainmod, module, pyEventId, **kwargs):
        threading.Thread.__init__(self)

        self.modId = modId
        self.module = module
        self.mainmod = mainmod
        self.pyEventId= pyEventId
        self.kwargs = kwargs
        self.messageQueue = Queue.PriorityQueue()

        self.runners = list()

        self.timeout = None
        # Avoid Python waiting for this thread to terminate
        # self.daemon = True
        self.start()

    def invokeMethod(methodName, arg):
        try:
            method = getattr(self.dataProcessor, methodName)
            method(arg)
        except:
            pass

    def run(self):
        try:
            self.dataProcessor = self.module.DataProcessor(api=self, **self.kwargs)
        except Exception, e:
            if printMessages:
                print '------------------------------'
                print 'Exception starting data processor'
                print str(e)
                print '------------------------------'
            return

        # message = EmptyMessage()
        doPlay = False
        timeout = self.timeout
        timeSpan = None
        timeStart = time.clock()

        while True:
            if not doPlay:
                timeout = None

            timeStart = time.clock()
            try:
                prio, message = self.messageQueue.get(block=True, timeout=timeout)
                if prio == self.prioExit:
                    try:
                        if hasattr(self.dataProcessor, 'doExit'):
                            self.dataProcessor.doExit(message)
                    except:
                        pass
                    return
            except Queue.Empty:
                prio = self.prioHeartBeat

            except Exception, e:
                # We are blocking so there should be no exception
                # if one is found -> bail out
                if printMessages:
                    print '------------------------------'
                    print 'Exception waiting for message'
                    print str(e)
                    print 'Exiting'
                    print '------------------------------'
                return

            # Try action
            try:
                if prio == self.prioHeartBeat:
                    if hasattr(self.dataProcessor, 'heartBeat'):
                        self.dataProcessor.heartBeat()
                    timeout = self.timeout
                    continue
                elif prio == self.prioPlayPause:
                    doPlay = message.play
                    if doPlay:
                        timeout = self.timeout
                        if hasattr(self.dataProcessor, 'play'):
                            self.dataProcessor.play()
                    else:
                        if hasattr(self.dataProcessor, 'pause'):
                            self.dataProcessor.pause()
                    continue

                elif prio == self.prioParams:
                    if hasattr(self.dataProcessor, 'setParams'):
                        self.dataProcessor.setParams(message.setParams)

                        # Timeout may have been (re)set when setting the params
                        if self.messageQueue.qsize():
                            prio, message = self.messageQueue.get(block=True, timeout=None)
                            if prio != self.prioTimeout:
                                # if not timeout - put back into the queue for later processing
                                self.messageQueue.put((prio, message))
                                prio = self.prioParams

                elif prio == self.prioRunners:
                    self.runners = message
                elif prio == self.prioMessage:
                    if hasattr(self.dataProcessor, 'processData'):
                        self.dataProcessor.processData(message)
                elif prio == self.prioOnPlaceBets:
                    if hasattr(self.dataProcessor, 'onPlaceBets'):
                        self.dataProcessor.onPlaceBets(message)
                elif prio == self.prioOnCancelBets:
                    if hasattr(self.dataProcessor, 'onCancelBets'):
                        self.dataProcessor.onCancelBets(message)
                elif prio == self.prioOnUpdateBets:
                    if hasattr(self.dataProcessor, 'onUpdateBets'):
                        self.dataProcessor.onUpdateBets(message)
                elif prio == self.prioAction:
                    if hasattr(self.dataProcessor, 'doAction'):
                        self.dataProcessor.doAction(message)

                timeSpan = time.clock() - timeStart

                if prio == self.prioTimeout:
                    self.timeout = message.setTimeout
                    if self.timeout is not None:
                        timeout = self.timeout - timeSpan
                        if timeout < 0.0:
                            timeout = 0.0

                    else:
                        timeout = None
                    continue

                if timeout is not None:
                    timeout -= timeSpan
                    if timeout < 0.0:
                        timeout = 0.0

            except Exception, e:
                if printMessages:
                    print '------------------------------'
                    print 'Exception processing message'
                    print e
                    print '------------------------------'


    def passMessage(self, msg):
        self.messageQueue.put((self.prioMessage, msg))


    def play(self):
        message = self.createMessage()
        message.play = True
        self.messageQueue.put((self.prioPlayPause, message))


    def pause(self):
        message = self.createMessage()
        message.play = False
        self.messageQueue.put((self.prioPlayPause, message))


    def doExit(self, appExiting=False):
        self.messageQueue.put((self.prioExit, appExiting))


    def setTimeout(self, timeout):
        message = self.createMessage()
        if not timeout or timeout < 0.0:
            message.setTimeout = None
        else:
            message.setTimeout = timeout

        self.messageQueue.put((self.prioTimeout, message))


    def setParams(self, params):
        message = EmptyMessage()
        message.setParams = params
        self.messageQueue.put((self.prioParams, message))


    def getParams(self):
        if hasattr(self.dataProcessor, 'getParams'):
            return self.dataProcessor.getParams()

        return dict()


    def getActions(self):
        if hasattr(self.dataProcessor, 'getActions'):
            return self.dataProcessor.getActions()

        return dict()


    def doAction(self, actionId):
        self.messageQueue.put((self.prioAction, actionId))


    def setRunners(self, runners):
        self.messageQueue.put((self.prioRunners, runners))


    def getRunners(self):
        return self.runners


    def createMessage(self):
        return EmptyMessage()


    def modMessage(self, subAction, **kwargs):
        message = Message(action='module', subAction=subAction)
        message.exception = None
        message.response = Message()
        for name, value in kwargs.iteritems():
            setattr(message.response, name, value)
        self.sendMessage(message, self.pyEventId)


    def sendMessage(self, message, pyEventId):
        if self.mainmod:
            try:
                # The destination notifyFrame may not exist and therefore an exception may be raised
                wx.PostEvent(self.mainmod, ThreadPyEvent(pyEventId, message))
                return True
            except Exception, e:
                # print '%s/PostEvents: %s' % (self.oname, str(e))
                pass

        return False


    def logMessage(self, logMsg):
        message = Message(action='module', subAction='logMsg')
        message.exception = None
        message.response = Message()
        message.response.logMsg = logMsg
        self.sendMessage(message, self.pyEventId)


    def createMarketTuple(self, exchangeId, marketId):
        return self.mainmod.BfMarketTuple(exchangeId, marketId)


    def createEvent(self, eventId=-1, eventName=''):
        return self.mainmod.BfCreateEvent(eventId, eventName)


    def createMarket(self):
        return self.mainmod.BfCreateMarket()


    def createRunner(self):
        return self.mainmod.BfCreateRunner()

    def createMarketPrices(self):
        return self.mainmod.BfCreateMarketPrices()


    def createRunnerPrices(self):
        return self.mainmod.BfCreateRunnerPrices()


    def createPrice(self):
        return self.mainmod.BfCreatePrice()


    def createPlaceBet(self):
        return self.mainmod.BfCreatePlaceBet()


    def placeBets(self, marketTuple, placeBets, fillOrKill=False, fillOrKillTime=15):
        message = Message(action='module', subAction='placeBets')
        message.exception = None
        message.response = Message()
        message.response.marketTuple = marketTuple
        message.response.placeBets = placeBets
        message.response.fillOrKill = fillOrKill
        message.response.fillOrKillTime = fillOrKillTime
        message.response.modId = self.modId
        self.sendMessage(message, self.pyEventId)


    def onPlaceBets(self, betResults):
        self.messageQueue.put((self.prioOnPlaceBets, betResults))


    def createCancelBet(self):
        return self.mainmod.BfCreateCancelBet()


    def cancelBets(self, marketTuple, cancelBets):
        message = Message(action='module', subAction='cancelBets')
        message.exception = None
        message.response = Message()
        message.response.marketTuple = marketTuple
        message.response.cancelBets = cancelBets
        message.response.modId = self.modId
        self.sendMessage(message, self.pyEventId)


    def onCancelBets(self, betResults):
        self.messageQueue.put((self.prioOnCancelBets, betResults))


    def createUpdateBet(self):
        return self.mainmod.BfCreateUpdateBet()


    def updateBets(self, marketTuple, updateBets):
        message = Message(action='module', subAction='updateBets')
        message.exception = None
        message.response = Message()
        message.response.marketTuple = marketTuple
        message.response.updateBets = updateBets
        message.response.modId = self.modId
        self.sendMessage(message, self.pyEventId)


    def onUpdateBets(self, betResults):
        self.messageQueue.put((self.prioOnUpdateBets, betResults))


    def getAccountFunds(self, exchangeId):
        message = Message(action='module', subAction='getAccountFunds')
        message.exception = None
        message.response = Message()
        message.response.exchangeId = exchangeId
        message.response.modId = self.modId
        self.sendMessage(message, self.pyEventId)


    def onGetAccountFunds(self, accountFunds):
        self.messageQueue.put((self.prioOnGetAccountFunds, accountFunds))
