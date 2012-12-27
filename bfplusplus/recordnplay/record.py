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

from ConfigParser import ConfigParser as ConfigParser
from gzip import GzipFile
import time

# 1. Module Loaded
#    Actions can be executed during module load
# print 'sample.py module loaded'

# 2. Class DataProcessor
#    The framework will look for that class name
#    One and only 1 instance of the class per module will be created

class DataProcessor(object):

    status2Num = {'ACTIVE': 0, 'SUSPENDED': 1, 'CLOSED': 2}

    marketInfoName = 'marketInfo'
    priceInfoName = 'priceInfo'

    def __init__(self, api, **kwargs):
        self.api = api
        self.marketDir = kwargs.get('marketDir', '.')
        self.separator = kwargs.get('separator', ';')

        self.canRecord = True
        self.marketInfoWritten = False
        self.marketInfoFile = None
        self.priceInfoFile = None
        self.priceInfoFileOrig = None


    def doExit(self, appExiting=False):
        if not appExiting:
            self.api.logMessage('End of recording')

        if self.marketInfoFile:
            self.marketInfoFile.close()

        if self.priceInfoFile:
            self.priceInfoFile.close()
            self.priceInfoFileOrig.close()


    def play(self):
        pass


    def pause(self):
        pass


    def getParams(self):
        pass


    def setParams(self, params):
        pass


    def processData(self, message):
        if not self.canRecord:
            return

        if not self.marketInfoWritten:
            if not self.writeMarketInfo(message):
                return

        self.writePriceInfo(message)


    def writePriceInfo(self, message):
        if not self.priceInfoFile:
            fileName = '%s/%s' % (self.marketDir, self.priceInfoName)
            try:
                self.priceInfoFileOrig = open('%s.gz' % fileName, 'wb')
                self.priceInfoFile = GzipFile(self.priceInfoName, fileobj=self.priceInfoFileOrig)
            except Exception, e:
                self.api.logMessage('Stopping market recording. Error opening file %s: %s' % (fileName, str(e)))
                self.canRecord = False
                return False

            self.api.logMessage('Starting recording.')
            header = '#Timestamp'
            header += '%sMarket Id' % self.separator
            header += '%sMarket Status' % self.separator
            header += '%sIn-Play delay' % self.separator
            header += '%snumberOfWinners' % self.separator

            header += '%sSelection Id' % self.separator
            header += '%sAsian Line Id' % self.separator
            header += '%sHandicap' % self.separator
            header += '%sLast Price Matched' % self.separator
            header += '%sTotal Amount Matched' % self.separator

            header += '%sBack Price 1' % self.separator
            header += '%sBack Amount 1' % self.separator
            header += '%sBack Price 2' % self.separator
            header += '%sBack Amount 2' % self.separator
            header += '%sBack Price 3' % self.separator
            header += '%sBack Amount 3' % self.separator
            header += '%sLay Price 1' % self.separator
            header += '%sLay Amount 1' % self.separator
            header += '%sLay Price 2' % self.separator
            header += '%sLay Amount 2' % self.separator
            header += '%sLay Price 3' % self.separator
            header += '%sLay Amount 3' % self.separator

            header += '%sSelection Id ... Structure repeated for each runner' % self.separator
            header += '\r\n'

            self.priceInfoFile.write(header)


        market = message.market
        timeclock = time.clock()
        text = '%f' % timeclock
        text += '%s%d' % (self.separator, message.marketPrices.marketId)
        text += '%s%d' % (self.separator, self.status2Num[message.marketPrices.marketStatus])
        text += '%s%d' % (self.separator, message.marketPrices.delay)
        text += '%s%d' % (self.separator, message.marketPrices.numberOfWinners)

        for runner in market.runners:
            runnerPrices = message.runnerPrices[runner.selectionId]

            text += '%s%d' % (self.separator, runnerPrices.selectionId)
            text += '%s%d' % (self.separator, runnerPrices.asianLineId)
            text += '%s%.2f' % (self.separator, runnerPrices.handicap)
            text += '%s%.2f' % (self.separator, runnerPrices.lastPriceMatched)
            text += '%s%.2f' % (self.separator, runnerPrices.totalAmountMatched)

            for bestPrices in [runnerPrices.bestPricesToBack, runnerPrices.bestPricesToLay]:
                i = 0
                for bestPrice in bestPrices:
                    i += 1
                    text += '%s%.2f%s%.2f' % (self.separator, bestPrice.price,
                                              self.separator, bestPrice.amountAvailable)

                while i < 3:
                    i += 1
                    text += '%s0.00%s0.00' % (self.separator, self.separator)

        text += '\r\n'
        self.priceInfoFile.write(text)
        self.priceInfoFile.flush()

        if message.marketPrices.marketStatus == 'CLOSED':
            self.canRecord = False

        return True


    def writeMarketInfo(self, message):
        market = message.market
        fileName = '%s/%s' % (self.marketDir, self.marketInfoName)
        try:
            self.marketInfoFile = open(fileName, 'wb')
        except Exception, e:
            self.api.logMessage('Stopping market recording. Error opening file %s: %s' % (fileName, str(e)))
            self.canRecord = False
            return False

        mktFields = [
            'eventHierarchy', 'licenceId', 'marketId', 'exchangeId',
            'marketStatus', 'marketTime', 'marketType', 'menuPath',
            'name', 'numberOfWinners', 'parentEventId', 'runnersMayBeAdded',
            'timezone'
            ]

        config = ConfigParser()
        mktSection = 'market'
        config.add_section(mktSection)
        for mktField in mktFields:
            fieldValue = str(getattr(market, mktField))
            config.set(mktSection, mktField, fieldValue)

        marketDescription = market.marketDescription.encode('utf-8')
        config.set(mktSection, 'marketDescription', marketDescription)

        config.add_section('runners')
        config.set('runners', 'len', str(len(market.runners)))

        runnerFields = ['asianLineId', 'handicap', 'name', 'selectionId']
        
        for runnerIndex, runner in enumerate(market.runners):
            runnerSection = 'Runner %d' % runnerIndex
            config.add_section(runnerSection)
            for runnerField in runnerFields:
                fieldValue = str(getattr(runner, runnerField))
                config.set(runnerSection, runnerField, fieldValue)

        try:
            config.write(self.marketInfoFile)
            self.marketInfoWritten = True
        except Exception, e:
            self.api.logMessage('Stopping market recording. Error %s' % str(e))
            self.canRecord = False
        finally:
            self.marketInfoFile.close()
            self.marketInfoFile = None

        return True
