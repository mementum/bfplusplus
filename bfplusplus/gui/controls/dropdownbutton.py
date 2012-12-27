#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of Bfplusplus
#
# Bfplusplus is a graphical interface to the Betfair Betting Exchange
# Copyright (C) 2010  Daniel Rodriguez (aka Daniel Rodriksson)
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

class OptionButton(wx.PyPanel):
    def __init__(self, parent, id=wx.ID_ANY, label=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL|wx.NO_BORDER,
                 name='OptionButton'):

        self._sizeDrop = '01'

        # Notice that label isn't set in the PyPanel constructor
        wx.PyPanel.__init__(self, parent, id, pos, size, style, name)

        self.InheritAttributes()

        self._sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._button = wx.Button(self, wx.ID_ANY, label, style=wx.BU_EXACTFIT)
        self._drop = DropDownButton(self, wx.ID_ANY, '0')

        bw, bh = self._button.GetBestSize()
        dw, dh = self._drop.GetBestSize()
        self.bestSize = wx.Size(bw + dw, max(bh, dh))

        self._sizer.Add(self._button, 1, wx.EXPAND, 5)
        self._sizer.Add(self._drop, 0, wx.EXPAND, 5)

        self.SetSizer(self._sizer)
        self.Layout()

        self._button.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        self._drop.Bind(wx.EVT_BUTTON, self.OnDropClick)

        # self._button.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDownButton)


    def SetLabel(self, label):
        self._button.SetLabel(label)


    def GetLabel(self):
        return self._button.GetLabel()


    def OnLeftDownButton(self, event):
        # evt = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, self.GetId())
        pass


    def OnButtonClick(self, event):
        evt = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, self.GetId())
        evt.SetEventObject(self)
        self.GetEventHandler().ProcessEvent(evt)


    def OnDropClick(self, event):
        evt = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, self.GetId())
        evt.SetEventObject(self)
        self.GetEventHandler().ProcessEvent(evt)


    def DoGetBestSize(self):
        return self.bestSize
                                 

class DropDownButton(wx.PyControl):

    def __init__(self, parent, id=wx.ID_ANY, label=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.NO_BORDER,
                 validator=wx.DefaultValidator, name='DropDownButton'):

        self._sizeDrop = '00' + label

        wx.PyControl.__init__(self, parent, id, pos, size, style, validator, name)

        # By default, we start unpressed
        self._pressed = False

        # Bind the events related to our control: first of all, we use a
        # combination of wx.BufferedPaintDC and an empty handler for
        # wx.EVT_ERASE_BACKGROUND (see later) to reduce flicker
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        
        # Then we want to monitor user clicks, so that we can switch our
        # state between checked and unchecked
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        if wx.Platform == '__WXMSW__':
            # MSW Sometimes does strange things...
            self.Bind(wx.EVT_LEFT_DCLICK,  self.OnLeftDown)

        self.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)


    def OnEraseBackground(self, event):
        """ Handles the wx.EVT_ERASE_BACKGROUND event for CustomCheckBox. """

        # This is intentionally empty, because we are using the combination
        # of wx.BufferedPaintDC + an empty OnEraseBackground event to
        # reduce flicker
        pass


    def OnEnterWindow(self, event):
        if self.HasCapture():
            self._pressed = True
            self.Refresh()


    def OnLeaveWindow(self, event):
        if self.HasCapture():
            self._pressed = False
            self.Refresh()


    def OnLeftDown(self, event):
        self._pressed = True
        self.CaptureMouse()
        self.Refresh()


    def OnLeftUp(self, event):
        if self.GetCapture() == self:
            self.ReleaseMouse()
        if self._pressed:
            self._pressed = False
            self.Refresh()
            evt = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, self.GetId())
            evt.SetEventObject(self)
            self.GetEventHandler().ProcessEvent(evt)
    

    def OnPaint(self, event):
        """ Handles the wx.EVT_PAINT event for CustomCheckBox. """

        # If you want to reduce flicker, a good starting point is to
        # use wx.BufferedPaintDC.
        dc = wx.BufferedPaintDC(self)

        # It is advisable that you don't overcrowd the OnPaint event
        # (or any other event) with a lot of code, so let's do the
        # actual drawing in the Draw() method, passing the newly
        # initialized wx.BufferedPaintDC
        self.Draw(dc)


    def Draw(self, dc):
        """
        Actually performs the drawing operations, for the bitmap and
        for the text, positioning them centered vertically.
        """

        # Get the actual client size of ourselves
        width, height = self.GetClientSize()

        if not width or not height:
            # Nothing to do, we still don't have dimensions!
            return

        # Initialize the wx.BufferedPaintDC, assigning a background
        # colour and a foreground colour (to draw the text)
        backColour = self.GetBackgroundColour()
        backBrush = wx.Brush(backColour, wx.SOLID)
        dc.SetBackground(backBrush)
        dc.Clear()

        # dropWidth, dropHeight = dc.GetTextExtent(self._sizeDrop)
        # dropHeight = height - 2 * 1
        dropWidth = width
        dropHeight = height

        # Position the dropbutton centered vertically and horizontally
        # dropXpos = (width - dropWidth) / 2
        # dropYpos = (height - dropHeight) / 2
        dropXpos = 0
        dropYpos = 0

        # Draw the dropdownbutton
        render = wx.RendererNative.Get()
        pos = wx.Rect(dropXpos, dropYpos, dropWidth, dropHeight)
        status = wx.CONTROL_PRESSED if self._pressed else wx.CONTROL_CURRENT
        render.DrawComboBoxDropButton(self, dc, pos, status)
    

    def DoGetBestSize(self):
        height = 2 * 1
        width = 2 * 1

        if self._sizeDrop:
            dWidth, dHeight = self.GetTextExtent(self._sizeDrop)
            width += dWidth
            height += dHeight

        bestSize = wx.Size(width, height)
        self.CacheBestSize(bestSize)
        return bestSize


