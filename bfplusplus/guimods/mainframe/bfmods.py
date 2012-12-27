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

import copy
from cStringIO import StringIO
import datetime
import glob
import imp
import operator
import os
import sys

import wx

from gui.EditModParams import EditModParams
from gui.EditStringList import EditStringList

from threads.threadmodule import ThreadModule

if True:
    def init(self):
        modulesDir = self.config.Read('BfModules directory', '')
        self.config.Write('BfModules directory', modulesDir)
        self.m_dirPickerBfModules.SetPath(modulesDir)

        self.RegisterFocusWin(self.m_checkListBfModules)
        self.RegisterFocusWin(self.m_listCtrlModParams)
        self.RegisterFocusWin(self.m_checkListModulesRunners)
        self.RegisterFocusWin(self.m_listBoxModLogging)

        self.bfModules = dict()
        self.bfModulesUser = dict()
        self.bfModulesActive = False

        self.m_listCtrlModParams.InsertColumn(0, 'Type')
        self.m_listCtrlModParams.InsertColumn(1, 'Name')
        self.m_listCtrlModParams.InsertColumn(2, 'Value')
        charLen = [6, 15, 14]
        for i in range(self.m_listCtrlModParams.GetColumnCount()):
            # The autosize applies when some content has been inserted
            #self.m_listCtrlFavs.SetColumnWidth(l_i, wx.LIST_AUTOSIZE)
            self.m_listCtrlModParams.SetColumnWidth(i, charLen[i]*self.avgCharWidth)

        self.paramsType = ''


    def LogMessagesModule(self, messages):
        if not isinstance(messages, (tuple, list)):
            messages = str(messages)
            messages = [messages]

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamped = ['%s: %s' % (timestamp, message) for message in messages]
        self.m_listBoxModLogging.InsertItems(timestamped, 0)
        self.m_listBoxModLogging.Refresh()


    def OnToggleButtonBfModules(self, event):
        baseModName = 'usermodules'
        if baseModName not in sys.modules:
            usermodule = imp.new_module(baseModName)
            sys.modules[baseModName] = usermodule

        bfModulesOn = self.m_toggleBfModules.GetValue()
        baseDirName = self.m_dirPickerBfModules.GetPath()

        if bfModulesOn:
            self.m_toggleBfModules.SetLabel('Unload Modules')
            self.bSizer69.Layout()
            self.m_buttonBfModulesOn.Enable()

            if not baseDirName or not os.path.isdir(baseDirName):
                self.LogMessagesModule('User Modules directory %s is not valid' % baseDirName)
                self.m_toggleBfModules.SetValue(False)
                self.m_toggleBfModules.SetLabel('Load Modules')
                return
            else:
                self.config.Write('BfModules directory', baseDirName)
                self.m_dirPickerBfModules.Disable()

                moduleFileNames = [os.path.basename(filename) for filename in glob.glob('%s/*.py' % baseDirName)]

                baseModName = 'usermodules'
                for moduleFileName in moduleFileNames:
                    if moduleFileName.startswith('__'):
                        continue
                    moduleName = moduleFileName.split('.')[0]
                    self.m_checkListBfModules.Append(moduleName)

                    moduleFullFileName = '%s/%s' % (baseDirName, moduleFileName)
                    moduleFullName = '%s.%s' % (baseModName, moduleName)

                    moduleThread, error = self.LoadModule(moduleFullFileName, moduleFullName)

                    if not moduleThread:
                        self.LogMessagesModule('BfModules Loading error: %s - Error: %s' % (moduleFileName, str(error)))
                        continue

                    self.bfModulesUser[moduleFullName] = moduleThread
                    self.LogMessagesModule('%s - Successfully loaded: %s' % (baseModName, moduleName))

            self.ModulesFillRunners()
            self.m_notebookModuleParams.Enable()

        else:
            self.m_notebookModuleParams.ChangeSelection(0)
            self.m_notebookModuleParams.Disable()
            self.m_toggleBfModules.SetLabel('Load Modules')
            self.m_buttonBfModulesOn.Disable()
            self.m_buttonBfModulesPause.Disable()
            self.BfModulesStop()

            # Clear Params and disable buttons
            self.m_listCtrlModParams.DeleteAllItems()
            self.m_buttonEditModParam.Disable()
            self.m_buttonModParamsSend.Disable()
            self.m_buttonModParamsReload.Disable()
            self.m_buttonModParamsDefaults.Disable()

            # Clear Runners and disable buttons
            self.m_checkListModulesRunners.Clear()
            self.m_buttonModuleRunnersApply.Disable()
            self.m_buttonModuleRunnersRefresh.Disable()
            self.m_buttonModuleRunnersCheckAll.Disable()
            self.m_buttonModuleRunnersUncheckAll.Disable()

            # Clear Actions
            self.ModuleActionsClear()


    def ModuleActionsClear(self):
        sizerItems = self.sizerModActions.GetChildren()
        for sizerItem in sizerItems:
            if sizerItem.IsWindow():
                win = sizerItem.GetWindow()
                win.Unbind(wx.EVT_BUTTON)

        self.sizerModActions.Clear()
        self.m_scrolledWindowModActions.DestroyChildren()
        self.sizerModActions.Layout()
        self.m_scrolledWindowModActions.Refresh()


    def ModulesFillRunners(self, changedMarket=False):
        count = self.m_checkListModulesRunners.GetCount()
        self.m_checkListModulesRunners.Clear()

        # Fill Runners
        if count and self.marketTuple is not None:
            marketComp = self.marketCache[self.marketTuple]
            for runner in marketComp.runners:
                itemIdx = self.m_checkListModulesRunners.Append(runner.name)

        if changedMarket:
            # clear the runner selections also in the modules
            modRunners = list()
            for bfModule in self.bfModulesUser.itervalues():
                bfModule.setRunners(modRunners)


    def BfModulesStop(self):
        self.bfModulesActive = False

        self.m_dirPickerBfModules.Enable()

        baseModName = 'usermodules'
        count = self.m_checkListBfModules.GetCount()
        for itemId in xrange(0, count):
            moduleName = self.m_checkListBfModules.GetString(0)
            moduleFullName = '%s.%s' % (baseModName, moduleName)

            moduleThread = self.bfModulesUser.get(moduleFullName, None)
            if moduleThread:
                if moduleFullName in self.bfModules:
                    del self.bfModules[moduleFullName]
                self.UnloadModule(moduleThread, moduleFullName)
                del self.bfModulesUser[moduleFullName]
                self.LogMessagesModule('BfModules - Unloaded: %s' % moduleName)

        self.m_checkListBfModules.Clear()


    def OnButtonClickBfModulesSwitchOn(self, event):
        self.bfModulesActive = True
        self.m_buttonBfModulesOn.Disable()
        self.m_buttonBfModulesPause.Enable()

        for modName, bfModule in self.bfModules.iteritems():
            bfModule.play()


    def OnButtonClickBfModulesPause(self, event):
        self.bfModulesActive = False
        self.m_buttonBfModulesOn.Enable()
        self.m_buttonBfModulesPause.Disable()

        for modName, bfModule in self.bfModules.iteritems():
            bfModule.pause()


    def OnCheckListBoxBfModulesToggle(self, event):
        baseModName = 'usermodules'

        # Add/Remove the module from the list of modules
        itemId = event.GetInt()

        checked = self.m_checkListBfModules.IsChecked(itemId)
        moduleName = self.m_checkListBfModules.GetString(itemId)
        moduleFullName = '%s.%s' % (baseModName, moduleName)

        playing = self.bfModulesActive

        if checked:
            self.bfModules[moduleFullName] = self.bfModulesUser[moduleFullName]
            if playing:
                self.bfModules[moduleFullName].play()
        else:
            self.bfModules[moduleFullName].pause()
            del self.bfModules[moduleFullName]


    def UnloadModule(self, moduleThread, moduleFullName, appExiting=False):
        if moduleFullName in self.bfModules:
            self.bfModules[moduleFullName].pause()
            del self.bfModules[moduleFullName]

        moduleThread.doExit(appExiting)
        # moduleThread.join()
        del sys.modules[moduleFullName]


    def LoadModule(self, moduleFullFileName, moduleFullName, preLoadedMod=None, **kwargs):

        if preLoadedMod is not None:
            module = preLoadedMod

        else:
            try:
                moduleFile = open(moduleFullFileName, 'r')
            except IOError, e:
                self.LogMessagesModule('BfModules %s - LoadError: %s' % (moduleFullName, str(e)))
                return (None, e)

            try:
                module = imp.load_module(moduleFullName, moduleFile, moduleFullFileName, ('.py', 'r', imp.PY_SOURCE))
            except Exception, e:
                self.LogMessagesModule('BfModules %s - LoadError: %s' % (moduleFullName, str(e)))
                return (None, e)
            finally:
                # No matter if exception or not ... the file must be closed
                moduleFile.close()

        try:
            thModule = ThreadModule(modId=moduleFullName,
                                    mainmod=self,
                                    module=module,
                                    pyEventId=self.thMisc.pyEventId,
                                    **kwargs)
            return (thModule, None)
        except Exception, e:
            self.LogMessagesModule('BfModules %s - LoadError: %s' % (moduleFullName, str(e)))
            return (None, e)

        return (None, None)


    def OnListItemSelectedModParam(self, event):
        itemId = event.GetIndex()
        self.m_buttonEditModParam.Enable()


    def OnListItemDeSelectedModParam(self, event):
        self.m_buttonEditModParam.Disable()


    def OnListItemActivatedModParam(self, event):
        itemId = event.GetIndex()
        self.EditParam(itemId)


    def OnButtonClickModParamsEdit(self, event):
        itemId = self.m_listCtrlModParams.GetFirstSelected()

        # wx.NOT_FOUND ??
        if itemId == -1:
            return

        self.EditParam(itemId)


    def EditParam(self, itemId):
        paramName = self.modParamsNames[itemId]
        param = self.modParams[paramName]


        if isinstance(param[2], list):
            singleEdit = False
            dlg = EditStringList(self, param[2], param[0])
        else:
            singleEdit = True
            dlg = EditModParams(self, paramName, param)

        if dlg.ShowModal() != wx.ID_OK:
            return

        self.m_buttonModParamsSend.Enable()

        if singleEdit:
            self.modParams[paramName] = dlg.param
        else:
            self.modParams[paramName] = [param[0], param[1], dlg.values]

        paramDisplayStr = str(self.modParams[paramName][2])
        self.m_listCtrlModParams.SetStringItem(itemId, 2, paramDisplayStr)
                      

    def OnCheckListBoxBfModules(self, event):
        itemId = self.m_checkListBfModules.GetSelection()
        if itemId == wx.NOT_FOUND:
            return

        self.LoadModuleParams(itemId, 'user')

        self.m_buttonEditModParam.Enable()
        self.m_buttonModParamsReload.Enable()
        self.m_buttonModParamsDefaults.Enable()

        self.ModuleRunnersRefresh(itemId, 'user')
        self.m_buttonModuleRunnersApply.Disable()
        self.m_buttonModuleRunnersRefresh.Enable()
        self.m_buttonModuleRunnersCheckAll.Enable()
        self.m_buttonModuleRunnersUncheckAll.Enable()

        self.LoadModuleActions(itemId, 'user')


    def LoadModuleActions(self, itemId, paramsType):
        if paramsType == 'user':
            baseModName = 'usermodules'
            moduleName = self.m_checkListBfModules.GetString(itemId)

        moduleFullName = '%s.%s' % (baseModName, moduleName)

        self.paramsType = paramsType
        if paramsType == 'user':
            self.modActions = self.bfModulesUser[moduleFullName].getActions()

        self.ModuleActionsClear()

        self.modActionsMap = dict()
        for modActionName, modActionId in self.modActions.iteritems():
            button = wx.Button(self.m_scrolledWindowModActions,
                               wx.ID_ANY, modActionName)

            button.Bind(wx.EVT_BUTTON, self.OnModAction)
            self.modActionsMap[button.GetId()] = (paramsType, moduleFullName, modActionName)
            self.sizerModActions.Add(button, flag=wx.ALIGN_CENTER)

        self.sizerModActions.Layout()


    def OnModAction(self, event):
        paramsType, moduleFullName, modActionName = self.modActionsMap[event.GetId()]

        if paramsType == 'user':
            theMod = self.bfModulesUser[moduleFullName]

        modActionId = self.modActions[modActionName]
        theMod.doAction(modActionId)


    def LoadModuleParams(self, itemId, paramsType):
        # Display properties in the property box
        if paramsType == 'user':
            baseModName = 'usermodules'
            moduleName = self.m_checkListBfModules.GetString(itemId)

        moduleFullName = '%s.%s' % (baseModName, moduleName)

        self.paramsType = paramsType
        if paramsType == 'user':
            self.modParams = copy.deepcopy(self.bfModulesUser[moduleFullName].getParams())

        self.modParamsNames = self.modParams.keys()
        self.modParamsNames.sort(key=operator.itemgetter(0))

        self.m_listCtrlModParams.DeleteAllItems()

        for paramIndex, paramName in enumerate(self.modParamsNames):
            param = self.modParams[paramName]
            nametype = str(param[0]).split("'")[1]
            # Type
            row = self.m_listCtrlModParams.InsertStringItem(paramIndex, nametype)
            # Name
            self.m_listCtrlModParams.SetStringItem(row, 1, paramName)
            # Value
            self.m_listCtrlModParams.SetStringItem(row, 2, str(param[2]))


    def OnButtonClickModParamsSend(self, event):
        if self.paramsType == 'user':
            itemId = self.m_checkListBfModules.GetSelection()

        if itemId == wx.NOT_FOUND:
            return

        self.m_buttonModParamsSend.Disable()

        if self.paramsType == 'user':
            baseModName = 'usermodules'
            moduleName = self.m_checkListBfModules.GetString(itemId)
            moduleFullName = '%s.%s' % (baseModName, moduleName)
            self.bfModulesUser[moduleFullName].setParams(copy.deepcopy(self.modParams))


    def OnButtonClickModParamsReload(self, event):
        if self.paramsType == 'user':
            itemId = self.m_checkListBfModules.GetSelection()

        if itemId == wx.NOT_FOUND:
            return

        self.LoadModuleParams(itemId, self.paramsType)
        self.m_buttonModParamsSend.Disable()


    def OnButtonClickModParamsDefaults(self, event):
        for paramIndex, paramName in enumerate(self.modParamsNames):
            param = self.modParams[paramName]
            defValue = param[1]
            param[2] = defValue
            self.m_listCtrlModParams.SetStringItem(paramIndex, 2, str(defValue))

        self.m_buttonModParamsSend.Enable()


    def OnMenuSelectionModuleLoggingClearAllMessages(self, event):
        self.m_listBoxModLogging.Clear()


    def OnNoteBookPageChangedModules(self, event):
        event.Skip()
        # Change the displayed params to those of the visible listbox
        # or delete the params
        page = event.GetSelection()

        if page == 0:
            paramsType = 'user'
            itemId = self.m_checkListBfModules.GetSelection()
        else:
            itemId = wx.NOT_FOUND

        if itemId == wx.NOT_FOUND:
            self.m_listCtrlModParams.DeleteAllItems()
            self.m_buttonEditModParam.Disable()
            self.m_buttonModParamsSend.Disable()
            self.m_buttonModParamsReload.Disable()
            self.m_buttonModParamsDefaults.Disable()

            # Clear Runners and disable buttons
            self.m_checkListModulesRunners.Clear()
            self.m_buttonModuleRunnersApply.Disable()
            self.m_buttonModuleRunnersRefresh.Disable()
            self.m_buttonModuleRunnersCheckAll.Disable()
            self.m_buttonModuleRunnersUncheckAll.Disable()

            self.ModuleActionsClear()
            return

        self.paramsType = paramsType

        self.m_buttonEditModParam.Disable()
        self.m_buttonModParamsReload.Enable()
        self.m_buttonModParamsDefaults.Enable()

        self.LoadModuleParams(itemId, paramsType)

        self.m_buttonModuleRunnersApply.Disable()
        self.m_buttonModuleRunnersRefresh.Enable()
        self.m_buttonModuleRunnersCheckAll.Enable()
        self.m_buttonModuleRunnersUncheckAll.Enable()

        self.ModuleRunnersRefresh(itemId, paramsType)

        self.LoadModuleActions(itemId, paramsType)

                        
    def OnButtonClickModuleRunnersApply(self, event):
        if self.paramsType == 'user':
            itemId = self.m_checkListBfModules.GetSelection()

        if itemId == wx.NOT_FOUND:
            return

        self.ModuleRunnersApply(itemId, self.paramsType)
        self.m_buttonModuleRunnersApply.Disable()


    def ModuleRunnersApply(self, itemId, paramsType):
        if paramsType == 'user':
            baseModName = 'usermodules'
            moduleName = self.m_checkListBfModules.GetString(itemId)

        moduleFullName = '%s.%s' % (baseModName, moduleName)

        count = self.m_checkListModulesRunners.GetCount()
        modRunners = list()
        for runnerIdx in xrange(count):
            if self.m_checkListModulesRunners.IsChecked(runnerIdx):
                runnerName = self.m_checkListModulesRunners.GetString(runnerIdx)
                modRunners.append(runnerName)

        if paramsType == 'user':
            self.bfModulesUser[moduleFullName].setRunners(modRunners)


    def OnButtonClickModuleRunnersRefresh(self, event):
        itemId = wx.NOT_FOUND

        if self.paramsType == 'user':
            itemId = self.m_checkListBfModules.GetSelection()

        if itemId == wx.NOT_FOUND:
            return

        self.ModuleRunnersRefresh(itemId, self.paramsType)
        self.m_buttonModuleRunnersApply.Disable()


    def ModuleRunnersRefresh(self, itemId, paramsType):
        count = self.m_checkListModulesRunners.GetCount()
        if not count:
            if self.marketTuple is not None:
                marketComp = self.marketCache[self.marketTuple]

                for runner in marketComp.runners:
                    self.m_checkListModulesRunners.Append(runner.name)

        if paramsType == 'user':
            baseModName = 'usermodules'
            moduleName = self.m_checkListBfModules.GetString(itemId)

        moduleFullName = '%s.%s' % (baseModName, moduleName)

        if paramsType == 'user':
            modRunners = self.bfModulesUser[moduleFullName].getRunners()

        count = self.m_checkListModulesRunners.GetCount()

        for runnerIdx in xrange(count):
            runnerName = self.m_checkListModulesRunners.GetString(runnerIdx)
            if runnerName in modRunners:
                checkStatus = True
            else:
                checkStatus = False
            self.m_checkListModulesRunners.Check(runnerIdx, checkStatus)


    def OnButtonClickModuleRunnersCheckAll(self, event):
        count = self.m_checkListModulesRunners.GetCount()

        for i in xrange(count):
            self.m_checkListModulesRunners.Check(i, True)


    def OnButtonClickModuleRunnersUncheckAll(self, event):
        count = self.m_checkListModulesRunners.GetCount()

        for i in xrange(count):
            self.m_checkListModulesRunners.Check(i, False)


    def OnCheckListBoxToggledModuleRunners(self, event):
        self.m_buttonModuleRunnersApply.Enable()


    def m_listBoxModLoggingOnContextMenu(self, event):
        event.Skip()

        position = event.GetPosition()
        item = self.m_listBoxModLogging.HitTest(position)

        itemFound = (item != wx.NOT_FOUND)
        selections = self.m_listBoxModLogging.GetSelections()

        if itemFound and item not in selections:
            self.m_listBoxModLogging.DeselectAll()
            self.m_listBoxModLogging.Select(item)
            selections = [item]

        count = self.m_listBoxModLogging.GetCount()
        numSelections = len(selections)
        # multiSelection = (numSelections > 1)

        self.m_menuItemModLoggingSelectAll.Enable(numSelections < count)
        self.m_menuItemModLoggingDeselectAll.Enable(numSelections)
        self.m_menuItemModLoggingClearAll.Enable(count)
        self.m_menuItemModLoggingClearSelected.Enable(numSelections)
        self.m_menuItemModLoggingCopyAll.Enable(count)
        self.m_menuItemModLoggingCopySelected.Enable(numSelections)

        self.m_listBoxModLogging.PopupMenu(self.m_menuModLogging, position)


    def OnMenuSelectionModuleLoggingSelectAllMessages(self, event):
        event.Skip()
        count = self.m_listBoxModLogging.GetCount()
        for i in xrange(count):
            self.m_listBoxModLogging.Select(i)


    def OnMenuSelectionModuleLoggingDeselectAllMessages(self, event):
        event.Skip()
        self.m_listBoxModLogging.DeselectAll()


    def OnMenuSelectionModuleLoggingClearAllMessages(self, event):
        event.Skip()
        self.m_listBoxModLogging.Clear()


    def OnMenuSelectionModuleLoggingClearSelectedMessages(self, event):
        event.Skip()

        selections = list(self.m_listBoxModLogging.GetSelections())
        selections.sort(reverse=True)
        for selection in selections:
            self.m_listBoxModLogging.Delete(selection)


    def OnMenuSelectionModuleLoggingCopyAllMessages(self, event):
        event.Skip()

        if wx.TheClipboard.Open():
            selectionList = list()
            count = self.m_listBoxModLogging.GetCount()
            for i in xrange(count):
                selectionList.append(self.m_listBoxModLogging.GetString(i))

            textToCopy = '\r\n'.join(selectionList)
            textDataObject = wx.TextDataObject(textToCopy)
            wx.TheClipboard.AddData(textDataObject)
            wx.TheClipboard.Close()
        

    def OnMenuSelectionModuleLoggingCopySelectedMessages(self, event):
        event.Skip()

        if wx.TheClipboard.Open():
            selectionList = list()
            selections = self.m_listBoxModLogging.GetSelections()
            for selection in selections:
                selectionList.append(self.m_listBoxModLogging.GetString(selection))

            textToCopy = '\r\n'.join(selectionList)
            textDataObject = wx.TextDataObject(textToCopy)
            wx.TheClipboard.AddData(textDataObject)
            wx.TheClipboard.Close()


    def OnCharListBoxModLogging(self, event):
        event.Skip()
        
        keycode = event.GetKeyCode()

        if keycode == wx.WXK_DELETE:
            selections = list(self.m_listBoxModLogging.GetSelections())
            if selections:
                selections.sort(reverse=True)

                for selection in selections:
                    self.m_listBoxModLogging.Delete(selection)
