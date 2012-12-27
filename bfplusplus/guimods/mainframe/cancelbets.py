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

import bfpy
from util import Message

if True:

    def CancelBetsByMarket(self, marketTuple, modId=None):
        message = Message(action='cancelBetsByMarket', marketTuple=marketTuple, modId=modId)
        self.thMisc.passMessage(message)
        self.LogMessages('Issued a Cancel request for all bets in this market')


    def OnCancelBetsByMarket(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessagesError('CancelBetsByMarket result: Error')
                self.LogMessages(exception)
            return

        if message.modId and message.modId in self.bfModules:
            self.bfModules[message.modId].onCancelBetsByMarket(response.results)

        resultMessages = list()
        for result in response.results:
            resultStr = 'CancelBet Result: %s / marketId: %d'
            resultStr = resultStr % (result.resultCode, result.marketId)
            resultMessages.append(resultStr)

        self.LogMessages(resultMessages)


    def CancelBets(self, marketTuple, cancelBets, modId=None):
        message = Message(action='cancelBets',
                          marketTuple=marketTuple,
                          cancelBets=cancelBets,
                          modId=modId)

        self.thMisc.passMessage(message)

        marketComp = self.marketCache[marketTuple]

        cancelBetMessages = list()
        for cancelBet in cancelBets:
            cancelBetStr = 'CancelBet: BetId %d'
            cancelBetStr = cancelBetStr % (cancelBet.betId)
            cancelBetMessages.append(cancelBetStr)

        self.LogMessages(cancelBetMessages)


    def OnCancelBets(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessagesError('CancelBet result: Error')
                self.LogMessages(exception)
            return

        if message.modId and message.modId in self.bfModules:
            self.bfModules[message.modId].onCancelBets(response.betResults)

        betResultMessages = list()
        for betResult in response.betResults:

            betResultStr = 'CancelBet result: %s / BetId: %d / Size Cancelled: %.2f / Success: %s'
            betResultStr = betResultStr % (betResult.resultCode, betResult.betId,
                                           betResult.sizeCancelled, str(betResult.success))

            betResultMessages.append(betResultStr)

        self.LogMessages(betResultMessages)


    def OnButtonClickCancelAllBets(self, event):
        maxCancelBets = 40

        if self.marketTuple is None:
            return

        if self.productId != bfpy.freeApiId:
            self.CancelBetsByMarket(self.marketTuple)
            return

        marketComp = self.marketCache[self.marketTuple]

        cancelBets = list()
        for betKey in marketComp.betsActive.itervalues():
            bet = marketComp.bets[betKey]

            if bet.betStatus == 'M':
                continue

            cancelBet = self.BfCreateCancelBet()
            cancelBet.betId = bet.betId
            cancelBets.append(cancelBet)

            if len(cancelBets) ==  maxCancelBets:
                self.CancelBets(self.marketTuple, cancelBets)
                cancelBets = list()

        # Send the remaining to be removed
        if cancelBets:
            self.CancelBets(self.marketTuple, cancelBets)


