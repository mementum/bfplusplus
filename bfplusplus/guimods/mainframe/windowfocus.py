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

from gui.OverlayMessage import OverlayMessage
from gui.ProgressDialog import ProgressDialog
from gui.TransientMessage import TransientMessage

if True:
    def init(self):
        self.preFocusWin = None

        self.blockLogin = ProgressDialog(self)
        self.blockGetEvents = ProgressDialog(self.m_treeEvents)
        self.blockGetMarket = ProgressDialog(self.m_splitterMarketBets)
        self.blockFavs = ProgressDialog(self.m_listCtrlFavs)

        self.transMsg = TransientMessage(self.m_panelMarketBets, xrel=0, yrel=100)
        self.transMsgError = TransientMessage(self.m_panelMarketBets, xrel=100, yrel=100)

        self.marketStatusOverlay = OverlayMessage(self.m_gridMarket, xrel=50, yrel=25, transLevel=50)
        suspFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=False, face='Verdana')
        self.marketStatusOverlay.SetFont(suspFont)
        self.marketStatusOverlay.Layout()

        self.stoppedOverlay = OverlayMessage(self.m_gridMarket, xrel=100, yrel=0, transLevel=10)
        # suspFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=False, face='Verdana')
        # self.stoppedOverlay.SetFont(suspFont)
        self.stoppedOverlay.SetMessage('STOPPED')
        self.stoppedOverlay.SetBackgroundColour(self.whiteColour)
        self.stoppedOverlay.Layout()

        self.matchedOverlay = OverlayMessage(self.m_gridMarket, xrel=0, yrel=0, transLevel=10)
        self.matchedOverlay.SetMessage('')
        self.matchedOverlay.SetBackgroundColour(self.whiteColour)
        self.matchedOverlay.Layout()

        self.panelControlIcons = dict()
        bmp = wx.Bitmap('./icons/famfamfam-silk/application_side_expand.png')
        self.panelControlIcons[0] = bmp
        bmp = wx.Bitmap('./icons/famfamfam-silk/application_side_contract.png')
        self.panelControlIcons[1] = bmp


    def RegisterFocusWin(self, win):
        if not hasattr(self, 'focusWindows'):
            self.focusWindows = list()

        self.focusWindows.append(win)
        

    def ActivateFocusWindows(self):
        for win in self.focusWindows:
            win.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindowBf)
            win.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindowBf)
            

    def OnEnterWindowBf(self, event):
        event.Skip()
        win = event.GetEventObject()
        if self.IsActive():
            self.preFocusWin = self.FindFocus()
            win.SetFocus()


    def OnLeaveWindowBf(self, event):
        event.Skip()
        if self.preFocusWin != None:
            self.preFocusWin.SetFocus()
            self.preFocusWin = None


    def OnButtonClickPanelShowHide(self, event):
        event.Skip()

        smbwidth, smbheight = self.m_splitterMarketBets.GetSizeTuple()

        # Action to take
        if self.m_panelMainLeft.IsShown():
            # Hide panel and change button bitmap
            self.m_bpButtonPanelShowHide.SetBitmapLabel(self.panelControlIcons[0])
            self.m_staticTextShowHidePanel.SetLabel('Show Panel')
            self.m_panelMainLeft.Show(False)
            self.Layout()
            self.Refresh()
            self.RePosOverlays()

        else:
            # Split the window and do it at the width of the lft panel - change the icon
            self.m_bpButtonPanelShowHide.SetBitmapLabel(self.panelControlIcons[1])
            self.m_staticTextShowHidePanel.SetLabel('Hide Panel')
            self.m_panelMainLeft.Show(True)
            self.Layout()
            self.Refresh()
            self.RePosOverlays()

