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

import wx

from bfobj import Bet, BetCollection, MarketTuple
from util import Message

if True:
    def init(self):
        self.colSelection = 0
        # colSelectionId = 1
        self.colBetType = 1
        self.colBetPersistence = 2
        self.colBetStatus = 3
        self.colBetPrice = 4
        self.colBetSize = 5
        self.colBetId = 6
        self.colBetProfitLiab = 7        
        self.colBetBalance = 8

        # self.bitmapProfit = wx.Bitmap('./icons/money_add.png')
        # self.bitmapLoss = wx.Bitmap('./icons/money_delete.png')

        showMatched = self.config.ReadBool('Bets - Show Matched', True)
        self.config.WriteBool('Bets - Show Matched', showMatched)
        self.m_checkBoxShowMatched.SetValue(showMatched)

        showUnmatched = self.config.ReadBool('Bets - Show Unmatched', True)
        self.config.WriteBool('Bets - Show Unmatched', showUnmatched)
        self.m_checkBoxShowUnmatched.SetValue(showUnmatched)

        showBack = self.config.ReadBool('Bets - Show Back', True)
        self.config.WriteBool('Bets - Show Back', showBack)
        self.m_checkBoxShowBack.SetValue(showBack)

        showLay = self.config.ReadBool('Bets - Show Lay', True)
        self.config.WriteBool('Bets - Show Lay', showLay)
        self.m_checkBoxShowLay.SetValue(showLay)

        self.RegisterFocusWin(self.m_listCtrlBets)

        self.m_listCtrlBets.InsertColumn(self.colSelection, 'Selection')
        # self.m_listCtrlBets.InsertColumn(self.colSelectionId, 'Sel. Id')
        self.m_listCtrlBets.InsertColumn(self.colBetType, 'Type')
        self.m_listCtrlBets.InsertColumn(self.colBetPersistence, 'Keep')
        self.m_listCtrlBets.InsertColumn(self.colBetStatus, 'Status')
        self.m_listCtrlBets.InsertColumn(self.colBetPrice, 'Price')
        self.m_listCtrlBets.InsertColumn(self.colBetSize, 'Size')
        self.m_listCtrlBets.InsertColumn(self.colBetId, 'Bet Id')
        self.m_listCtrlBets.InsertColumn(self.colBetProfitLiab, 'Profit/Liability')
        self.m_listCtrlBets.InsertColumn(self.colBetBalance, 'Comp. bet with ... Size @Price Bet Wins/Loses')

        # colSizes = [115, 65, 40, 40, 45, 50, 65, 90, 200]
        colSizes = [115, 40, 40, 45, 50, 55, 85, 80, 240]
        for col, size in enumerate(colSizes):
            self.m_listCtrlBets.SetColumnWidth(col, size)


    def GetMUBets(self, marketTuple):
        if self.thGetMarketPrices:
            if marketTuple in self.marketCache:
                marketComp = self.marketCache[marketTuple]
                marketComp.nextbetCompDirty = True

            message = Message(marketTuple=marketTuple)
            self.thGetMUBets.passMessage(message)


    def OnGetMUBets(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessages(exception)
            return

        marketComp = self.marketCache[message.marketTuple]

        bets = BetCollection(response.bets)
        compPerc = float(self.m_sliderCompensate.GetValue())/100.0

        ticksAway = 0 if not self.compTicksAway else self.compTicksAwayCount
        marketComp.updateBets(bets, compPerc, ticksAway=ticksAway)

        if self.optNet:
            if self.saveCount:
                self.saveCount -= 1

            if not self.saveCount:
                canStop = True
                for betKey in marketComp.betsActive.itervalues():
                    if marketComp.bets[betKey].betStatus == 'U':
                        canStop = False
                        break
                if canStop:
                    self.GetMUBets(MarketTuple(0, 0))
                else:
                    self.saveCount = self.optNetGuard

        self.UpdateMUBets(message.marketTuple)


    def OnCheckBoxShowMatched(self, event):
        if self.thGetMarketPrices:
            self.UpdateMUBets(self.marketTuple)
        showMatched = self.m_checkBoxShowMatched.GetValue()
        self.config.WriteBool('Bets - Show Matched', showMatched)


    def OnCheckBoxShowUnmatched(self, event):
        if self.thGetMarketPrices:
            self.UpdateMUBets(self.marketTuple)
        showUnmatched = self.m_checkBoxShowUnmatched.GetValue()
        self.config.WriteBool('Bets - Show Unmatched', showUnmatched)


    def OnCheckBoxShowBack(self, event):
        if self.thGetMarketPrices:
            self.UpdateMUBets(self.marketTuple)
        showBack = self.m_checkBoxShowBack.GetValue()
        self.config.WriteBool('Bets - Show Back', showBack)


    def OnCheckBoxShowLay(self, event):
        if self.thGetMarketPrices:
            self.UpdateMUBets(self.marketTuple)
        showLay = self.m_checkBoxShowLay.GetValue()
        self.config.WriteBool('Bets - Show Lay', showLay)


    def UpdateBet(self, row, bet):
        self.m_listCtrlBets.SetStringItem(row, self.colBetPersistence, self.persistenceTypeStr[bet.betPersistenceType])
        self.m_listCtrlBets.SetStringItem(row, self.colBetPrice, '%.2f' % bet.price)
        self.m_listCtrlBets.SetStringItem(row, self.colBetSize, '%.2f' % bet.size)
        if bet.betType == 'B':
            profitLiabStr = '%.2f' % bet.profit
        else:
            profitLiabStr = '%.2f' % bet.risk
        self.m_listCtrlBets.SetStringItem(row, self.colBetProfitLiab, profitLiabStr)

        marketComp = self.marketCache[self.marketTuple]
        comp = marketComp.betComps.get(bet.betNum)
        if not comp:
            return

        if comp.size < self.minStakes.minimumStake:
            compStr = ''
        else:
            compStr = u'%s %.2f@%.2f for %.2f/%.2f' % \
                      (self.betTypeLegend[comp.betType], comp.size, comp.price, comp.compWin, comp.compLoss)
        self.m_listCtrlBets.SetStringItem(row, self.colBetBalance, compStr)
        

    def InsertBet(self, bet, betnum, row=0):
        marketComp = self.marketCache[self.marketTuple]
        row = self.m_listCtrlBets.InsertStringItem(row, marketComp.getRunnerLabelById(bet.selectionId, bet.asianLineId))
        self.m_listCtrlBets.SetStringItem(row, self.colBetType, self.betTypeLegend[bet.betType])
        self.m_listCtrlBets.SetStringItem(row, self.colBetPersistence, self.persistenceTypeStr[bet.betPersistenceType])
        self.m_listCtrlBets.SetStringItem(row, self.colBetStatus, bet.betStatus)
        self.m_listCtrlBets.SetStringItem(row, self.colBetPrice, '%.2f' % bet.price)
        self.m_listCtrlBets.SetStringItem(row, self.colBetSize, '%.2f' % bet.size)
        self.m_listCtrlBets.SetStringItem(row, self.colBetId, '%d' % bet.betId)
        if bet.betType == 'B':
            profitLiabStr = '%.2f' % bet.profit
        else:
            profitLiabStr = '%.2f' % bet.risk
        self.m_listCtrlBets.SetStringItem(row, self.colBetProfitLiab, profitLiabStr)
        # self.m_listCtrlBets.SetStringItem(row, self.colSelectionId, '%d' % bet.selectionId)

        self.m_listCtrlBets.SetItemData(row, betnum)

        betColour = self.matchedColour if bet.betStatus == 'M' else self.unmatchedColour
        self.m_listCtrlBets.SetItemBackgroundColour(row, betColour)

        return row


    def MuBetsColours(self):
        marketComp = self.marketCache[self.marketTuple]
        count = self.m_listCtrlBets.GetItemCount()

        for itemIndex in range(count):
            itemBetNum = self.m_listCtrlBets.GetItemData(itemIndex)
            itemBetKey = marketComp.betsActive[itemBetNum]
            bet = marketComp.bets[itemBetKey]

            betColour = self.matchedColour if bet.betStatus == 'M' else self.unmatchedColour
            betColourText = self.matchedColourText if bet.betStatus == 'M' else self.unmatchedColourText
            self.m_listCtrlBets.SetItemBackgroundColour(itemIndex, betColour)
            self.m_listCtrlBets.SetItemTextColour(itemIndex, betColourText)

        self.m_listCtrlBets.Refresh()


    def UpdateMUBetsCompensations(self, marketTuple):
        if marketTuple != self.marketTuple:
            return

        marketComp = self.marketCache[self.marketTuple]
        count = self.m_listCtrlBets.GetItemCount()

        for itemIndex in range(count):
            itemBetNum = self.m_listCtrlBets.GetItemData(itemIndex)
            itemBetKey = marketComp.betsActive[itemBetNum]
            bet = marketComp.bets[itemBetKey]

            self.UpdateBetCompensation(itemIndex, bet)
        

    def UpdateBetCompensation(self, row, bet):
        marketComp = self.marketCache[self.marketTuple]

        compDirty = marketComp.betCompsDirty.get(bet.betNum, False)
        if not compDirty:
            return
        marketComp.betCompsDirty[bet.betNum] = False

        comp = marketComp.betComps[bet.betNum]
        if not comp or comp.size < self.minStakes.minimumStake:
            compStr = ''
        else:
            compStr = u'%s %.2f@%.2f for %.2f/%.2f' % \
                      (self.betTypeLegend[comp.betType], comp.size, comp.price, comp.compWin, comp.compLoss)
        self.m_listCtrlBets.SetStringItem(row, self.colBetBalance, compStr)


    def MatchesFilter(self, bet):
        if bet.betStatus == 'M' and not self.m_checkBoxShowMatched.GetValue():
            return False
        if bet.betStatus == 'U' and not self.m_checkBoxShowUnmatched.GetValue():
            return False
        if bet.betType == 'B' and not self.m_checkBoxShowBack.GetValue():
            return False
        if bet.betType == 'L' and not self.m_checkBoxShowLay.GetValue():
            return False

        return True


    def UpdateMUBets(self, marketTuple):
        if marketTuple is None:
            return

        if marketTuple != self.marketTuple:
            # skip delayed prices from threads
            return

        marketComp = self.marketCache[marketTuple]

        maxCancelBets = 40
        if self.fillOrKillBets:
            cancelFills = list()
            curTime = time.clock()

            for betId in self.fillOrKillBets.copy():
                fillOrKillTuple = self.fillOrKillBets[betId]
                fillTimePlaced = fillOrKillTuple[0]
                fillPeriod = fillOrKillTuple[1]
                fillModId = fillOrKillTuple[2]
                mTuple = fillOrKillTuple[3]

                found = False
                for betkey in marketComp.betsActive.itervalues():
                    bet = marketComp.bets[betkey]
                    if bet.betId == betId and bet.betStatus == 'U':
                        found = True
                        break

                if not found and mTuple == self.marketTuple:
                    # Only if in the same market ... remove it
                    del self.fillOrKillBets[betId]
                    continue

                timeSpan = curTime - fillTimePlaced

                if timeSpan >= fillPeriod:
                    cancelBet = self.BfCreateCancelBet()
                    cancelBet.betId = betId
                    cancelFills.append(cancelBet)
                    self.LogMessages('Killing bet %d' % betId)

                    if len(cancelFills) == maxCancelBets:
                        self.CancelBets(self.marketTuple, cancelFills, modId=fillModId)
                        cancelFills = list()

                    if betId in self.fillOrKillBets:
                        del self.fillOrKillBets[betId]

            if cancelFills:
                self.CancelBets(self.marketTuple, cancelFills, modId=fillModId)

                    
        betKeys = marketComp.betsActive.values()
        betKeys.sort(reverse=True)

        betIndex = len(betKeys)
        itemIndex = self.m_listCtrlBets.GetItemCount()

        while itemIndex > 0 or betIndex:
            if itemIndex > 0:
                itemIndex -= 1

                itemBetNum = self.m_listCtrlBets.GetItemData(itemIndex)
                if itemBetNum not in marketComp.betsActive:
                    self.m_listCtrlBets.DeleteItem(itemIndex)
                    continue

                itemBetKey = marketComp.betsActive[itemBetNum]
                bet = marketComp.bets[itemBetKey]

                if not self.MatchesFilter(bet):
                    self.m_listCtrlBets.DeleteItem(itemIndex)
                    continue
            else:
                itemBetKey = "999999999999999999999999999999"
                itemIndex = -1

            while betIndex:
                betIndex -= 1
                betKey = betKeys[betIndex]

                if betKey < itemBetKey:
                    bet = marketComp.bets[betKey]
                    bet.dirty = False
                    if self.MatchesFilter(bet):
                        row = self.InsertBet(bet, bet.betNum, itemIndex + 1)
                        self.UpdateBetCompensation(row, bet)
                        
                elif betKey == itemBetKey:
                    bet = marketComp.bets[betKey]
                    if bet.dirty:
                        bet.dirty = False
                        self.UpdateBet(itemIndex, bet)
                    self.UpdateBetCompensation(itemIndex, bet)
                else:
                    betIndex += 1
                    break

        # self.m_listCtrlBets.Refresh()


    def m_listCtrlBetsOnContextMenu(self, event):
        pos = event.GetPosition()
        itemId, hitFlags = self.m_listCtrlBets.HitTest(pos)

        found = (itemId != wx.NOT_FOUND)

        if found:
            marketComp = self.marketCache[self.marketTuple]
            self.m_listCtrlBets.Select(itemId)
            betNum = self.m_listCtrlBets.GetItemData(itemId)
            betKey = marketComp.betsActive[betNum]
            bet = marketComp.bets[betKey]
        else:
            bet = None

        self.m_menuItemBetCancel.Enable(found and bet.betStatus == 'U')
        self.m_menuItemBetModify.Enable(found and bet.betStatus == 'U')

        if found and bet.betStatus == 'M':
            comp = marketComp.betComps.get(betNum)
        else:
            comp = None

        self.m_menuItemBetCompensate.Enable(bool(found and comp and comp.size >= self.minStakes.minimumStake))

        # Stop-bet info and labels
        stopBetPerc = self.m_sliderStopBet.GetValue()
        self.m_menuListBets.stopBetPerc = stopBetPerc

        # Enable/Disable Stop-bet menu items
        # stopLabel = 'Stop if profit on any outcome is >= %d%% of expected profit'
        # stopLabel = stopLabel % stopBetPerc
        # self.m_menuItemStopProfitProfit.SetItemLabel(stopLabel)

        # stopLabel = 'Stop if profit on any outcome is >= %d%% of assumed risk'
        # stopLabel = stopLabel % stopBetPerc
        # self.m_menuItemStopProfitRisk.SetItemLabel(stopLabel)

        # stopLabel = 'Stop if loss on any outcome is >= %d%% of expected profit'
        # stopLabel = stopLabel % stopBetPerc
        # self.m_menuItemStopLossProfit.SetItemLabel(stopLabel)

        # stopLabel = 'Stop if loss on any outcome is >= %d%% of assumed risk'
        # stopLabel = stopLabel % stopBetPerc
        # self.m_menuItemStopLossRisk.SetItemLabel(stopLabel)

        enableStopBetMenus = (bet is not None and bet.betStatus == 'M')
        self.m_menuItemStopProfitProfit.Enable(enableStopBetMenus)
        self.m_menuItemStopProfitRisk.Enable(enableStopBetMenus)
        self.m_menuItemStopLossProfit.Enable(enableStopBetMenus)
        self.m_menuItemStopLossRisk.Enable(enableStopBetMenus)

        # Store a reference to the bet we want to act upon
        self.m_menuListBets.bet = bet
        # Show the menu
        self.m_listCtrlBets.PopupMenu(self.m_menuListBets, pos)


    def OnMenuSelectionCancel(self, event):
        marketComp = self.marketCache[self.marketTuple]
        bet = self.m_menuListBets.bet

        if bet.betNum not in marketComp.betsActive:
            msg = 'Cannot cancel bet with betId %d: the bet is no longer active' % bet.betId
            self.LogMessages([msg])
            return

        cancelBet = self.BfCreateCancelBet()
        cancelBet.betId = bet.betId

        self.CancelBets(self.marketTuple, [cancelBet])


    def OnMenuSelectionModify(self, event):
        marketComp = self.marketCache[self.marketTuple]
        bet = self.m_menuListBets.bet

        if bet.betNum not in marketComp.betsActive:
            msg = 'Cannot modify bet with betId %d: the bet is no longer active' % bet.betId
            self.LogMessages([msg])
            return

        persistence = self.persistenceType[bet.betPersistenceType]
        self.VisualPlaceBet(selectionId=bet.selectionId, asianLineId=bet.asianLineId, \
                            betType=bet.betType, price=bet.price, size=bet.size, \
                            persistence=persistence, updating=True, showDlg=True, \
                            bet=bet)


    def OnMenuSelectionCompensate(self, event):
        marketComp = self.marketCache[self.marketTuple]
        bet = self.m_menuListBets.bet

        if bet.betNum not in marketComp.betsActive:
            msg = 'Cannot compensate bet with betId %d: the bet is no longer active' % bet.betId
            self.LogMessages([msg])
            return

        comp = marketComp.betComps.get(bet.betNum)

        if not comp or comp.size < self.minStakes.minimumStake:
            msg = 'Cannot compensate bet with betId %d: no compensation exists right now' % bet.betId
            self.LogMessages([msg])
            return

        # We want to get matched, so the idea is to remain in the market
        # regardless of the setting of the bet to compensate
        # persistence = self.persistenceType[bet.betPersistenceType]
        # FIXME: In markets that will not go in play, setting IP doesn't work
        persistence = True
        showDlg = self.verifyBets and self.verifyRClickBets

        price = comp.price

        self.VisualPlaceBet(selectionId=bet.selectionId, asianLineId=bet.asianLineId, \
                            betType=comp.betType, price=price, size=comp.size, \
                            persistence=persistence, updating=False, showDlg=showDlg)

    def OnButtonClickMUBetsFilter(self, event):
        event.Skip()
        showAction = not self.m_panelMUBetsFilter.IsShown()
        self.sizerMUBets.Show(self.m_panelMUBetsFilter, showAction)
        self.sizerMUBets.Layout()

        


