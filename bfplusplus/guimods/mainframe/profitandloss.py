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

from bfobj import MarketTuple
from util import Message

if True:
    def init(self):
        showPnL = self.config.ReadBool('Show Profit and Loss', True)
        self.config.WriteBool('Show Profit and Loss', showPnL)
        self.m_checkBoxShowProfitAndLoss.SetValue(showPnL)


    def GetMarketProfitAndLoss(self, marketTuple):
        if self.thGetMarketPrices:
            if marketTuple.marketId:
                marketComp = self.marketCache[marketTuple]
                marketComp.profitAndLossDirty()
                # Range markets do not support "profit and loss"
                if marketComp.marketType in ('R', 'L'):
                    marketTuple = MarketTuple(0, 0)

            message = Message(marketTuple=marketTuple)
            self.thGetMarketProfitAndLoss.passMessage(message)


    def OnGetMarketProfitAndLoss(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessages(exception)
            return

        marketComp = self.marketCache[message.marketTuple]
        compPerc = float(self.m_sliderCompensate.GetValue())/100.0
        ticksAway = 0 if not self.compTicksAway else self.compTicksAwayCount
        marketComp.updateMarketProfitAndLoss(response.annotations, compPerc, self.compIndex,
                                             ticksAway=ticksAway)

        if not self.saveCount:
            if self.saveCountPNL:
                self.saveCountPNL -= 1
            else:
                self.GetMarketProfitAndLoss(MarketTuple(0, 0))

        self.UpdateMarketProfitAndLoss(message.marketTuple)


    def OnCheckBoxShowProfitAndLoss(self, event):
        showPnL = self.m_checkBoxShowProfitAndLoss.GetValue()
        self.config.WriteBool('Show Profit and Loss', showPnL)
        if self.thGetMarketPrices:
            self.UpdateMarketProfitAndLoss(self.marketTuple, doShowPnL=showPnL)


    def UpdateMarketProfitAndLoss(self, marketTuple, doShowPnL=False, whatIf=False):
        if marketTuple is None:
            return

        if marketTuple != self.marketTuple:
            # skip delayed prices from threads
            return

        marketComp = self.marketCache[marketTuple]
        multiWinner = (marketComp.numberOfWinners != 1)

        # Prescan the selectionIds in Asian Markets to see how much the
        # first selection id repeats itself
        if marketComp.marketType == 'A':
            if marketComp.runners:
                selId = marketComp.runners[0].selectionId

            selIdCount = 0
            for runner in marketComp.runners:
                if runner.selectionId == selId:
                    selIdCount += 1

        showPNL = self.m_checkBoxShowProfitAndLoss.GetValue()
        seenAsianAnn = 0
        for row, runner in enumerate(marketComp.runners):
            pnlStr = ''

            if showPNL:
                if not doShowPnL and not whatIf and \
                       not marketComp.annotationsDirty[runner.selectionId]:
                    continue

                try:
                    annotations = marketComp.annotations[runner.selectionId]
                except KeyError:
                    continue
                numAnn = len(annotations)

                if marketComp.marketType == 'A':
                    if selIdCount == 1:
                        if seenAsianAnn < numAnn and annotations:
                            seenAsianAnn = numAnn

                            for annotation in annotations:
                                pnlStr += '\n%.2f' % annotation.ifWin
                                pnlStr += ' (%s/%s)' % (getattr(annotation, 'from'), annotation.to)

                    elif seenAsianAnn < numAnn:
                        if annotations:
                            annotation = annotations[seenAsianAnn]
                            seenAsianAnn += 1

                            pnlStr += '\n%.2f' % annotation.ifWin
                            pnlStr += ' (%s/%s)' % (getattr(annotation, 'from'), annotation.to)

                elif annotations:
                    annotation = annotations[0]
                    pnlStr += '\n%.2f' % annotation.ifWin

                    if multiWinner:
                        pnlStr += '%s%.2f' % (self.annSep['MW'], annotation.ifLoss)

                    if self.curCompensation and not self.curCompensation.size < self.minStakes.minimumStake:
                        if multiWinner and self.curCompensation.selectionId != runner.selectionId:
                            pass
                        else:
                            pnlStr += '\n'
                            ifWin = annotation.ifWin
                            ifWin += self.curCompensation.getIfWinForSelectionId(runner.selectionId)
                            pnlStr += '(%.2f' % ifWin

                            if multiWinner:
                                ifLoss = annotation.ifLoss
                                ifLoss += self.curCompensation.ifLoss
                                pnlStr += '%s%.2f' % (self.annSep['MW'], ifLoss)

                            pnlStr += ')'

            label = marketComp.getRunnerLabel(runner)
            fullLabel = '%s%s' % (label, pnlStr)
            self.m_gridMarket.SetRowLabelValue(row, fullLabel)

        # Fill the "Balance column" with the best/worst compensations for each runner
        for row, runner in enumerate(marketComp.runners):
            runnerComps = marketComp.getCompensations(runner)

            if not runnerComps:
                self.m_gridMarket.SetCellValue(row, self.colGridBalance, '')
                continue

            label = ''
            i = 0
            for comp in runnerComps:
                if i > 3:
                    break
                if not comp.size < self.minStakes.minimumStake:
                    label += u'%.2f/%.2f\n' % (comp.compWin, comp.compLoss)
                    i += 1

            self.m_gridMarket.SetCellValue(row, self.colGridBalance, label.rstrip())
