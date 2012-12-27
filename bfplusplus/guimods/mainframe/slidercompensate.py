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
        self.compPerc = self.config.ReadInt('Compensation Percentage', 50)
        self.config.WriteInt('Compensation Percentage', self.compPerc)
        self.m_sliderCompensate.SetValue(self.compPerc)
        self.m_staticTextCompensate.SetLabel(' %d%%' % self.compPerc)


    def OnScrollCompensate(self, event):
        newPos = event.GetPosition()

        # The calculations below overcome a bug in the wxWidgets
        # implementation. With the mouse, the slider will not stop
        # at 50%
        oldPos = int(self.m_staticTextCompensate.GetLabel().rstrip('%'))

        posAvg = (newPos + oldPos)/2
        posDiff = abs(newPos - oldPos)

        if posAvg == 50 and posDiff <= 2:
            newPos = 50

        self.compPerc = newPos

        self.UpdateCompensateThings(newPos)


    def OnMenuSelectionSliderCompensate(self, event):
        itemId = event.GetId()
        menuItems = self.m_menuCompensate.GetMenuItems()

        for menuItem in menuItems:
            if itemId == menuItem.GetId():
                compPercStr = menuItem.GetLabel().rstrip('%')
                self.compPerc = int(compPercStr)

                self.UpdateCompensateThings(self.compPerc)
                break


    def UpdateCompensateThings(self, compPerc):
        self.config.WriteInt('Compensation Percentage', compPerc)
        self.m_sliderCompensate.SetValue(compPerc)
        self.m_staticTextCompensate.SetLabel('%d%%' % compPerc)
        if self.marketTuple is not None:
            self.UpdateCompensations(compPerc)


    def UpdateCompensations(self, compPerc):
        compPerc = float(compPerc)/100.0

        if self.marketTuple is None:
            return

        marketComp = self.marketCache[self.marketTuple]
        ticksAway = 0 if not self.compTicksAway else self.compTicksAwayCount
        marketComp.updateBetCompensations(compPerc, ticksAway=ticksAway)
        marketComp.updatePnLCompensations(compPerc, self.compIndex, ticksAway=ticksAway)

        self.UpdateMarketProfitAndLoss(self.marketTuple)
        self.UpdateMUBets(self.marketTuple)
