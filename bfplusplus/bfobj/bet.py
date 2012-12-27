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

import bfpy

from compensation import Compensation

class Bet(object):

    def __init__(self):
        self.muBets = list()

        self.risk = 0.0
        self.profit = 0.0

        self.size = 0.0
        self.price = 0.0


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        text = ''
        text += 'Id: %d\n' % self.betId
        text += 'Type: %s\n' % self.betType
        text += 'Persistence: %s\n' % self.betPersistenceType
        text += 'Category: %s\n' % self.betCategoryType
        text += 'Status: %s\n' % self.betStatus
        text += 'Price: %s\n' % self.price
        text += 'Size: %s\n' % self.size

        return text


    muOrder = {'M': 2, 'U': 1}

    @staticmethod
    def makeKey(betId, betStatus):
        betKey = '%d%d' % (betId, Bet.muOrder[betStatus])
        return betKey


    oppBet = {'B': 'L', 'L': 'B'}

    def getCompensate(self, runnerPrices, compPerc, ticksAway=0):
        if self.betStatus == 'U':
            return None

        if self.betType == 'B':
            bestPrices = runnerPrices.bestPricesToLay
        else:
            bestPrices = runnerPrices.bestPricesToBack

        if not bestPrices:
            return None

        compBetType = self.oppBet[self.betType]
        compPrice = bestPrices[0].price

        compPrice = bfpy.GetPriceTicks(compPrice, ticksAway, compBetType)

        prenumer = self.profit if self.betType == 'B' else -self.risk
        numer = prenumer - compPerc * (self.profit - self.risk)
        denom = (compPrice - 1.0) + (compPerc * (2.0 - compPrice))
        compSize = round(abs(numer/denom), 2)

        profitOrRisk = compSize * (compPrice - 1.0)


        if compBetType == 'B':
            compRisk = compSize
            compProfit = profitOrRisk
        else:
            compRisk = profitOrRisk
            compProfit = compSize

        compBetWins = self.profit - compRisk
        compBetLoses = compProfit - self.risk

        return Compensation(self.selectionId,
                            compBetType, compPrice, compSize,
                            compBetWins, compBetLoses, asianLineId=self.asianLineId)


    def isDirty(self, updatebet):
        return self.size != updatebet.size or \
               self.betPersistenceType != updatebet.betPersistenceType


    def update(self, updatebet):
        if self.isDirty(updatebet):
            self.dirty = True

            self.size = updatebet.size
            self.price = updatebet.price
            self.betPersistenceType = updatebet.betPersistenceType
            self.risk = updatebet.risk
            self.profit = updatebet.profit
            self.muBets = updatebet.muBets

        else:
            self.dirty = False


    def addMUBet(self, muBet):
        self.dirty = True

        if not self.muBets:
            self.betId = muBet.betId
            self.betType = muBet.betType
            self.betPersistenceType = muBet.betPersistenceType
            self.betCategoryType = muBet.betCategoryType
            self.asianLineId = muBet.asianLineId
            self.selectionId = muBet.selectionId
            self.betStatus = muBet.betStatus

        self.muBets.append(muBet)

        # someones risk - backer or layer
        profitOrLoss = muBet.size * (muBet.price - 1.0)

        if self.betType == 'B':
            risk = muBet.size
            profit = profitOrLoss
        else: # Lay
            risk = profitOrLoss
            profit = muBet.size
    
        # Get the new odds
        self.risk += risk
        self.profit += profit

        if muBet.betStatus == 'U':
            self.price = muBet.price
            self.size = muBet.size
            return
        
        self.size += muBet.size

        if self.betType == 'B':
            self.price = self.profit/self.risk + 1.0
        else:
            # if self.betType == 'L':
            # self.price = 1.0/(1.0 - 1.0/self.price)
            self.price = self.risk/self.profit + 1.0


class BetCollection(defaultdict):

    def __init__(self, muBets):
        defaultdict.__init__(self, Bet)

        for muBet in muBets:
            betKey = Bet.makeKey(muBet.betId, muBet.betStatus)
            self[betKey].addMUBet(muBet)


class BetStand(object):

    def __init__(self, betId):
        self.betId = betId

        self.matched = 0.0
        self.avgprice = 0.0
        self.unmatched = 0.0
        self.price = 0.0

        self.size = 0.0


    def addBet(self, bet):
        self.betType = bet.betType
        self.betPersistenceType = bet.betPersistenceType
        self.betCategoryType = bet.betCategoryType

        if bet.betStatus == 'M':
            self.matched = bet.size
            self.avgprice = bet.price
            self.size += self.matched
        else:
            self.unmatched = bet.size
            self.size += self.unmatched
            self.price = bet.price
