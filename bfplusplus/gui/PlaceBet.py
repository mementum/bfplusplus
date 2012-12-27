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
"""Subclass of PlaceBet, which is generated by wxFormBuilder."""

import MainGui

import wx

from bfobj import Compensation

# Implementing PlaceBet
class PlaceBet(MainGui.PlaceBet):

    betTypeLegend = {'B': 'Backing', 'L': 'Laying'}
    updateTypeLegend = {'B': 'Modify Back for', 'L': 'Modify Lay for'}

    def __init__(self, parent, betType):
	MainGui.PlaceBet.__init__(self, parent)

        self.betType = betType
        self.updating = False

        self.myparent = self.GetParent()


    def SetPersistence(self, persistence, inPlay):
        self.m_checkBoxKeepInPlay.Enable(inPlay == False)
        self.persistence = persistence
        self.m_checkBoxKeepInPlay.SetValue(self.persistence)


    def SetDetails(self, selectionId, runnerName, betType, price, size, updating=False):
        self.selectionId = selectionId
        self.betType = betType
        self.price = price
        self.size = size
        self.updating = updating

        self.m_textCtrlPrice.SetValue('%.2f' % self.price)
        self.m_textCtrlSize.SetValue('%.2f' % self.size)

        if not self.updating:
            label = '%s %s' % (self.betTypeLegend[betType], runnerName)
        else:
            self.SetTitle('Modify Bet')
            label = '%s %s' % (self.updateTypeLegend[betType], runnerName)

        self.m_staticTextBetType.SetLabel(label)

        self.UpdateDisplay()


    def UpdateDisplay(self):
	try:
	    price = float(self.m_textCtrlPrice.GetValue())
            size = float(self.m_textCtrlSize.GetValue())

            if price <1.00 or price > 1000.0:
                raise AttributeError

            if self.betType == 'L':
                risk = (price - 1.0) * size
                profit = size
            else: # back
                risk = size
                profit = size * (price - 1.0)

            riskStr = '%.2f' % risk
            profitStr = '%.2f' % profit

            comp = Compensation(self.selectionId, self.betType, price, size)
            self.myparent.curCompensation = comp
                
	except:
            riskStr = ''
            profitStr = ''
            self.myparent.curCompensation = None

        self.myparent.UpdateMarketProfitAndLoss(self.myparent.marketTuple, whatIf=True)

        self.m_staticTextRisk.SetLabel(u'\u20ac %s' %  riskStr)
        self.m_staticTextProfit.SetLabel(u'\u20ac %s' % profitStr)


    def OnTextPrice(self, event):
        self.UpdateDisplay()
	event.Skip()


    def OnTextSize(self, event):
        self.UpdateDisplay()
	event.Skip()


    def OnButtonClickPlaceBet(self, event):
        event.Skip()
        
        try:
            price = float(self.m_textCtrlPrice.GetValue())
            size = float(self.m_textCtrlSize.GetValue())
        except:
            wx.MessageBox( 'Wrong number in either price or stake', 'Error')
            return

        if self.updating == True:
            if price != self.price and size != self.size:
                wx.MessageBox( 'Both odds and stake may not be modified when updating a bet', 'Error')
                return

            # self.oldPrice = self.price
             #self.oldSize = self.size

        self.price = price
        self.size = size
        self.persistence = self.m_checkBoxKeepInPlay.GetValue()

        self.myparent.curCompensation = None
        self.myparent.UpdateMarketProfitAndLoss(self.myparent.marketTuple, whatIf=True)

        self.EndModal(wx.ID_OK)


    def OnButtonClickCancel(self, event):
        self.myparent.curCompensation = None
        self.myparent.UpdateMarketProfitAndLoss(self.myparent.marketTuple)

        self.EndModal(wx.ID_CANCEL)



        