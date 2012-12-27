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

import wx

from gui.EditStringList import EditStringList

if True:
    def init(self):
        self.verifyBets = self.config.ReadBool('Verify Bets', True)
        self.config.WriteBool('Verify Bets', self.verifyBets)
        self.m_checkBoxVerifyBets.SetValue(self.verifyBets)

        self.m_checkBoxVerifyRClickBets.Enable(self.verifyBets)

        self.verifyRClickBets = self.config.ReadBool('Verify Right Click Bets', False)
        self.config.WriteBool('Verify Right Click Bets', self.verifyRClickBets)
        self.m_checkBoxVerifyRClickBets.SetValue(self.verifyRClickBets)

        self.singleClick = self.config.ReadBool('Single Click Betting', False)
        self.config.WriteBool('Single Click Betting', self.singleClick)
        self.m_checkBoxSingleClickBetting.SetValue(self.singleClick)

        self.stakeIsLiability = self.config.ReadBool('Stake is Liability', False)
        self.config.WriteBool('Stake is Liability', self.stakeIsLiability)
        self.m_checkBoxSingleClickLiability.SetValue(self.stakeIsLiability)

        self.fillOrKill = self.config.ReadBool('Fill Or Kill', False)
        self.config.WriteBool('Fill Or Kill', self.fillOrKill)
        self.m_checkBoxFillOrKill.SetValue(self.fillOrKill)

        self.fillOrKillTime = self.config.ReadInt('Fill Or Kill - Time', 15)
        self.config.WriteInt('Fill Or Kill - Time', self.fillOrKillTime)
        self.m_spinCtrlFillOrKill.SetValue(self.fillOrKillTime)

        self.betTicksAway = self.config.ReadBool('Bet Ticks Away', False)
        self.config.WriteBool('Bet Ticks Away', self.betTicksAway)
        self.m_checkBoxTicksAway.SetValue(self.betTicksAway)

        self.compTicksAway = self.config.ReadBool('Comp Ticks Away', False)
        self.config.WriteBool('Comp Ticks Away', self.compTicksAway)
        self.m_checkBoxCompAway.SetValue(self.compTicksAway)

        self.betTicksAwayCount = self.config.ReadInt('Bet Ticks Away - Count', 0)
        self.config.WriteInt('Bet Ticks Away - Count', self.betTicksAwayCount)
        self.m_spinCtrlTicksFromPrice.SetValue(self.betTicksAwayCount)

        self.compTicksAwayCount = self.config.ReadInt('Comp Ticks Away - Count', 0)
        self.config.WriteInt('Comp Ticks Away - Count', self.compTicksAwayCount)
        self.m_spinCtrlTicksFromComp.SetValue(self.compTicksAwayCount)


    def OnCheckBoxTicksAway(self, event):
        self.betTicksAway = self.m_checkBoxTicksAway.GetValue()
        self.config.WriteBool('Bet Ticks Away', self.betTicksAway)


    def OnCheckBoxCompAway(self, event):
        self.compTicksAway = self.m_checkBoxCompAway.GetValue()
        self.config.WriteBool('Comp Ticks Away', self.compTicksAway)
        if self.compTicksAway:
            self.UpdateCompensations(self.compPerc)


    def OnSpinCtrlTicksFromPrice(self, event):
        self.betTicksAwayCount = self.m_spinCtrlTicksFromPrice.GetValue()
        self.config.WriteInt('Bet Ticks Away - Count', self.betTicksAwayCount)


    def OnSpinCtrlTicksFromComp(self, event):
        self.compTicksAwayCount = self.m_spinCtrlTicksFromComp.GetValue()
        self.config.WriteInt('Comp Ticks Away - Count', self.compTicksAwayCount)
        if self.compTicksAway:
            self.UpdateCompensations(self.compPerc)


    def OnCheckBoxVerifyBets(self, event):
        self.verifyBets = self.m_checkBoxVerifyBets.GetValue()
        self.config.WriteBool('Verify Bets', self.verifyBets)

        self.m_checkBoxVerifyRClickBets.Enable(self.verifyBets)


    def OnCheckBoxVerifyRClickBets(self, event):
        self.verifyRClickBets = self.m_checkBoxVerifyRClickBets.GetValue()
        self.config.WriteBool('Verify Right Click Bets', self.verifyRClickBets)


    def OnCheckBoxSingleClickBetting(self, event):
        self.singleClick = self.m_checkBoxSingleClickBetting.GetValue()
        self.config.WriteBool('Single Click Betting', self.singleClick)


    def OnCheckBoxSingleClickBettingStakeLiability(self, event):
        self.stakeIsLiability = self.m_checkBoxSingleClickLiability.GetValue()
        self.config.WriteBool('Stake is Liability', self.stakeIsLiability)


    def OnCheckBoxFillOrKill(self, event):
        self.fillOrKill = self.m_checkBoxFillOrKill.GetValue()
        self.config.WriteBool('Fill Or Kill', self.fillOrKill)


    def OnSpinCtrlFillOrKill(self, event):
        self.fillOrKillTime = self.m_spinCtrlFillOrKill.GetValue()
        self.config.WriteInt('Fill Or Kill - Time', self.fillOrKillTime)


    def OnButtonClickQuickStakes(self, event):
        event.Skip()
        # btn = event.GetEventObject()
        btn = self.m_buttonQuickStakes

        btnSize = btn.GetSize()
        # Get position
        btnPt = btn.GetPosition()
        # Use parent to translate to screen coordinates
        btnPt = btn.GetParent().ClientToScreen(btnPt)
        # The main frame will display the menu, so coordinates have to be main frame-client area relative
        btnPt = self.ScreenToClient(btnPt)

        popUpMenu = wx.Menu()

        mItem = wx.MenuItem(popUpMenu, wx.ID_ANY, 'Edit Stakes ...', '', wx.ITEM_NORMAL)
        popUpMenu.AppendItem(mItem)
        self.Bind(wx.EVT_MENU, self.OnMenuSelectionEditGridMarketStakes, id=mItem.GetId())

        mItem = wx.MenuItem(popUpMenu, wx.ID_ANY, 'Default Stakes', '', wx.ITEM_NORMAL)
        popUpMenu.AppendItem(mItem)
        self.Bind(wx.EVT_MENU, self.OnMenuSelectionDefaultGridMarketStakes, id=mItem.GetId())

        popUpMenu.AppendSeparator()

        menuIds = list()
        for stake in self.bettingStakes:
            mItem = wx.MenuItem(popUpMenu, wx.ID_ANY, str(stake), '', wx.ITEM_CHECK)
            popUpMenu.AppendItem(mItem)
            mId = mItem.GetId()
            menuIds.append(mId)
            self.Bind(wx.EVT_MENU, self.OnMenuSelectionStake, id=mId)

            if stake == self.singleClickStake:
                popUpMenu.Check(mItem.GetId(), True)

        btnPt.y += btnSize.height
        self.PopupMenu(popUpMenu, btnPt)

        for mId in menuIds:
            self.Unbind(wx.EVT_MENU, id=mId)


    def OnMenuSelectionStake(self, event):
        event.Skip()

        menuId = event.GetId()
        menu = event.GetEventObject()
        mItems = menu.GetMenuItems()

        for mItem in mItems:
            if menuId == mItem.GetId():
                stakeStr = mItem.GetLabel()
                self.singleClickStake = float(stakeStr)
                self.config.WriteFloat('Single Click Stake', self.singleClickStake)
                self.m_buttonQuickStakes.SetLabel(stakeStr)
                break


