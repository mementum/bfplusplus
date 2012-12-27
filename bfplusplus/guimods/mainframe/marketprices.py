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

from datetime import datetime
import time

from bfobj import MarketTuple
from util import Message, splitThousands


if True:
    def init(self):
        self.virtualPrices = self.config.ReadBool('Virtual Prices', True)
        self.config.WriteBool('Virtual Prices', self.virtualPrices)
        self.m_checkBoxVirtualPrices.SetValue(self.virtualPrices)


    def OnCheckBoxVirtualPrices(self, event):
        self.virtualPrices = self.m_checkBoxVirtualPrices.GetValue()
        self.config.WriteBool('Virtual Prices', self.virtualPrices)
        if self.marketTuple:
            marketComp = self.marketCache[self.marketTuple]
            virtualPrices = marketComp.marketType == 'O'
            self.GetMarketPrices(self.marketTuple, virtualPrices=virtualPrices)
        else:
            nullMarketTuple = MarketTuple(0, 0)
            self.GetMarketPrices(nullMarketTuple)


    def OnCheckBoxDisplayPercPrices(self, event):
        if self.thGetMarketPrices:
            self.UpdateMarketPrices(self.marketTuple)
        showProb = self.m_checkBoxDisplayPercPrices.GetValue()
        self.config.WriteBool('Show Probability', showProb)


    def GetMarketPrices(self, marketTuple, virtualPrices=False):
        if self.thGetMarketPrices:
            message = Message(marketTuple=marketTuple, ladder=False,
                              virtualPrices=(virtualPrices and self.virtualPrices))

            self.thGetMarketPrices.passMessage(message)


    def OnGetMarketPrices(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessages(exception)
            return

        marketComp = self.marketCache[message.marketTuple]
        compPerc = float(self.m_sliderCompensate.GetValue()) / 100.0
        ticksAway = 0 if not self.compTicksAway else self.compTicksAwayCount
        marketComp.updateMarketPrices(response.marketPrices, compPerc, self.compIndex,
                                      ticksAway=ticksAway)

        if self.bfModulesActive or self.recordModule or self.excelModActive:
            clone = marketComp.clone()
            if self.recordModule:
                self.recordModule.passMessage(clone)
            for bfModule in self.bfModules.itervalues():
                bfModule.passMessage(clone)
            if self.excelModActive and not self.excelModPaused:
                excelMsg = Message(marketComp=clone)
                excelMsg.workbooks = self.workbooks
                excelMsg.sheets = self.sheets
                self.excelModule.passMessage(excelMsg)

        self.UpdateMarket(message.marketTuple)
        self.UpdateMarketPrices(message.marketTuple)
        self.UpdateMarketProfitAndLoss(message.marketTuple)
        self.UpdateMUBetsCompensations(message.marketTuple)
        self.StopBetCheck()


    def InPlayColours(self):
        label = self.m_staticTextInPlayDelay.GetLabel()

        if not label:
            return

        marketComp = self.marketCache[self.marketTuple]

        if marketComp.delay:
            inPlayColourBG = self.inplayColour
            inPlayColourFG = self.inplayColourText
        else:
            inPlayColourBG = self.inplayOffColour
            inPlayColourFG = self.inplayOffColourText

        self.m_staticTextInPlayDelay.SetBackgroundColour(inPlayColourBG)
        self.m_staticTextInPlayDelay.SetForegroundColour(inPlayColourFG)
        self.m_staticTextInPlayDelay.Refresh()


    def UpdateMarketPrices(self, marketTuple):
        if marketTuple is None:
            return

        if marketTuple != self.marketTuple:
            # skip delayed prices from threads
            return

        marketComp = self.marketCache[marketTuple]

        if not self.useFreeApi:
            curTime = datetime.now()
            curMicroSecs = curTime.microsecond
            curDecSecs = int(float(curMicroSecs) / 100000.0)
            self.m_staticTextRefreshTime.SetLabel('%s.%d' % (time.strftime('%H:%M:%S'), curDecSecs))
        else:
            self.m_staticTextRefreshTime.SetLabel('%s' % time.strftime('%H:%M:%S'))
        self.m_staticTextRefreshTime.SetBackgroundColour(self.networkOKColour)
        self.m_staticTextRefreshTime.SetForegroundColour(self.networkOKColourText)
        self.m_staticTextRefreshTime.Refresh()


        if self.ipdelay != marketComp.delay:
            self.stopBetSupsStamp = time.clock()
            self.ipdelay = marketComp.delay

            self.m_bitmapInPlay.SetBitmap(self.inPlayIcons[2])

        self.m_staticTextInPlayDelay.SetLabel('%d' % marketComp.delay)
        self.InPlayColours()

        if marketComp.marketStatus != 'CLOSED':
            rows2Remove = list()
            for row, runner in enumerate(marketComp.runners):

                # runnerPrices = marketComp.runnerPrices[runner.selectionId]
                runnerPrices = marketComp.getRunnerPrices(runner)
                if not runnerPrices:
                    rows2Remove.append(row)

            if rows2Remove:
                marketComp.removeRunners(rows2Remove)

            rows2Remove.sort(reverse=True)
            for row in rows2Remove:
                self.m_gridMarket.DeleteRows(row, 1)

        numberOfWinners = marketComp.numberOfWinners
        numberOfRunners = len(marketComp.runnerPrices)
        winnersOverRunners = '%d/%d' % (numberOfWinners, numberOfRunners)
        self.m_staticTextWinners.SetLabel(winnersOverRunners)

        for row, runner in enumerate(marketComp.runners):
            # runnerPrices = marketComp.runnerPrices[runner.selectionId]
            runnerPrices = marketComp.getRunnerPrices(runner)

            if not runnerPrices:
                for col in xrange(0, self.colGridBalance):
                    self.m_gridMarket.SetCellValue(row, col, '')

                continue

            backPrices = runnerPrices.bestPricesToBack
            layPrices = runnerPrices.bestPricesToLay

            priceStr = u'%.2f\n%s'

            for col, backPrice in enumerate(backPrices):
                backPriceStr = priceStr % (backPrice.price, splitThousands(int(backPrice.amountAvailable)))
                if not col and self.m_checkBoxDisplayPercPrices.GetValue() and self.m_checkBoxDisplayPercPrices.IsEnabled():
                    backPriceStr += '\n(%.2f%%)' % runnerPrices.perc
                    
                self.m_gridMarket.SetCellValue(row, self.colBackEnd - col, backPriceStr)

            for col in xrange(0, self.numPrices - len(backPrices)):
                self.m_gridMarket.SetCellValue(row, self.colBackStart + col, '')
                           
            for col, layPrice in enumerate(layPrices):
                layPriceStr = priceStr % (layPrice.price, splitThousands(int(layPrice.amountAvailable)))
                self.m_gridMarket.SetCellValue(row, self.colLayStart + col, layPriceStr)

            for col in xrange(0, self.numPrices - len(layPrices)):
                self.m_gridMarket.SetCellValue(row, self.colLayEnd - col, '')

        self.matchedOverlay.SetMessage(u'%s %s' % (self.currency, splitThousands(int(marketComp.totalAmountMatched))))
        self.matchedOverlay.Refresh()
        
        if marketComp.marketType == 'O' and marketComp.numberOfWinners == 1:
            self.m_gridMarket.SetColLabelValue(self.colOverroundBack, '%.2f%%' % marketComp.backOverround)
            self.m_gridMarket.SetColLabelValue(self.colOverroundLay, '%.2f%%' % marketComp.layOverround)
