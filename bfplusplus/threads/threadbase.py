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

import copy
from collections import defaultdict
import Queue
import random
import threading
import time

import wx

import bfpy


class EmptyMessage(object):
    pass

class ThreadPyEvent(wx.PyEvent):
    def __init__(self, pyEventId, message=None):

        wx.PyEvent.__init__(self)
        self.SetEventType(pyEventId)
        self.message = message


class DataRequest(object):
    __slots__ = ['__weakref__', 'tstamp', 'weight']

    def __init__(self, tstamp, weight):
        self.tstamp = tstamp
        self.weight = weight


class DataCounter(object):

    def __init__(self, maxRequests=20):
        self.lock = threading.Lock()
        self.maxRequests = maxRequests
        self.reqs = list()
        self.weight = 0


    def add(self, weight):
        with self.lock:
            tnow = time.clock()

            while self.reqs:
                req = self.reqs[0]
                if tnow - req.tstamp > 1.0:
                    self.reqs.pop(0)
                    self.weight -= req.weight
                else:
                    break

            self.reqs.append(DataRequest(tnow, weight))
            self.weight += weight

            if self.weight > self.maxRequests:
                # All remaining requests happened within one second
                # see how much has to be waited until we may issue another
                # request
                excess = self.weight - self.maxRequests

                for req in self.reqs:
                    excess -= req.weight

                    if excess <= 0:
                        throttle = 1.0 - (tnow - req.tstamp) + 0.05
                        break

                # Execute the throttle with a small guard
                time.sleep(throttle)


class ThreadBase(threading.Thread):

    threadManager = dict()
    bfClientMaster = None
    defaultTimeout = 1.0
    masterLock = threading.Lock()
    proxydict = dict()
    dataCounter = defaultdict(DataCounter)

    def __init__(self, oname, notifyFrame, function, pyEventId=None, loginthread=False, useBF=True, version=None):

        self.timeout = None
        self.oname = oname
        self.action = ''

        threading.Thread.__init__(self)

        self.version = version
        self.loginthread = loginthread
        self.useBF = useBF
        self.doBlock = True
        self.dontSleepOnMessage = False

        self.bfCient = None

        if pyEventId is not None:
            self.pyEventId = pyEventId
        else:
            self.pyEventId = wx.NewId()
        self.notifyFrame = notifyFrame
        self.function = function
        self.messageQueue = Queue.Queue()
        self.timeQueue = Queue.Queue()
        # Connect the frame and its function to our "pyEventId"
        if self.notifyFrame:
            self.notifyFrame.Connect(wx.ID_ANY, wx.ID_ANY, self.pyEventId, self.function)

        self.threadManager[self.oname] = self

        if self.loginthread:
            self.loginRetry = False
        else:
            self.loginRetry = True

        self.daemon = True
        self.start()

    def addRequest(self, exchangeId, weight):
        # Using the BfPy internal data counter
        if False:
            ThreadBase.dataCounter[exchangeId].add(weight)

        
    @staticmethod
    def exitThreads():
        for th in ThreadBase.threadManager.itervalues():
            th.passMessage(None)

        for th in self.ThreadManager.itervalues():
            th.join()


    def passMessage(self, message):
        # self.messageQueue.put(copy.deepcopy(message))
        self.messageQueue.put(message)


    def run(self):
        if self.loginthread:
            ThreadBase.bfClientMaster = bfpy.BfClient(fullDirect=True, proxydict=ThreadBase.proxydict, maxRequests=20)
            self.bfClient = ThreadBase.bfClientMaster
            bftransport = self.bfClient.transport
            httxmanager = bftransport.httxmanager
            httxmanager.setuseragent('Bfplusplus %s' % self.version)
            # Locked in thMisc constructor
            self.masterLock.release()
        else:
            if self.useBF:
                with self.masterLock:
                    self.bfClient = ThreadBase.bfClientMaster.clone()

        message = EmptyMessage()
        doKeepAlive = False
        timeStart = time.clock()

        try:
            while True:
                # Do an initial (and later if needed) login
                while self.useBF and self.loginRetry:
                    try:
                        self.bfClient.login()
                        self.loginRetry = False
                        break

                    except (bfpy.BfTransportError, bfpy.BfBetfairError), e:
                        # Since we know we had good credentials, we will retry
                        # print "%s/Relogin exception %s:%s" % (self.oname, e.__class__.__name__, str(e))
                        time.sleep(15)

                    except Exception, e:
                        # Something very unexpected has happened
                        # print '%s/ReLogin: %s' % (self.oname, str(e))
                        return

                # Get Item for which the events have to be loaded
                # message = None
                try:
                    if self.loginthread:
                        timeout = None
                    elif self.useBF:
                        # to do a keepalive every 2-3 min
                        timeout = 120 + random.uniform(1, 60) # in seconds
                        # timeout = 5 + random.uniform(1, 2) # in seconds
                    else:
                        timeout = self.timeout

                    message = self.messageQueue.get(block=self.doBlock, timeout=timeout)
                    if message is None:
                        # Time to go
                        return

                    # Sleep if needed to avoid being throttled and we had a timeout
                    if  not self.dontSleepOnMessage and not self.doBlock:
                        self.doSleep(timeStart)

                except Queue.Empty:
                    if self.doBlock:
                        if self.useBF:
                            doKeepAlive = True
                    else:
                        self.doSleep(timeStart)

                except Exception, e:
                    # print '%s/Queue.get: %s' % (self.oname, str(e))
                    return
            
                # Try action or keepalive
                try:
                    if doKeepAlive:
                        result = self.bfClient.keepAlive()
                    else:
                        timeStart = time.clock()
                        result = self.runAction(message)

                    if result is None:
                        continue

                    message = result
                    message.exception = None

                except bfpy.BfApiError, e:
                    if e.response.header.errorCode == 'NO_SESSION':
                        self.loginRetry = True
                    # print '%s/RunAction Api Error (%s): %s' % (self.oname, self.action, str(e))
                    # continue

                    message.response = None
                    message.exception = e

                except (bfpy.BfTransportError, bfpy.BfBetfairError), e:
                    message.response = None
                    message.exception = e
                    # print '%s/RunAction Transport/Betfair Error (%s): %s' % (self.oname, self.action, str(e))

                except Exception, e:
                    message.response = None
                    message.exception = e
                    # print '%s/RunAction (%s): %s' % (self.oname, self.action, str(e))
                    # continue

                if doKeepAlive:
                    doKeepAlive = False
                    continue

                try:
                    # The destination frame may not exist and therefore an exception may be raised
                    wx.PostEvent(self.notifyFrame, ThreadPyEvent(self.pyEventId, message))
                except Exception, e:
                    # print '%s/PostEvents: %s' % (self.oname, str(e))
                    return
        except:
            pass

        return


    def doSleep(self, timeStart):
        timeGuard = 0.005
        timeEnd = time.clock()
        timeSpan = timeEnd - timeStart
        # add 0.01 guard to avoid THROTLE_EXCEEDED
        timeToSleep = self.timeout - timeSpan + timeGuard
        while timeToSleep > 0.0:
            timeBeforeWait = time.clock()
            try:
                newTimeout = self.timeQueue.get(block=True, timeout=timeToSleep)
            except Queue.Empty:
                break

            while self.timeQueue.qsize():
                newTimeout = self.timeQueue.get(block=True, timeout=None)
            self.timeout = newTimeout
            # We have received a new Timeout - Calculate if more has to be waited
            # or we may proceed
            timeoutElapsed = time.clock() - timeBeforeWait
            timeoutRemaining = timeToSleep - timeoutElapsed
            # This could be negative
            extraTimeout = newTimeout - (timeToSleep - timeGuard)
            timeToSleep = timeoutRemaining + extraTimeout + timeGuard
