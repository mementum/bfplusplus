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
import datetime
import time

import wx

from bfobj import MarketComp, MarketTuple
import bfpy
from util import Message

if True:
    def init(self):
        self.marketStopped = self.config.ReadBool('Market Stopped', False)
        self.m_toggleBtnStopMarket.SetValue(self.marketStopped)
        label = 'Start Market' if self.marketStopped else 'Stop Market'
        self.m_toggleBtnStopMarket.SetLabel(label)
        self.m_toggleBtnStopMarket.SetLabel(label)

        # Indicates if a market is currently loaded
        self.noMarketLoaded = True

        # self.marketCache = defaultdict(dict)
        self.marketCache = dict()
        self.marketTuple = None

        self.ipdelay = 0

        # Wallet icons
        self.walletFlags = dict()
        bmp = wx.Bitmap('./icons/famfamfam-silk/world.png')
        self.walletFlags[bfpy.Global] = bmp
        bmp = wx.Bitmap('./icons/famfamfam-flags/au_stretched.png')
        self.walletFlags[bfpy.ExchangeAus] = bmp
        bmp = wx.Bitmap('./icons/famfamfam-flags/gb_stretched.png')
        self.walletFlags[bfpy.ExchangeUK] = bmp

        self.inPlayIcons = dict()
        bmp = wx.Bitmap('./icons/famfamfam-silk/cancel.png')
        self.inPlayIcons[0] = bmp
        bmp = wx.Bitmap('./icons/famfamfam-silk/accept_grayed.png')
        self.inPlayIcons[1] = bmp
        bmp = wx.Bitmap('./icons/famfamfam-silk/accept.png')
        self.inPlayIcons[2] = bmp

        self.m_listCtrlMarketInfo.InsertColumn(0, 'Name')
        self.m_listCtrlMarketInfo.InsertColumn(1, 'Value')
        charLen = [12, 254]
        for i in range(self.m_listCtrlMarketInfo.GetColumnCount()):
            # The autosize applies when some content has been inserted
            #self.m_listCtrlFavs.SetColumnWidth(l_i, wx.LIST_AUTOSIZE)
            self.m_listCtrlMarketInfo.SetColumnWidth(i, charLen[i]*self.avgCharWidth)

        self.m_listCtrlGetAllMarketsInfo.InsertColumn(0, 'Name')
        self.m_listCtrlGetAllMarketsInfo.InsertColumn(1, 'Value')
        charLen = [12, 254]
        for i in range(self.m_listCtrlGetAllMarketsInfo.GetColumnCount()):
            # The autosize applies when some content has been inserted
            #self.m_listCtrlFavs.SetColumnWidth(l_i, wx.LIST_AUTOSIZE)
            self.m_listCtrlGetAllMarketsInfo.SetColumnWidth(i, charLen[i]*self.avgCharWidth)

        self.m_listCtrlRunnersInfo.InsertColumn(0, 'Name')
        self.m_listCtrlRunnersInfo.InsertColumn(1, 'Value')
        charLen = [12, 254]
        for i in range(self.m_listCtrlRunnersInfo.GetColumnCount()):
            # The autosize applies when some content has been inserted
            #self.m_listCtrlFavs.SetColumnWidth(l_i, wx.LIST_AUTOSIZE)
            self.m_listCtrlRunnersInfo.SetColumnWidth(i, charLen[i]*self.avgCharWidth)

        self.RegisterFocusWin(self.m_listCtrlMarketInfo)
        self.RegisterFocusWin(self.m_listCtrlGetAllMarketsInfo)
        self.RegisterFocusWin(self.m_listCtrlRunnersInfo)


    def GetMarket(self, marketTuple, forceReload=False, expandEvents=False):
        if not self.useMarketCache:
            forceReload = True

        # Do not load if loaded
        if marketTuple == self.marketTuple and not forceReload:
            if expandEvents:
                self.ExpandEvents(marketTuple)
            return

        recordOn = self.m_toggleBtnRecord.GetValue()
        playOn = self.m_toggleBtnPlay.GetValue()

        if self.marketTuple and (self.bfModulesActive or recordOn or playOn):
            retcode = wx.MessageBox('Either a module, or record/play session is active for the current market\n\n'
                                    'Press "Yes" to switch to the new market and stop the module/record/play session',
                                    'Market Change - Confirmation required', wx.YES_NO)

            if retcode != wx.YES:
                return

            # the dialog tends to remain on-screen
            self.Refresh()

            if bfModsOn:
                self.BfModulesStop()
            if recordOn:
                self.RecordStop()
            elif playOn:
                self.PlayStop()

        if self.marketTuple:
            stopBetsExist = False
            marketComp = self.marketCache[self.marketTuple]
            for stopbetinfo in marketComp.stopbetinfos:
                if stopbetinfo.status == 'active':
                    stopBetsExist = True
                    break

            if stopBetsExist:
                retcode = wx.MessageBox('One or more stop bets are active. They will not be watched until\n'
                                        'you switch back to this market'
                                        'Press "Yes" to switch to the new market',
                                        'Market Change - Confirmation required', wx.YES_NO)

                if retcode != wx.YES:
                    return

        self.blockGetMarket.Show(True)

        if not forceReload and marketTuple in self.marketCache:
            self.LoadMarket(marketTuple, expandEvents=expandEvents)

        else:
            message = Message(action='getMarket', marketTuple=marketTuple)
            message.expandEvents = expandEvents
            self.thMisc.passMessage(message)


    def OnGetMarket(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if self.blockGetMarket.IsShown():
                self.blockGetMarket.Show(False)

            self.m_buttonExpandEvents.Disable()
            self.m_buttonSaveAsFav.Disable()
            count = self.m_choiceMarketHistory.GetCount()
            if not count:
                self.m_choiceMarketHistory.Disable()
            self.noMarketLoaded = True

            self.marketTuple = None

            nullMarketTuple = MarketTuple(0, 0)
            self.GetMarketPrices(nullMarketTuple)
            self.GetMarketProfitAndLoss(nullMarketTuple)
            self.GetMUBets(nullMarketTuple)

            numRows = self.m_gridMarket.GetNumberRows()
            if numRows > 0:
                self.m_gridMarket.DeleteRows(0, numRows)

            self.m_gridMarket.SetColLabelValue(self.colOverroundBack, '')
            self.m_gridMarket.SetColLabelValue(self.colOverroundLay, '')
            self.m_listCtrlBets.DeleteAllItems()

            self.marketStatusOverlay.SetMessage('Unloaded')
            self.marketStatusOverlay.Show(True)

            self.matchedOverlay.SetMessage('%s ' % self.currency)

            self.m_bitmapExchange.SetBitmap(self.walletFlags[bfpy.Global])
            self.m_staticTextMarketType.SetLabel('')
            self.m_staticTextStartTime.SetLabel('')
            self.m_staticTextWinners.SetLabel('')
            self.m_staticTextRefreshTime.SetLabel('')
            self.m_staticTextInPlayDelay.SetLabel('')
            self.m_bitmapInPlay.SetBitmap(self.inPlayIcons[0])

            if exception:
                self.LogMessages(exception)
            return

        marketTuple = message.marketTuple
        self.marketCache[marketTuple] = MarketComp(response.market)

        if hasattr(response, 'play'):
            play = True
        else:
            play = False
        self.LoadMarket(marketTuple, expandEvents=message.expandEvents, play=play)


    def LoadMarket(self, marketTuple, expandEvents=False, play=False):
        if self.blockGetMarket.IsShown():
            self.blockGetMarket.Show(False)

        self.marketTuple = marketTuple
        marketComp = self.marketCache[marketTuple]

        self.ipdelay = 0
        self.stopBetSupsStamp = time.clock()
        self.FillStopBetCtrl()

        if self.noMarketLoaded:
            self.m_buttonExpandEvents.Enable()
            self.m_buttonSaveAsFav.Enable()
            self.m_choiceMarketHistory.Enable()

            self.noMarketLoaded = False

        self.m_bitmapExchange.SetBitmap(self.walletFlags[marketTuple.exchangeId])
        self.m_staticTextMarketType.SetLabel(self.mktTyp[marketComp.marketType])

        self.m_listCtrlMarketInfo.DeleteAllItems()
        self.m_listCtrlGetAllMarketsInfo.DeleteAllItems()
        self.m_listCtrlRunnersInfo.DeleteAllItems()

        def stripList(l):
            return str(l).strip('[]')
        
        infoItems = [
            ('bspMarket', None), ('countryISO3', None), ('discountAllowed', None), ('eventHierarchy', stripList),
            ('eventTypeId', None), ('interval', None), ('lastRefresh', None), ('licenseId', None),
            ('marketBaseRate', None), ('marketDescriptionHasDate', None), ('marketDisplayTime', None),
            ('marketId', None), ('exchangeId', None), ('marketStatus', None),
            ('marketId', None), ('exchangeId', None), ('marketSuspendTime', None), ('marketTime', None),
            ('marketType', None), ('marketTypeVariant', None), ('maxUnitValue', None), ('menuPath', None),
            ('minUnitValue', None), ('name', None), ('numberOfWinners', None), ('parentEventId', None),
            ('runners', len), ('runnersMayBeAdded', None), ('timezone', None), ('unit', None),
            ]

        row = 0
        for itemName, itemFunc in infoItems:
            row = self.m_listCtrlMarketInfo.InsertStringItem(row, itemName)

            itemContent = getattr(marketComp, itemName)
            if itemFunc:
                itemContent = itemFunc(itemContent)
                
            if isinstance(itemContent, basestring):
                self.m_listCtrlMarketInfo.SetStringItem(row, 1, itemContent)
            else:
                self.m_listCtrlMarketInfo.SetStringItem(row, 1, str(itemContent))

            row += 1

        infoItems = [
            ('marketId', None), ('marketName', None), ('marketType', None), ('marketStatus', None),
            ('eventDate', None), ('menuPath', None), ('eventHierarchy', stripList), ('betDelay', None),
            ('exchangeId', None), ('countryISO3', None), ('lastRefresh', None), ('numberOfRunners', None),
            ('numberOfWinners', None), ('totalAmountMatched', None), ('bspMarket', None), ('turningInPlay', None),
            ]

        row = 0
        for itemName, itemFunc in infoItems:
            row = self.m_listCtrlGetAllMarketsInfo.InsertStringItem(row, itemName)

            itemContent = getattr(marketComp, itemName)
            if itemFunc:
                itemContent = itemFunc(itemContent)
                
            if isinstance(itemContent, basestring):
                self.m_listCtrlGetAllMarketsInfo.SetStringItem(row, 1, itemContent)
            else:
                self.m_listCtrlGetAllMarketsInfo.SetStringItem(row, 1, str(itemContent))

            row += 1


        infoItems = [
            ('asianLineId', None), ('handicap', None), ('name', None), ('selectionId', None),
            ]

        row = 0
        for runner in marketComp.runners:
            for itemName, itemFunc in infoItems:
                row = self.m_listCtrlRunnersInfo.InsertStringItem(row, itemName)

                itemContent = getattr(runner, itemName)
                if itemFunc:
                    itemContent = itemFunc(itemContent)

                if isinstance(itemContent, basestring):
                    self.m_listCtrlRunnersInfo.SetStringItem(row, 1, itemContent)
                else:
                    self.m_listCtrlRunnersInfo.SetStringItem(row, 1, str(itemContent))
                row += 1

        if marketComp.marketType == 'R':
            self.m_checkBoxDisplayPercPrices.Disable()
        else:
            self.m_checkBoxDisplayPercPrices.Enable()

        playOn = self.m_toggleBtnPlay.GetValue()
        if not playOn:
            self.m_toggleBtnRecord.Enable()
        
        if expandEvents:
            self.ExpandEvents(marketTuple)

        menuPath, menuParts = marketComp.getFullMenuPath()
        self.SetTitle('%s - %s' % (self.BetBuddyStr, menuPath))

        # History implementation
        historyCount = self.m_choiceMarketHistory.GetCount()
        for pos in xrange(historyCount):
            histMarketTuple = self.m_choiceMarketHistory.GetClientData(pos)
            if histMarketTuple == marketTuple:
                self.m_choiceMarketHistory.Delete(pos)
                historyCount -= 1
                break

        if historyCount == 10:
            self.m_choiceMarketHistory.Delete(historyCount - 1)

        if False:
            historyParts = menuParts[0:3]
            menuPartsLen = len(menuParts)

            if menuPartsLen > 5:
                historyParts.extend(['...', menuParts[-2], menuParts[-1]])
            elif menuPartsLen > 4:
                historyParts.extend(['...', menuParts[-1]])
            elif menuPartsLen > 3:
                historyParts.extend([menuParts[-1]])
        else:
            historyParts = menuParts

        historyPath = '\\'.join(historyParts)
        self.m_choiceMarketHistory.Insert(historyPath, 0, marketTuple)
        self.m_choiceMarketHistory.SetSelection(0)

        self.m_staticTextStartTime.SetLabel(marketComp.marketTime.strftime('%Y-%m-%d %H:%M'))

        # Either Back/Lay, Buy/Sell or others
        self.m_gridMarket.SetColLabelValue(self.colBackLegend, self.backLegend[marketComp.marketType])
        self.m_gridMarket.SetColLabelValue(self.colLayLegend, self.layLegend[marketComp.marketType])

        self.m_htmlWinMarketInfo.SetPage(marketComp.marketDescription)

        # Remove list of bets since we loaded (or re-loaded) a market
        self.m_listCtrlBets.DeleteAllItems()

        # Delete existing rows if needed
        numRows = self.m_gridMarket.GetNumberRows()
        if numRows > 0:
            self.m_gridMarket.DeleteRows(0, numRows)

        self.m_gridMarket.AppendRows(len(marketComp.runners))
        self.m_gridMarket.Refresh()

        self.CellColours()
        aFont = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=False, face='Arial')
        for row, runner in enumerate(marketComp.runners):
            label = marketComp.getRunnerLabel(runner)
            self.m_gridMarket.SetRowLabelValue(row, label)
            self.m_gridMarket.SetRowSize(row, 60)
            self.m_gridMarket.SetCellFont(row, self.colGridBalanceRef, aFont)

        if marketComp.runners and marketComp.numberOfWinners == 1:
            self.m_gridMarket.SetCellValue(0, self.colGridBalanceRef, u'\u25A0')
            self.compIndex = 0
        else:
            self.compIndex = None

        # self.m_buttonLadder.Enable(marketComp.marketType == 'A')

        self.matchedOverlay.Show(True)
        dataMarket = self.dataMarkets.get(marketComp.exchangeId, None)
        if dataMarket:
            marketItem = dataMarket.get(marketComp.marketId, None)
            if marketItem:
                if marketItem.turningInPlay:
                    self.m_bitmapInPlay.SetBitmap(self.inPlayIcons[1])
                else:
                    self.m_bitmapInPlay.SetBitmap(self.inPlayIcons[0])
        

        self.UpdateMarket(marketTuple, fromLoadMarket=True)
        self.m_listCtrlBets.DeleteAllItems()
        if not playOn:
            if self.optNet:
                self.saveCount = self.optNetGuard
                self.saveCountPNL = int(self.optNetGuard / 2) + 1
            if not self.marketStopped:
                self.GetMarketPrices(marketTuple, virtualPrices=(marketComp.marketType == 'O'))
                self.GetMUBets(marketTuple)
                self.GetMarketProfitAndLoss(marketTuple)

        else:
            nullMarketTuple = MarketTuple(0, 0)
            self.GetMarketPrices(nullMarketTuple)
            self.GetMUBets(nullMarketTuple)
            self.GetMarketProfitAndLoss(nullMarketTuple)

        if self.bfModulesActive:
            self.ModulesFillRunners(changedMarket=True)


    def CellColours(self):
        numRows = self.m_gridMarket.GetNumberRows()
        for row in xrange(numRows):
            for col in xrange(0, self.numPrices):
                self.m_gridMarket.SetCellBackgroundColour(row, col, self.cellBackColour)
                self.m_gridMarket.SetCellTextColour(row, col, self.cellBackColourText)
                self.m_gridMarket.SetCellBackgroundColour(row, col + self.numPrices, self.cellLayColour)
                self.m_gridMarket.SetCellTextColour(row, col + self.numPrices, self.cellLayColourText)

        self.m_gridMarket.Refresh()


    def MarketStatusColours(self):

        if self.marketTuple is None:
            return

        marketComp = self.marketCache[self.marketTuple]

        self.marketStatusOverlay.SetMessage(marketComp.marketStatus)

        if marketComp.marketStatus in ('SUSPENDED', 'CLOSED'):

            if marketComp.marketStatus == 'SUSPENDED':
                self.stopBetSusp = True
 
            if not self.marketStatusOverlay.IsShown():
                self.marketStatusOverlay.SetBackgroundColour(self.marketSuspClosedColour)
                self.marketStatusOverlay.SetForegroundColour(self.marketSuspClosedColourText)
                self.marketStatusOverlay.Layout()
                self.marketStatusOverlay.Show(True)
            
        elif marketComp.marketStatus in ('ACTIVE'):
            if self.stopBetSusp == True:
                self.stopBetSusp = False
                self.stopBetSupsStamp = time.clock()

            self.marketStatusOverlay.Show(False)
            if True and self.marketStatusOverlay.IsShown():
                self.marketStatusOverlay.Layout()

            # For testing purposes
            if False and not self.marketStatusOverlay.IsShown():
                self.marketStatusOverlay.SetBackgroundColour(self.marketActiveColour)
                self.marketStatusOverlay.SetForegroundColour(self.marketActiveColourText)
                self.marketStatusOverlay.SetMessage(marketComp.marketStatus)
                self.marketStatusOverlay.Layout()
                self.marketStatusOverlay.Show(True)


    def UpdateMarket(self, marketTuple, fromLoadMarket=False):
        if marketTuple != self.marketTuple:
            # skip delayed prices from threads
            return

        marketComp = self.marketCache[marketTuple]

        numberOfWinners = marketComp.numberOfWinners
        numberOfRunners = len(marketComp.runners)
        winnersOverRunners = '%d/%d' % (numberOfWinners, numberOfRunners)
        self.m_staticTextWinners.SetLabel(winnersOverRunners)

        self.MarketStatusColours()

        if marketComp.marketStatus == 'CLOSED':
            nullMarketTuple = MarketTuple(0, 0)
            self.GetMarketPrices(nullMarketTuple)
            self.GetMarketProfitAndLoss(nullMarketTuple)
            self.GetMUBets(nullMarketTuple)

            # Stop stopbets
            self.StopBetsStop()

            self.m_gridMarket.SetColLabelValue(self.colOverroundBack, '')
            self.m_gridMarket.SetColLabelValue(self.colOverroundLay, '')

            # Remove the bets (they may have been automatically removed)
            # self.m_listCtrlBets.DeleteAllItems()

        # Remove a closed market from the saved favourites
        if fromLoadMarket and marketComp.marketStatus == 'CLOSED' and marketTuple in self.savedMarkets:
            msgDlg = wx.MessageDialog(self,
                                      'This market has been closed, but it is saved as favourite.\n\n'
                                      'Remove the market from the list of saved markets?',
                                      'Closed Market',
                                      wx.YES_NO|wx.ICON_QUESTION)
            
            if msgDlg.ShowModal() == wx.ID_YES:
                self.RemoveSavedMarket(marketTuple)


    def OnButtonClickExpandMarket(self, event):
        self.ExpandEvents(self.marketTuple)


    def OnToggleButtonStopMarket(self, event):
        self.marketStopped = self.m_toggleBtnStopMarket.GetValue()
        self.MarketStartStop()

        if self.marketStopped:
            self.stoppedOverlay.Show(True)
            label = 'Start Market'
        else:
            self.stoppedOverlay.Show(False)
            label = 'Stop Market'

        self.m_toggleBtnStopMarket.SetLabel(label)
        self.m_toggleBtnStopMarket.Refresh()


    def MarketStartStop(self):
        if self.marketStopped:
            nullMarketTuple = MarketTuple(0, 0)
            self.GetMarketPrices(nullMarketTuple)
            self.GetMarketProfitAndLoss(nullMarketTuple)
            self.GetMUBets(nullMarketTuple)

        else:
            if self.marketTuple is not None:
                marketComp = self.marketCache[self.marketTuple]
                self.GetMarketPrices(self.marketTuple, virtualPrices=(marketComp.marketType == 'O'))
                self.GetMarketProfitAndLoss(self.marketTuple)
                self.GetMUBets(self.marketTuple)
