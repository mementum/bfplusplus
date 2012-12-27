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

from datetime import datetime

class StopBetInfo(object):
    nextIdx = 0

    def getNextIdx(self):
        StopBetInfo.nextIdx += 1
        return StopBetInfo.nextIdx - 1

    def __init__(self, action, bet, stopPerc, compPerc=50):
        self.idx = self.getNextIdx()
        # active, voided, paused, executed
        self.status = 'active'

        self.timestamp = datetime.now()

        self.comment = ''

        self.action = action
        self.bet = bet
        self.stopPerc = stopPerc
        self.compPerc = compPerc / 100.0

        if self.action == 'profitOnProfit':
            self.threshold = self.stopPerc * bet.profit / 100.0

        elif self.action == 'profitOnRisk':
            self.threshold = self.stopPerc * bet.risk / 100.0

        elif self.action == 'lossOnProfit':
            self.threshold = -1.0 * self.stopPerc * bet.profit / 100.0

        elif self.action == 'lossOnRisk':
            self.threshold = -1.0 * self.stopPerc * bet.risk / 100.0
        else:
            self.threshold = None


    def checkThreshold(self, compWin):
        if self.threshold is None:
            return

        if self.action == 'profitOnProfit':
            if compWin >= self.threshold:
                return True

        elif self.action == 'profitOnRisk':
            if compWin >= self.threshold:
                return True

        elif self.action == 'lossOnProfit':
            if compWin <= self.threshold:
                return True

        elif self.action == 'lossOnRisk':
            if compWin <= self.threshold:
                return True
