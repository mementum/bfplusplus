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

from collections import defaultdict
from operator import attrgetter
from datetime import datetime

import wx

import bfobj
import bfpy
from util import Message

if True:

    class CBetsMarket(object):
        def __init__(self):
            self.selbets = defaultdict(list)

        def addBet(self, bet):
            if not self.selbets:
                self.marketId = bet.marketId
                self.exchangeId = bet.exchangeId
                self.marketName = bet.fullMarketName

            self.selbets[bet.selectionName].append(bet)


    def init(self):
        self.curBetsRefresh = self.config.ReadInt('Current Bets Refresh', 60)
        self.config.WriteInt('Current Bets Refresh', self.curBetsRefresh)

        self.curBetsAutoRefresh = self.config.ReadBool('Current Bets AutoRefresh', True)
        self.config.WriteBool('Current Bets AutoRefresh', self.curBetsAutoRefresh)
        self.m_checkBoxCurrentBetsAutoRefresh.SetValue(self.curBetsAutoRefresh)

        self.RegisterFocusWin(self.m_treeCtrlCurrentBetsUK)
        self.RegisterFocusWin(self.m_treeCtrlCurrentBetsAus)
        self.RegisterFocusWin(self.m_listCtrlCurrentBetsInfo)

        self.currentBets = defaultdict(list)
        self.cbetsDisplayed = defaultdict(int)

        self.m_listCtrlCurrentBetsInfo.InsertColumn(0, '')
        self.m_listCtrlCurrentBetsInfo.InsertColumn(1, '')
        charLen = [12, 23]
        for i in range(self.m_listCtrlCurrentBetsInfo.GetColumnCount()):
            self.m_listCtrlCurrentBetsInfo.SetColumnWidth(i, charLen[i] * self.avgCharWidth)

        self.m_treeCtrlCurrentBetsUK.AddRoot('')
        self.m_treeCtrlCurrentBetsAus.AddRoot('')

        self.lastUpdate = dict()
        self.lastUpdate[bfpy.ExchangeUK] = None
        self.lastUpdate[bfpy.ExchangeAus] = None


    def OnCheckBoxCurrentBetsAutoRefresh(self, event):
        event.Skip()

        self.curBetsAutoRefresh = self.m_checkBoxCurrentBetsAutoRefresh.GetValue()
        self.config.WriteBool('Current Bets AutoRefresh', self.curBetsAutoRefresh)

        timeout = 0 if not self.curBetsAutoRefresh else self.curBetsRefresh
        message = Message(timeout=timeout)
        self.thCurrentBets.passMessage(message)


    def GetTreeCtrlCurrentBets(self, exchangeId):
        if exchangeId == bfpy.ExchangeUK:
            treeCtrl = self.m_treeCtrlCurrentBetsUK
        elif exchangeId == bfpy.ExchangeAus:
            treeCtrl = self.m_treeCtrlCurrentBetsAus

        return treeCtrl


    def OnButtonClickCurrentBets(self, event):
        if not hasattr(self, 'currentBets'):
            self.currentBets = list()

        self.m_staticTextCurrentBetsNum.SetLabel('--Loading--')
        for exchangeId in [bfpy.ExchangeUK, bfpy.ExchangeAus]:
            self.GetCurrentBets(exchangeId)

        self.m_listCtrlCurrentBetsInfo.DeleteAllItems()


    def GetCurrentBets(self, exchangeId):
	message = Message(action='getCurrentBets')
        message.exchangeId = exchangeId

	self.thMisc.passMessage(message)


    def OnGetCurrentBets(self, event):
        message, response, exception = self.SplitEventResponse(event)
        if not response:
            if exception:
                self.LogMessages(exception)
            return

        # self.currentBets = response.bets
        exchangeId = message.exchangeId

        self.currentBets[exchangeId] = response.bets
        self.lastUpdate[exchangeId] = datetime.now()
        self.UpdateCurrentBets(message.exchangeId)


    def OnNotebookPageChangedCurrentBets(self, event):
        event.Skip()
        page = event.GetSelection()

        exchangeId = page + 1
        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)

        treeItem = treeCtrl.GetSelection()
        if not treeItem.IsOk():
            # self.m_buttonCurrentBetsLoadMarket.Disable()
            self.m_listCtrlCurrentBetsInfo.DeleteAllItems()
            return

        self.CurrentBetsTreeItemSelected(exchangeId, treeItem)


    def OnCheckBoxCurrentBetsFilter(self, event):
        if self.thGetMarketPrices:
            self.UpdateCurrentBetsDisplay()


    def UpdateCurrentBetsDisplay(self):
        for exchangeId in [bfpy.ExchangeUK, bfpy.ExchangeAus]:
            self.UpdateCurrentBets(exchangeId)


    def UpdateCurrentBets(self, exchangeId):
        # Gather the bets on a per market basis
        showMatched = self.m_checkBoxCurrentBetsMatched.GetValue()
        showUnmatched = self.m_checkBoxCurrentBetsUnmatched.GetValue()
        showBack = self.m_checkBoxCurrentBetsBack.GetValue()
        showLay = self.m_checkBoxCurrentBetsLay.GetValue()

        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)

        self.cbetsDisplayed[exchangeId] = 0
        markets = defaultdict(CBetsMarket)
        for bet in self.currentBets[exchangeId]:
            if not showMatched and bet.betStatus == 'M':
                continue
            if not showUnmatched and bet.betStatus == 'U':
                continue
            if not showBack and bet.betType == 'B':
                continue
            if not showLay and bet.betType == 'L':
                continue

            mId = '%s:%s' % (bet.exchangeId, bet.marketId)
            markets[mId].addBet(bet)

            self.cbetsDisplayed[exchangeId] += 1

        totalDisplayedBets = 0
        totalBets = 0
        for exId in [bfpy.ExchangeUK, bfpy.ExchangeAus]:
            totalDisplayedBets += self.cbetsDisplayed[exId]
            totalBets += len(self.currentBets[exId])

        numBetsStr = '%d of %d (UK: %d/%d - Aus: %d/%d)'
        numBetsStr = numBetsStr % \
                     (totalDisplayedBets, totalBets,
                      self.cbetsDisplayed[bfpy.ExchangeUK],
                      len(self.currentBets[bfpy.ExchangeUK]),
                      self.cbetsDisplayed[bfpy.ExchangeAus],
                      len(self.currentBets[bfpy.ExchangeAus]))

        self.m_staticTextCurrentBetsNum.SetLabel(numBetsStr)

        updateStr = 'Uk %s /Aus %s'
        if self.lastUpdate[bfpy.ExchangeUK]:
            ukUpdateStr = self.lastUpdate[bfpy.ExchangeUK].strftime('%Y-%m-%d %H:%M')
        else:
            ukUpdateStr = '-'

        if self.lastUpdate[bfpy.ExchangeAus]:
            ausUpdateStr = self.lastUpdate[bfpy.ExchangeAus].strftime('%Y-%m-%d %H:%M')
        else:
            ausUpdateStr = '-'

        self.m_staticTextCurrentBetsUpdate.SetLabel(updateStr % (ukUpdateStr, ausUpdateStr))

        # Get just the list of markets and sort on name
        markets = markets.values()
        markets.sort(key=attrgetter('marketName'))

        # Check if selection is going to be voided
        page = self.m_notebookCurrentBets.GetSelection()
        if exchangeId == (page + 1):
            # self.m_buttonCurrentBetsLoadMarket.Disable()
            self.m_listCtrlCurrentBetsInfo.DeleteAllItems()

        # Fill the tree
        rootTreeItem = treeCtrl.GetRootItem()
        treeCtrl.DeleteChildren(rootTreeItem)

        for market in markets:
            mktTreeItem = treeCtrl.AppendItem(rootTreeItem, market.marketName[1:])
            treeCtrl.SetPyData(mktTreeItem, market)
            mktProfit = 0.0
            mktRisk = 0

            for selbet, betlist in market.selbets.iteritems():
                selbetTreeItem = treeCtrl.AppendItem(mktTreeItem, selbet)
                treeCtrl.SetPyData(selbetTreeItem, betlist)
                selbetProfit = 0.0
                selbetRisk = 0.0
                for bet in betlist:
                    if bet.betStatus == 'M':
                        size = bet.matchedSize
                        price = bet.avgPrice
                    else:
                        size = bet.remainingSize
                        price = bet.price

                    if bet.betType == 'B':
                        risk = size
                        profit = size * (bet.price - 1.0)
                    else:
                        risk = size * (bet.price - 1.0)
                        profit = size

                    selbetProfit += profit
                    selbetRisk += risk

                    betstr = '%s: %s - %.2f@%.2f (%.2f, -%.2f)'
                    betstr = betstr % (self.betStatusLegend[bet.betStatus],
                                       self.betTypeLegend[bet.betType],
                                       size, bet.price, risk, profit)
                        
                    betTreeItem = treeCtrl.AppendItem(selbetTreeItem, betstr)
                    treeCtrl.SetPyData(betTreeItem, bet)

                selbetStr = '%s (%.2f, -%.2f)' % (selbet, selbetProfit, selbetRisk)
                # treeCtrl.SetItemText(selbetTreeItem, selbetStr)
                mktProfit += selbetProfit
                mktRisk += selbetRisk

            mktStr = '%s (%.2f, -%.2f)' % (market.marketName[1:], mktProfit, mktRisk)
            # treeCtrl.SetItemText(mktTreeItem, mktStr)


    def OnTreeItemActivatedCurrentBetsAus(self, event):
        event.Skip()
        self.CurrentBetsTreeItemActivated(bfpy.ExchangeAus, event.GetItem())


    def OnTreeItemActivatedCurrentBetsUK(self, event):
        event.Skip()
        self.CurrentBetsTreeItemActivated(bfpy.ExchangeUK, event.GetItem())


    def CurrentBetsTreeItemActivated(self, exchangeId, treeItem):
        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)
        data = treeCtrl.GetPyData(treeItem)

        if hasattr(data, 'fullMarketName'):
            self.CurrentBetsLoadMarket(exchangeId, treeItem)


    def OnTreeSelChangedCurrentBetsAus(self, event):
        event.Skip()
        self.CurrentBetsTreeItemSelected(bfpy.ExchangeAus, event.GetItem())


    def OnTreeSelChangedCurrentBetsUK(self, event):
        event.Skip()
        self.CurrentBetsTreeItemSelected(bfpy.ExchangeUK, event.GetItem())


    def CurrentBetsTreeItemSelected(self, exchangeId, treeItem):

        if not treeItem.IsOk():
            return

        # self.m_buttonCurrentBetsLoadMarket.Enable()

        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)
        self.m_listCtrlCurrentBetsInfo.DeleteAllItems()
        data = treeCtrl.GetPyData(treeItem)

        if hasattr(data, 'fullMarketName'):
            bet = data
            # Display the information of the bet
            row = self.m_listCtrlCurrentBetsInfo.InsertStringItem(0, 'Selection')
            self.m_listCtrlCurrentBetsInfo.SetStringItem(row, 1, bet.selectionName)

            row = self.m_listCtrlCurrentBetsInfo.InsertStringItem(row + 1, 'Bet Id')
            self.m_listCtrlCurrentBetsInfo.SetStringItem(row, 1, '%d' % bet.betId)

            row = self.m_listCtrlCurrentBetsInfo.InsertStringItem(row + 1, 'Keep in Play')
            self.m_listCtrlCurrentBetsInfo.SetStringItem(row, 1, '%s' % self.persistenceType[bet.betPersistenceType])

            row = self.m_listCtrlCurrentBetsInfo.InsertStringItem(row + 1, 'Status')
            self.m_listCtrlCurrentBetsInfo.SetStringItem(row, 1, '%s' % self.betStatusLegend[bet.betStatus])

            row = self.m_listCtrlCurrentBetsInfo.InsertStringItem(row + 1, 'Type')
            self.m_listCtrlCurrentBetsInfo.SetStringItem(row, 1, '%s' % self.betTypeLegend[bet.betType])

            if bet.betStatus == 'M':
                row = self.m_listCtrlCurrentBetsInfo.InsertStringItem(row + 1, 'Matched size')
                self.m_listCtrlCurrentBetsInfo.SetStringItem(row, 1, '%.2f' % bet.matchedSize)

                row = self.m_listCtrlCurrentBetsInfo.InsertStringItem(row + 1, 'Avg. Price')
                self.m_listCtrlCurrentBetsInfo.SetStringItem(row, 1, '%.2f' % bet.avgPrice)

            else:
                row = self.m_listCtrlCurrentBetsInfo.InsertStringItem(row + 1, 'Unmatched size')
                self.m_listCtrlCurrentBetsInfo.SetStringItem(row, 1, '%.2f' % bet.remainingSize)

                row = self.m_listCtrlCurrentBetsInfo.InsertStringItem(row + 1, 'Price')
                self.m_listCtrlCurrentBetsInfo.SetStringItem(row, 1, '%.2f' % bet.price)

        elif isinstance(data, list):
            pass
        else:
            # market level
            pass


    def OnButtonClickCurrentBetsLoadMarket(self, event):
        event.Skip()

        page = self.m_notebookCurrentBets.GetSelection()
        exchangeId = page + 1
        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)

        treeItem = treeCtrl.GetSelection()
        if not treeItem.IsOk():
            # In theory the button is only enabled is a selection
            # is active, but a double check isn't bad
            return

        self.CurrentBetsLoadMarket(exchangeId, treeItem)


    def CurrentBetsLoadMarket(self, exchangeId, treeItem):
        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)

        # The highest node before the root has to be found
        rootTreeItem = treeCtrl.GetRootItem()
        while True:
            parentTreeItem = treeCtrl.GetItemParent(treeItem)

            if not parentTreeItem.IsOk():
                # This SHOULD NOT HAPPEN
                return

            if parentTreeItem == rootTreeItem:
                # Target found
                break

            treeItem = parentTreeItem

        # Hit found, gather data and load market
        mktData = treeCtrl.GetPyData(treeItem)
        exchangeId = mktData.exchangeId
        marketId = mktData.marketId

        marketTuple = bfobj.MarketTuple(exchangeId, marketId)
        self.GetMarket(marketTuple, expandEvents=True)


    def OnButtonClickCurrentBetsCollapseAll(self, event):
        event.Skip()

        page = self.m_notebookCurrentBets.GetSelection()
        exchangeId = page + 1

        self.CollapseAllCurrentBets(exchangeId)


    def CollapseAllCurrentBets(self, exchangeId):
        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)
        rootTreeItem = treeCtrl.GetRootItem()
        treeItem, treeItemCookie = treeCtrl.GetFirstChild(rootTreeItem)

        while treeItem.IsOk():
            treeCtrl.CollapseAllChildren(treeItem)
            treeItem = treeCtrl.GetNextSibling(treeItem)

    def OnMenuSelectionCurrentBetsCancel(self, event):
        bet = self.menuCurrentBets.bet

        cancelBet = self.BfCreateCancelBet()
        cancelBet.betId = bet.betId

        marketTuple = bfobj.MarketTuple(bet.exchangeId, bet.marketId)

        self.CancelBets(marketTuple, [cancelBet])
        self.GetCurrentBets(bet.exchangeId)


    def CurrentBetsColours(self):
        if False:
            if not hasattr(self, 'currentBetsDisplayed'):
                return

            for row, bet in enumerate(self.currentBetsDisplayed):
                if bet.betStatus == 'M':
                    colour = self.matchedColour
                    colourText = self.matchedColourText
                else:
                    colour = self.unmatchedColour
                    colourTExt = self.unmatchedColourText

                    self.m_gridCurrentBets.SetCellBackgroundColour(row, 0, colour)
                    self.m_gridCurrentBets.SetCellTextColour(row, 0, colourText)

            self.m_gridCurrentBets.Refresh()


    def ContextMenuCurrentBets(self, exchangeId, position):
        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)
        treeItem, hitTestFlags = treeCtrl.HitTest(position)

        if not treeItem.IsOk():
            self.m_menuCurrentBetsLoadMarket.Enable(False)
            self.m_menuItemCurrentBetsCancelBet.Enable(False)
            self.m_menuItemCurrentBetsModifyBet.Enable(False)
        else:
            self.m_menuCurrentBetsLoadMarket.Enable(True)
            data = treeCtrl.GetPyData(treeItem)
            if hasattr(data, 'fullMarketName'):
                bet = data
                if bet.betStatus == 'U':
                    self.m_menuItemCurrentBetsCancelBet.Enable(True)
                    self.m_menuItemCurrentBetsModifyBet.Enable(True)
                else:
                    self.m_menuItemCurrentBetsCancelBet.Enable(False)
                    self.m_menuItemCurrentBetsModifyBet.Enable(False)
            else:
                self.m_menuItemCurrentBetsCancelBet.Enable(False)
                self.m_menuItemCurrentBetsModifyBet.Enable(False)

        self.m_menuCurrentBetsUK.treeItem = treeItem
        self.m_menuCurrentBetsUK.exchangeId = exchangeId
        treeCtrl.PopupMenu(self.m_menuCurrentBetsUK, position)


    def m_treeCtrlCurrentBetsUKOnContextMenu(self, event):
        self.ContextMenuCurrentBets(bfpy.ExchangeUK,
                                    event.GetPosition())


    def m_treeCtrlCurrentBetsAusOnContextMenu(self, event):
        self.ContextMenuCurrentBets(bfpy.ExchangeAus,
                                    event.GetPosition())


    def OnMenuSelectionCurrentBetsLoadMarket(self, event):
        treeItem = self.m_menuCurrentBetsUK.treeItem
        exchangeId = self.m_menuCurrentBetsUK.exchangeId
        self.CurrentBetsLoadMarket(exchangeId, treeItem)


    def OnMenuSelectionCurrentBetsCancelBet(self, event):
        treeItem = self.m_menuCurrentBetsUK.treeItem
        exchangeId = self.m_menuCurrentBetsUK.exchangeId

        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)
        bet = treeCtrl.GetPyData(treeItem)

        cancelBet = self.BfCreateCancelBet()
        cancelBet.betId = bet.betId
        marketTuple = bfobj.MarketTuple(bet.exchangeId, bet.marketId)

        self.CancelBets(marketTuple, [cancelBet])


    def OnMenuSelectionCurrentBetsModifyBet(self, event):
        treeItem = self.m_menuCurrentBetsUK.treeItem
        exchangeId = self.m_menuCurrentBetsUK.exchangeId

        treeCtrl = self.GetTreeCtrlCurrentBets(exchangeId)
        bet = treeCtrl.GetPyData(treeItem)

        showDlg = self.verifyBets
        self.VisualPlaceBet(bet.selectionId,
                            bet.asianLineId,
                            bet.betType,
                            bet.price,
                            bet.remainingSize,
                            self.persistenceType[bet.betPersistenceType],
                            updating=True,
                            showDlg=showDlg,
                            bet=bet,
                            selectionName=bet.selectionName)
