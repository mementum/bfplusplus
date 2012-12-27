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

from gui.PlaceBet import PlaceBet

import wx

from util import Message
import time


if True:
    def init(self):
        self.fillOrKillBets = dict()


    def VisualPlaceBet(self, selectionId, asianLineId, betType, price, size, persistence, updating, showDlg, bet=None, selectionName=None):
        if self.marketTuple is not None:
            marketComp = self.marketCache[self.marketTuple]
        else:
            marketComp = None

        fillOrKill = self.fillOrKill
        fillOrKillTime = self.fillOrKillTime

        if marketComp is None:
            # Because we don't know it ... sensible defaults
            inPlay = True
            # Remove persistence if requested because we have no reference market
            # and we don't want the bet to fail
            persistencemod = True

            # Just with the bet we can't find out if the market is already
            # in play, just if the market will be (or has already been) turned in play
            # Loading the market would be needed or checking the start time against the
            # current time. But the market (like tennis matches) may be turned in-play
            # hours or days later
            if bet is not None:
                dataMarket = self.dataMarkets.get(bet.exchangeId, None)
                if dataMarket:
                    marketItem = dataMarket.get(bet.marketId, None)
                    if marketItem:
                        if marketItem.turningInPlay:
                            # We have a reference and therefore disable persistence mod
                            persistencemod = False

                # Asian Markets seem to have a problem accepting Keep In-Play bets
                if bet.asianLineId:
                    inPlay = True
                    persistencemod = True

            if persistence and persistencemod:
                persistence = False
        else:
            inPlay = (marketComp.delay > 0)
            # Market already in play - do not modify the requested persistence
            persistencemod = False

            if not inPlay:
                dataMarket = self.dataMarkets.get(marketComp.exchangeId, None)
                if dataMarket:
                    marketItem = dataMarket.get(marketComp.marketId, None)
                    if marketItem:
                        turningInPlay = marketItem.turningInPlay
                else:
                    turningInPlay = False

                # if the market isn't in-play and it will not be turned "in-play" then
                # we mark it as "in-play" for the dialog to disallow placement of
                # "keep in-play bets"
                if not turningInPlay:
                    inPlay = True
                    # Market not in play and will not turn in play - mod the requested
                    # persistence if needed
                    persistencemod = True

            # Asian Markets seem to have a problem accepting Keep In-Play bets
            if marketComp.marketType == 'A':
                inPlay = True
                persistencemod = True

            if persistence and persistencemod:
                persistence = False

        if showDlg:
            # Create the bet dialog, fill it in and execute it
            placeBetDlg = PlaceBet(self, betType)
            if selectionName is not None:
                runnerName = selectionName
            else:
                runnerName = marketComp.getRunnerLabelById(selectionId, asianLineId)
            placeBetDlg.SetDetails(selectionId, runnerName, betType, price, size, updating=updating)

            placeBetDlg.SetPersistence(persistence=persistence, inPlay=inPlay)

            if not updating:
                placeBetDlg.m_checkBoxFillOrKill.SetValue(fillOrKill)
                placeBetDlg.m_spinCtrlFillOrKill.SetValue(fillOrKillTime)
            else:
                placeBetDlg.m_checkBoxFillOrKill.Disable()
                placeBetDlg.m_spinCtrlFillOrKill.Disable()

            if placeBetDlg.ShowModal() != wx.ID_OK:
                return

            price = placeBetDlg.price
            size = placeBetDlg.size
            persistence = placeBetDlg.persistence

            fillOrKill = placeBetDlg.m_checkBoxFillOrKill.GetValue()
            fillOrKillTime = placeBetDlg.m_spinCtrlFillOrKill.GetValue()

        if not updating:
            # Create and fill a bet in
            placeBet = self.BfCreatePlaceBet()

            placeBet.price = price
            placeBet.size = size
            placeBet.betType = betType

            # Asian Markets seem to have a problem accepting Keep In-Play bets
            # And persistence may have been set in the dialog
            if True:
                if (bet and bet.asianLineId) or (marketComp and marketComp.marketType == 'A'):
                    persistence = False

            placeBet.betPersistenceType = self.persistenceEnum[persistence]

            placeBet.marketId = marketComp.marketId
            placeBet.asianLineId = asianLineId
            placeBet.selectionId = selectionId

            # Asian Markets seem to have a problem accepting Keep In-Play bets
            # And persistence may have been set in the dialog
            self.PlaceBets(self.marketTuple, [placeBet], modId=None,
                           fillOrKill=fillOrKill, fillOrKillTime=fillOrKillTime)

        else:
            updateBet = self.BfCreateUpdateBet()

            updateBet.betId = bet.betId
            # Asian Markets seem to have a problem accepting Keep In-Play bets
            if True:
                if (bet and bet.asianLineId) or (marketComp and marketComp.marketType == 'A'):
                    persistence = False
            updateBet.newBetPersistenceType = self.persistenceEnum[persistence]
            updateBet.newPrice = price
            updateBet.newSize = size

            updateBet.oldBetPersistenceType = bet.betPersistenceType
            updateBet.oldPrice = bet.price
            try:
                updateBet.oldSize = bet.size
            except:
                updateBet.oldSize = bet.remainingSize

            self.UpdateBets(self.marketTuple, [updateBet])


    def PlaceBets(self, marketTuple, placeBets, modId=None, fillOrKill=None, fillOrKillTime=None):
        message = Message(action='placeBets', marketTuple=marketTuple, placeBets=placeBets, modId=modId)
        message.fillOrKill = self.fillOrKill if fillOrKill is None else fillOrKill
        message.fillOrKillTime = self.fillOrKillTime if not fillOrKillTime else fillOrKillTime

        self.thMisc.passMessage(message)

        marketComp = self.marketCache[marketTuple]
        placeBetMessages = list()
        for placeBet in placeBets:
            placeBetStr = 'PlaceBet: MktId %d / Runner: %s / Persistence: %s / Type: %s / Price %.2f / Size %.2f, / Fill or Kill: %s'
            placeBetStr = placeBetStr % (placeBet.marketId,
                                         marketComp.getRunnerLabelById(placeBet.selectionId, placeBet.asianLineId),
                                         self.persistenceTypeStr[placeBet.betPersistenceType],
                                         self.betTypeLegend[placeBet.betType],
                                         placeBet.price,
                                         placeBet.size,
                                         str(fillOrKill))
            placeBetMessages.append(placeBetStr)

        self.LogMessages(placeBetMessages)

        if self.optNet and not self.saveCount:
            self.GetMUBets(marketTuple)
            self.GetMarketProfitAndLoss(marketTuple)

        self.saveCount = self.optNetGuard
        self.saveCountPNL = int(self.optNetGuard / 2) + 1

        delay = marketComp.delay
        if delay:
            self.saveCount += delay


    def OnPlaceBets(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessagesError('PlaceBet result: Error, please check the list of bets')
                self.LogMessages(exception)
            return

        if message.modId and message.modId in self.bfModules:
            self.bfModules[message.modId].onPlaceBets(response.betResults)

        betResultMessages = list()
        for betResult in response.betResults:

            if message.fillOrKill and betResult.success:
                self.fillOrKillBets[betResult.betId] = (time.clock(), message.fillOrKillTime,
                                                        message.modId, message.marketTuple)

            betResultStr = 'PlaceBet result: %s / BetId: %d / Avg. Price: %.2f / Size Matched: %.2f / Success: %s'
            betResultStr = betResultStr % (betResult.resultCode, betResult.betId,
                                           betResult.averagePriceMatched, betResult.sizeMatched,
                                           str(betResult.success))

            betResultMessages.append(betResultStr)

        self.LogMessages(betResultMessages)
