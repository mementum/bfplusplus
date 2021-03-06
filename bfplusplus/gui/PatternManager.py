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
"""Subclass of PatternManager, which is generated by wxFormBuilder."""

import wx

import MainGui

from EditPattern import EditPattern
from EditString import EditString

# Implementing PatternManager
class PatternManager(MainGui.PatternManager):

    def __init__(self, parent, patterns, canLoad):
	MainGui.PatternManager.__init__(self, parent)

        self.config = parent.config

        self.patterns = patterns
	for patternName in patterns:
	    self.m_checkListPatterns.Append(patternName)

        if self.patterns:
            self.m_buttonCheckAll.Enable()
        self.m_buttonUncheckAll.Disable()

        # LOAD to be enabled/disabled on "login" status
        self.canLoad = canLoad


    def CheckAll(self, state):
	count = self.m_checkListPatterns.GetCount()
	for itemIndex in xrange(count):
	    self.m_checkListPatterns.Check(itemIndex, state)

	
    def OnButtonClickCheckAll(self, event):
	self.CheckAll(True)
        self.m_buttonCheckAll.Disable()
        self.m_buttonUncheckAll.Enable()
        if self.canLoad:
            self.m_buttonLoadPatterns.Enable()
        

    def OnButtonClickUncheckAll(self, event):
	self.CheckAll(False)
        self.m_buttonCheckAll.Enable()
        self.m_buttonUncheckAll.Disable()
        self.m_buttonLoadPatterns.Disable()


    def OnButtonClickClose(self, event):
	self.EndModal(wx.ID_CANCEL)

	
    def OnButtonClickLoad(self, event):
        self.loadPatterns = dict()

	count = self.m_checkListPatterns.GetCount()
	for itemIndex in xrange(count):
	    if self.m_checkListPatterns.IsChecked(itemIndex):
                patternName = self.m_checkListPatterns.GetString(itemIndex)
                self.loadPatterns[patternName] = self.patterns[patternName]

	self.EndModal(wx.ID_OK)


    def NewOrEdit(self, itemIndex=-1):
	if itemIndex != -1:
	    name = self.m_checkListPatterns.GetString(itemIndex)
	    pattern = self.patterns[name]
	    title = 'Edit Pattern'
            patternNames = []
	else:
	    name = ''
	    pattern = [[], [], []]
	    title = 'New Pattern'
            patternNames = self.patterns.keys()

	dlg = EditPattern(self, name, pattern, patternNames)
	dlg.SetTitle(title)
	if dlg.ShowModal() != wx.ID_OK:
	    return

        # Delete old pattern (if editing)
        if itemIndex != -1:
            self.m_checkListPatterns.Delete(itemIndex)

            self.config.SetPath('/Favourites')
            self.config.DeleteEntry(name, False)
            self.config.SetPath('/')

            del self.patterns[name]

        # Delete existing pattern from registry if overwriting
        if dlg.name in self.patterns:
            self.config.SetPath('/Favourites')
            self.config.DeleteEntry(dlg.name, False)
            self.config.SetPath('/')

            # Delete from existing patterns
            del self.patterns[dlg.name]

            # Delete from checkListBox
            count = self.m_checkListPatterns.GetCount()
            for itemIndex in xrange(count):
                pname = self.m_checkListPatterns.GetString(itemIndex)
                if pname == dlg.name:
                    self.m_checkListPatterns.Delete(itemIndex)
                    break

        # Store in the registry
        self.config.SetPath('/Favourites')
	self.config.Write(dlg.name, str(dlg.pattern))
        self.config.SetPath('/')

        # Insert & select in check listbox
        selection = self.m_checkListPatterns.Append(dlg.name)
        self.m_checkListPatterns.Select(selection)

        # Insert in patterns
	self.patterns[dlg.name] = dlg.pattern

        # Because we have selected it, enable the needed buttons
        self.m_buttonPatternEdit.Enable()
        self.m_buttonPatternCopy.Enable()
        self.m_buttonPatternDelete.Enable()

	
    # Handlers for EditFavSearchPatterns events.
    def OnButtonClickPatternNew(self, event):
	self.NewOrEdit()

	
    def OnButtonClickPatternEdit(self, event):
	itemIndex = self.m_checkListPatterns.GetSelection()
	if itemIndex == wx.NOT_FOUND:
	    return
	self.NewOrEdit(itemIndex)


    def OnButtonClickPatternCopy(self, event):
	itemIndex = self.m_checkListPatterns.GetSelection()
	if itemIndex == wx.NOT_FOUND:
	    return

	name = self.m_checkListPatterns.GetString(itemIndex)
	dlg = EditString(self, 'Copy of %s' % name)
	dlg.SetTitle('Enter name for the copy')
	if dlg.ShowModal() != wx.ID_OK:
	    return

	if dlg.value == name:
	    wx.MessageBox('The name of the copy must be different',
			  'Duplicate name')
	    return

	if not dlg.value:
	    wx.MessageBox('No name provided.',
			  'No name')
	    return

	pattern = self.patterns[name]
        # Make a copy
	pattern = pattern[:]

	selection = self.m_checkListPatterns.Append(dlg.value)
	self.patterns[dlg.value] = pattern

        self.config.SetPath('/Favourites')
	self.config.Write(dlg.value, str(pattern))
        self.config.SetPath('/')

        self.m_buttonPatternEdit.Enable()
        self.m_buttonPatternCopy.Enable()
        self.m_buttonPatternDelete.Enable()


    def OnButtonClickPatternDelete(self, event):
	itemIndex = self.m_checkListPatterns.GetSelection()
	if itemIndex == wx.NOT_FOUND:
	    return

	name = self.m_checkListPatterns.GetString(itemIndex)

	self.m_checkListPatterns.Delete(itemIndex)
	del self.patterns[name]

        self.config.SetPath('/Favourites')
	self.config.DeleteEntry(name, False)
        self.config.SetPath('/')

        self.m_buttonPatternEdit.Disable()
        self.m_buttonPatternCopy.Disable()
        self.m_buttonPatternDelete.Disable()


    def OnCheckListBoxTogglePatterns(self, event):
        count = self.m_checkListPatterns.GetCount()

        checkedCount = 0
        for itemIndex in xrange(count):
            if self.m_checkListPatterns.IsChecked(itemIndex):
                checkedCount += 1

        if checkedCount and self.canLoad:
            self.m_buttonLoadPatterns.Enable()
        else:
            self.m_buttonLoadPatterns.Disable()

        if checkedCount == count:
            self.m_buttonCheckAll.Disable()
        elif not checkedCount:
            self.m_buttonUncheckAll.Disable()
        else:
            self.m_buttonCheckAll.Enable()
            self.m_buttonUncheckAll.Enable()


    def OnCheckListBoxPatterns(self, event):
        self.m_buttonPatternEdit.Enable()
        self.m_buttonPatternCopy.Enable()
        self.m_buttonPatternDelete.Enable()
