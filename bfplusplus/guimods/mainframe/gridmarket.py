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

from cStringIO import StringIO

import wx
from wx.lib.pubsub import setupkwargs
from wx.lib.pubsub import pub

from gui.EditStringList import EditStringList
from gui.RunnerAction import RunnerAction

import bfpy
from bfobj import Compensation
from util import Message

if True:
    def init(self):
        self.runnerAction = None

        self.numPrices = 3

        self.colBackStart = 0
        self.colBackEnd = self.colBackStart + (self.numPrices - 1)
        self.colLayStart = self.colBackEnd + 1
        self.colLayEnd = self.colLayStart + (self.numPrices - 1)
        self.colOverroundBack = 1
        self.colOverroundLay = self.colOverroundBack + self.numPrices
        self.colBackLegend = 2
        self.colLayLegend = 3
    
        self.colGridBalance = self.colLayEnd + 1
        self.colGridBalanceRef = self.colGridBalance + 1

        showProb = self.config.ReadBool('Show Probability', False)
        self.config.WriteBool('Show Probability', showProb)
        self.m_checkBoxDisplayPercPrices.SetValue(showProb)

        self.bettingStakesDefault = [2.0, 4.0, 8.0, 10.0, 20.0, 25.0, 50.0, 100.0, 200.0,
                                     250.0, 300.0, 500.0, 750.0, 1000.0, 1500.0, 2000.0]
        self.bettingStakes = self.config.Read('Betting Stakes', str(self.bettingStakesDefault))
        self.bettingStakes = eval(self.bettingStakes)
        self.config.Write('Betting Stakes', str(self.bettingStakes))

        self.singleClickStake = self.config.ReadFloat('Single Click Stake', self.bettingStakes[0])
        self.config.WriteFloat('Single Click Stake', self.singleClickStake)
        self.m_buttonQuickStakes.SetLabel(str(self.singleClickStake))

        # See discussion at for these four windows need to react to the event
        # http://bytes.com/topic/python/answers/430042-wxgrid-focus-event
        self.RegisterFocusWin(self.m_gridMarket.GetGridWindow())
        self.RegisterFocusWin(self.m_gridMarket.GetGridCornerLabelWindow())
        self.RegisterFocusWin(self.m_gridMarket.GetGridColLabelWindow())
        self.RegisterFocusWin(self.m_gridMarket.GetGridRowLabelWindow())

        self.m_gridMarket.SetSelectionMode(wx.grid.Grid.SelectCells)

        self.compIndex = None
        self.curCompensation = None


    def OnGridCellRightClick(self, event):
        event.Skip()
        # Gather data
        row = event.GetRow()
        col = event.GetCol()
        position = event.GetPosition()
        marketComp = self.marketCache[self.marketTuple]
        runner = marketComp.runners[row]
        runnerPrices = marketComp.getRunnerPrices(runner)

        fakeComps = False

        if col == self.colGridBalanceRef:
            return

        elif col <= self.colLayEnd:
            if col < self.colLayStart:
                betType = 'B'
                # Find out if this column has a back price
                priceIndex = self.colBackEnd - col
                if runnerPrices:
                    bestPrices = runnerPrices.bestPricesToBack
                else:
                    bestPrices = None
                price = 1000.0
            else:
                betType = 'L'
                priceIndex = col - self.colLayStart
                if runnerPrices:
                    bestPrices = runnerPrices.bestPricesToLay
                else:
                    bestPrices = None
                price = 1.01

            if bestPrices:
                numPrices = len(bestPrices)
            else:
                numPrices = 0

            # Use the selected column or the next best price (if available)
            while numPrices and priceIndex >= 0:
                if numPrices > priceIndex:
                    price = bestPrices[priceIndex].price
                    break
                priceIndex -= 1

            fakeComps = True
            compensations = list()
            ticksAway = self.betTicksAwayCount if self.betTicksAway else 0
            price = bfpy.GetPriceTicks(price, ticksAway, betType)

            for stake in self.bettingStakes:
                if betType == 'L' and self.stakeIsLiability:
                    size = stake / (price - 1.0)
                    size = '%.2f' % size
                    size = float(size)
                else:
                    size = stake

                compensation = Compensation(runner.selectionId, betType, price, size, asianLineId=runner.asianLineId)
                compensation.fake = True
                compensations.append(compensation)
            titleLabel = 'Bet on %s ... (Selection Bet Wins/Loses)' % marketComp.getRunnerLabel(runner)

        elif col == self.colGridBalance:
            compensations = marketComp.compensations[runner.selectionId]
            titleLabel = 'Compensate %s with a ... (Result Bet Wins/Loses)' % marketComp.getRunnerLabel(runner)

        if not compensations:
            return

        menuBalance = wx.Menu()
        menuBalance.SetTitle(titleLabel)

        menuItem = wx.MenuItem(menuBalance, wx.ID_ANY, 'Edit Stakes ...', 'Edit Stakes ...', wx.ITEM_NORMAL)
        fakeCompMenuId = menuItem.GetId()
        self.Bind(wx.EVT_MENU, self.OnMenuSelectionEditGridMarketStakes, id=fakeCompMenuId)
        self.Bind(wx.EVT_MENU_HIGHLIGHT, self.OnMenuSelectionEditGridMarketStakesHighlight, id=fakeCompMenuId)
        menuBalance.AppendItem(menuItem)
        menuItem.Enable(fakeComps)

        menuItem = wx.MenuItem(menuBalance, wx.ID_ANY, 'Default Stakes', 'Default Stakes', wx.ITEM_NORMAL)
        fakeCompMenuId2 = menuItem.GetId()
        self.Bind(wx.EVT_MENU, self.OnMenuSelectionDefaultGridMarketStakes, id=fakeCompMenuId2)
        self.Bind(wx.EVT_MENU_HIGHLIGHT, self.OnMenuSelectionDefaultGridMarketStakesHighlight, id=fakeCompMenuId2)
        menuBalance.AppendItem(menuItem)
        menuItem.Enable(fakeComps)

        menuBalance.AppendSeparator()

        self.compensations = dict()
        for comp in compensations:
            if comp.size < self.minStakes.minimumStake:
                continue

            label = marketComp.getRunnerLabelById(comp.selectionId)
            
            menuBaseStr = u'%s of %s %.2f @ %.2f for %.2f/%.2f'
            menuStr = menuBaseStr % (self.betTypeLegend[comp.betType], label, comp.size, comp.price, comp.compWin, comp.compLoss)
            menuItem = wx.MenuItem(menuBalance, wx.ID_ANY, menuStr, menuStr, wx.ITEM_NORMAL)
            menuBalance.AppendItem(menuItem)

            compId = menuItem.GetId()
            self.compensations[compId] = comp

            # I need to associate the compensation with the menu id
            self.Bind(wx.EVT_MENU, self.OnMenuSelectionBalance, id=compId)
            self.Bind(wx.EVT_MENU_HIGHLIGHT, self.OnMenuSelectionBalanceHighlight, id=compId)

        # self.m_gridMarket.PopupMenu(menuBalance, position)
        # The only way to get HIGHLIGHT handled is to popup the menu from the frame
        position = self.ScreenToClient(self.m_gridMarket.ClientToScreen(position))
        self.PopupMenu(menuBalance, position)

        self.curCompensation = None
        self.UpdateMarketProfitAndLoss(self.marketTuple, whatIf=True)

        # XXX: Unbinding too early??? It does not seem so
        self.Unbind(wx.EVT_MENU, id=fakeCompMenuId)
        self.Unbind(wx.EVT_MENU_HIGHLIGHT, id=fakeCompMenuId)
        self.Unbind(wx.EVT_MENU, id=fakeCompMenuId2)
        self.Unbind(wx.EVT_MENU_HIGHLIGHT, id=fakeCompMenuId2)
            
        for compId in self.compensations:
            self.Unbind(wx.EVT_MENU, id=compId)
            self.Unbind(wx.EVT_MENU_HIGHLIGHT, id=compId)


    def OnMenuSelectionEditGridMarketStakes(self, event):
        dlg = EditStringList(self, values=self.bettingStakes, valueType=float)

        if dlg.ShowModal() != wx.ID_OK:
            return

        self.bettingStakes = dlg.values
        self.config.Write('Betting Stakes', str(self.bettingStakes))

        if self.singleClickStake not in self.bettingStakes:
            self.singleClickStake = self.bettingStakes[0]
            self.config.WriteFloat('Single Click Stake', self.singleClickStake)
            self.m_buttonQuickStakes.SetLabel(stakeStr)


    def OnMenuSelectionDefaultGridMarketStakes(self, event):
        self.bettingStakes = self.bettingStakesDefault
        self.config.Write('Betting Stakes', str(self.bettingStakes))

        if self.singleClickStake not in self.bettingStakes:
            self.singleClickStake = self.bettingStakes[0]
            self.config.WriteFloat('Single Click Stake', self.singleClickStake)
            self.m_buttonQuickStakes.SetLabel(stakeStr)


    def OnMenuSelectionEditGridMarketStakesHighlight(self, event):
        self.curCompensation = None
        self.UpdateMarketProfitAndLoss(self.marketTuple, whatIf=True)


    def OnMenuSelectionDefaultGridMarketStakesHighlight(self, event):
        self.curCompensation = None
        self.UpdateMarketProfitAndLoss(self.marketTuple, whatIf=True)


    def OnMenuSelectionBalance(self, event):
        compId = event.GetId()
        comp = self.compensations[compId]

        # Changed to default False to avoid errors (see Issue #2)
        persistence = True
        showDlg = self.verifyBets and self.verifyRClickBets

        price = comp.price
        self.VisualPlaceBet(selectionId=comp.selectionId, asianLineId=comp.asianLineId,
                            betType=comp.betType, price=price, size=comp.size,
                            persistence=persistence, updating=False, showDlg=showDlg)


    def OnMenuSelectionBalanceHighlight(self, event):
        compId = event.GetMenuId()
        self.curCompensation = self.compensations[compId]

        self.UpdateMarketProfitAndLoss(self.marketTuple, whatIf=True)


    def OnGridCellLeftClick(self, event):
        row = event.GetRow()
        col = event.GetCol()

        if self.marketTuple is not None:
            marketComp = self.marketCache[self.marketTuple]
            numberOfWinners = marketComp.numberOfWinners
        else:
            numberOfWinners = 0

        if col == self.colGridBalanceRef and numberOfWinners == 1:
            if self.compIndex is None:
                self.compIndex == -1
            if row != self.compIndex:
                self.m_gridMarket.SetCellValue(self.compIndex, self.colGridBalanceRef, u'')
                self.compIndex = row
                self.m_gridMarket.SetCellValue(self.compIndex, self.colGridBalanceRef, u'\u25A0')

                compPerc = self.m_sliderCompensate.GetValue()
                compPerc /= 100.0
                marketComp.updatePnLCompensations(compPerc, self.compIndex)
                self.UpdateMarketProfitAndLoss(self.marketTuple)
                event.Skip()
                return

        elif not self.singleClick:
            event.Skip()
            return

        event.Skip()
        self.GridBet(event)


    def OnGridCellLeftDClick(self, event):
        event.Skip()
        stake = self.singleClickStake
        self.GridBet(event)


    def GridBet(self, event):
        # Gather data
        row = event.GetRow()
        col = event.GetCol()
        marketComp = self.marketCache[self.marketTuple]
        runner = marketComp.runners[row]
        runnerPrices = marketComp.getRunnerPrices(runner)

        if col >= self.colGridBalance:
            return

        size = self.singleClickStake

        if col < self.colLayStart:
            betType = 'B'
            # Find out if this column has a back price
            priceIndex = self.colBackEnd - col
            bestPrices = runnerPrices.bestPricesToBack
            price = 1000.0
        else:
            betType = 'L'
            priceIndex = col - self.colLayStart
            bestPrices = runnerPrices.bestPricesToLay
            price = 1.01

        numPrices = len(bestPrices)

        # Use the selected column or the next best price (if available)
        while priceIndex >= 0:
            if numPrices > priceIndex:
                price = bestPrices[priceIndex].price
                break
            priceIndex -= 1

        # single click betting
        if betType == 'L' and self.stakeIsLiability:
            size = size / (price - 1.0)
            size = '%.2f' % size
            size = float(size)

        showDlg = self.verifyBets

        ticksAway = self.betTicksAwayCount if self.betTicksAway else 0
        price = bfpy.GetPriceTicks(price, ticksAway, betType)
        self.VisualPlaceBet(selectionId=runner.selectionId, asianLineId=runner.asianLineId,
                            betType=betType, price=price, size=size,
                            persistence=False, updating=False, showDlg=showDlg)


    def OnGridLabelLeftClick(self, event):
        pass


    def OnGridLabelLeftDClick(self, event):
        # Open the dialog (and if open, tell it to display what we want)

        if self.marketTuple is None:
            return

        if self.runnerAction is None:
            self.runnerAction = RunnerAction(self)
            self.runnerAction.Center()
            self.runnerAction.Show()

        self.runnerAction.Raise()

        marketComp = self.marketCache[self.marketTuple]
        selection = event.GetRow()
        pub.sendMessage('runner.action',
                        marketComp=marketComp, selection=selection)
        

    def OnRunnerActionBitmap(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if exception:
            self.LogMessages(exception)
            return

        pub.sendMessage('runner.actionbitmap', imageStream=StringIO(response))


    def OnRunnerActionTradedVolume(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if exception:
            self.LogMessages(exception)
            return

        pub.sendMessage('runner.actiontradedVolume', tradedVolume=response.tradedVolume)


    def OnRunnerActionCompletePrices(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if exception:
            self.LogMessages(exception)
            return

        pub.sendMessage('runner.actioncompletePrices', completePrices=response.completeMarketPrices)
