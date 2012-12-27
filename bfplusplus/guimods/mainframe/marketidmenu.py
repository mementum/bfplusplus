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

if True:

    def m_bitmapExchangeOnContextMenu(self, event):
        if self.BetBuddyBeta:
            self.m_bitmapExchange.PopupMenu(self.m_menuWallet, event.GetPosition())


    def OnMenuSelectionWalletLoadGUIModules(self, event):
        wx.GetApp().LoadAllGuiModules()


    def OnMenuSelectionMarketIdCopyToClipBoard(self, event):
        if self.marketTuple is not None:
            if wx.TheClipboard.Open():
                marketComp = self.marketCache[self.marketTuple]
                marketId = '%d' % marketComp.marketId
                textDataObject = wx.TextDataObject(marketId)
                wx.TheClipboard.AddData(textDataObject)
                wx.TheClipboard.Close()
