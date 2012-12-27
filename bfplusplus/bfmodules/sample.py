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

import time

modname = 'Sample'
# 1. Module Loaded
#    Actions can be executed during module load
# To see prints, the program has to be started from a console
# print '%s module loaded' % modname

# 2. Class DataProcessor
#    The framework will look for that class name
#    One and only 1 instance of the class per module will be created

class DataProcessor(object):

    def __init__(self, api, **kwargs):
        self.api = api

        # Dictionary of tuples (Var value, Var Type)
        self.params = dict()
        self.params['Heartbeat'] = [float, 5.0, 5.0]
        self.params['PricesToSkip'] = [int, 1, 1]
        self.params['PricesToPrint'] = [int, 2, 2]
        self.params['PrintToConsole'] = [bool, True, True]

        self.actions = dict()
        self.actions['Place Bet'] = 1
        self.actions['Do Nothing'] = 2
        self.actions['Other Action'] = 3
        self.actions['Yet Another'] = 4

        # Call heartbeat each 5 seconds
        self.api.setTimeout(self.params['Heartbeat'][2])
        self.api.logMessage('%s DataProcessor created' % modname)

        self.lastClock = time.clock()
        self.skippedPrices = 0


    def doExit(self, appExiting):
        # Logging would generate an error, because we are exiting
        if not appExiting:
            self.api.logMessage('%s DataProcessor exiting' % modname)


    def play(self):
        self.api.logMessage('%s DataProcessor - data pump starting' % modname)


    def pause(self):
        self.api.logMessage('%s DataProcessor - data pump pausing' % modname)


    def heartBeat(self):
        curClock = time.clock()
        timeSpan = curClock - self.lastClock
        self.lastClock = curClock
        self.api.logMessage('%s - Heartbeat called. Interval: %.2f' % (modname, timeSpan))


    def runnerChoices(self, runnerChoices):
        self.runnerChoices = runnerChoices

        for runnerName, checkStatus in self.runnerChoices:
            if checkStatus:
                self.api.logMessage('%s - %s is On' % (modname, runnerName))
        

    def getParams(self):
        return self.params


    def setParams(self, params):
        self.params = params

        self.api.logMessage('setting timeout to %.2f' % (self.params['Heartbeat'][2]))
        self.api.setTimeout(self.params['Heartbeat'][2])


    def getActions(self):
        return self.actions


    def doAction(self, actionId):
        for aLabel, aId in self.actions.iteritems():
            if actionId == aId:
                print aLabel
                break

    # ProcessData
    # 
    # Function called with the market and prices
    #   -- info.market (check GetMarket documentation)
    #      it contains the static market info (loaded once per market)
    #   -- info.marketPrices (see GetMarketPrices documentation)
    #      it contains the prices and dynamic market info
    #   -- info.runnerPrices (see GetMarketPrices documentation)
    #      it contains the prices on a per runner basis (dictionary with
    #      the runner selectionId as the key

    # Check the Betfair documentation to see what fields are available for
    # each type of info
    #
    
    def processData(self, info):
        self.api.logMessage('%s ProcessData processing data' % modname)

        pricesToSkip = self.params['PricesToSkip'][2]

        if self.skippedPrices < pricesToSkip:
            self.skippedPrices += 1
            self.api.logMessage('Skipping prices num %d' % self.skippedPrices)
            return

        self.skippedPrices = 0

        if self.params['PrintToConsole'][2]:
            print '-----------------------------------'
            print 'Market Info:'
            print '-----------------------------------'
            print '-- Market Name: %s - Id: %d' % (info.market.name, info.market.marketId)

            print '-----------------------------------'
            print 'Runner Info:'
            print '-----------------------------------'
            # Example
            for runnerIdx, runner in enumerate(info.market.runners):
                if runnerIdx >= self.params['PricesToPrint'][2]:
                    break
            
                runnerPrices = info.runnerPrices[runner.selectionId]

                if runnerPrices.bestPricesToBack:
                    backPrice = '%.2f' % runnerPrices.bestPricesToBack[0].price
                    backAmount = '%.2f' % runnerPrices.bestPricesToBack[0].amountAvailable
                else:
                    backPrice = '--.--'
                    backAmount = '--.--'

                if runnerPrices.bestPricesToLay:
                    layPrice = '%.2f' % runnerPrices.bestPricesToLay[0].price
                    layAmount = '%.2f' % runnerPrices.bestPricesToLay[0].amountAvailable
                else:
                    layPrice = '--.--'
                    layAmount = '--.--'

                print '-- Name: %s\tBack %s @%s\tLay %s @%s' % (runner.name,
                                                                backAmount, backPrice,
                                                                layAmount, layPrice)

            print ''


