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

import bfpy

if True:
    def LogMessagesError(self, messages):

        if not isinstance(messages, (tuple, list)):
            messages = [messages]

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamped = list()

        for message in messages:
            if isinstance(message, bfpy.BfNetworkError):
                if isinstance(message.errorCode, (list, tuple)):
                    if len(message.errorCode) > 1:
                        msg = 'Network Error: %s - Code: %d - Reason: %s' % (message.name, message.errorCode[0], message.errorCode[1])
                    else:
                        msg = 'Network Error: %s - Reason: %s' % (message.name, message.errorCode[0])
                else:
                    msg = 'Network Error: %s - Reason: %s' % (message.name, str(message.errorCode))

            elif isinstance(message, bfpy.BfApiError):
                msg = 'Api Error: %s - Reason: %s' % (message.name, message.errorCode)

            elif isinstance(message, bfpy.BfServiceError):
                msg = 'Service Error: %s -  Reason: %s' % (message.name, message.errorCode)

            elif isinstance(message, (bfpy.BfError)):
                msg = 'Call Error: %s - Error: %s' % (message.name, message.text)

            else:
                msg = 'Error: %s' % str(message)

            if isinstance(message, (bfpy.BfError)):
                self.m_staticTextRefreshTime.SetBackgroundColour(self.networkErrorsColour)
                self.m_staticTextRefreshTime.SetForegroundColour(self.networkErrorsColourText)
                self.m_staticTextRefreshTime.Refresh()

            self.transMsgError.AddMessage(msg)
            timestamped.insert(0, '%s: %s' % (timestamp, msg))
            
        self.m_listBoxMessagesError.InsertItems(timestamped, 0)
        self.m_listBoxMessagesError.Refresh()

        page = self.m_notebookInfoLog.GetSelection()
        if page == 3:
            return

        self.errorCount += len(messages)
        self.m_notebookInfoLog.SetPageText(4, 'Error Log (%d)' % self.errorCount)


    def m_listBoxMessagesErrorOnContextMenu(self, event):
        event.Skip()

        position = event.GetPosition()

        item = self.m_listBoxMessagesError.HitTest(position)
        
        itemFound = (item != wx.NOT_FOUND)
        selections = self.m_listBoxMessagesError.GetSelections()

        if itemFound and item not in selections:
            self.m_listBoxMessagesError.DeselectAll()
            self.m_listBoxMessagesError.Select(item)
            selections = [item]

        count = self.m_listBoxMessagesError.GetCount()
        numSelections = len(selections)
        # multiSelection = (numSelections > 1)

        self.m_menuItemMessagesErrorSelectAll.Enable(numSelections < count)
        self.m_menuItemMessagesErrorDeselectAll.Enable(numSelections)
        self.m_menuItemMessagesErrorCopySelected.Enable(numSelections)
        self.m_menuItemMessagesErrorClearSelected.Enable(numSelections)
        self.m_menuItemMessagesErrorClearAll.Enable(count)

        self.m_listBoxMessagesError.PopupMenu(self.m_menuLogMessagesError, position)


    def OnMenuSelectionLogMessagesErrorSelectAll(self, event):
        event.Skip()

        count = self.m_listBoxMessagesError.GetCount()
        for i in xrange(count):
            self.m_listBoxMessagesError.Select(i)


    def OnMenuSelectionLogMessagesErrorDeselectAll(self, event):
        event.Skip()

        self.m_listBoxMessagesError.DeselectAll()
    

    def OnMenuSelectionLogMessagesErrorCopySelectedToClipBoard(self, event):
        event.Skip()

        if wx.TheClipboard.Open():
            selections = self.m_listBoxMessagesError.GetSelections()
            selectionList = list()
            for selection in selections:
                selectionList.append(self.m_listBoxMessagesError.GetString(selection))

            textToCopy = '\r\n'.join(selectionList)
            textDataObject = wx.TextDataObject(textToCopy)
            wx.TheClipboard.AddData(textDataObject)
            wx.TheClipboard.Close()


    def OnMenuSelectionLogMessagesErrorClearSelected(self, event):
        event.Skip()

        selections = list(self.m_listBoxMessagesError.GetSelections())
        selections.sort(reverse=True)

        for selection in selections:
            self.m_listBoxMessagesError.Delete(selection)
            

    def OnMenuSelectionLogMessagesErrorClearAll(self, event):
        event.Skip()

        count = self.m_listBoxMessagesError.GetCount()
        for i in range(count - 1, -1, -1):
            self.m_listBoxMessagesError.Delete(i)


    def OnCharListBoxMessagesError(self, event):
        event.Skip()
        
        keycode = event.GetKeyCode()

        if keycode == wx.WXK_DELETE:
            selections = list(self.m_listBoxMessagesError.GetSelections())
            selections.sort(reverse=True)

            for selection in selections:
                self.m_listBoxMessagesError.Delete(selection)
