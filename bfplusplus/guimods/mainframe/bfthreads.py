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

import threading

import wx

import threads.threadbase as threadbase
import threads.threadsbf as threadsbf

if True:
    def init(self):
        self.bfLock = threading.Lock()

        self.bfClient = None
        self.thMisc = None
        self.thGetMarketPrices = None
        self.thGetMarketProfitAndLoss = None
        self.thGetMUBets = None

        # Early binding to allow play in off-line mode
        self.pyEventIdMarketPrices = wx.NewId()
	self.Connect(wx.ID_ANY, wx.ID_ANY, self.pyEventIdMarketPrices, self.OnGetMarketPrices)
        

    def startThreads(self):
        # Keep a copy of the master bfClient to create data objects out of it
        # self.bfClient = self.thLogin.bfClient
        self.bfClient = threadbase.ThreadBase.bfClientMaster

        self.thMisc.startSubThreads()

        self.thGetMarketPrices = threadsbf.ThreadGetMarketPrices(self, self.OnGetMarketPrices, self.pyEventIdMarketPrices)
        self.thGetMarketProfitAndLoss = threadsbf.ThreadGetMarketProfitAndLoss(self, self.OnGetMarketProfitAndLoss)
        self.thGetMUBets = threadsbf.ThreadGetMUBets(self, self.OnGetMUBets)

        refreshTime = float(self.m_sliderRefresh.GetValue()) / 10.0
        self.thGetMarketPrices.timeout = refreshTime
        self.thGetMUBets.timeout = refreshTime
        self.thGetMarketProfitAndLoss.timeout = refreshTime

        self.thAllMarkets = threadsbf.ThreadAllMarkets()
        self.thAccountFunds = threadsbf.ThreadAccountFunds()
        self.thCurrentBets = threadsbf.ThreadCurrentBets()



