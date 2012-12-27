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

import wx

from gui.EditPattern import EditPattern
from gui.PrioritizeEvents import PrioritizeEvents

import bfobj
import bfpy
from util import Message

if True:
    def init(self):
        self.prioEventId = -2
        self.prioEventName = '--------------------------------------------'

        self.autoExpand = self.config.ReadBool('Auto Expand', True)
        self.config.WriteBool('Auto Expand', self.autoExpand)
        self.m_checkBoxAutoExpand.SetValue(self.autoExpand)

        self.useMarketCache = self.config.ReadBool('Use MarketCache', True)
        self.config.WriteBool('Use MarketCache', self.useMarketCache)
        self.m_checkBoxCacheMarkets.SetValue(self.useMarketCache)


        self.loadMarketsAfterLogin = self.config.ReadBool('Load Markets after Login', True)
        self.config.WriteBool('Load Markets after Login', self.loadMarketsAfterLogin)
        self.m_checkBoxLoadMarketsAfterLogin.SetValue(self.loadMarketsAfterLogin)

        self.useBfOrder = self.config.ReadBool('Use Bf Order', False)
        self.config.WriteBool('Use Bf Order', self.useBfOrder)
        self.m_checkBoxUseBfOrder.SetValue(self.useBfOrder)

        # Flag to indicate if the Root Betfair Events are loaded
        self.noEventsLoaded = True
        self.RegisterFocusWin(self.m_treeEvents)

        self.SetImageList()

        # Key: eventId
        # value: name of the icon in the icon dictionary
        # comment: real sport
        self.iconDict = {
            1: 'Soccer', # Soccer
            14: 'Soccer', # Soccer - Fixtures
            2: 'Tennis', # Tennis
            3: 'Golf', # Golf
            7522: 'Basketball', # Basketball
            6423: 'Football', # American Football
            5: 'Football', # Rugby Union
            1477: 'Football', # Rugby League
            10: 'Special Bets', # Special Bets
            6231: 'Financial Bets', # Financial Bets
            3145419: 'Cross Sport Accumulators', # Cross Sports Accummulators
            2378961: 'Politics', # Politics
            315220: 'Poker', # Poker
            4339: 'Greyhound Racing', # Greyhound Racing
            15: 'Greyhound Racing', # Greyhound - Todays Card
            8: 'Motor Sport', # Motor Sport
            678378: 'Football', # International Rules
            61420: 'Australian Rules', # Australian Rules
            4: 'Cricket', # Cricket
            11 : 'Cycling', # Cycling
            3503: 'Darts', # Darts
            998920: 'Floorball', # Floorball
            468328: 'Handball', # Handball
            6422: 'Snooker', # Snooker
            72382: 'Pool', # Pool
            6: 'Boxing', # Boxing
            256284: 'Trotting', # Trotting
            7: 'Horse Racing', # Horse Racing
            26397698: 'Horse Racing', # Horse Racing - Virtual
            13: 'Horse Racing', # Horse Racing - Todays Card
            26420387: 'Mixed Martial Arts', # Mixed Martial Arts
            998917: 'Volleyball', # Volleyball
            7524: 'Hockey',# Ice Hockey
            7511: 'Baseball', # Baseball
            5412697: 'Volleyball', # Pelota
            451485: 'Winter Sports', # Winter Sports
            136332: 'Chess', # Chess
            2593174: 'Table Tennis', # Table Tennis
            66598: 'Volleyball', # Gaelic Football
            998919: 'Bandy', # Bandy
            12: 'Rowing', # Rowing
            300000: 'Commonwealth Games', # Commonwealth Games
            2152880: 'Gaelic Games', # Commonwealth Games
            998918: 'Bowls', # Bowls
            606611: 'Netball', # Netball
            26686903: 'Olympic Games', # Olympics 2012
            3088925: 'Fishing', # Fishing
            3988: 'Athletics', # Athletics
        }


    def SetImageList(self):
        self.eventsImgList = wx.ImageList(16, 16)
        self.imgIdx = dict()

        ##############################
        # Others
        ##############################
        self.bmp = wx.Bitmap('./icons/others/rowing.png')
        idx = self.eventsImgList.Add(self.bmp)
        self.imgIdx['Rowing'] = idx

        self.bmp = wx.Bitmap('./icons/others/fishing.png')
        idx = self.eventsImgList.Add(self.bmp)
        self.imgIdx['Fishing'] = idx

        self.bmp = wx.Bitmap('./icons/others/athletics.png')
        idx = self.eventsImgList.Add(self.bmp)
        self.imgIdx['Athletics'] = idx
        ##############################
        # Kevin Anderson
        ##############################
        self.bmp = wx.Bitmap('./icons/kevinanderson.dk/bowling_16x16.png')
        idx = self.eventsImgList.Add(self.bmp)
        self.imgIdx['Bowls'] = idx

        ##############################
        # FamFamFam Flags
        ##############################
        self.bmp = wx.Bitmap('./icons/famfamfam-flags/gb_stretched.png')
        idx = self.eventsImgList.Add(self.bmp)
        self.imgIdx['Commonwealth Games'] = idx

        ##############################
        # FamFamFam Silk
        ##############################
        self.bmpTextfield = wx.Bitmap('./icons/famfamfam-silk/layout.png')
        idx = self.eventsImgList.Add(self.bmpTextfield)
        self.imgIdx['Textfield'] = idx

        self.bmpBulletGo = wx.Bitmap('./icons/famfamfam-silk/sport_8ball.png')
        idx = self.eventsImgList.Add(self.bmpBulletGo)
        self.imgIdx['Pool'] = idx

        self.bmpBulletGo = wx.Bitmap('./icons/famfamfam-silk/bullet_go.png')
        idx = self.eventsImgList.Add(self.bmpBulletGo)
        self.imgIdx['MarketItem'] = idx

        self.bmpSoccer = wx.Bitmap('./icons/famfamfam-silk/sport_soccer.png')
        idx = self.eventsImgList.Add(self.bmpSoccer)
        self.imgIdx['Soccer'] = idx

        self.bmpTennis = wx.Bitmap('./icons/famfamfam-silk/sport_tennis.png')
        idx = self.eventsImgList.Add(self.bmpTennis)
        self.imgIdx['Tennis'] = idx

        self.bmpGolf = wx.Bitmap('./icons/famfamfam-silk/sport_golf.png')
        idx = self.eventsImgList.Add(self.bmpGolf)
        self.imgIdx['Golf'] = idx

        self.bmpBasketball = wx.Bitmap('./icons/famfamfam-silk/sport_basketball.png')
        idx = self.eventsImgList.Add(self.bmpBasketball)
        self.imgIdx['Basketball'] = idx

        self.bmpFootball = wx.Bitmap('./icons/famfamfam-silk/sport_football.png')
        idx = self.eventsImgList.Add(self.bmpFootball)
        self.imgIdx['Football'] = idx

        self.bmpStar = wx.Bitmap('./icons/famfamfam-silk/star.png')
        idx = self.eventsImgList.Add(self.bmpStar)
        self.imgIdx['Special Bets'] = idx

        self.bmpChartLine = wx.Bitmap('./icons/famfamfam-silk/chart_line.png')
        idx = self.eventsImgList.Add(self.bmpChartLine)
        self.imgIdx['Financial Bets'] = idx

        self.bmpStatusOffline = wx.Bitmap('./icons/famfamfam-silk/group.png')
        idx = self.eventsImgList.Add(self.bmpStatusOffline)
        self.imgIdx['Politics'] = idx

        self.bmpCrossSports = wx.Bitmap('./icons/famfamfam-silk/arrow_switch.png')
        idx = self.eventsImgList.Add(self.bmpCrossSports)
        self.imgIdx['Cross Sport Accumulators'] = idx

        ##############################
        # Everaldo Com
        ##############################
        self.bmpPoker = wx.Bitmap('./icons/everaldo.com/Crystal_package_games_card.png')
        idx = self.eventsImgList.Add(self.bmpPoker)
        self.imgIdx['Poker'] = idx

        ##############################
        # WikiMedia
        ##############################
        self.bmpNetball = wx.Bitmap('./icons/wikimedia.com/Netball.png')
        idx = self.eventsImgList.Add(self.bmpNetball)
        self.imgIdx['Netball'] = idx

        self.bmpDog = wx.Bitmap('./icons/wikimedia.com/Dog_Silhouette_01.svg.png')
        idx = self.eventsImgList.Add(self.bmpDog)
        self.imgIdx['Greyhound Racing'] = idx

        self.bmp = wx.Bitmap('./icons/wikimedia.com/gaelic_games.png')
        idx = self.eventsImgList.Add(self.bmp)
        self.imgIdx['Gaelic Games'] = idx

        self.bmp = wx.Bitmap('./icons/wikimedia.com/olympicflag.png')
        idx = self.eventsImgList.Add(self.bmp)
        self.imgIdx['Olympic Games'] = idx

        ##############################
        # Nordic factory
        ##############################
        self.bmpBandy = wx.Bitmap('./icons/nordicfactory.com/icon_bandy.png')
        idx = self.eventsImgList.Add(self.bmpBandy)
        self.imgIdx['Bandy'] = idx

        self.bmpGaelicFootball = wx.Bitmap('./icons/nordicfactory.com/icon_gaelic_football.png')
        idx = self.eventsImgList.Add(self.bmpGaelicFootball)
        self.imgIdx['Gaelic Football'] = idx

        self.bmpChess = wx.Bitmap('./icons/nordicfactory.com/icon_chess.png')
        idx = self.eventsImgList.Add(self.bmpChess)
        self.imgIdx['Chess'] = idx

        self.bmpTableTennis = wx.Bitmap('./icons/nordicfactory.com/icon_table_tennis.png')
        idx = self.eventsImgList.Add(self.bmpTableTennis)
        self.imgIdx['Table Tennis'] = idx

        self.bmpCar = wx.Bitmap('./icons/nordicfactory.com/icon_motor.png')
        idx = self.eventsImgList.Add(self.bmpCar)
        self.imgIdx['Motor Sport'] = idx

        self.bmpAusRules = wx.Bitmap('./icons/nordicfactory.com/icon_australian_rules.png')
        idx = self.eventsImgList.Add(self.bmpAusRules)
        self.imgIdx['Australian Rules'] = idx

        self.bmpCricket = wx.Bitmap('./icons/nordicfactory.com/icon_cricket.png')
        idx = self.eventsImgList.Add(self.bmpCricket)
        self.imgIdx['Cricket'] = idx

        self.bmpCycling = wx.Bitmap('./icons/nordicfactory.com/icon_cycling.png')
        idx = self.eventsImgList.Add(self.bmpCycling)
        self.imgIdx['Cycling'] = idx

        self.bmpDarts = wx.Bitmap('./icons/nordicfactory.com/icon_darts.png')
        idx = self.eventsImgList.Add(self.bmpDarts)
        self.imgIdx['Darts'] = idx

        self.bmpFloorball = wx.Bitmap('./icons/nordicfactory.com/icon_floorball.png')
        idx = self.eventsImgList.Add(self.bmpFloorball)
        self.imgIdx['Floorball'] = idx

        self.bmpHandball = wx.Bitmap('./icons/nordicfactory.com/icon_handball.png')
        idx = self.eventsImgList.Add(self.bmpHandball)
        self.imgIdx['Handball'] = idx

        self.bmpSnooker = wx.Bitmap('./icons/nordicfactory.com/icon_snooker.png')
        idx = self.eventsImgList.Add(self.bmpSnooker)
        self.imgIdx['Snooker'] = idx

        self.bmpTrotting = wx.Bitmap('./icons/nordicfactory.com/icon_trotting.png')
        idx = self.eventsImgList.Add(self.bmpTrotting)
        self.imgIdx['Horse Racing'] = idx

        self.bmpUltFighting = wx.Bitmap('./icons/nordicfactory.com/icon_ultimate_fighting.png')
        idx = self.eventsImgList.Add(self.bmpUltFighting)
        self.imgIdx['Mixed Martial Arts'] = idx

        self.bmpVolleyball = wx.Bitmap('./icons/nordicfactory.com/icon_volleyball.png')
        idx = self.eventsImgList.Add(self.bmpVolleyball)
        self.imgIdx['Volleyball'] = idx

        self.bmpHockey = wx.Bitmap('./icons/nordicfactory.com/icon_icehockey.png')
        idx = self.eventsImgList.Add(self.bmpHockey)
        self.imgIdx['Hockey'] = idx

        self.bmpBaseball = wx.Bitmap('./icons/nordicfactory.com/icon_baseball.png')
        idx = self.eventsImgList.Add(self.bmpBaseball)
        self.imgIdx['Baseball'] = idx

        self.bmpBoxing = wx.Bitmap('./icons/nordicfactory.com/icon_boxing.png')
        idx = self.eventsImgList.Add(self.bmpBoxing)
        self.imgIdx['Boxing'] = idx

        self.bmpWinterSports = wx.Bitmap('./icons/zeusbox/snow flake_16x16.png')
        idx = self.eventsImgList.Add(self.bmpWinterSports)
        self.imgIdx['Winter Sports'] = idx

        self.m_treeEvents.SetImageList(self.eventsImgList)
        self.m_treeEvents.Refresh()


    def postLoginEvents(self):
	eventItem = self.BfCreateEvent()
	self.m_treeEvents.AddRoot('Betfair Markets', data=wx.TreeItemData(eventItem))


    def OnCheckBoxUseBfOrder(self, event):
        self.useBfOrder = self.m_checkBoxUseBfOrder.GetValue()
        self.config.WriteBool('Use Bf Order', self.useBfOrder)
        # Ideally all loaded items could be reordered in realtime to match the setting


    def OnCheckBoxMarketsAfterLogin(self, event):
        event.Skip()
        self.loadMarketsAfterLogin = self.m_checkBoxLoadMarketsAfterLogin.GetValue()
        self.config.WriteBool('Load Markets after Login', self.loadMarketsAfterLogin)


    def ExpandEvents(self, marketTuple):
        if not self.autoExpand:
            return

        marketComp = self.marketCache[marketTuple]

        if not marketComp.eventHierarchy:
            # Australian market
            self.ExpandEventsAus(marketTuple)
            return

        self.m_notebookMain.ChangeSelection(1)
        self.m_notebookFavs.ChangeSelection(0)

        eventHierarchy = marketComp.eventHierarchy[:]
        marketId = marketComp.marketId
        eventHierarchy.append(marketId)

        treeItem = self.m_treeEvents.GetRootItem()

        for eventId in eventHierarchy:
            treeItem, treeItemCookie = self.m_treeEvents.GetFirstChild(treeItem)

            while True:
                if not treeItem.IsOk():
                    return

                bfItem = self.m_treeEvents.GetPyData(treeItem)

                if eventId == marketId:
                    if hasattr(bfItem, 'marketId') and bfItem.marketId == marketId:
                        self.m_treeEvents.EnsureVisible(treeItem)
                        # This should generate a "selchanged event"
                        self.m_treeEvents.SelectItem(treeItem)
                        # Without the refresh the windows was not updating properly
                        self.m_treeEvents.Refresh()
                        return

                    treeItem = self.m_treeEvents.GetNextSibling(treeItem)
                    continue
                else:
                    # Still at event level
                    if not hasattr(bfItem, 'eventId') or eventId != bfItem.eventId:
                        treeItem = self.m_treeEvents.GetNextSibling(treeItem)
                        continue

                    if self.m_treeEvents.GetChildrenCount(treeItem):
                        self.m_treeEvents.Expand(treeItem)
                        self.m_treeEvents.Refresh()
                        break

                    # We have to execute a GetEvents
                    self.GetEvents(bfItem.eventId, treeItem, marketTuple)
                    return


    def GetEvents(self, eventId, treeItem=None, marketTuple=None):
        self.blockGetEvents.Show(True)

	message = Message(action='getEvents', eventId=eventId)
        message.treeItem = treeItem
        message.marketTuple=marketTuple

	self.thMisc.passMessage(message)


    def OnGetEvents(self, event):
        self.blockGetEvents.Show(False)

        message, response, exception = self.SplitEventResponse(event)
        if not response:
            if exception:
                self.LogMessagesError('Market loading has failed. Please try it again')
                self.LogMessages(exception)
            return

        if self.noEventsLoaded:
            self.m_buttonTreeEventsReloadAll.Enable()
            self.m_buttonTreeEventsReloadSelected.Enable()
            self.m_buttonTreeEventsEdit.Enable()
            self.m_bpButtonGenerateSearchPattern.Enable()
            self.m_buttonTreeEventsCollapseAll.Enable()
            self.m_menuItemTreeItemReloadAll.Enable()

            self.noEventsReloaded = False

        treeItem = message.treeItem
	eventItems = response.eventItems
        marketItems = response.marketItems

        self.DisplayTreeItems(treeItem, eventItems, marketItems)

        if treeItem != self.m_treeEvents.GetRootItem():
            # The root node can't be expanded because we have hidden it
            self.m_treeEvents.Expand(treeItem)

        if message.marketTuple:
            self.ExpandEvents(message.marketTuple)


    def DisplayTreeItems(self, treeItem, eventItems, marketItems=None):
        if marketItems is None:
            marketItems = list()

	bfItem = self.m_treeEvents.GetPyData(treeItem)
        eventTypeId = bfItem.eventTypeId
        eventParentId = bfItem.eventId

        if self.useBfOrder:
            if eventParentId!= bfpy.eventRootId:
                eventItems.sort(key=operator.attrgetter('orderIndex'))
            else:
                eventItems.sort(key=operator.attrgetter('eventName'))
            marketItems.sort(key=operator.attrgetter('orderIndex'))
        else:
            eventItems.sort(key=operator.attrgetter('eventName'))
            marketItems.sort(key=operator.attrgetter('startTime', 'marketName'))

	self.m_treeEvents.DeleteChildren(treeItem)

        rootTreeItem = self.m_treeEvents.GetRootItem()

        if treeItem == rootTreeItem:
            prioEvents = self.config.Read('Prioritized Events', '[]')
            prioList = eval(prioEvents)

            # Do some ordering of the events
            prioritized = prioList
            prioritized.reverse()

            prioEvent = self.BfCreateEvent(self.prioEventId, self.prioEventName)
            eventItems.insert(0, prioEvent)
            for prio in prioritized:
                for i, eventItem in enumerate(eventItems):
                    if eventItem.eventName == prio:
                        eventItems.insert(0, eventItems.pop(i))
                        break

	for eventItem in eventItems:
            if eventItem.eventName == 'Coupons':
                continue

	    newTreeItem = self.m_treeEvents.AppendItem(treeItem, eventItem.eventName, data=wx.TreeItemData(eventItem))
            # Displays a '+' icon for expansion - The children count remains: 0
            if eventItem.eventId != self.prioEventId:
                self.m_treeEvents.SetItemHasChildren(newTreeItem, True)

            if eventItem.eventId != self.prioEventId:
                if treeItem == rootTreeItem:
                    iconName = self.iconDict.get(eventItem.eventId, 'Textfield')
                else:
                    iconName = 'Textfield'

                self.m_treeEvents.SetItemImage(newTreeItem, self.imgIdx[iconName])

	for marketItem in marketItems:
            marketName = marketItem.marketName
            # The startTime contains only a sensible value for markets where the startTime
            # has to be displayed along with the name
            if marketItem.startTime.year >= 1900:
                startTime = marketItem.startTime.strftime('%H:%M')
                marketName = '%s %s' % (startTime, marketName)

	    newTreeItem = self.m_treeEvents.AppendItem(treeItem, marketName, data=wx.TreeItemData(marketItem))        
            self.m_treeEvents.SetItemImage(newTreeItem, self.imgIdx['MarketItem'])


    def OnTreeSelChanged(self, event):
	treeItem = event.GetItem()
	bfItem = self.m_treeEvents.GetPyData(treeItem)

        if hasattr(bfItem, 'marketId'):
            self.GetMarket(bfobj.MarketTuple(bfItem.exchangeId, bfItem.marketId))


    def OnTreeItemExpanding(self, event):
        treeItem = event.GetItem()
	bfEventItem = self.m_treeEvents.GetPyData(treeItem)

        if not self.m_treeEvents.GetChildrenCount(treeItem):
            self.GetEvents(bfEventItem.eventId, treeItem)


    def m_treeEventsOnContextMenu(self, event):
        position = event.GetPosition()
        treeItem, hitTestFlags = self.m_treeEvents.HitTest(position)

        subMenu = wx.Menu()
        if not treeItem.IsOk():
            self.m_menuItemTreeItemSelect.Enable(False)
            self.m_menuItemTreeCollapseAll.Enable(False)
            self.m_menuItemTreeItemReload.Enable(False)
            self.m_menuItemGenerateSearchPattern.Enable(False)
        else:
            self.m_menuItemTreeItemSelect.Enable(True)
            self.m_menuItemTreeCollapseAll.Enable(True)
            self.m_menuItemGenerateSearchPattern.Enable(True)

            bfItem = self.m_treeEvents.GetPyData(treeItem)

            if hasattr(bfItem, 'eventId') or self.m_treeEvents.IsSelected(treeItem):
                self.m_menuItemTreeItemReload.Enable(True)
            else:
                self.m_menuItemTreeItemReload.Enable(False)

            if hasattr(bfItem, 'eventId'):
                infoItems = ['eventTypeId', 'eventId', 'eventName', 'eventTypeId', 'menuLevel', 'orderIndex']
            else:
                infoItems = ['eventTypeId', 'exchangeId', 'eventParentId', 'marketId', 'marketName',
                             'marketType', 'marketTypeVariant', 'menuLevel', 'orderIndex',
                             'startTime', 'timezone', 'venue', 'betDelay', 'numberOfWinners']

            if hasattr(bfItem, 'startTime'):
                if bfItem.startTime.year >= 1900:
                    infoItems.extend(['startTime', 'timezone'])

            for infoItem in infoItems:
                if hasattr(bfItem, infoItem):
                    label = '%s: %s' % (infoItem, str(getattr(bfItem, infoItem)))
                    menuItem = wx.MenuItem(subMenu, wx.ID_ANY, label, label , wx.ITEM_NORMAL)
                    subMenu.AppendItem(menuItem)

        menuItem = wx.MenuItem(subMenu, wx.ID_ANY, 'Information', 'Information' , wx.ITEM_NORMAL, subMenu=subMenu)
        self.m_menuTreeEvents.AppendItem(menuItem)

        self.m_menuTreeEvents.treeItem = treeItem
        # self.m_menuTreeEvents.SetTitle('...')
        self.m_treeEvents.PopupMenu(self.m_menuTreeEvents, event.GetPosition())
        self.m_menuTreeEvents.RemoveItem(menuItem)

                
    def TreeEventsReloadItem(self, treeItem):
        bfItem = self.m_treeEvents.GetPyData(treeItem)

        if hasattr(bfItem, 'marketId'):
            self.GetMarket(bfobj.MarketTuple(bfItem.exchangeId, bfItem.marketId), forceReload=True)

        elif bfItem.eventId != self.prioEventId:
            self.GetEvents(bfItem.eventId, treeItem)
            self.m_treeEvents.SelectItem(treeItem)


    def OnMenuSelectionTreeItemReload(self, event):
        treeItem = self.m_menuTreeEvents.treeItem
        self.TreeEventsReloadItem(treeItem)


    def OnButtonClickTreeEventsReloadSelected(self, event):
        treeItem = self.m_treeEvents.GetSelection()
        if not treeItem.IsOk():
            return
        self.TreeEventsReloadItem(treeItem)


    def TreeEventsReloadAll(self):
        rootTreeItem = self.m_treeEvents.GetRootItem()
        bfItem = self.m_treeEvents.GetPyData(rootTreeItem)
        self.GetEvents(bfItem.eventId, rootTreeItem)


    def OnMenuSelectionTreeItemReloadAll(self, event):
        self.TreeEventsReloadAll()


    def OnButtonClickTreeEventsReloadAll(self, event):
        self.TreeEventsReloadAll()


    def TreeEventsCollapseAll(self):
        rootTreeItem = self.m_treeEvents.GetRootItem()
        treeItem, treeItemCookie = self.m_treeEvents.GetFirstChild(rootTreeItem)

        while treeItem.IsOk():
            self.m_treeEvents.CollapseAllChildren(treeItem)
            treeItem = self.m_treeEvents.GetNextSibling(treeItem)

        
    def OnButtonClickTreeEventsCollapseAll(self, event):
        self.TreeEventsCollapseAll()


    def OnMenuSelectionTreeCollapseAll(self, event):
        self.TreeEventsCollapseAll()


    def OnMenuSelectionTreeItemSelect(self, event):
        treeItem = self.m_menuTreeEvents.treeItem
        self.m_treeEvents.SelectItem(treeItem)


    def OnButtonClickTreeEventsEdit(self, event):
        eventList = list()
        bfItems = list()

        # Create the complete list of events
        rootTreeItem = self.m_treeEvents.GetRootItem()

        treeItem = rootTreeItem
        treeItem, treeItemCookie = self.m_treeEvents.GetFirstChild(treeItem)
        while treeItem.IsOk():
            bfItem = self.m_treeEvents.GetPyData(treeItem)

            if bfItem.eventId > 0:
                bfText = self.m_treeEvents.GetItemText(treeItem)
                eventList.append(bfText)
                bfItems.append(bfItem)

            treeItem = self.m_treeEvents.GetNextSibling(treeItem)

        # Fetch from the registry the prioritized list of events
        prioEvents = self.config.Read('Prioritized Events', '[]')
        prioList = eval(prioEvents)

        dlg = PrioritizeEvents(self, eventList, prioList)
        if dlg.ShowModal() != wx.ID_OK:
            return

        # Store in the registry the prioritized list of events
        self.config.Write('Prioritized Events', str(dlg.prioList))

        # Re-build the tree display
        self.DisplayTreeItems(rootTreeItem, bfItems)


    def OnButtonClickGenerateSearchPattern(self, event):
        treeItem = self.m_treeEvents.GetSelection()
        if not treeItem.IsOk():
            treeItem = None
        self.GenerateSearchPatternFromTree(treeItem)


    def OnMenuSelectionGenerateSearchPattern(self, event):
        treeItem = self.m_menuTreeEvents.treeItem
        self.GenerateSearchPatternFromTree(treeItem)


    def GenerateSearchPatternFromTree(self, treeItem=None):
        # 1. Get a list of parents until the root
        # 2. The name will be the first and (second if present)
        # 3. If this is a market, the last name will be added to the "market"
        #    part of the pattern
        # 4. If not it will be added to the list
        # 5. Bring up the pattern editor
        # 6. If OK store the pattern in the registry and return

        menuPath = list()
        marketName = ''
        patternName = ''

        if treeItem:
            bfItem = self.m_treeEvents.GetPyData(treeItem)
            itemText = self.m_treeEvents.GetItemText(treeItem)
            if hasattr(bfItem, 'marketId'):
                marketName = itemText
            else:
                menuPath.append(itemText)

            rootItem = self.m_treeEvents.GetRootItem()
            while True:
                treeItem = self.m_treeEvents.GetItemParent(treeItem)
                if treeItem == rootItem:
                    break
                if not treeItem.IsOk():
                    break

                itemText = self.m_treeEvents.GetItemText(treeItem)
                menuPath.append(itemText)

            # Put top menupath names first
            menuPath.reverse()
            
            # Generate the pattern name
            patternName = menuPath[0]
            if len(menuPath) > 1:
                patternName += ' - %s' % menuPath[1]

        # Fake the pattern
        pattern = []
        if marketName:
            pattern.append([marketName])
        else:
            pattern.append([])

        menuPatterns = [[menup] for menup in menuPath]
        pattern.append(menuPatterns)
        pattern.append([])

        # Bring up the pattern editor
        patternNames = list()
        self.config.SetPath('/Favourites')
        more, value, index = self.config.GetFirstEntry()
        while more:
            patternNames.append(value)
            more, value, index = self.config.GetNextEntry(index)
        self.config.SetPath('/')

	dlg = EditPattern(self, patternName, pattern, patternNames)
        title = "Edit Generated Pattern"
	dlg.SetTitle(title)
	retcode = dlg.ShowModal()
	if retcode != wx.ID_OK:
	    return

        self.config.SetPath('/Favourites')
	self.config.Write(dlg.name, str(dlg.pattern))
        self.config.SetPath('/')


    def OnCheckBoxAutoExpand(self, event):
        event.Skip()
        self.autoExpand = self.m_checkBoxAutoExpand.GetValue()
        self.config.WriteBool('Auto Expand', self.autoExpand)


    def OnCheckBoxCacheMarkets(self, event):
        event.Skip()
        self.useMarketCache = self.m_checkBoxCacheMarkets.GetValue()
        self.config.WriteBool('Use MarketCache', self.useMarketCache)


    def ExpandEventsAus(self, marketTuple):
        if not self.autoExpand:
            return

        marketComp = self.marketCache[marketTuple]

        self.m_notebookMain.ChangeSelection(1)
        self.m_notebookFavs.ChangeSelection(0)

        marketId = marketComp.marketId

        eventTypeId = marketComp.eventTypeId
        menuPath, menuParts = marketComp.getFullMenuPath()
        menuParts = menuParts[1:]

        treeItem = self.m_treeEvents.GetRootItem()

        treeItem, treeItemCookie = self.m_treeEvents.GetFirstChild(treeItem)
        while treeItem.IsOk():
            bfItem = self.m_treeEvents.GetPyData(treeItem)

            if bfItem.eventId != eventTypeId:
                treeItem = self.m_treeEvents.GetNextSibling(treeItem)
                continue

            # Need to expand or load
            if self.m_treeEvents.GetChildrenCount(treeItem):
                self.m_treeEvents.Expand(treeItem)
                self.m_treeEvents.Refresh()
            else:
                # need to load
                self.GetEvents(bfItem.eventId, treeItem, marketTuple)
                return

            # Found it ... proceed with menu parts
            for menuPart in menuParts:
                treeItem, treeItemCookie = self.m_treeEvents.GetFirstChild(treeItem)

                while treeItem.IsOk():
                    menuName = self.m_treeEvents.GetItemText(treeItem)
                    if menuName != menuPart:
                        treeItem = self.m_treeEvents.GetNextSibling(treeItem)
                        continue

                    # Found it ...
                    bfItem = self.m_treeEvents.GetPyData(treeItem)
                    # Check if this if the final destination
                    if hasattr(bfItem, 'marketId'):
                        self.m_treeEvents.EnsureVisible(treeItem)
                        self.m_treeEvents.SelectItem(treeItem)
                        self.m_treeEvents.Refresh()
                        return

                    # Need to expand or load
                    if self.m_treeEvents.GetChildrenCount(treeItem):
                        self.m_treeEvents.Expand(treeItem)
                        self.m_treeEvents.Refresh()
                        break                    

                    # Need to expand
                    self.GetEvents(bfItem.eventId, treeItem, marketTuple)
                    return

                if not treeItem.IsOk():
                    break
