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

from gui.CustomizeColours import CustomizeColours

if True:
    def init(self):
        self.whiteColour = wx.TheColourDatabase.Find('WHITE')

        colourRGB = self.config.Read('Colour - Cell Back', '(128, 128, 255)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Cell Back', str(colourRGB))
        self.cellBackColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Cell Back Text', '(0, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Cell Back Text', str(colourRGB))
        self.cellBackColourText = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Cell Lay', '(128, 128, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Cell Lay', str(colourRGB))
        self.cellLayColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Cell Lay Text', '(0, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Cell Lay Text', str(colourRGB))
        self.cellLayColourText = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Cell Matched', '(0, 255, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Cell Matched', str(colourRGB))
        self.matchedColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Cell Matched Text', '(0, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Cell Matched Text', str(colourRGB))
        self.matchedColourText = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Cell Unmatched', '(255, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Cell Unmatched', str(colourRGB))
        self.unmatchedColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Cell Unmatched Text', '(0, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Cell Unmatched Text', str(colourRGB))
        self.unmatchedColourText = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - InPlay', '(0, 255, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - InPlay', str(colourRGB))
        self.inplayColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - InPlay Text', '(255, 255, 255)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - InPlay Text', str(colourRGB))
        self.inplayColourText = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - InPlay Off', '(255, 255, 255)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - InPlay Off', str(colourRGB))
        self.inplayOffColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - InPlay Off Text', '(0, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - InPlay Off Text', str(colourRGB))
        self.inplayOffColourText = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Market Active', '(255, 255, 255)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Market Active', str(colourRGB))
        self.marketActiveColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Market Active Text', '(0, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Market Active Text', str(colourRGB))
        self.marketActiveColourText = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Market SuspClosed', '(255, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Market SuspClosed', str(colourRGB))
        self.marketSuspClosedColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Market SuspClosed Text', '(255, 255, 255)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Market SuspClosed Text', str(colourRGB))
        self.marketSuspClosedColourText = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Network OK', '(255, 255, 255)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Network OK', str(colourRGB))
        self.networkOKColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Network OK Text', '(0, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Network OK Text', str(colourRGB))
        self.networkOKColourText = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Network Errors', '(255, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Network Errors', str(colourRGB))
        self.networkErrorsColour = wx.Colour(*colourRGB)

        colourRGB = self.config.Read('Colour - Network Errors Text', '(0, 0, 0)')
        colourRGB = eval(colourRGB)
        self.config.Write('Colour - Network Errors Text', str(colourRGB))
        self.networkErrorsColourText = wx.Colour(*colourRGB)


    def OnButtonClickCustomizeColours(self, event):
        dlg = CustomizeColours(self)

        dlg.m_colourPickerBack.SetColour(self.cellBackColour)
        dlg.m_colourPickerBackText.SetColour(self.cellBackColourText)

        dlg.m_colourPickerLay.SetColour(self.cellLayColour)
        dlg.m_colourPickerLayText.SetColour(self.cellLayColourText)

        dlg.m_colourPickerMatched.SetColour(self.matchedColour)
        dlg.m_colourPickerMatchedText.SetColour(self.matchedColourText)

        dlg.m_colourPickerUnmatched.SetColour(self.unmatchedColour)
        dlg.m_colourPickerUnmatchedText.SetColour(self.unmatchedColourText)

        dlg.m_colourPickerInPlay.SetColour(self.inplayColour)
        dlg.m_colourPickerInPlayText.SetColour(self.inplayColourText)

        dlg.m_colourPickerInPlayOff.SetColour(self.inplayOffColour)
        dlg.m_colourPickerInPlayOffText.SetColour(self.inplayOffColourText)

        dlg.m_colourPickerMarketActive.SetColour(self.marketActiveColour)
        dlg.m_colourPickerMarketActiveText.SetColour(self.marketActiveColourText)

        dlg.m_colourPickerMarketSuspClosed.SetColour(self.marketSuspClosedColour)
        dlg.m_colourPickerMarketSuspClosedText.SetColour(self.marketSuspClosedColourText)

        dlg.m_colourPickerNetworkOK.SetColour(self.networkOKColour)
        dlg.m_colourPickerNetworkOKText.SetColour(self.networkOKColourText)

        dlg.m_colourPickerNetworkErrors.SetColour(self.networkErrorsColour)
        dlg.m_colourPickerNetworkErrorsText.SetColour(self.networkErrorsColourText)

        dlg.SetSampleColours()

        retcode = dlg.ShowModal()
        if retcode != wx.ID_OK:
            return

        self.cellBackColour = dlg.m_colourPickerBack.GetColour()
        colourRGB = self.cellBackColour.Get()
        self.config.Write('Colour - Cell Back', str(colourRGB))

        self.cellBackColourText = dlg.m_colourPickerBackText.GetColour()
        colourRGB = self.cellBackColourText.Get()
        self.config.Write('Colour - Cell Back Text', str(colourRGB))

        self.cellLayColour = dlg.m_colourPickerLay.GetColour()
        colourRGB = self.cellLayColour.Get()
        self.config.Write('Colour - Cell Lay', str(colourRGB))

        self.cellLayColourText = dlg.m_colourPickerLayText.GetColour()
        colourRGB = self.cellLayColourText.Get()
        self.config.Write('Colour - Cell Lay Text', str(colourRGB))

        self.CellColours()

        self.matchedColour = dlg.m_colourPickerMatched.GetColour()
        colourRGB = self.matchedColour.Get()
        self.config.Write('Colour - Cell Matched', str(colourRGB))

        self.matchedColourText = dlg.m_colourPickerMatchedText.GetColour()
        colourRGB = self.matchedColourText.Get()
        self.config.Write('Colour - Cell Matched Text', str(colourRGB))

        self.unmatchedColour = dlg.m_colourPickerUnmatched.GetColour()
        colourRGB = self.unmatchedColour.Get()
        self.config.Write('Colour - Cell Unmatched', str(colourRGB))

        self.unmatchedColourText = dlg.m_colourPickerUnmatchedText.GetColour()
        colourRGB = self.unmatchedColourText.Get()
        self.config.Write('Colour - Cell Unmatched Text', str(colourRGB))

        self.MuBetsColours()
        self.CurrentBetsColours()

        self.inplayColour = dlg.m_colourPickerInPlay.GetColour()
        colourRGB = self.inplayColour.Get()
        self.config.Write('Colour - InPlay', str(colourRGB))

        self.inplayColourText = dlg.m_colourPickerInPlayText.GetColour()
        colourRGB = self.inplayColourText.Get()
        self.config.Write('Colour - InPlay Text', str(colourRGB))

        self.inplayOffColour = dlg.m_colourPickerInPlayOff.GetColour()
        colourRGB = self.inplayOffColour.Get()
        self.config.Write('Colour - InPlay Off', str(colourRGB))

        self.inplayOffColourText = dlg.m_colourPickerInPlayOffText.GetColour()
        colourRGB = self.inplayOffColourText.Get()
        self.config.Write('Colour - InPlay Off Text', str(colourRGB))

        self.InPlayColours()

        self.marketActiveColour = dlg.m_colourPickerMarketActive.GetColour()
        colourRGB = self.marketActiveColour.Get()
        self.config.Write('Colour - Market Active', str(colourRGB))

        self.marketActiveColourText = dlg.m_colourPickerMarketActiveText.GetColour()
        colourRGB = self.marketActiveColourText.Get()
        self.config.Write('Colour - Market Active Text', str(colourRGB))

        self.marketSuspClosedColour = dlg.m_colourPickerMarketSuspClosed.GetColour()
        colourRGB = self.marketSuspClosedColour.Get()
        self.config.Write('Colour - Market SuspClosed', str(colourRGB))

        self.marketSuspClosedColourText = dlg.m_colourPickerMarketSuspClosedText.GetColour()
        colourRGB = self.marketSuspClosedColourText.Get()
        self.config.Write('Colour - Market SuspClosed Text', str(colourRGB))

        self.MarketStatusColours()

        self.networkOKColour = dlg.m_colourPickerNetworkOK.GetColour()
        colourRGB = self.networkOKColour.Get()
        self.config.Write('Colour - Network OK', str(colourRGB))

        self.networkOKColourText = dlg.m_colourPickerNetworkOKText.GetColour()
        colourRGB = self.networkOKColourText.Get()
        self.config.Write('Colour - Network OK Text', str(colourRGB))

        self.networkErrorsColour = dlg.m_colourPickerNetworkErrors.GetColour()
        colourRGB = self.networkErrorsColour.Get()
        self.config.Write('Colour - Network Errors', str(colourRGB))

        self.networkErrorsColourText = dlg.m_colourPickerNetworkErrorsText.GetColour()
        colourRGB = self.networkErrorsColourText.Get()
        self.config.Write('Colour - Network Errors Text', str(colourRGB))
