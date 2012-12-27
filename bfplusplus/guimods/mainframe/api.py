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

from bfobj import MarketTuple
from bfpy.bfutil import EmptyObject

if True:
    def OnMessageFromModule(self, event):
        if event.message.subAction == 'logMsg':
            self.OnModuleLogMessage(event)
        elif event.message.subAction == 'placeBets':
            self.OnModulePlaceBets(event)
        elif event.message.subAction == 'cancelBets':
            self.OnModuleCancelBets(event)
        elif event.message.subAction == 'updateBets':
            self.OnModuleUpdateBets(event)
        elif event.message.subAction == 'getAccountFunds':
            self.OnModuleGetAccountFunds(event)
        elif event.message.subAction == 'getExcelSheets':
            self.OnGetExcelSheets(event)


    def OnModuleLogMessage(self, event):
        message, response, exception = self.SplitEventResponse(event)
        self.LogMessagesModule(response.logMsg)


    def OnModulePlaceBets(self, event):
        message, response, exception = self.SplitEventResponse(event)
        self.PlaceBets(response.marketTuple,
                       response.placeBets,
                       modId=response.modId,
                       fillOrKill=response.fillOrKill,
                       fillOrKillTime=response.fillOrKillTime)


    def OnModuleCancelBets(self, event):
        message, response, exception = self.SplitEventResponse(event)
        self.CancelBets(response.marketTuple, response.cancelBets, modId=response.modId)


    def OnModuleUpdateBets(self, event):
        message, response, exception = self.SplitEventResponse(event)
        self.UpdateBets(response.marketTuple, response.updateBets, modId=response.modId)


    def OnModuleGetAccountFunds(self, event):
        message, response, exception = self.SplitEventResponse(event)
        self.GetAccountFunds(response.exchangeId, modId=response.modId)


    def BfMarketTuple(self, exchangeId, marketId):
        return MarketTuple(exchangeId, marketId)

        
    def BfCreateEvent(self, eventId=-1, eventName=''):
        if False:
            with self.bfLock:
                return self.bfClient.createBFEvent(eventId=eventId, eventName=eventName)
        else:
            obj = EmptyObject()
            obj.eventId = eventId
            obj.eventTypeId = eventId
            obj.eventName = eventName
            return obj


    def BfCreateMarket(self):
        with self.bfLock:
            return self.bfClient.createMarket()


    def BfCreatePlaceBet(self):
        with self.bfLock:
            placeBet = self.bfClient.createPlaceBets()
            placeBet.bspLiability = 0.0
            placeBet.betCategoryType = 'E'
            return placeBet


    def BfCreateUpdateBet(self):
        with self.bfLock:
            return self.bfClient.createUpdateBets()


    def BfCreateCancelBet(self):
        with self.bfLock:
            return self.bfClient.createCancelBets()


    def BfCreateRunner(self):
        with self.bfLock:
            return self.bfClient.createRunner()


    def BfCreateMarketPrices(self):
        with self.bfLock:
            return self.bfClient.createMarketPrices()


    def BfCreateRunnerPrices(self):
        with self.bfLock:
            return self.bfClient.createRunnerPrices()


    def BfCreatePrice(self):
        with self.bfLock:
            return self.bfClient.createPrice()
