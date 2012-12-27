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

from datetime import datetime
import time

import wx

if True:
    def init(self):
        self.stopBetSusp = False
        self.stopBetSuspStamp = 0

        self.stopBetPerc = self.config.ReadInt('StopBet Perc', 15)
        self.UpdateStopBetThings()

        self.stopbetGuard = self.config.ReadInt('StopBet Guard', 7)
        self.config.WriteInt('StopBet Guard', self.stopbetGuard)
        self.m_spinCtrlStopBetSuspGuard.SetValue(self.stopbetGuard)

        self.m_listCtrlStopBets.InsertColumn(0, 'Time')
        self.m_listCtrlStopBets.InsertColumn(1, 'Type')
        self.m_listCtrlStopBets.InsertColumn(2, 'Bet Id')
        self.m_listCtrlStopBets.InsertColumn(3, '%')
        self.m_listCtrlStopBets.InsertColumn(4, 'Threshold')
        self.m_listCtrlStopBets.InsertColumn(5, 'Status')
        self.m_listCtrlStopBets.InsertColumn(6, 'Comment')

        charLen = [20, 14, 12, 5, 10, 9, 50]
        for i in range(self.m_listCtrlStopBets.GetColumnCount()):
            self.m_listCtrlStopBets.SetColumnWidth(i, charLen[i] * self.avgCharWidth)

        self.RegisterFocusWin(self.m_listCtrlStopBets)


    def OnSpinCtrlStopBetGuard(self, event):
        event.Skip()
        self.stopbetGuard = self.m_spinCtrlStopBetSuspGuard.GetValue()
        self.config.WriteInt('StopBet Guard', self.stopbetGuard)
        

    def OnScrollStopBet(self, event):
        event.Skip()
        newPos = event.GetPosition()
        oldPos = int(self.m_staticTextStopBet.GetLabel().rstrip('%'))

        posAvg = (newPos + oldPos)/2
        posDiff = abs(newPos - oldPos)

        if posAvg == 50 and posDiff <= 2:
            newPos = 50

        self.stopBetPerc = newPos
        self.UpdateStopBetThings()


    def OnMenuSelectionSliderStopBet(self, event):
        event.Skip()
        itemId = event.GetId()
        menuItems = self.m_menuSliderStopBet.GetMenuItems()

        for menuItem in menuItems:
            if itemId == menuItem.GetId():
                stopBetPercStr = menuItem.GetLabel()
                self.stopBetPerc = int(stopBetPercStr.rstrip('%'))
                self.UpdateStopBetThings()
                break


    def UpdateStopBetThings(self):
        self.m_sliderStopBet.SetValue(self.stopBetPerc)
        self.m_staticTextStopBet.SetLabel('%d%%' % self.stopBetPerc)
        self.config.WriteInt('StopBet Perc', self.stopBetPerc)


    def AddStopBet(self, action, bet):
        if self.marketTuple is None:
            return
        marketComp = self.marketCache[self.marketTuple]
        stopbetinfo = marketComp.AddStopBet(action, bet, self.stopBetPerc)
        self.UpdateStopBet(stopbetinfo, addBetInfo=True)


    def UpdateStopBet(self, stopbetinfo, addBetInfo=False):
        if addBetInfo:
            timeStr = stopbetinfo.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            self.m_listCtrlStopBets.InsertStringItem(0, timeStr)
            self.m_listCtrlStopBets.SetItemData(0, stopbetinfo.idx)
            self.m_listCtrlStopBets.SetStringItem(0, 0, timeStr)
            self.m_listCtrlStopBets.SetStringItem(0, 1, stopbetinfo.action)
            self.m_listCtrlStopBets.SetStringItem(0, 2, '%d' % stopbetinfo.bet.betId)
            self.m_listCtrlStopBets.SetStringItem(0, 3, '%d%%' % stopbetinfo.stopPerc)
            self.m_listCtrlStopBets.SetStringItem(0, 4, '%d' % stopbetinfo.threshold)
            self.m_listCtrlStopBets.SetStringItem(0, 5, stopbetinfo.status)
            self.m_listCtrlStopBets.SetStringItem(0, 6, stopbetinfo.comment)
            return

        for i in xrange(self.m_listCtrlStopBets.GetItemCount()):
            if stopbetinfo.idx == self.m_listCtrlStopBets.GetItemData(i):
                timeStr = stopbetinfo.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                self.m_listCtrlStopBets.SetStringItem(i, 0, timeStr)
                self.m_listCtrlStopBets.SetStringItem(i, 1, stopbetinfo.action)
                self.m_listCtrlStopBets.SetStringItem(i, 2, '%d' % stopbetinfo.bet.betId)
                self.m_listCtrlStopBets.SetStringItem(i, 3, '%d%%' % stopbetinfo.stopPerc)
                self.m_listCtrlStopBets.SetStringItem(i, 4, '%d' % stopbetinfo.threshold)
                self.m_listCtrlStopBets.SetStringItem(i, 5, stopbetinfo.status)
                self.m_listCtrlStopBets.SetStringItem(i, 6, stopbetinfo.comment)
                break


    def FillStopBetCtrl(self):
        self.m_listCtrlStopBets.DeleteAllItems()

        if self.marketTuple is None:
            return
        marketComp = self.marketCache[self.marketTuple]
        for stopbetinfo in marketComp.stopbetinfos:
            self.UpdateStopBet(stopbetinfo, addBetInfo=True)
    

    def OnMenuSelectionStopBetProfitProfit(self, event):
        event.Skip()
        self.AddStopBet('profitOnProfit', self.m_menuListBets.bet)


    def OnMenuSelectionStopBetProfitRisk(self, event):
        event.Skip()
        self.AddStopBet('profitOnRisk', self.m_menuListBets.bet)


    def OnMenuSelectionStopBetLossProfit(self, event):
        event.Skip()
        self.AddStopBet('lossOnProfit', self.m_menuListBets.bet)


    def OnMenuSelectionStopBetLossRisk(self, event):
        event.Skip()
        self.AddStopBet('lossOnRisk', self.m_menuListBets.bet)


    def StopBetsStop(self):
        if self.marketTuple is None:
            return
        marketComp = self.marketCache[self.marketTuple]
        for stopbetinfo in marketComp.stopbetinfos:
            stopbetinfo.status = 'voided'
            self.UpdateStopBet(stopbetinfo)


    def StopBetCheck(self):
        timeSinceSusp = time.clock() - self.stopBetSuspStamp
        if timeSinceSusp < self.stopbetGuard:
            # Do nothing if the market was suspended recently
            return

        # Get a market reference
        if self.marketTuple is None:
            return

        marketComp = self.marketCache[self.marketTuple]
        for stopbetinfo in marketComp.stopbetinfos:
            if stopbetinfo.status != 'active':
                # Do nothing for those that are not active
                continue

            bet = stopbetinfo.bet
            if not marketComp.getMatchedBetById(bet.betId):
                # Bet is no longer active
                stopbetinfo.status = 'voided'
                # Update the display
                self.UpdateStopBet(stopbetinfo)
                # And carry on
                continue

            runnerPrices = marketComp.getRunnerPricesId(bet.selectionId, bet.asianLineId)
            if not runnerPrices:
                # Can't make a bet against non existing prices
                return

            # Calculate the current compensation
            comp = bet.getCompensate(runnerPrices, stopbetinfo.compPerc)

            # And check if the bet has to be stopped
            if not stopbetinfo.checkThreshold(comp.compWin):
                continue

            # Create and fill in a bet
            placeBet = self.BfCreatePlaceBet()
            placeBet.price = comp.price
            placeBet.size = comp.size
            placeBet.betType = comp.betType
            persistence = True
            placeBet.betPersistenceType = self.persistenceEnum[persistence]

            placeBet.marketId = marketComp.marketId
            placeBet.asianLineId = bet.asianLineId
            placeBet.selectionId = bet.selectionId

            # Place the bet
            self.LogMessages('Stop bet %d executed for betId %d' % (stopbetinfo.idx, bet.betId))
            self.PlaceBets(self.marketTuple, [placeBet])

            # Change the status of the stop bet
            stopbetinfo.status = 'executed'
            timeStr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            stopbetinfo.comment = 'Executed at %s' % timeStr

            # Update the display
            self.UpdateStopBet(stopbetinfo)


    def m_listCtrlStopBetsOnContextMenu(self, event):
        position = event.GetPosition()
        itemId, hitFlags = self.m_listCtrlStopBets.HitTest(position)

        found = (itemId != wx.NOT_FOUND)
        if not found:
            return

        idx = self.m_listCtrlStopBets.GetItemData(itemId)
        if self.marketTuple is None:
            return
        marketComp = self.marketCache[self.marketTuple]
        stopbetinfo = None
        for stopbet in marketComp.stopbetinfos:
            if idx == stopbet.idx:
                stopbetinfo = stopbet
                break

        if stopbetinfo is None:
            return

        if stopbetinfo.status == 'active':
            self.m_menuItemStopBetPause.Enable()
            self.m_menuItemStopBetRestart.Enable(False)
            self.m_menuItemStopBetCancel.Enable()
        elif stopbetinfo.status == 'paused':
            self.m_menuItemStopBetPause.Enable(False)
            self.m_menuItemStopBetRestart.Enable()
            self.m_menuItemStopBetCancel.Enable()
        elif stopbetinfo.status == 'voided':
            self.m_menuItemStopBetPause.Enable(False)
            self.m_menuItemStopBetRestart.Enable()
            self.m_menuItemStopBetCancel.Enable(False)
        elif stopbetinfo.status == 'executed':
            self.m_menuItemStopBetPause.Enable(False)
            self.m_menuItemStopBetRestart.Enable(False)
            self.m_menuItemStopBetCancel.Enable(False)
        else:
            self.m_menuItemStopBetPause.Enable(False)
            self.m_menuItemStopBetRestart.Enable(False)
            self.m_menuItemStopBetCancel.Enable(False)

        self.m_listCtrlStopBets.stopbetinfo = stopbetinfo
        self.m_listCtrlStopBets.PopupMenu(self.m_menuStopBet, position)


    def OnMenuSelectionStopBetPause(self, event):
        event.Skip()
        stopbetinfo = self.m_listCtrlStopBets.stopbetinfo
        stopbetinfo.status = 'paused'
        self.UpdateStopBet(stopbetinfo)


    def OnMenuSelectionStopBetRestart(self, event):
        event.Skip()
        stopbetinfo = self.m_listCtrlStopBets.stopbetinfo
        stopbetinfo.status = 'active'
        self.UpdateStopBet(stopbetinfo)


    def OnMenuSelectionStopBetCancel(self, event):
        event.Skip()
        stopbetinfo = self.m_listCtrlStopBets.stopbetinfo
        stopbetinfo.status = 'voided'
        self.UpdateStopBet(stopbetinfo)
