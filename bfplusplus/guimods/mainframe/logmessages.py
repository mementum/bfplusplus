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

import datetime

import wx

from httxlib import SocketException

if True:
    def init(self):
        self.RegisterFocusWin(self.m_listBoxMessages)
        self.RegisterFocusWin(self.m_listBoxMessagesError)
        self.errorCount = 0
        self.bettingCount = 0


    def OnNoteBookPageChangedInfoLog(self, event):
        event.Skip()
        
        page = event.GetSelection()

        if page == 3:
            self.bettingCount = 0
            self.m_notebookInfoLog.SetPageText(3, 'Betting Log')
        elif page == 4:
            self.errorCount = 0
            self.m_notebookInfoLog.SetPageText(4, 'Error Log')


    def LogMessages(self, messages):
        if isinstance(messages, Exception):
            self.LogMessagesError(messages)
            return
            
        if not isinstance(messages, (tuple, list)):
            messages = str(messages)
            messages = [messages]

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        timestamped = ['%s: %s' % (timestamp, message) for message in messages]
        self.m_listBoxMessages.InsertItems(timestamped, 0)
        self.m_listBoxMessages.Refresh()

        for message in timestamped:
            self.transMsg.AddMessage(message)

        page = self.m_notebookInfoLog.GetSelection()
        if page == 2:
            return

        self.bettingCount += len(messages)
        self.m_notebookInfoLog.SetPageText(3, 'Betting Log (%d)' % self.bettingCount)


    def m_listBoxMessagesOnContextMenu(self, event):
        event.Skip()

        position = event.GetPosition()

        item = self.m_listBoxMessages.HitTest(position)
        
        itemFound = (item != wx.NOT_FOUND)
        selections = self.m_listBoxMessages.GetSelections()

        if itemFound and item not in selections:
            self.m_listBoxMessages.DeselectAll()
            self.m_listBoxMessages.Select(item)
            selections = [item]

        count = self.m_listBoxMessages.GetCount()
        numSelections = len(selections)
        # multiSelection = (numSelections > 1)

        self.m_menuItemMessagesSelectAll.Enable(numSelections < count)
        self.m_menuItemMessagesDeselectAll.Enable(numSelections)
        self.m_menuItemMessagesCopySelected.Enable(numSelections)
        self.m_menuItemMessagesClearSelected.Enable(numSelections)
        self.m_menuItemMessagesClearAll.Enable(count)

        self.m_listBoxMessages.PopupMenu(self.m_menuLogMessages, position)


    def OnMenuSelectionLogMessagesSelectAll(self, event):
        event.Skip()

        count = self.m_listBoxMessages.GetCount()
        for i in xrange(count):
            self.m_listBoxMessages.Select(i)


    def OnMenuSelectionLogMessagesDeselectAll(self, event):
        event.Skip()

        self.m_listBoxMessages.DeselectAll()
    

    def OnMenuSelectionLogMessagesCopySelectedToClipBoard(self, event):
        event.Skip()

        if wx.TheClipboard.Open():
            selections = self.m_listBoxMessages.GetSelections()
            selectionList = list()
            for selection in selections:
                selectionList.append(self.m_listBoxMessages.GetString(selection))

            textToCopy = '\r\n'.join(selectionList)
            textDataObject = wx.TextDataObject(textToCopy)
            wx.TheClipboard.AddData(textDataObject)
            wx.TheClipboard.Close()


    def OnMenuSelectionLogMessagesClearSelected(self, event):
        event.Skip()

        selections = list(self.m_listBoxMessages.GetSelections())
        selections.sort(reverse=True)

        for selection in selections:
            self.m_listBoxMessages.Delete(selection)
            

    def OnMenuSelectionLogMessagesClearAll(self, event):
        event.Skip()
        self.m_listBoxMessages.Clear()


    def OnCharListBoxMessages(self, event):
        event.Skip()
        
        keycode = event.GetKeyCode()

        if keycode == wx.WXK_DELETE:
            selections = list(self.m_listBoxMessages.GetSelections())
            if selections:
                selections.sort(reverse=True)

                for selection in selections:
                    self.m_listBoxMessages.Delete(selection)
