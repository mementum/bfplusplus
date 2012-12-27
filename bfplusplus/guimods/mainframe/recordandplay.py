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

import imp
import os
import sys

import wx

from bfobj import MarketTuple
import threads.threadbase as threadbase

if True:
    def init(self):
        recordAndPlayDir = self.config.Read('RecordAndPlay directory', '')
        self.config.Write('RecordAndPlay directory', recordAndPlayDir)
        self.m_dirPickerRecordAndPlay.SetPath(recordAndPlayDir)

        separator = self.config.Read('RecordAndPlay separator', ';')
        self.config.Write('RecordAndPlay separator', separator)
        self.m_textCtrlRecordAndPlaySeparator.SetValue(separator)

        tabAsSeparator = self.config.ReadBool('RecordAndPlay tab as separator', False)
        self.config.WriteBool('RecordAndPlay tab as separator', tabAsSeparator)
        self.m_checkBoxRecordAndPlayTabSeparator.SetValue(tabAsSeparator)

        self.recordModule = None
        self.playModule = None


    def OnToggleButtonRecord(self, event):
        # if not sys.modules.get('recordnplay' , None):
        #            __import__('recordnplay')
        if False:
            recNPlayName = 'recordnplay'
            if recNPlayName not in sys.modules:
                recNPlayMod = imp.new_module(recNPlayName)
                sys.modules[recNPlayName] = recNPlayMod

        recordOn = self.m_toggleBtnRecord.GetValue()

        if recordOn:
            marketDir = self.m_dirPickerRecordAndPlay.GetPath()
            separator = self.m_textCtrlRecordAndPlaySeparator.GetValue()

            if not separator:
                wx.MessageBox('The separator character cannot be none',
                              'Missing separator')
                return

            tabAsSeparator = self.m_checkBoxRecordAndPlayTabSeparator.GetValue()
            if tabAsSeparator:
                separator = '\t'

            if separator == '.':
                wx.MessageBox('The separator cannot be a dot (.)',
                              'Wrong separator')
                return

            if not os.path.isdir(marketDir):
                wx.MessageBox('Record directory %s is not valid' % marketDir,
                              'Invalid directory')
                self.m_toggleBtnRecord.SetValue(False)
                return

            self.m_toggleBtnPlay.Disable()
            self.config.Write('RecordAndPlay directory', marketDir)
            self.config.Write('RecordAndPlay separator', separator)

            # Load the module
            if True:
                import recordnplay.record
                # reload(recordnplay.record)
                self.recordModule, error = self.LoadModule('',
                                                           'recordnplay.record',
                                                           preLoadedMod=recordnplay.record,
                                                           marketDir=marketDir,
                                                           separator=separator)
            else:
                self.recordModule, error = self.LoadModule('recordnplay/record.py',
                                                           'recordnplay.record',
                                                           marketDir=marketDir,
                                                           separator=separator)

            if not self.recordModule:
                self.LogMessagesModule('Failed to start recording: %s' % str(error))
                self.m_toggleBtnRecord.SetValue(False)
                self.m_toggleBtnPlay.Enable()
                                
        else:
            self.RecordStop()


    def RecordStop(self):
        self.m_toggleBtnRecord.SetValue(False)
        self.m_toggleBtnPlay.Enable()
        self.UnloadModule(self.recordModule, 'recordnplay.record')
        self.recordModule = None


    def OnToggleButtonPlay(self, event):
        if not sys.modules.get('recordnplay' , None):
            __import__('recordnplay')

        playOn = self.m_toggleBtnPlay.GetValue()

        if playOn:
            marketDir = self.m_dirPickerRecordAndPlay.GetPath()
            separator = self.m_textCtrlRecordAndPlaySeparator.GetValue()

            tabAsSeparator = self.m_checkBoxRecordAndPlayTabSeparator.GetValue()
            if tabAsSeparator:
                separator = '\t'
            
            if separator == '.':
                wx.MessageBox('The separator cannot be a dot (.)',
                              'wrong separator')
                return

            if not os.path.isdir(marketDir):
                wx.MessageBox('Record directory %s is not valid' % marketDir,
                              'Invalid directory')
                self.m_toggleBtnPlay.SetValue(False)
                return

            self.m_toggleBtnRecord.Disable()
            self.config.Write('RecordAndPlay directory', marketDir)

            marketTuple = MarketTuple(exchangeId=0, marketId=0)
            self.GetMarketPrices(marketTuple)
            self.GetMarketProfitAndLoss(marketTuple)
            self.GetMUBets(marketTuple)

            if self.bfClient is None:
                while True:
                    if threadbase.ThreadBase.bfClientMaster is not None:
                        break
                self.bfClient = threadbase.ThreadBase.bfClientMaster

            # Load the module
            if True:
                import recordnplay.play
                self.playModule, error = self.LoadModule('',
                                                         'recordnplay.play',
                                                         preLoadedMod=recordnplay.play,
                                                         marketDir=marketDir,
                                                         separator=separator,
                                                         pyIdMarket=self.thMisc.pyEventId,
                                                         pyIdPrices=self.pyEventIdMarketPrices)
            else:
                self.playModule, error = self.LoadModule('recordnplay/play.py',
                                                         'recordnplay.play',
                                                         marketDir=marketDir,
                                                         separator=separator,
                                                         pyIdMarket=self.thMisc.pyEventId,
                                                         pyIdPrices=self.pyEventIdMarketPrices)

            if not self.playModule:
                self.LogMessagesModule('Failed to start playing recording: %s' % str(error))
                self.m_toggleBtnPlay.SetValue(False)
                self.m_toggleBtnRecord.Enable()

            else:
                self.playModule.play()

        else:
            self.PlayStop()


    def PlayStop(self):
        self.m_toggleBtnPlay.SetValue(False)
        if self.thGetMarketPrices:
            self.m_toggleBtnRecord.Enable()
        self.UnloadModule(self.playModule, 'recordnplay.play')


    def OnCheckBoxUseTabAsSeparator(self, event):
        tabAsSeparator = self.m_checkBoxRecordAndPlayTabSeparator.GetValue()
        self.config.WriteBool('RecordAndPlay tab as separator', tabAsSeparator)
        self.m_textCtrlRecordAndPlaySeparator.Enable(not tabAsSeparator)
