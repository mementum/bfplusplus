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

import bfpy
import httxlib

import threadbase
from util import Generic, Message

import time


class ThreadCurrentBets(threadbase.ThreadBase):

    def __init__(self):
        self.exchanges = [bfpy.ExchangeUK, bfpy.ExchangeAus]
        threadbase.ThreadBase.__init__(self, 'CurrentBets', None, None, useBF=False)
        self.timeout = None


    def runAction(self, message):
        if not message.timeout:
            self.timeout = None
            return None

        self.timeout = message.timeout

        thMisc = threadbase.ThreadBase.threadManager['Misc']
        for exchange in self.exchanges:
            miscMsg = Message(action='getCurrentBets',
                              exchangeId=exchange)
            thMisc.passMessage(miscMsg)

        return None


class ThreadAccountFunds(threadbase.ThreadBase):

    def __init__(self):
        self.exchanges = [bfpy.ExchangeUK, bfpy.ExchangeAus]
        threadbase.ThreadBase.__init__(self, 'AccountFunds', None, None, useBF=False)
        self.timeout = None


    def runAction(self, message):
        if not message.timeout:
            self.timeout = None
            return None

        self.timeout = message.timeout

        thMisc = threadbase.ThreadBase.threadManager['Misc']
        for exchange in self.exchanges:

            miscMsg = Message(action='getAccountFunds',
                              exchangeId=exchange)
            thMisc.passMessage(miscMsg)

        return None


class ThreadAllMarkets(threadbase.ThreadBase):

    def __init__(self):
        threadbase.ThreadBase.__init__(self, 'AllMarkets', None, None, useBF=False)
        self.timeout = None

        self.timeLast = 0
        self.exchanges = [bfpy.ExchangeUK, bfpy.ExchangeAus]
        self.maxExchanges = len(self.exchanges)
        self.lastExchange = self.maxExchanges - 1


    def runAction(self, message):
        if not message.timeout:
            self.timeout = None
            return None

        self.timeout = message.timeout / float(self.maxExchanges)
        thMisc = threadbase.ThreadBase.threadManager['Misc']

        # Fetch data from both exchanges on first run
        if not self.timeLast:
            self.timeLast = time.clock()
            for exchangeId in self.exchanges:
                miscMsg = Message(action='getAllMarkets')
                miscMsg.exchangeId = exchangeId
                thMisc.passMessage(miscMsg)
            return None

        timeNow = time.clock()
        timeSpan = timeNow - self.timeLast

        if timeSpan < self.timeout:
            # Time gone is less than set timeout
            # re-set timeout to the remaining time
            # and go
            self.timeout -= timeSpan
            return None

        # the elapsed time is greater or equal than timeout
        self.timeLast = timeNow

	miscMsg = Message(action='getAllMarkets')
        self.lastExchange += 1
        if self.lastExchange == self.maxExchanges:
            self.lastExchange = 0
        miscMsg.exchangeId = self.exchanges[self.lastExchange]
        thMisc.passMessage(miscMsg)

        return None


class ThreadMulti(threadbase.ThreadBase):
    def __init__(self, notifyFrame, function, pyEventId, parent, index, loginthread=False, version=None):
        threadbase.ThreadBase.__init__(self, 'Multi' + str(index),
                                       notifyFrame, function,
                                       pyEventId=pyEventId,
                                       loginthread=loginthread,
                                       version=version)
        self.parent = parent


    def runAction(self, message):
        try:
            return self.runSubAction(message)
        except:
            # re-raise any exception
            raise
        finally:
            # good or bad --- reinsert ourselves in the threadpool
            self.parent.restoreQueue(self)

        
    def runSubAction(self, message):
        self.action = message.action

        if message.action == 'runnerActionBitmap':
            bftransport = self.bfClient.transport
            httxmanager = bftransport.httxmanager

            baseurlUK = 'http://uk.site.sports.betfair.com/betting/LoadRunnerInfoChartAction.do?marketId=%d&selectionId=%d&asianLineId=%d'
            baseurlAus = 'http://au.site.sports.betfair.com/betting/LoadRunnerInfoChartAction.do?marketId=%d&selectionId=%d&asianLineId=%d'

            if message.marketTuple.exchangeId == bfpy.ExchangeUK:
                baseurl = baseurlUK
            else:
                baseurl = baseurlAus

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3',
                }

            marketId = message.marketTuple.marketId
            url = baseurl % (marketId, message.selectionId, message.asianLineId)

            if message.inverseAxis:
                url += '&logarithmic=true'

            httxreq = httxlib.HttxRequest(url, headers=headers)
            httxresp = httxmanager.urlopen(httxreq)

            message.response = httxresp.body

        elif message.action == 'runnerActionTradedVolume':
            self.addRequest(message.marketTuple.exchangeId, weight=1)
            message.response = self.bfClient.getMarketTradedVolumeCompressed(message.marketTuple.exchangeId,
                                                                             marketId=message.marketTuple.marketId)
        elif message.action == 'runnerActionCompletePrices':
            self.addRequest(message.marketTuple.exchangeId, weight=1)
            message.response = self.bfClient.getCompleteMarketPricesCompressed(message.marketTuple.exchangeId,
                                                                               marketId=message.marketTuple.marketId)

        elif message.action == 'seekUpdates':
            bftransport = self.bfClient.transport
            httxmanager = bftransport.httxmanager

            url = 'http://code.google.com/p/bfplusplus/wiki/FAQ'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3',
                }
            httxreq = httxlib.HttxRequest(url, headers=headers)
            httxresp = httxmanager.urlopen(httxreq)
            #print httxresp.body

            pos1 = httxresp.body.find('Version: ')
            pos1 += len('Version: ')
            pos2 = httxresp.body.find(' ', pos1)

            version = httxresp.body[pos1:pos2]
            message.response = version


        elif message.action == 'login':
            message.response = self.bfClient.login(username=message.username,
                                                   password=message.password,
                                                   productId=message.productId,
                                                   vendorSoftwareId=message.vendorSoftwareId)

            self.loginThread = False
        elif message.action == 'getAllCurrenciesV2':
            if self.bfClient.productId != bfpy.freeApiId:
                message.response = self.bfClient.getAllCurrenciesV2()

        elif message.action == 'getEvents':
            message.response = self.bfClient.getEvents(eventParentId=message.eventId)

        elif message.action == 'getMarket':
            message.response = self.bfClient.getMarket(message.marketTuple.exchangeId,
                                                       marketId=message.marketTuple.marketId)

        elif message.action == 'getAccountFunds':
            message.response = self.bfClient.getAccountFunds(message.exchangeId)

        elif message.action == 'transferFunds':
            message.response = self.bfClient.transferFunds(sourceWalletId=message.sourceWalletId,
                                                           targetWalletId=message.targetWalletId,
                                                           amount=message.amount)
        elif message.action == 'getCurrentBets':
            # Issue two different requests, each with its own weight
            self.addRequest(message.exchangeId, weight=5)
            mResponse = self.bfClient.getCurrentBets(message.exchangeId, betStatus='M')
            self.addRequest(message.exchangeId, weight=5)
            uResponse = self.bfClient.getCurrentBets(message.exchangeId, betStatus='U')

            # Mix and order the results
            mResponse.totalRecordCount += uResponse.totalRecordCount
            mResponse.bets.extend(uResponse.bets)
            mResponse.bets.sort(key=operator.attrgetter('betId', 'betStatus'))

            message.response = mResponse

        elif message.action == 'getAllMarkets':
            message.response = self.bfClient.getAllMarkets(message.exchangeId)

            dataMarket = dict()
            for marketItem in message.response.marketData:
                dataMarket[marketItem.marketId] = marketItem
            message.response.dataMarket = dataMarket

        elif message.action == 'placeBets':
            message.response = self.bfClient.placeBets(message.marketTuple.exchangeId,
                                                       bets=message.placeBets,
                                                       _nonIPRePlace=False)

        elif message.action == 'cancelBetsByMarket':
            message.response = self.bfClient.cancelBetsByMarket(message.marketTuple.exchangeId,
                                                                markets=[message.marketTuple.marketId])
        elif message.action == 'cancelBets':
            message.response = self.bfClient.cancelBets(message.marketTuple.exchangeId,
                                                        bets=message.cancelBets)

        elif message.action == 'updateBets':
            message.response = self.bfClient.updateBets(message.marketTuple.exchangeId,
                                                        bets=message.updateBets)
        else:
            return None

        return message


class ThreadMisc(threadbase.ThreadBase):

    def __init__(self, notifyFrame, function, proxydict=None, numThreads=5, version=None):
        self.numThreads = numThreads
        self.thQueue = Queue.Queue()
        self.thQueueBetting = Queue.Queue(0)
        self.delegate = True

        threadbase.ThreadBase.proxydict = dict()
        if proxydict is not None:
            threadbase.ThreadBase.proxydict = proxydict

        # To create the master bfClient object quietly
        self.masterLock.acquire()

        self.timeout = None

        threadbase.ThreadBase.__init__(self, 'Misc', notifyFrame, function, useBF=False, version=None)

        th = ThreadMulti(self.notifyFrame, self.function, self.pyEventId, self, -1,
                         loginthread=True, version=version)
        self.thQueue.put(th)


    def startSubThreads(self):
        self.loginThread = False
        
        for i in xrange(self.numThreads):
            th = ThreadMulti(self.notifyFrame, self.function, self.pyEventId, self, i)
            self.thQueue.put(th)

        self.thQueueBetting = Queue.Queue(3)
        for i in xrange(3):
            th = ThreadMulti(self.notifyFrame, self.function, self.pyEventId, self, i)
            self.thQueueBetting.put(th)

        miscMsg = Message(action='getAllCurrenciesV2')
        self.passMessage(miscMsg)


    def restoreQueue(self, th):
        try:
            # try to keep the betting queue loaded
            # unless the thread is the main login thread
            if not th.loginthread:
                self.thQueueBetting.put(th, block=False)
            else:
                raise Queue.Full
        except Queue.Full:
            # else fill the standard queue
            self.thQueue.put(th)


    def runAction(self, message):
        if message.action in ('placeBets', 'cancelBets', 'updateBets'):
            q = self.thQueueBetting
        else:
            q = self.thQueue

        try:
            th = q.get(block=False)
        except Queue.Empty:
            th = self.thQueue.get(block=True)

        th.passMessage(message)
        return None


class ThreadGetMarketPrices(threadbase.ThreadBase):

    def __init__(self, notifyFrame, function, pyEventId=None):
        
        threadbase.ThreadBase.__init__(self, 'GetMarketPrices', notifyFrame, function)
        self.timeout = 1.0


    def runAction(self, message):
        if not message.marketTuple.marketId:
            self.doBlock = True
            return None

        self.doBlock = False
        self.addRequest(message.marketTuple.exchangeId, weight=1)
        if not message.ladder:
            message.response = self.bfClient.getMarketPricesCompressed(message.marketTuple.exchangeId,
                                                                       marketId=message.marketTuple.marketId,
                                                                       _virtualPrices=message.virtualPrices)
        else:
            message.response = self.bfClient.getCompleteMarketPricesCompressed(message.marketTuple.exchangeId,
                                                                               marketId=message.marketTuple.marketId)
        return message


class ThreadGetMarketProfitAndLoss(threadbase.ThreadBase):

    def __init__(self, notifyFrame, function):
        threadbase.ThreadBase.__init__(self, 'GetMarketProfitAndLoss', notifyFrame, function)
        self.timeout = 1.0
    

    def runAction(self, message):
        if not message.marketTuple.marketId:
            self.doBlock = True
            return None

        self.doBlock = False
        if not hasattr(message, 'source'):
            self.addRequest(message.marketTuple.exchangeId, weight=1)
            message.response = self.bfClient.getMarketProfitAndLoss(message.marketTuple.exchangeId,
                                                                    marketId=message.marketTuple.marketId)
        else:
            message.response = message.source.get(block=True)
        return message


class ThreadGetMUBets(threadbase.ThreadBase):
    def __init__(self, notifyFrame, function):
        threadbase.ThreadBase.__init__(self, 'GetMUbets', notifyFrame, function)
        self.timeout = 1.0
    

    def runAction(self, message):
        if not message.marketTuple.marketId:
            self.doBlock = True
            return None

        self.doBlock = False
        self.addRequest(message.marketTuple.exchangeId, weight=1)
        message.response = self.bfClient.getMUBets(message.marketTuple.exchangeId,
                                                   marketId=message.marketTuple.marketId)
        return message


import operator

class ThreadFavs(threadbase.ThreadBase):

    def __init__(self, notifyFrame, function):
        threadbase.ThreadBase.__init__(self, 'Favourites', notifyFrame, function, useBF=False)

        # Wait forever for messages
        self.timeout = None

        # Wait nothing after new message
        self.dontSleepOnMessage = True


    def runAction(self, message):
        patternSets = message.patterns
        favMarkets = list()

        for exchangeId in message.marketData.keys():
            # browse a copy of the list, not the list itself, because
            # the list may be updated by other thread and then the GUI
            for marketItem in message.marketData[exchangeId][:]:
                for patternSet in patternSets:
                    marketNames = patternSet[0]
                    posMatches = patternSet[1]
                    negMatches = patternSet[2]

                    if not self.patternMatcher(marketItem.menuPath, posMatches, positiveMatch=True):
                        continue

                    if not self.patternMatcher(marketItem.menuPath, negMatches, positiveMatch=False):
                        continue

                    if not self.patternMatcher(marketItem.marketName, marketNames, positiveMatch=True, orComp=True):
                        continue
                
                    marketItem.lastMenuPart = marketItem.menuPathParts[-1]
                    favMarkets.append(marketItem)
                    break

        favMarkets.sort(key=operator.attrgetter('marketTime', 'lastMenuPart', 'marketName'))

        message.response = Generic()
        message.response.favMarkets = favMarkets
        return message


    def patternMatcher(self, text, patterns, positiveMatch=True, orComp=False):
        if not orComp:
            numToMatch = len(patterns)
        else:
            numToMatch = 1

        matchCount = 0
        for pattern in patterns:
            if isinstance(pattern, basestring):
                if pattern in text:
                    if positiveMatch:
                        matchCount += 1
                        if orComp:
                            return True
                    else:
                        return False
            elif isinstance(pattern, list):
                for orPattern in pattern:
                    if orPattern in text:
                        if positiveMatch:
                            matchCount += 1
                            if orComp:
                                return True
                            break
                        else:
                            return False

        if matchCount == numToMatch or not positiveMatch:
            return True

        return False


class ThreadSearch(threadbase.ThreadBase):

    def __init__(self, notifyFrame, function):
        threadbase.ThreadBase.__init__(self, 'Search', notifyFrame, function, useBF=False)

        # Wait forever for messages
        self.timeout = None

        # Wait nothing after new message
        self.dontSleepOnMessage = True


    def runAction(self, message):
        search = message.search.lower()
        favMarkets = list()
        searchCache = list()

        for exchangeId in message.marketData.keys():
            # browse a copy of the list, not the list itself, because
            # the list may be updated by other thread and then the GUI
            for marketItem in message.marketData[exchangeId][:]:
                if search in marketItem.menuPath.lower() or search in marketItem.marketName.lower():
                    menuCache = marketItem.menuPathParts[:-1]
                    if menuCache in searchCache:
                        continue
                    searchCache.append(menuCache)
                    marketItem.lastMenuPart = marketItem.menuPathParts[-1]
                    favMarkets.append(marketItem)
                    
        favMarkets.sort(key=operator.attrgetter('marketTime', 'lastMenuPart', 'marketName'))

        message.response = Generic()
        message.response.favMarkets = favMarkets
        return message
