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

from collections import defaultdict, namedtuple
from copy import copy

import bfpy

from bet import BetStand
from compensation import Compensation
from util.generic import Generic
from stopbet import StopBetInfo

MarketTuple = namedtuple('MarketTuple', ['exchangeId', 'marketId'])

class MarketComp(object):
    def __init__(self, market=None):
        self.market = market
        self.marketPrices = None
        self.runnerNames = dict()
        self.runnerNamesAsian = dict()
        self.runnerPrices = dict()
        self.runnerPricesAsian = dict()
        self.annotations = dict()
        self.annotationsDirty = defaultdict(bool)
        self.nextPnLDirty = False
        self.compensations = defaultdict(list)
        self.bets = dict()
        self.betsActive = dict()
        self.betNum = self.betSequence()
        self.betComps = dict()
        self.betCompsDirty = dict()
        self.nextbetCompDirty = False
        self.stopbetinfos = list()
                    
        if market is not None:
            self.updateMarket()


    def clone(self):
        if True:
            return copy(self)
        else:
            clone = self.__class__()

            # set once - can be passed along
            clone.market = self.market

            # MarketComp will use a new reference with each beat
            clone.marketPrices = self.marketPrices

            # set each time - must be copied
            clone.runnerNames = self.runnerNames.copy()
            clone.runnerNamesAsian = self.runnerNamesAsian.copy()

            # Copy needed because the list has reference to objects
            # and this references will be changed
            clone.runnerPrices = self.runnerPrices.copy()
            clone.runnerPricesAsian = self.runnerPricesAsian.copy()

            # MarketComp will use a new reference with each beat
            clone.annotations = self.annotations.copy()
            clone.annotationsDirty = self.annotationsDirty.copy()

            clone.compensations = self.compensations.copy()

            # Copy needed because the list has reference to objects
            # and this references will be changed
            clone.bets = self.bets.copy()
            clone.betsActive = self.betsActive.copy()

            clone.betComps = self.betComps.copy()
            clone.betCompsDirty = self.betCompsDirty.copy()

            # make a copy
            clone.stopbetinfos = self.stopbetinfos[:]

            return clone


    def AddStopBet(self, action, bet, stopBetPerc):
        stopbetinfo = StopBetInfo(action, bet, stopBetPerc)
        self.stopbetinfos.append(stopbetinfo)
        return stopbetinfo


    def betSequence(self):
        betSeq = 1
        while True:
            yield betSeq
            betSeq += 1


    def __getattr__(self, attr):
        if attr.startswith('_'):
            return object.__getattribute__(attr)

        elif hasattr(self.marketPrices, attr):
            return getattr(self.marketPrices, attr)

        elif hasattr(self.market, attr):
            return getattr(self.market, attr)

        return None


    def getMenuPath(self):
        menuPath = self.menuPath.lstrip()

        if menuPath.startswith('\\Group '):
            menuPath = menuPath[8:]

        menuPath = menuPath.lstrip('\\')
        menuParts = menuPath.split('\\')
        menuParts = [menuPart.strip() for menuPart in menuParts]
        menuParts.insert(0, '')
        menuPath = '\\'.join(menuParts)
        return menuPath, menuParts


    def getFullMenuPath(self):
        menuPath, menuParts = self.getMenuPath()
        menuParts.append(self.name)
        menuPath = '\\'.join(menuParts)
        return menuPath, menuParts


    @staticmethod
    def makeAsianId(selectionId, asianLineId):
        return '%s:%s' % (selectionId, asianLineId)


    def getCompensations(self, runner):
        return self.getCompensationsById(runner.selectionId)


    def getCompensationsById(self, selectionId):
        return self.compensations.get(selectionId, None)


    def getAnnotation(self, runner):
        return self.getAnnotationById(runner.selectionId)


    def getAnnotationById(self, selectionId):
        annotations = self.annotations.get(selectionId, None)
        if not annotations:
            return None

        return annotations[0]


    def removeRunners(self, runnersIdxList):
        runnersIdxList.sort(reverse=True)

        for runnerIdx in runnersIdxList:
            del self.market.runners[runnerIdx]


    def getRunnerLabel(self, runner):
        return self.getRunnerLabelById(runner.selectionId, runner.asianLineId)


    def getRunnerLabelById(self, selectionId, asianLineId=0):
        if not asianLineId:
            return self.runnerNames[selectionId]

        asianId = self.makeAsianId(selectionId, asianLineId)
        return self.runnerNamesAsian[asianId]


    def updateMarket(self):
        for runner in self.market.runners:
            self.runnerNames[runner.selectionId] = runner.name

            if self.market.marketType == 'A':
                asianName = '%s (%s)' % (runner.name, runner.handicap)
                asianId = self.makeAsianId(runner.selectionId, runner.asianLineId)
                self.runnerNamesAsian[asianId] = asianName


    def getRunnerPrices(self, runner):
        return self.getRunnerPricesId(runner.selectionId, runner.asianLineId)


    def getRunnerPricesId(self, selectionId, asianLineId=0):
        if self.market.marketType != 'A':
            return self.runnerPrices.get(selectionId, None)

        asianId = self.makeAsianId(selectionId, asianLineId)
        return self.runnerPricesAsian.get(asianId, None)


    def updateMarketPrices(self, marketPrices, compPerc, refRunnerIndex, ticksAway=0):
        self.marketPrices = marketPrices

        for runnerPrice in marketPrices.runnerPrices:
            self.runnerPrices[runnerPrice.selectionId] = runnerPrice

            if self.market.marketType == 'A':
                handicap = runnerPrice.handicap

                for runner in self.market.runners:
                    if runner.selectionId == runnerPrice.selectionId and runner.handicap == handicap:
                        asianId = self.makeAsianId(runner.selectionId, runner.asianLineId)
                        self.runnerPricesAsian[asianId] = runnerPrice

        self.marketPrices.backOverround = 0.0
        self.marketPrices.layOverround = 0.0
        self.marketPrices.totalAmountMatched = 0.0

        if self.market.marketType != 'A':
            runnerPricesValues = self.runnerPrices.itervalues()
        else:
            runnerPricesValues = self.runnerPricesAsian.itervalues()

        for runnerPrice in runnerPricesValues:
            self.marketPrices.totalAmountMatched += runnerPrice.totalAmountMatched

            if runnerPrice.bestPricesToBack:
                self.marketPrices.backOverround += 100.0 * 1.0 / runnerPrice.bestPricesToBack[0].price
            else:
                # To avoid detecting a false overround positive
                self.marketPrices.backOverround += 100.0 * 1.0 / 1.0

            if runnerPrice.bestPricesToLay:
                self.marketPrices.layOverround += 100.0 * 1.0 / runnerPrice.bestPricesToLay[0].price
            else:
                # self.marketPrices.layOverround += 100.0 * 1.0/1001.0
                self.marketPrices.layOverround += 0.0

        if self.market.marketType != 'A':
            runnerPricesValues = self.runnerPrices.itervalues()
        else:
            runnerPricesValues = self.runnerPricesAsian.itervalues()
        for runnerPrice in runnerPricesValues:
            runnerPrice.perc = 0.0

            if runnerPrice.bestPricesToBack:
                runnerPrice.perc = 100.0 * (1.0 / runnerPrice.bestPricesToBack[0].price)
                if self.marketPrices.numberOfWinners == 1:
                    runnerPrice.perc /= (self.marketPrices.backOverround / 100.0)
                else:
                    if False and runnerPrice.bestPricesToLay:
                        perc2 = 100.0 * (1.0 / runnerPrice.bestPricesToLay[0].price)
                        runnerPrice.perc += perc2
                        runnerPrice.perc /= 2.0

        self.updateBetCompensations(compPerc, ticksAway=ticksAway)
        self.updatePnLCompensations(compPerc, refRunnerIndex, ticksAway=ticksAway)


    @staticmethod
    def calcAggregateCompensation(selectionId, runnerPrices, ifWin, ifLoss, compPerc, multiWinner=False, ticksAway=0, asianLineId=0):
        if multiWinner:
            compPerc = 1.0 - compPerc
            ifWin, ifLoss = ifLoss, ifWin

        if ifWin == 0.0 and ifLoss == 0.0:
            return None

        if ifWin <= ifLoss:
            betType = 'L'
            bestPrices = runnerPrices.bestPricesToLay
        elif ifWin > ifLoss:
            betType = 'B'
            bestPrices = runnerPrices.bestPricesToBack

        if not bestPrices:
            return None

        price = bestPrices[0].price
        price = bfpy.GetPriceTicks(price, ticksAway, betType)

        numer = ifWin - compPerc * (ifWin + ifLoss)
        denom = 1.0 + compPerc * (price - 2.0)

        size = round(abs(numer/denom), 2)

        # 3. Calculate the results
        winOrLoss = size * (price - 1.0)

        compA = -size if betType == 'B' else size
        compB = winOrLoss if betType == 'B' else -winOrLoss

        compWin = ifWin + compA
        compLoss = ifLoss + compB

        if multiWinner:
            compWin, compLoss = compLoss, compWin

        return Compensation(selectionId, betType, price, size, compWin, compLoss, asianLineId=asianLineId)


    def profitAndLossDirty(self):
        self.nextPnLDirty = True


    def updateMarketProfitAndLoss(self, annotations, compPerc, refRunnerIndex, ticksAway=0):
        doPnL = False
        newAnnotations = defaultdict(list)
        
        for annotation in annotations:
            newAnnotations[annotation.selectionId].append(annotation)

        # Purge the existing annotations
        for selectionId in self.annotations.copy():
            if selectionId not in newAnnotations:
                doPnL = True
                del self.annotations[selectionId]

        # Update annotations and flags
        for selectionId, newRunnerAnn in newAnnotations.iteritems():
            # Default flag status
            self.annotationsDirty[selectionId] = (False or self.nextPnLDirty)

            # If new: annotate and flag
            if selectionId not in self.annotations:
                self.annotations[selectionId] = newRunnerAnn
                self.annotationsDirty[selectionId] = True
                doPnL = True
                continue

            runnerAnn = self.annotations[selectionId]

            # If different number of annotations (Asian Market)
            # annotate and flag
            if len(newRunnerAnn) != len(runnerAnn):
                self.annotations[selectionId] = newRunnerAnn
                self.annotationsDirty[selectionId] = True
                doPnL = True
                continue

            # If any annotation has changed: annotate and flag
            for annIdx in xrange(len(newRunnerAnn)):
                newAnn = newRunnerAnn[annIdx]
                curAnn = runnerAnn[annIdx]

                if newAnn.ifWin != curAnn.ifWin:
                    self.annotations[selectionId] = newRunnerAnn
                    self.annotationsDirty[selectionId] = True
                    doPnL = True
                    break

                if self.numberOfWinners != 1 and self.market.marketType != 'A':
                    # Handicap lines have no "ifLoss" field
                    if newAnn.ifLoss != curAnn.ifLoss:
                        self.annotations[selectionId] = newRunnerAnn
                        self.annotationsDirty[selectionId] = True
                        doPnL = True
                        break

        if self.nextPnLDirty:
            self.nextPnLDirty = False

        # FIXME: How to calculate the compensations for Asian Markets
        if self.market.marketType == 'A':
            return

        if True or doPnL:
            self.updatePnLCompensations(compPerc, refRunnerIndex, ticksAway=ticksAway)

        
    def updatePnLCompensations(self, compPerc, refRunnerIndex, ticksAway=0):
        self.compensations.clear()

        # FIXME: How to calculate the compensations for Asian Markets
        if self.market.marketType == 'A':
            return

        numRunners = len(self.market.runners)

        if refRunnerIndex is not None and refRunnerIndex < numRunners:
            refRunner = self.market.runners[refRunnerIndex]
            refSelectionId = refRunner.selectionId
            # refAnn = self.getAnnotation(refRunner)
            # refPrices = self.getRunnerPrices(refRunner)
        else:
            refSelectionId = -1

        for runner in self.market.runners:
            annotation = self.getAnnotation(runner)
            if not annotation:
                continue

            if self.market.numberOfWinners != 1:
                runnerPrices = self.getRunnerPrices(runner)
                if not runnerPrices:
                    continue

                compensation = self.calcAggregateCompensation(runner.selectionId,
                                                              runnerPrices,
                                                              annotation.ifWin,
                                                              annotation.ifLoss,
                                                              compPerc,
                                                              multiWinner=True,
                                                              ticksAway=ticksAway,
                                                              asianLineId=runner.asianLineId)

                if compensation and compensation.size != 0.0:
                    self.compensations[runner.selectionId].append(compensation)
                continue

            # Not asian Market and only one winner
            for compRunner in self.market.runners:
                if compRunner.selectionId == runner.selectionId:
                    continue

                compRunnerPrices = self.getRunnerPrices(compRunner)
                if not compRunnerPrices:
                    continue

                compAnnotation = self.getAnnotation(compRunner)
                if not compAnnotation:
                    continue

                if runner.selectionId == refSelectionId:
                    refCompPerc = compPerc
                else:
                    refCompPerc = 1.0 - compPerc

                compensation = self.calcAggregateCompensation(compRunner.selectionId,
                                                              compRunnerPrices,
                                                              annotation.ifWin,
                                                              compAnnotation.ifWin,
                                                              refCompPerc,
                                                              ticksAway=ticksAway,
                                                              asianLineId=compRunner.asianLineId)


                if compensation and compensation.size != 0.0:
                    self.compensations[runner.selectionId].append(compensation)


    def updateBets(self, bets, compPerc, ticksAway=0):
        toRemove = list()
        toCalcComp = list()
        for betnum, betkey in self.betsActive.iteritems():
            if betkey in bets:
                # bet can be updated
                self.bets[betkey].update(bets.pop(betkey))
                toCalcComp.append((betnum, betkey))
            else:
                # bet has been removed
                toRemove.append(betnum)

        for betnum in toRemove:
            del self.betsActive[betnum]

        # The remaining bets are new bets
        for betkey, bet in bets.iteritems():
            bet.betNum = self.betNum.next()
            self.bets[betkey] = bet
            self.betsActive[bet.betNum] = betkey
            toCalcComp.append((bet.betNum, betkey))

        if toCalcComp:
            self.updateBetCompensations(compPerc, toCalcComp, ticksAway=ticksAway)
        elif self.nextbetCompDirty:
            self.updateBetCompensations(compPerc, ticksAway=ticksAway)


    def updateBetCompensations(self, compPerc, toCalcComp=None, ticksAway=0):
        if toCalcComp is None:
            toCalcComp = self.betsActive.iteritems()

        for betNum, betKey in toCalcComp:
            bet = self.bets[betKey]
            runnerPrice = self.getRunnerPricesId(bet.selectionId, bet.asianLineId)
            if runnerPrice:
                comp = bet.getCompensate(runnerPrice, compPerc, ticksAway)
            else:
                comp = None

            oldComp = self.betComps.get(betNum, None)

            oneWasNone = (not oldComp and comp) or (oldComp and not comp)
            bothExistAndNotEqual = (comp and oldComp) and (comp != oldComp)
            
            if self.nextbetCompDirty or oneWasNone or bothExistAndNotEqual:
                self.betComps[betNum] = comp
                self.betCompsDirty[betNum] = True

        if self.nextbetCompDirty:
            self.nextbetCompDirty = False


    def getBetById(self, betId):
        betStand = BetStand(betId)

        count = 0
        for betKey in self.betsActive.itervalues():
            bet = self.bets[betKey]
            if bet.betId == betId:
                betStand.addBet(bet)
                count += 1
                if count == 2:
                    break

        if not count:
            return None

        return betStand


    def getMatchedBetById(self, betId):
        for betKey in self.betsActive.itervalues():
            bet = self.bets[betKey]
            if bet.betId == betId and bet.betStatus == 'M':
                return bet

        return None


    def getBetCompById(self, betId):
        betComp = None
        for betKey in self.betsActive.iteritems():
            bet = self.bets[betKey]
            if bet.betId == betId and bet.betStatus == 'M':
                betNum = bet.betNum
                betComp = self.betComps.get(betNum, None)
                break

        return betComp
