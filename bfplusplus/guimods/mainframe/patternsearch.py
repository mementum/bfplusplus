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

import operator
import datetime

import wx

from gui.PatternManager import PatternManager

import bfobj
import bfpy
import threads.threadsbf as threadsbf
from util import Message


if True:
    def init(self):
        self.colFavDateTime = 0
        self.colFavDescription = 1
        self.colFavMarketName = 2

        self.RegisterFocusWin(self.m_listCtrlFavs)
        self.loadPatterns = dict()

        self.favMarkets = list()
        self.m_listCtrlFavs.InsertColumn(self.colFavDateTime, 'Date/Time')
        self.m_listCtrlFavs.InsertColumn(self.colFavDescription, 'Event')
        self.m_listCtrlFavs.InsertColumn(self.colFavMarketName, 'Market Name')

        charLen = [15, 24, 15]
        for i in range(self.m_listCtrlFavs.GetColumnCount()):
            # The autosize applies when some content has been inserted
            #self.m_listCtrlFavs.SetColumnWidth(l_i, wx.LIST_AUTOSIZE)
            self.m_listCtrlFavs.SetColumnWidth(i, charLen[i]*self.avgCharWidth)


    def OnFavourites(self, event):
        self.blockFavs.Show(False)
        self.m_listCtrlFavs.DeleteAllItems()

        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessages(exception)
            return

        self.favMarkets = response.favMarkets
        
        for row, marketItem in enumerate(response.favMarkets):
            strDateTime = marketItem.marketTime.strftime('%a, %b %d %H:%M')

            self.m_listCtrlFavs.InsertStringItem(row, strDateTime)
            self.m_listCtrlFavs.SetStringItem(row, self.colFavDescription, marketItem.lastMenuPart)
            self.m_listCtrlFavs.SetStringItem(row, self.colFavMarketName, marketItem.marketName)

        self.m_listCtrlFavs.Refresh()


    def OnListItemActivatedFavs(self, event):
        itemId = event.GetIndex()

        marketId = self.favMarkets[itemId].marketId
        exchangeId = self.favMarkets[itemId].exchangeId

        self.GetMarket(bfobj.MarketTuple(exchangeId, marketId), expandEvents=True)


    def OnButtonClickPatternManager(self, event):
        event.Skip()
        self.LoadPatternManager()


    def LoadPatternManager(self):
        patterns = self.PatternsFromReg()

        canLoad = True if self.thGetMarketPrices else False
        dlg = PatternManager(self, patterns, canLoad)
        retcode = dlg.ShowModal()

        if retcode != wx.ID_OK:
            return

        self.loadPatterns = dlg.loadPatterns
        if self.loadPatterns:
            self.LoadPatterns()


    def m_listCtrlFavsOnContextMenu(self, event):
        position = event.GetPosition()
        itemId, hitFlags = self.m_listCtrlFavs.HitTest(position)

        found = (itemId != wx.NOT_FOUND)
        self.m_menuItemFavSearchLoad.Enable(found)

        if found:
            self.m_listCtrlFavs.Select(itemId)

        self.m_menuItemReloadPattern.Enable(len(self.loadPatterns))

        patternNames = self.PatternNamesFromReg()
        self.loadPatternMenuItems = list()
        if patternNames:
            patternNames.sort()

            for patternName in patternNames:
                menuStr = 'Load: %s' % patternName
                menuItem = wx.MenuItem(self.m_menuFavSearch, wx.ID_ANY, menuStr, menuStr, wx.ITEM_CHECK)
                menuItem.patternName = patternName
                self.m_menuFavSearch.AppendItem(menuItem)
                if patternName in self.loadPatterns:
                    menuItem.Check(True)
                self.loadPatternMenuItems.append(menuItem)
                self.Bind(wx.EVT_MENU, self.OnMenuSelectionLoadPattern, id=menuItem.GetId())

        self.m_menuFavSearch.itemId = itemId
        self.m_listCtrlFavs.PopupMenu(self.m_menuFavSearch, position)

        if patternNames:
            for menuItem in self.loadPatternMenuItems:
                self.Unbind(wx.EVT_MENU, id=menuItem.GetId())
                self.m_menuFavSearch.Remove(menuItem.GetId())


    def OnMenuSelectionFavSearchLoad(self, event):
        itemId = self.m_menuFavSearch.itemId

        marketId = self.favMarkets[itemId].marketId
        exchangeId = self.favMarkets[itemId].exchangeId

        self.GetMarket(bfobj.MarketTuple(exchangeId, marketId), expandEvents=True)


    def OnMenuSelectionReloadPattern(self, event):
        event.Skip()
        self.LoadPatterns()


    def OnMenuSelectionPatternManager(self, event):
        event.Skip()
        self.LoadPatternManager()


    def OnMenuSelectionLoadPattern(self, event):
        itemId = event.GetId()
        menuItems = self.loadPatternMenuItems

        for menuItem in menuItems:
            if itemId == menuItem.GetId():
                patternName = menuItem.patternName
                break

        patterns = self.PatternsFromReg()
        self.loadPatterns = dict()
        self.loadPatterns[patternName] = patterns[patternName]
        self.LoadPatterns()


    def LoadPatterns(self):
        self.m_listCtrlFavs.DeleteAllItems()
        self.m_listCtrlFavs.InsertStringItem(0, '')
        self.m_listCtrlFavs.SetStringItem(0, 1, '--Processing--')
        self.m_listCtrlFavs.Refresh()

        if not hasattr(self, 'thFavourites'):
            self.thFavourites = threadsbf.ThreadFavs(self, self.OnFavourites)

        message = Message(action='favourites')
        message.marketData = self.marketData
        message.patterns = self.loadPatterns.values()
        self.blockFavs.Show(True)

        self.thFavourites.passMessage(message)


    def PatternNamesFromReg(self):
        patternNames = list()
        self.config.SetPath('/Favourites')
        more, value, index = self.config.GetFirstEntry()
        while more:
            patternNames.append(value)
            more, value, index = self.config.GetNextEntry(index)

        self.config.SetPath('/')
        return patternNames


    def PatternsFromReg(self):
        patterns = dict()
        self.config.SetPath('/Favourites')
        more, value, index = self.config.GetFirstEntry()
        while more:
            pattern = self.config.Read(value)
            pattern = eval('%s' % pattern)
            patterns[value] = pattern
            more, value, index = self.config.GetNextEntry(index)

        self.config.SetPath('/')
        return patterns


    def OnTextEnterSearch(self, event):
        self.DoSearch()

    def OnButtonClickSearch(self, event):
        self.DoSearch()
        
    def DoSearch(self):
        text2search = self.m_textCtrlSearch.GetValue()
        if not text2search:
            return

        self.m_listCtrlFavs.DeleteAllItems()
        self.m_listCtrlFavs.InsertStringItem(0, '')
        self.m_listCtrlFavs.SetStringItem(0, 1, '--Processing--')
        self.m_listCtrlFavs.Refresh()

        if not hasattr(self, 'thSearch'):
            self.thSearch = threadsbf.ThreadSearch(self, self.OnFavourites)

        message = Message(action='search')
        message.marketData = self.marketData
        message.search = text2search
        self.blockFavs.Show(True)

        self.thSearch.passMessage(message)
