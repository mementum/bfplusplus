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

from util import Message

if True:
    def UpdateBets(self, marketTuple, updateBets, modId=None):

        message = Message(action='updateBets', marketTuple=marketTuple, updateBets=updateBets)
        message.modId = modId
        self.thMisc.passMessage(message)

        marketComp = self.marketCache[marketTuple]
        updateBetMessages = list()
        for updateBet in updateBets:
            updateBetStr = 'UpdateBet: BetId %d /Old/ Price %.2f / Size: %.2f / Persistence: %s /New/ Price %.2f / Size: %.2f / Persistence: %s'
            updateBetStr = updateBetStr % (updateBet.betId,
                                           updateBet.oldPrice, updateBet.oldSize, self.persistenceTypeStr[updateBet.oldBetPersistenceType],
                                           updateBet.newPrice, updateBet.newSize, self.persistenceTypeStr[updateBet.newBetPersistenceType])
            updateBetMessages.append(updateBetStr)

        self.saveCount = self.optNetGuard
        self.saveCountPNL = int(self.optNetGuard / 2) + 1
        delay = marketComp.delay
        if delay:
            self.saveCount += delay

        self.LogMessages(updateBetMessages)


    def OnUpdateBets(self, event):

        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessagesError('UpdateBet result: Communications error, please check the list of bets')
                self.LogMessages(exception)
            return

        if message.modId and message.modId in self.bfModules:
            self.bfModules[message.modId].onUpdateBets(response.betResults)

        betResultMessages = list()
        for betResult in response.betResults:

            betResultStr = 'UpdateBet result: %s / BetId: %d /Size Cancelled: %.2f /New/ BetId: %d / Price: %.2f / Size: %.2f/ Success: %s'
            betResultStr = betResultStr % (betResult.resultCode, betResult.betId, betResult.sizeCancelled,
                                           betResult.newBetId, betResult.newPrice, betResult.newSize,
                                           str(betResult.success))

            betResultMessages.append(betResultStr)

        self.LogMessages(betResultMessages)
