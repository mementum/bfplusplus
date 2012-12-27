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
from wx.lib.agw.toasterbox import ToasterBox, TB_SIMPLE, TB_COMPLEX, TB_ONCLICK
from wx.lib.agw.hyperlink import HyperLinkCtrl
from wx.lib.pubsub import setupkwargs
from wx.lib.pubsub import pub


import gui.UpdateChecker
from util import Message

if True:

    def init(self):
        self.checkUpdateOnStart = self.config.ReadBool('Check Update On Start', False)
        self.m_checkBoxSeekUpdateOnAppStart.SetValue(self.checkUpdateOnStart)


    def CheckUpdateOnStart(self):
        if self.checkUpdateOnStart:
            self.SeekUpdates()


    def OnCheckBoxUpdateOnAppStart(self, event):
        self.checkUpdateOnStart = self.m_checkBoxSeekUpdateOnAppStart.GetValue()
        self.config.WriteBool('Check Update On Start', self.checkUpdateOnStart)
    

    def OnButtonClickLookForUpdates(self, event):
        event.Skip()
        self.SeekUpdates()


    def SeekUpdates(self, topic=None):
        message = Message(action='seekUpdates', topic=topic)
        self.thMisc.passMessage(message)
        

    def OnSeekUpdates(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                if message.topic:
                    pub.sendMessage(message.topic, version=None, exception=exception)
                    return
                self.LogMessages(exception)
            return

        version = message.response

        if message.topic:
            pub.sendMessage(message.topic, version=version, exception=None)
            return

        tb = ToasterBox(self, TB_COMPLEX, closingstyle=TB_ONCLICK)
        tb.SetPopupSize(wx.Size(275, 100))
        tb.SetPopupPositionByInt(3)
        # tb.SetPopupPosition(wx.Point(0,0))
        tb.SetPopupPauseTime(7000)

        tbpanel = tb.GetToasterBoxWindow()
        panel = wx.Panel(tbpanel)
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add((0,5))
        if version > self.version:
            stText = wx.StaticText(panel, wx.ID_ANY, 'Bfplusplus version "%s" is available at:' % version)
            sizer.Add(stText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)

            hlink = HyperLinkCtrl(panel, wx.ID_ANY, 'http://code.google.com/p/bfplusplus',
                                        URL='http://code.google.com/p/bfplusplus')

            sizer.Add((0,5))
            sizer.Add(hlink, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)

        else:
            stText = wx.StaticText(panel, wx.ID_ANY, 'Bfplusplus: No new version is available')
            sizer.Add(stText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)

        sizer.Layout()
        panel.SetSizer(sizer)

        tb.AddPanel(panel)

        tb.Play()





        
