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

import bfpy
from util import Message

from gui.LoginInfoRegistration import LoginInfoRegistration

if True:
    def init(self):
        self.vendorSoftwareId = 0
        self.productId = 0


    def OnTextEnterPassword(self, event):
        # It seems that (for example) on MacOS skipping the event
        # implies that the OS also handles the enter
        # event.Skip()
        buttonId = self.m_buttonLogin.GetId()
        cmdEvent = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, buttonId)
        self.m_buttonLogin.Command(cmdEvent)


    def OnButtonClickLogin(self, event):
        event.Skip()
        self.blockLogin.Show(True)

        username = self.m_comboBoxUsername.GetValue()
        password = self.m_textCtrlPassword.GetValue()

        if self.useFreeApi:
            productId = bfpy.freeApiId
        else:
            try:
                productId = int(self.m_textCtrlProductId.GetValue())
            except ValueError:
                wx.MessageBox('Wrong Product Id.', 'Login cannot proceed!')
                return

        self.productId = productId

        message = Message(action='login')
        message.username = username
        message.password = password
        message.productId = productId
        message.vendorSoftwareId = self.vendorSoftwareId

        self.thMisc.passMessage(message)


    def OnLogin(self, event):
        self.blockLogin.Show(False)


        message, response, exception = self.SplitEventResponse(event)
        if not response:
            if exception:
                self.LogMessages(exception)
                # errmsg = str(exception)
                # wx.MessageBox(errmsg, 'Login Failed')

                errmsg = None
                if isinstance(exception, bfpy.BfServiceError):
                    vendorCheckCodes = ['LOGIN_UNAUTHORIZED', 'INVALID_VENDOR_SOFTWARE_ID']
                    if self.vendorSoftwareId and exception.response.errorCode in vendorCheckCodes:
                        dlg = LoginInfoRegistration(self)
                        retcode = dlg.ShowModal()
                        return
                    else:
                        errmsg = 'Login Error\n\nBetfair Service Message: %s' % exception.response.errorCode

                elif isinstance(exception, bfpy.BfApiError):
                    errmsg = 'Login Error\n\nBetfair Api Message: %s' % exception.response.header.errorCode

                elif isinstance(exception, bfpy.BfNetworkError):
                    if isinstance(exception.errorCode, (list, tuple)):
                        if len(exception.errorCode) > 1:
                            errmsg = 'Login Error\n\nNetwork Error: %s - Code: %d - Reason: %s' \
                                     % (exception.name, exception.errorCode[0], exception.errorCode[1])
                        else:
                            errmsg = 'Login Error\n\nNetwork Error: %s - Reason: %s' % (exception.name, exception.errorCode[0])
                    else:
                        errmsg = 'Login Error\n\nNetwork Error: %s - Reason: %s' % (exception.name, str(exception.errorCode))
                else:
                    errmsg = 'Login Error\n\nReason: %s' % str(exception)

                if errmsg:
                    wx.MessageBox(errmsg, 'Login Failed')
            return

        if message.productId == bfpy.freeApiId:
            # Virtual prices can't be exactly calculated (due to the lack of rateExchange)
            # with the FreeAPI
            self.m_checkBoxVirtualPrices.SetValue(False)
            self.m_checkBoxVirtualPrices.Disable()
            self.m_checkBoxVirtualPrices.Show(False)
            self.virtualPrices = False

        self.postLoginUsernames(response.currency, message.productId)
        self.startThreads()
        self.EnableElements()
        self.LoadSavedMarkets()
        self.ActivateFocusWindows()
        self.postLoginEvents()

        if self.loadMarketsAfterLogin:
            self.GetEvents(bfpy.eventRootId, self.m_treeEvents.GetRootItem())
            self.m_notebookMain.ChangeSelection(1)
            self.m_notebookFavs.ChangeSelection(0)

            # Start fetching all markets
            message = Message(timeout=self.refreshMarketsPeriod)
            self.thAllMarkets.passMessage(message)

            # Start fetching funds
            if self.showFunds:
                message = Message(timeout=self.fundsRefresh)
                self.thAccountFunds.passMessage(message)

            # Start fetching current bets if needed
            if self.curBetsAutoRefresh:
                message = Message(timeout=self.curBetsRefresh)
                self.thCurrentBets.passMessage(message)


    def EnableElements(self):
        self.m_buttonLogin.Disable()
        self.m_comboBoxUsername.Disable()
        self.m_textCtrlPassword.Disable()
        
        self.m_checkboxShowFunds.Enable()
        self.m_bpButtonAus2UK.Enable()
        self.m_bpButtonUK2Aus.Enable()
        self.m_buttonCurrentBets.Enable()
        self.m_buttonCancelAllBets.Enable()

        self.m_buttonTreeEventsReloadAll.Enable()
        self.m_menuItemTreeItemReloadAll.Enable()
