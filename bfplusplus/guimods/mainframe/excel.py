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

if True:
    from collections import defaultdict

    from util import Message
    
    def init(self):
        try:
            # To enable multithreading in COM
            # sys.coinit_flags = 0
            # Can't be used together with wx.DirPickerCtrl
            import pythoncom
            import win32com.client
        except ImportError:
            self.m_bpButtonExcelPlay.Enable(False)
            self.m_bpButtonExcelPause.Enable(False)
            self.m_bpButtonExcelPause.Enable(False)
            self.m_bpButtonExcelUpdateWorkbooks.Enable(False)
            self.m_bpButtonExcelOpen.Enable(False)
            self.m_textCtrlExcelCell.Enable(False)

        self.excelModCell = self.config.Read('Excel Base Cell', 'A1')
        self.config.Write('Excel Base Cell', self.excelModCell)
        self.m_textCtrlExcelCell.SetValue(self.excelModCell)

        self.workbooks = dict()
        self.sheets = defaultdict(dict)

        self.excelModActive = False
        self.excelModPaused = False
        self.excelModSheets = dict()
        self.excelModule = None


    def OnButtonClickExcelOpen(self, event):
        event.Skip()

        self.LoadExcelModule()
        if self.excelModule is not None:
            message = Message(subAction='openExcel')
            self.excelModule.passMessage(message)


    def LoadExcelModule(self):
        if self.excelModule is not None:
            return

        import excelmod.excelmod
        self.excelModule, error = self.LoadModule('', 'excelmod.excelmod',
                                                  preLoadedMod=excelmod.excelmod)


    def OnGetExcelSheets(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if exception is not None:
            return

        for wbname in response.sheets:
            self.m_checkListExcelWorkbooks.Append(wbname)
            self.workbooks[wbname] = False

            for sheetname in response.sheets[wbname]:
                self.sheets[wbname][sheetname] = False


    def OnButtonClickExcelUpdateWorkbooks(self, event):
        event.Skip()

        self.m_checkListExcelSheets.Clear()
        self.m_checkListExcelWorkbooks.Clear()

        self.workbooks = dict()
        self.sheets = defaultdict(dict)

        self.LoadExcelModule()
        if self.excelModule is not None:
            message = Message()
            message.subAction = 'getExcelSheets'
            self.excelModule.passMessage(message)


    def OnCheckListBoxExcelWorkbooks(self, event):
        event.Skip()
        self.ExcelUpdateSheetsDisplay()


    def ExcelUpdateSheetsDisplay(self):
        wbname = self.m_checkListExcelWorkbooks.GetStringSelection()
        wbsheets = self.sheets[wbname]

        self.m_checkListExcelSheets.Clear()
        for sheetname, status in wbsheets.iteritems():
            itemId = self.m_checkListExcelSheets.Append(sheetname)
            self.m_checkListExcelSheets.Check(itemId, status)


    def OnCheckListBoxToggleExcelWorkbooks(self, event):
        event.Skip()
        itemId = event.GetInt()
        checked = self.m_checkListExcelWorkbooks.IsChecked(itemId)
        wbname = self.m_checkListExcelWorkbooks.GetString(itemId)

        # Update the sheets display
        self.m_checkListExcelWorkbooks.SetSelection(itemId)
        self.ExcelUpdateSheetsDisplay()

        self.workbooks[wbname] = checked


    def OnCheckListBoxToggleExcelSheets(self, event):
        event.Skip()
        itemId = event.GetInt()
        checked = self.m_checkListExcelSheets.IsChecked(itemId)
        sheetname = self.m_checkListExcelSheets.GetString(itemId)
        wbname = self.m_checkListExcelWorkbooks.GetStringSelection()

        self.sheets[wbname][sheetname] = checked


    def OnButtonClickExcelPlay(self, event):
        event.Skip()

        self.LoadExcelModule()
        if self.excelModule is None:
            return

        if not self.excelModActive:
            self.excelModCell = self.m_textCtrlExcelCell.GetValue()
            self.m_textCtrlExcelCell.Enable(False)

            message = Message(subAction='setActiveCell')
            message.cell = self.excelModCell
            self.excelModule.passMessage(message)

            self.m_bpButtonExcelStop.Enable(True)
            self.m_bpButtonExcelUpdateWorkbooks.Enable(False)
            self.excelModActive = True

        else: # pause mode
            pass

        self.excelModPaused = False
        self.m_bpButtonExcelPlay.Enable(False)
        self.m_bpButtonExcelPause.Enable(True)
        self.excelModule.play()


    def OnButtonClickExcelPause(self, event):
        event.Skip()

        self.excelModule.pause()
        self.excelModPaused = True

        self.m_bpButtonExcelPlay.Enable(True)
        self.m_bpButtonExcelPause.Enable(False)


    def OnButtonClickExcelStop(self, event):
        event.Skip()

        self.UnloadModule(self.excelModule, 'excelmod.excelmod')
        self.excelModActive = False
        self.excelModPaused = False

        self.m_bpButtonExcelPlay.Enable(True)
        self.m_bpButtonExcelPause.Enable(False)
        self.m_bpButtonExcelStop.Enable(False)
        self.m_bpButtonExcelUpdateWorkbooks.Enable(True)
        self.m_textCtrlExcelCell.Enable(True)
