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

from collections import namedtuple
from ConfigParser import ConfigParser as ConfigParser
import datetime
from gzip import GzipFile
import time

MarketTuple2 = namedtuple('MarketTuple2', ('exchangeId', 'marketId'))

class DataProcessor(object):

    num2Status = {0: 'ACTIVE', 1: 'SUSPENDED', 2: 'CLOSED'}

    marketInfoName = 'marketInfo'
    priceInfoName = 'priceInfo'

    def __init__(self, api, **kwargs):
        self.api = api
        self.marketDir = kwargs.get('marketDir', '.')
        self.separator = kwargs.get('separator', '')
        self.pyIdMarket = kwargs.get('pyIdMarket', -1)
        self.pyIdPrices = kwargs.get('pyIdPrices', -1)

        self.marketInfoFile = None
        self.priceInfoFile = None
        self.priceInfoFileOrig = None

        self.canPlay = True
        self.firstPrice = True

        self.readMarketInfo()


    def readMarketInfo(self):

        fileName = '%s/%s' % (self.marketDir, self.marketInfoName)
        try:
            self.marketInfoFile = open(fileName, 'rb')
        except Exception, e:
            self.api.logMessage('Stopping market playback. Error opening file %s: %s' % (fileName, str(e)))
            self.canPlay = False
            return

        self.api.logMessage('Starting playback.')

        self.config = ConfigParser()
        self.config.readfp(self.marketInfoFile)

        market = self.api.createMarket()
        market.eventHierarchy = eval(self.config.get('market', 'eventHierarchy'))
        market.licenceId = self.config.getint('market', 'licenceId')
        market.marketId = self.config.getint('market', 'marketId')
        self.marketId = market.marketId
        market.exchangeId = self.config.getint('market', 'exchangeId')
        self.exchangeId = market.exchangeId
        market.marketStatus = self.config.get('market', 'marketStatus')        
        # market.marketStatus = self.num2Status[marketStatus]
        marketTime = self.config.get('market', 'marketTime')
        # Default value
        market.marketTime = datetime.datetime.now()
        try:
            market.marketTime = datetime.datetime.strptime(marketTime, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            pass
        market.marketType = self.config.get('market', 'marketType')
        market.menuPath = self.config.get('market', 'menuPath')
        market.name = self.config.get('market', 'name')
        market.numberOfWinners = self.config.getint('market', 'numberOfWinners')
        market.parentEventId = self.config.getint('market', 'parentEventId')
        market.runnersMayBeAdded = self.config.getboolean('market', 'runnersMayBeAdded')
        market.timezone = self.config.get('market', 'timezone')
        market.marketDescription = self.config.get('market', 'marketDescription')
        # market.marketDescription = market.marketDescription.decode('utf-8', 'replace')
        market.marketDescription = market.marketDescription.decode('utf-8')
        market.runners = list()

        numRunners = self.config.getint('runners', 'len')
        for runnerIndex in xrange(numRunners):
            runnerSection = 'Runner %d' % runnerIndex
            runner = self.api.createRunner()
            runner.asianLineId = self.config.getint(runnerSection, 'asianLineId')
            runner.handicap = self.config.getfloat(runnerSection, 'handicap')
            runner.name = self.config.get(runnerSection, 'name')
            runner.selectionId = self.config.getint(runnerSection, 'selectionId')

            market.runners.append(runner)

        message = self.api.createMessage()
        message.exception = None
        message.action = 'getMarket'
        message.marketTuple = MarketTuple2(self.exchangeId, self.marketId)
        message.response = self.api.createMessage()
        message.expandEvents = False
        message.response.market = market
        message.response.play = True
        
        self.marketInfoFile.close()
        self.api.sendMessage(message, self.pyIdMarket)

        fileName = '%s/%s' % (self.marketDir, self.priceInfoName)
        try:
            self.priceInfoFileOrig = open('%s.gz' % fileName, 'rb')
            self.priceInfoFile = GzipFile(self.priceInfoName, fileobj=self.priceInfoFileOrig)
        except Exception, e:
            self.api.logMessage('Stopping market playback. Error opening file %s: %s' % (fileName, str(e)))
            self.canPlay = False
            return

        header = self.priceInfoFile.next()

        self.lastTimeClock = None
        self.api.setTimeout(1.0)


    def play(self):
        pass


    def pause(self):
        pass


    def getParams(self):
        pass


    def setParams(self, params):
        pass


    def doExit(self, appExiting=False):
        if not appExiting:
            self.api.logMessage('End of playback')

        if self.priceInfoFile:
            self.priceInfoFile.close()
            self.priceInfoFileOrig.close()


    def processData(self, message):
        pass


    def heartBeat(self):
        if not self.canPlay:
            return

        try:
            line = self.priceInfoFile.next()
            line = line.rstrip()
            if not line:
                raise StopIteration
        except StopIteration:
            self.api.logMessage('End of prices information. Stopping playback')
            self.canPlay = False
            self.api.setTimeout(None)
            return
        except Exception, e:
            self.api.logMessage('Error reading from file. Stopping playback')
            self.canPlay = False
            self.api.setTimeout(None)
            return

        if self.firstPrice or not self.separator:
            # try to find it out automagically
            index = 0
            while True and line[index] in '0123456789.':
                index += 1

            if index >= len(line):
                self.api.logMessage('Could not figure separator for prices file. Stopping playback')
                self.canPlay = False
                self.api.setTimeout(None)
                return

            separator = line[index]
            if separator != self.separator:
                self.api.logMessage('Changed separator from %s to %s' % (self.separator, separator))
                self.separator = separator

        self.firstPrice = False

        priceParts = line.split(self.separator)

        timeClock = float(priceParts[0])

        marketPrices = self.api.createMarketPrices()
        marketPrices.marketId = int(priceParts[1])
        marketStatus = int(priceParts[2])
        marketPrices.marketStatus = self.num2Status[marketStatus]
        marketPrices.delay = int(priceParts[3])
        marketPrices.numberOfWinners = int(priceParts[4])

        marketPrices.runnerPrices = list()
        numRunners = (len(priceParts) - 5) / 17 # 17 ???

        # parse & create runnerPrices
        baseIndex = 5
        for runnerIndex in range(numRunners):
            runnerPrices = self.api.createRunnerPrices()

            runnerPrices.selectionId = int(priceParts[baseIndex])
            runnerPrices.asianLineId = int(priceParts[baseIndex + 1])
            runnerPrices.handicap = float(priceParts[baseIndex + 2])
            runnerPrices.lastPriceMatched = float(priceParts[baseIndex + 3])
            runnerPrices.totalAmountMatched = float(priceParts[baseIndex + 4])

            baseIndex += 5
            runnerPrices.bestPricesToBack = list()

            for index in range(baseIndex, baseIndex + 6, 2):
                price = float(priceParts[index])
                amountAvailable = float(priceParts[index + 1])

                if price:
                    priceobj = self.api.createPrice()
                    priceobj.price = price
                    priceobj.amountAvailable = amountAvailable
                    runnerPrices.bestPricesToBack.append(priceobj)

            baseIndex += 6
            runnerPrices.bestPricesToLay = list()

            for index in range(baseIndex, baseIndex + 6, 2):
                price = float(priceParts[index])
                amountAvailable = float(priceParts[index + 1])

                if price:
                    priceobj = self.api.createPrice()
                    priceobj.price = price
                    priceobj.amountAvailable = amountAvailable
                    runnerPrices.bestPricesToLay.append(priceobj)

            baseIndex += 6

            marketPrices.runnerPrices.append(runnerPrices)

        message = self.api.createMessage()
        message.exception = None
        message.action = 'getMarketPrices'
        message.marketTuple = MarketTuple2(self.exchangeId, self.marketId)
        message.response = self.api.createMessage()
        message.response.marketPrices = marketPrices
        message.response.play = True

        self.api.sendMessage(message, self.pyIdPrices)

        if not self.lastTimeClock:
            timeToSleep = 1.0
        else:
            timeToSleep = timeClock - self.lastTimeClock

        self.lastTimeClock = timeClock
        self.api.setTimeout(timeToSleep)
