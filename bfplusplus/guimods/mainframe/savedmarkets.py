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

from operator import itemgetter

from bfobj import MarketTuple

if True:
    def init(self):
        page = self.config.ReadInt('Favourites Page', 0)
        self.config.WriteInt('Favourites Page', page)
        self.m_notebookFavs.ChangeSelection(page)

        self.RegisterFocusWin(self.m_listBoxSavedMarkets)


    def OnNotebookPageChangedFavs(self, event):
        event.Skip()
        page = event.GetSelection()
        self.config.WriteInt('Favourites Page', page)


    def RemoveSavedMarket(self, marketTuple):
        for item in range(self.m_listBoxSavedMarkets.GetCount()):

            if marketTuple == self.m_listBoxSavedMarkets.GetClientData(item):

                # Remove from the internal list
                del self.savedMarkets[marketTuple]
                
                self.config.SetPath('/Saved')
                # Remove from the registry
                configKey = '%d%d' % (marketTuple.exchangeId, marketTuple.marketId)
                self.config.DeleteEntry(configKey, False)
                self.config.SetPath('/')

                # Removefrom the control
                self.m_listBoxSavedMarkets.Delete(item)
                break


    def OnButtonClickSaveMarket(self, event):
        if not self.marketTuple:
            return

        marketTuple = self.marketTuple
        if marketTuple in self.savedMarkets:
            return

        marketComp = self.marketCache[marketTuple]
        menuPath, menuParts = marketComp.getFullMenuPath()

        if False:
            savedMaxLen = max(0, len(menuParts) - 3)
            menuSavedParts = menuParts[savedMaxLen:]
            if savedMaxLen > 0:
                menuSavedParts.insert(0, '')
        else:
            menuSavedParts = menuParts
        savedPath = '\\'.join(menuSavedParts)

        self.savedMarkets[marketTuple] = savedPath

        self.config.SetPath('/Saved');
        configKey = '%d%d' % (marketTuple.exchangeId, marketTuple.marketId)
        self.config.Write(configKey, savedPath)
        self.config.SetPath('/');

        item = self.m_listBoxSavedMarkets.Append(savedPath, marketTuple)
        self.m_listBoxSavedMarkets.DeselectAll()
        self.m_listBoxSavedMarkets.Select(item)

        self.m_notebookFavs.ChangeSelection(1)


    def LoadSavedMarkets(self):
        self.savedMarkets = dict()

        self.config.SetPath('/Saved')

        more, value, index = self.config.GetFirstEntry()
        while more:
            savedPath = self.config.Read(value)

            exchangeId = int(value[0])
            marketId = int(value[1:])
            marketTuple = MarketTuple(exchangeId, marketId)

            self.savedMarkets[marketTuple] = savedPath
            more, value, index = self.config.GetNextEntry(index)

        self.config.SetPath('/')

        for marketTuple, savedPath in self.savedMarkets.iteritems():
            self.m_listBoxSavedMarkets.Append(savedPath, marketTuple)


    def m_listBoxSavedMarketsOnContextMenu(self, event):
        position = event.GetPosition()

        item = self.m_listBoxSavedMarkets.HitTest(position)

        itemFound = (item != wx.NOT_FOUND)
        selections = self.m_listBoxSavedMarkets.GetSelections()

        if itemFound and item not in selections:
            self.m_listBoxSavedMarkets.DeselectAll()
            self.m_listBoxSavedMarkets.Select(item)
            selections = [item]

        count = self.m_listBoxSavedMarkets.GetCount()
        numSelections = len(selections)
        multiSelection = (numSelections > 1)

        self.m_menuItemSavedMarketsLoad.Enable(itemFound and not multiSelection)
        self.m_menuItemSavedMarketsSelectAll.Enable(numSelections < count)
        self.m_menuItemSavedMarketsDeleteAll.Enable(count and numSelections < count)
        self.m_menuItemSavedMarketsDeleteSelected.Enable(numSelections)

        self.m_listBoxSavedMarkets.PopupMenu(self.m_menuSavedMarkets, position)


    def OnMenuSelectionSavedMarketsLoadMarket(self, event):
        items = self.m_listBoxSavedMarkets.GetSelections()
        marketTuple = self.m_listBoxSavedMarkets.GetClientData(items[0])
        self.GetMarket(marketTuple, expandEvents=True)


    def OnMenuSelectionSavedMarketsSelectAll(self, event):
        count = self.m_listBoxSavedMarkets.GetCount()
        for index in xrange(count):
            self.m_listBoxSavedMarkets.Select(index)


    def OnMenuSelectionSavedMarketsDeleteAll(self, event):
        # Remove all from the control
        count = self.m_listBoxSavedMarkets.GetCount()
        for item in xrange(count - 1, -1, -1):
            self.m_listBoxSavedMarkets.Delete(item)

        # Remove from the registry
        self.config.DeleteGroup('Saved')
        self.savedMarkets.clear()
        

    def OnMenuSelectionSavedMarketsDeleteSelected(self, event):
        # Get the selection
        selections = list(self.m_listBoxSavedMarkets.GetSelections())
        selections.sort(reverse=True)

        self.config.SetPath('/Saved')
        for item in selections:
            marketTuple = self.m_listBoxSavedMarkets.GetClientData(item)

            # Remove from the internal list
            del self.savedMarkets[marketTuple]

            # Remove from the registry
            configKey = '%d%d' % (marketTuple.exchangeId, marketTuple.marketId)
            self.config.DeleteEntry(configKey, False)
            # Removefrom the control
            self.m_listBoxSavedMarkets.Delete(item)

        self.config.SetPath('/')


    def OnListBoxDClickSavedMarkets(self, event):
        item = event.GetSelection()

        # item = self.m_listBoxSavedMarkets.HitTest(position)
        if item == wx.NOT_FOUND:
            return

        marketTuple = self.m_listBoxSavedMarkets.GetClientData(item)
        self.GetMarket(marketTuple, expandEvents=True)

        
