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

if True:
    def init(self):
        refreshTime = self.config.ReadFloat('Refresh Time', 1.0)
        self.config.WriteFloat('Refresh Time', refreshTime)
        self.m_sliderRefresh.SetValue(int(refreshTime * 10.0))
        self.m_staticTextRefresh.SetLabel('%.1f sec' % refreshTime)


    def OnScrollSliderRefresh(self, event):
        refreshTime = float(event.GetPosition() / 10.0)
        self.UpdateSliderThings(refreshTime)


    def OnMenuSelectionSliderRefresh(self, event):
        itemId = event.GetId()
        menuItems = self.m_menuSliderRefresh.GetMenuItems()

        for menuItem in menuItems:
            if itemId == menuItem.GetId():
                refreshTimeStr = menuItem.GetLabel()

                refreshTime = float(refreshTimeStr.split(' ')[0])
                self.UpdateSliderThings(refreshTime)

                refreshPos = int(refreshTime * 10.0)
                self.m_sliderRefresh.SetValue(refreshPos)
                break


    def UpdateSliderThings(self, refreshTime):
        self.m_staticTextRefresh.SetLabel('%.1f sec' % refreshTime)

        if self.thGetMarketPrices:
            self.thGetMarketPrices.timeQueue.put(refreshTime)
            self.thGetMarketProfitAndLoss.timeQueue.put(refreshTime)
            self.thGetMUBets.timeQueue.put(refreshTime)

        self.config.WriteFloat('Refresh Time', refreshTime)
