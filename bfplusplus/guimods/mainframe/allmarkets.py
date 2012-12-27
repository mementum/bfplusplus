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

from collections import defaultdict
from datetime import datetime

import wx

import bfpy
from util import Message

if True:
    def init(self):
        self.marketData = defaultdict(list)
        self.dataMarkets = dict()

        self.refreshMarketsPeriod = self.config.ReadInt('Refresh Markets Period', 300)
        self.config.WriteInt('Refresh Markets Period', self.refreshMarketsPeriod)

        refreshTime = int(self.refreshMarketsPeriod / 60.0)
        self.m_sliderMarketDataRefresh.SetValue(refreshTime)
        self.m_staticTextMarkeDataRefresh.SetLabel('%d mins' % refreshTime)
        self.m_staticTextMarkeDataRefresh.Refresh()

        self.allMarketsUpdate= dict()
        self.allMarketsUpdate[bfpy.ExchangeUK] = None
        self.allMarketsUpdate[bfpy.ExchangeAus] = None


    def GetAllMarkets(self, exchangeId, **kwargs):
	message = Message(action='getAllMarkets', **kwargs)
        message.exchangeId = exchangeId
	self.thMisc.passMessage(message)


    def OnGetAllMarkets(self, event):
        message, response, exception = self.SplitEventResponse(event)
        if not response:
            if exception:
                self.LogMessagesError('Loading all markets data has failed. Please try it again')
                self.LogMessages(exception)
        
            return

        self.allMarketsUpdate[message.exchangeId] = datetime.now()

        self.marketData[message.exchangeId] = response.marketData
        self.dataMarkets[message.exchangeId] = response.dataMarket


        ukCount = len(self.marketData[bfpy.ExchangeUK])
        ausCount = len(self.marketData[bfpy.ExchangeAus])
        label = 'UK: %d / Aus: %d' % (ukCount, ausCount)
        self.m_staticTextAvailableAllMarkets.SetLabel(label)

        updateStr = 'Uk %s /Aus %s'
        if self.allMarketsUpdate[bfpy.ExchangeUK]:
            ukUpdateStr = self.allMarketsUpdate[bfpy.ExchangeUK].strftime('%Y-%m-%d %H:%M')
        else:
            ukUpdateStr = '-'

        if self.allMarketsUpdate[bfpy.ExchangeAus]:
            ausUpdateStr = self.allMarketsUpdate[bfpy.ExchangeAus].strftime('%Y-%m-%d %H:%M')
        else:
            ausUpdateStr = '-'

        self.m_staticTextMarketsUpdate.SetLabel(updateStr % (ukUpdateStr, ausUpdateStr))


    def OnScrollMarketDataRefresh(self, event):
        event.Skip()

        refreshTime = event.GetPosition()

        if refreshTime * 60 == self.refreshMarketsPeriod:
            # Up to 3 events may arrive with the same value
            return

        self.refreshMarketsPeriod = refreshTime * 60

        
        self.config.WriteInt('Refresh Markets Period', self.refreshMarketsPeriod)

        if hasattr(self, 'thAllMarkets'):
            message = Message(timeout=self.refreshMarketsPeriod)
            self.thAllMarkets.passMessage(message)

        self.m_staticTextMarkeDataRefresh.SetLabel('%d mins' % refreshTime)
        self.m_staticTextMarkeDataRefresh.Refresh()

        if not self.refreshMarketsPeriod:
            wx.MessageBox('Auto-loading of markets data is disabled', 'Markets Data')


    def OnButtonClickRefreshMarkets(self, event):
        event.Skip()
        for exchangeId in bfpy.Exchanges:
            self.GetAllMarkets(exchangeId)
