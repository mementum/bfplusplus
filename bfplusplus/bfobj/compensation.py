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

class Compensation(object):

    def __init__(self, selectionId, betType, price, size, compWin=None, compLoss=None, asianLineId=0):
        self.asianLineId = asianLineId
        self.selectionId = selectionId
        self.betType = betType
        self.price = price
        self.size = size

        winOrLoss = size * (price - 1.0)

        if self.betType == 'B':
            self.ifWin = winOrLoss
            self.ifLoss = -size
        else:
            self.ifWin = -winOrLoss
            self.ifLoss = size

        self.compWin = compWin
        if self.compWin is None:
            self.compWin = self.ifWin

        self.compLoss = compLoss
        if self.compLoss is None:
            self.compLoss = self.ifLoss


    def __eq__(self, other):
        cond1 = (self.selectionId == other.selectionId)
        cond2 = (self.betType == other.betType)
        cond3 = (self.price == other.price)
        cond4 = (self.size == other.size)
        cond5 = (self.compWin == other.compWin)
        cond6 = (self.compLoss == other.compLoss)

        return cond1 and cond2 and cond3 and cond4 and cond5 and cond6


    def __ne__(self, other):
        return not self.__eq__(other)


    def getIfWinForSelectionId(self, selectionId):
        if selectionId == self.selectionId:
            return self.ifWin

        return self.ifLoss


    def __str__(self):
        text = ''
        text += 'SelId: %d\n' % self.selectionId
        text += 'BetType: %s\n' % self.betType
        text += 'Price: %.2f\n' % self.price
        text += 'Size: %.2f\n' % self.size
        text += 'CompWin: %.2f\n' % self.compWin
        text += 'CompLoss: %.2f\n' % self.compLoss

        return text


    def __repr__(self):
        return self.__str__()
