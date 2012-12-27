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
"""Subclass of OverlayMessage, which is generated by wxFormBuilder."""
import wx

import MainGui

# Implementing OverlayMessage
class OverlayMessage(MainGui.OverlayMessage):
    def __init__(self, parent, xrel=50, yrel=50, transLevel=50):
	MainGui.OverlayMessage.__init__(self, parent)

	self.xrel = xrel / 100.0
        self.yrel = yrel / 100.0

	self.transLevel = int((transLevel * 255.0) / 100.0)
	self.transLevel = 255 - self.transLevel

	if self.CanSetTransparent():
	    self.SetTransparent(self.transLevel)

        # parent.Bind(wx.EVT_ICONIZE, lambda evt: self.Hide())


    def OnIconize(self, event):
        event.Skip()
        if not event.Iconized():
            # win = self.GetParent()
            win = wx.GetApp().GetTopWindow()
            win.Iconize(False)


    def OnSetFocus(self, event):
        # Return the focus to the losing window
        # win = event.GetWindow()
        # win = self.GetParent()
        # Best method ... allows clicking on this window
        # to activate the main frame coming from other
        # windows, which seems natural
        win = wx.GetApp().GetTopWindow()

        if win.IsIconized():
            win.Iconize(False)

        win.SetFocus()
        # event.Skip()


    def SetFont(self, font):
        self.m_staticTextMessage.SetFont(font)
        

    def SetMessage(self, message):
	curMessage = self.m_staticTextMessage.GetLabel()
	if message != curMessage:
	    self.m_staticTextMessage.SetLabel(message)


    def CalcAndSetPosition(self):
	parentSize = self.GetParent().GetSize()
	mySize = self.GetSize()

        maxXCoord = parentSize.width - mySize.width
        xCoord = maxXCoord * self.xrel

        maxYCoord = parentSize.height - mySize.height
        yCoord = maxYCoord * self.yrel

        position = wx.Point(xCoord, yCoord)
        position = self.GetParent().ClientToScreen(position)
        self.SetPosition(position)


    def Show(self, toShow):
	if toShow:
	    self.CalcAndSetPosition()

	MainGui.OverlayMessage.Show(self, toShow)


    def SetBackgroundColour(self, colour):
	self.m_staticTextMessage.SetBackgroundColour(colour)
	MainGui.OverlayMessage.SetBackgroundColour(self, colour)

	
    def SetForegroundColour(self, colour):
	self.m_staticTextMessage.SetForegroundColour(colour)
