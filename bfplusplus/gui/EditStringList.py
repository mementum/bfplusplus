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
"""Subclass of EditStringList, which is generated by wxFormBuilder."""

import wx

import MainGui

from EditString import EditString

# Implementing EditStringList
class EditStringList(MainGui.EditStringList):

    def __init__(self, parent, values, valueType=None, fixedCount=False):
	MainGui.EditStringList.__init__(self, parent)

        self.valueType = valueType
	for value in values:
            if self.valueType is not None:
                value = self.valueType(value)
	    self.m_listBoxItemList.Append(str(value))


        if fixedCount:
            self.m_buttonNew.Hide()
            self.m_buttonDelete.Hide()
        self.Layout()

        self.m_buttonSort.Enable(len(values) >= 2)
        self.m_buttonReverse.Enable(len(values) >= 2)


    def NewOrEdit(self, itemIndex=-1):
	if itemIndex != -1:
	    value = self.m_listBoxItemList.GetString(itemIndex)
	else:
	    value = ''

	dlg = EditString(self, value, self.valueType)
	retcode = dlg.ShowModal()
	if retcode != wx.ID_OK:
	    return

        value = dlg.value
        if self.valueType is not None:
            value = self.valueType(value)

        if itemIndex != -1:
            self.m_listBoxItemList.SetString(itemIndex, str(value))
        else:
            itemIndex = self.m_listBoxItemList.Append(str(value))

        self.m_listBoxItemList.Select(itemIndex)
        self.m_buttonNew.Enable()
        self.m_buttonDelete.Enable()
            
        count = self.m_listBoxItemList.GetCount()
        self.m_buttonSort.Enable(count >= 2)
        self.m_buttonReverse.Enable(count >= 2)

        self.m_buttonMoveUp.Enable(itemIndex > 0)
        self.m_buttonMoveDown.Enable(count > 1 and itemIndex < (count - 1))


    def OnButtonClickNew(self, event):
	self.NewOrEdit()


    def OnButtonClickEdit(self, event):
	itemIndex = self.m_listBoxItemList.GetSelection()
	if itemIndex == wx.NOT_FOUND:
	    return
	self.NewOrEdit(itemIndex)


    def OnButtonClickDelete(self, event):
	itemIndex = self.m_listBoxItemList.GetSelection()
	if itemIndex == wx.NOT_FOUND:
	    return

	self.m_listBoxItemList.Delete(itemIndex)

        count = self.m_listBoxItemList.GetCount()
        self.m_buttonSort.Enable(count >= 2)
        self.m_buttonReverse.Enable(count >= 2)

        self.m_buttonEdit.Disable()
        self.m_buttonDelete.Disable()
        self.m_buttonMoveUp.Disable()
        self.m_buttonMoveDown.Disable()


    def MoveUpDown(self, direction):
        count = self.m_listBoxItemList.GetCount()
	if direction > 0:
	    limit = count - 1
	else:
	    limit = 0
	selection = self.m_listBoxItemList.GetSelection()

	if selection == wx.NOT_FOUND or selection == limit:
	    return

	stringItem = self.m_listBoxItemList.GetString(selection)
	self.m_listBoxItemList.Delete(selection)
	selection += direction
	self.m_listBoxItemList.Insert(stringItem, selection)
        self.m_listBoxItemList.Select(selection)

        self.m_buttonMoveUp.Enable(selection > 0)
        self.m_buttonMoveDown.Enable(count > 1 and selection < (count - 1))


    def OnButtonClickMoveUp(self, event):
        self.MoveUpDown(-1)


    def OnButtonClickMoveDown(self, event):
        self.MoveUpDown(1)
        

    def OnButtonClickSort(self, event):
        self.DoSort()


    def OnButtonClickReverse(self, event):
        self.DoSort(reverse=True)


    def DoSort(self, reverse=False):
        values = list()
	count = self.m_listBoxItemList.GetCount()

	for itemIndex in xrange(count):
	    value = self.m_listBoxItemList.GetString(0)
            if self.valueType is not None:
                value = self.valueType(value)
	    values.append(value)
            self.m_listBoxItemList.Delete(0)

        values.sort(reverse=reverse)

        for value in values:
            self.m_listBoxItemList.Append(str(value))


    def OnOKButtonClick(self, event):
	self.values = list()

	count = self.m_listBoxItemList.GetCount()
	for itemIndex in xrange(count):
	    value = self.m_listBoxItemList.GetString(itemIndex)
            if self.valueType is not None:
                value = self.valueType(value)
	    self.values.append(value)

        self.EndModal(wx.ID_OK)


    def OnListBoxItemList(self, event):
        itemIndex = self.m_listBoxItemList.GetSelection()
        if itemIndex == wx.NOT_FOUND:
            return

        self.m_buttonEdit.Enable()
        self.m_buttonDelete.Enable()

        self.m_buttonMoveUp.Enable(itemIndex > 0)
        count = self.m_listBoxItemList.GetCount()
        self.m_buttonMoveDown.Enable(count > 1 and itemIndex < (count - 1))


    def OnListBoxDClickItemList(self, event):
        itemIndex = self.m_listBoxItemList.GetSelection()
        if itemIndex == wx.NOT_FOUND:
            return

        self.NewOrEdit(itemIndex)
