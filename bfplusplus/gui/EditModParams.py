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
"""Subclass of EditModParams, which is generated by wxFormBuilder."""

import wx

import MainGui

# Implementing EditModParams
class EditModParams(MainGui.EditModParams):
    def __init__(self, parent, paramName, param):
	MainGui.EditModParams.__init__(self, parent)

	self.paramName = paramName
	self.param = param

	self.m_staticTextName.SetLabel(self.paramName)

        self.typestr = str(self.param[0]).split("'")[1]
	self.m_staticTextType.SetLabel(self.typestr)
        if self.typestr == 'bool':
            self.m_textCtrlValue.SetValue(str(int(self.param[2])))
        else:
            self.m_textCtrlValue.SetValue(str(self.param[2]))


    # Handlers for EditModParams events.
    def OnButtonClickDefault(self, event):
	self.param[2] = self.param[1]
	self.m_textCtrlValue.SetValue(str(sel.param[1]))

	
    def OnOKButtonClick(self, event):
	paramValueStr = self.m_textCtrlValue.GetValue()
	try:
            if self.typestr == 'bool':
                paramValue = self.param[0](int(paramValueStr))
            else:
                paramValue = self.param[0](paramValueStr)
	except:
	    wx.MessageBox('The value of the param is not of type %s' % str(self.paramName),
			  'Wrong param value')
	    return

	self.param[2] = paramValue
	self.EndModal(wx.ID_OK)

	
	