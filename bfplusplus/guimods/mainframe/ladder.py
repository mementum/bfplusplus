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
import wx.grid

from datetime import datetime
import time

from bfobj import MarketTuple
import bfpy
from util import Message, splitThousands


if True:
    def init(self):
        self.ladderView = False
        # self.ladderGrids

    def OnButtonClickLadder(self, event):
        event.Skip()

        self.ladderView = True

        self.m_gridMarket.Show(False)

        self.ladderScroll = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.ladderScroll.SetScrollRate( 5, 5 )

        scrollSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.ladderScroll.SetSizer(scrollSizer)
        self.ladderScroll.Layout()
        scrollSizer.Fit(self.ladderScroll)
        self.m_bettingSizer.Add(self.ladderScroll, 1, wx.EXPAND, 5 )
        self.ladderSizer = wx.BoxSizer(wx.HORIZONTAL);

        marketComp = self.marketCache[self.marketTuple]

        for runner in marketComp.runners:
            # 1. Create and store a grid for each runner
            runnerGrid = wx.Grid

            runnerGrid = wx.grid.Grid(self.m_panelBetting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		
            # Grid
            runnerGrid.CreateGrid(len(bfpy.PriceLadder), 3)
            runnerGrid.EnableEditing(False)
            runnerGrid.EnableGridLines(True)
            runnerGrid.EnableDragGridSize(False)
            runnerGrid.SetMargins(0, 0)

            # Columns
            runnerGrid.EnableDragColMove(False)
            runnerGrid.EnableDragColSize(True)
            runnerGrid.SetColLabelSize(30)
            runnerGrid.SetColLabelValue(0, u"Back")
            runnerGrid.SetColLabelValue(1, u"Lay")
            runnerGrid.SetColLabelValue(2, u"Traded")
            runnerGrid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Rows
            runnerGrid.EnableDragRowSize(True)
            runnerGrid.SetRowLabelSize(65)
            runnerGrid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Label Appearance

            # Cell Defaults
            runnerGrid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

            # Add Grid to Sizer
            self.bettingSizer.Add(runnerGrid, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)

            # Add a spacer
            self.bettingSizer.AddSpacer(( 3, 0), 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5)
            pass
