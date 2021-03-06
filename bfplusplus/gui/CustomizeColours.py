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
"""Subclass of CustomizeColours, which is generated by wxFormBuilder."""

import wx

import MainGui

# Implementing CustomizeColours
class CustomizeColours(MainGui.CustomizeColours):
    def __init__(self, parent):
	MainGui.CustomizeColours.__init__(self, parent)
	

    def OnButtonClickColoursBackDefaults(self, event):
        colourRGB = wx.Colour(128, 128, 255)
        self.m_colourPickerBack.SetColour(colourRGB)
        colourRGB = wx.Colour(0, 0, 0)
        self.m_colourPickerBackText.SetColour(colourRGB)
        self.SetSampleColours()


    def OnButtonClickColoursLayDefaults(self, event):
        colourRGB = wx.Colour(128, 128, 0)
        self.m_colourPickerLay.SetColour(colourRGB)
        colourRGB = wx.Colour(0, 0, 0)
        self.m_colourPickerLayText.SetColour(colourRGB)
        self.SetSampleColours()


    def OnButtonClickColoursMatchedDefaults(self, event):
        colourRGB = wx.Colour(0, 255, 0)
        self.m_colourPickerMatched.SetColour(colourRGB)
        colourRGB = wx.Colour(0, 0, 0)
        self.m_colourPickerMatchedText.SetColour(colourRGB)
        self.SetSampleColours()


    def OnButtonClickColoursUnmatchedDefaults(self, event):
        colourRGB = wx.Colour(255, 0, 0)
        self.m_colourPickerUnmatched.SetColour(colourRGB)
        colourRGB = wx.Colour(0, 0, 0)
        self.m_colourPickerUnmatchedText.SetColour(colourRGB)
        self.SetSampleColours()


    def OnButtonClickColoursInPlayDefaults(self, event):
        colourRGB = wx.Colour(0, 255, 0)
        self.m_colourPickerInPlay.SetColour(colourRGB)
        colourRGB = wx.Colour(255, 255, 255)
        self.m_colourPickerInPlayText.SetColour(colourRGB)
        self.SetSampleColours()


    def OnButtonClickColoursInPlayOffDefaults(self, event):
        colourRGB = wx.Colour(255, 255, 255)
        self.m_colourPickerInPlayOff.SetColour(colourRGB)
        colourRGB = wx.Colour(0, 0, 0)
        self.m_colourPickerInPlayOffText.SetColour(colourRGB)
        self.SetSampleColours()


    def OnButtonClickColoursMarketActiveDefaults(self, event):
        colourRGB = wx.Colour(255, 255, 255)
        self.m_colourPickerMarketActive.SetColour(colourRGB)
        colourRGB = wx.Colour(0, 0, 0)
        self.m_colourPickerMarketActiveText.SetColour(colourRGB)
        self.SetSampleColours()


    def OnButtonClickColoursMarketSuspClosedDefaults(self, event):
        colourRGB = wx.Colour(255, 0, 0)
        self.m_colourPickerMarketSuspClosed.SetColour(colourRGB)
        colourRGB = wx.Colour(255, 255, 255)
        self.m_colourPickerMarketSuspClosedText.SetColour(colourRGB)
        self.SetSampleColours()


    def OnButtonClickColoursNetworkOKDefaults(self, event):
        colourRGB = wx.Colour(255, 255, 255)
        self.m_colourPickerNetworkOK.SetColour(colourRGB)
        colourRGB = wx.Colour(0, 0, 0)
        self.m_colourPickerNetworkOKText.SetColour(colourRGB)
        self.SetSampleColours()


    def OnButtonClickColoursNetworkErrorsDefaults(self, event):
        colourRGB = wx.Colour(255, 0, 0)
        self.m_colourPickerNetworkErrors.SetColour(colourRGB)
        colourRGB = wx.Colour(0, 0, 0)
        self.m_colourPickerNetworkErrorsText.SetColour(colourRGB)
        self.SetSampleColours()


    def SetSampleColours(self):
        self.m_staticTextBack.SetBackgroundColour(self.m_colourPickerBack.GetColour())
        self.m_staticTextBack.SetForegroundColour(self.m_colourPickerBackText.GetColour())

        self.m_staticTextLay.SetBackgroundColour(self.m_colourPickerLay.GetColour())
        self.m_staticTextLay.SetForegroundColour(self.m_colourPickerLayText.GetColour())

        self.m_staticTextMatched.SetBackgroundColour(self.m_colourPickerMatched.GetColour())
        self.m_staticTextMatched.SetForegroundColour(self.m_colourPickerMatchedText.GetColour())

        self.m_staticTextUnmatched.SetBackgroundColour(self.m_colourPickerUnmatched.GetColour())
        self.m_staticTextUnmatched.SetForegroundColour(self.m_colourPickerUnmatchedText.GetColour())

        self.m_staticTextInPlay.SetBackgroundColour(self.m_colourPickerInPlay.GetColour())
        self.m_staticTextInPlay.SetForegroundColour(self.m_colourPickerInPlayText.GetColour())

        self.m_staticTextInPlayOff.SetBackgroundColour(self.m_colourPickerInPlayOff.GetColour())
        self.m_staticTextInPlayOff.SetForegroundColour( self.m_colourPickerInPlayOffText.GetColour())

        self.m_staticTextMarketActive.SetBackgroundColour(self.m_colourPickerMarketActive.GetColour())
        self.m_staticTextMarketActive.SetForegroundColour(self.m_colourPickerMarketActiveText.GetColour())

        self.m_staticTextMarketSuspClosed.SetBackgroundColour(self.m_colourPickerMarketSuspClosed.GetColour())
        self.m_staticTextMarketSuspClosed.SetForegroundColour(self.m_colourPickerMarketSuspClosedText.GetColour())

        self.m_staticTextNetworkOK.SetBackgroundColour(self.m_colourPickerNetworkOK.GetColour())
        self.m_staticTextNetworkOK.SetForegroundColour(self.m_colourPickerNetworkOKText.GetColour())

        self.m_staticTextNetworkErrors.SetBackgroundColour(self.m_colourPickerNetworkErrors.GetColour())
        self.m_staticTextNetworkErrors.SetForegroundColour(self.m_colourPickerNetworkErrorsText.GetColour())

        self.Refresh()


    def OnColourChangedAll(self, event):
        self.SetSampleColours()
