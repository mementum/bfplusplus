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

from base64 import b64encode, b64decode

import wx

from gui.EditStringList import EditStringList
from gui.UserSecurity import UserSecurity

import bfpy

if True:
    def init(self):
        usernames = self.config.Read('Usernames', '[]')
        usernames = eval(usernames)
        # This ensures a value in the registry (empty or the original)
        self.config.Write('Usernames', str(usernames))

        # decrypt the usernames
        try:
            usernames = [self.aes.decrypt(b64decode(username)) for username in usernames]
        except:
            # If decryption fails, clear the registry
            usernames = []
            self.config.Write('Usernames', str(usernames))

        self.m_comboBoxUsername.SetItems(usernames)

        username = self.config.Read('Username', '')
        self.config.Write('Username', username)

        if username:
            try:
                username = self.aes.decrypt(b64decode(username))
            except:
                # If decryption fails, clear the registry
                username = ''
                self.config.Write('Username', username)

        self.m_comboBoxUsername.SetValue(username)

        rememberUsername = self.config.ReadBool('Remember Username', False)
        self.config.WriteBool('Remember Username', rememberUsername)
        self.m_checkBoxRememberUsername.SetValue(rememberUsername)

        self.useFreeApi = self.config.ReadBool('Use Free Api', True)
        self.config.WriteBool('Use Free Api', self.useFreeApi)
        self.m_checkBoxFreeAPI.SetValue(self.useFreeApi)
        self.m_textCtrlProductId.Enable(not self.useFreeApi)

        productId = self.config.ReadInt('Api Product Id.', 82)
        self.config.WriteInt('Api Product Id.', productId)
        self.m_textCtrlProductId.SetValue(str(productId))

        # Currency of the logged-in account
        self.currency = ''

        self.m_comboBoxUsername.SetFocus()
        

    def postLoginUsernames(self, currency, productId):
        self.currency = currency
        self.minStakes = bfpy.BfApi.getMinStakes(self.currency)

        if not self.useFreeApi:
            # login has been successful, enable refresh times below 1sec (down to 0.2sec)
            # to comply with Betfair rules
            self.m_sliderRefresh.SetRange(2, 300)
            self.m_sliderRefresh.Refresh()

        username = self.m_comboBoxUsername.GetValue()
        if username not in self.m_comboBoxUsername.GetItems():
            self.m_comboBoxUsername.Append(username)

        if self.m_checkBoxRememberUsername.GetValue():
            # Last username
            username = b64encode(self.aes.encrypt(username))
            self.config.Write('Username', username)

            # List of usernames
            usernames = self.m_comboBoxUsername.GetItems()
            usernames = [b64encode(self.aes.encrypt(username)) for username in usernames]
            self.config.Write('Usernames', str(usernames))

        self.config.WriteInt('Api Product Id.', productId)


    def OnCheckBoxUseFreeApi(self, event):
        self.useFreeApi = self.m_checkBoxFreeAPI.GetValue()
        self.config.WriteBool('Use Free Api', self.useFreeApi)
        self.m_textCtrlProductId.Enable(not self.useFreeApi)


    def OnCheckBoxRememberUsername(self, event):
        remember = self.m_checkBoxRememberUsername.GetValue()

        if remember:
            userRemember = UserSecurity(self)
            retcode = userRemember.ShowModal()

            if retcode != wx.YES:
                self.m_checkBoxRememberUsername.SetValue(False)
                return

        self.config.WriteBool('Remember Username', remember)
        if remember:
            username = self.m_comboBoxUsername.GetValue()
            if username:
                username = b64encode(self.aes.encrypt(username))
                self.config.Write('Username', username)

            usernames = self.m_comboBoxUsername.GetItems()
            usernames = [b64encode(self.aes.encrypt(username)) for username in usernames]
            self.config.Write('Usernames', str(usernames))
        else:
            self.config.Write('Username', '')
            self.config.Write('Usernames', '[]')


    def OnButtonClickManageUsernames(self, event):
        usernames = self.m_comboBoxUsername.GetItems()
        dlg = EditStringList(self, values=usernames)

        if dlg.ShowModal() != wx.ID_OK:
            return

        username = self.m_comboBoxUsername.GetValue()

        usernames = dlg.values
        self.m_comboBoxUsername.SetItems(usernames)
        if self.m_checkBoxRememberUsername.GetValue():
            self.config.Write('Usernames', str(usernames))

        if username in usernames:
            self.m_comboBoxUsername.SetValue(username)
