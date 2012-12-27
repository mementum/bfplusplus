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
from bfobj import Funds
from util import Message

if True:
    def init(self):
        self.funds = Funds()

        self.fundsRefresh = self.config.ReadInt('Funds Refresh', 5)
        self.config.WriteInt('Funds Refresh', self.fundsRefresh)

        self.showFunds = self.config.ReadBool('Funds Show', False)
        self.config.WriteBool('Funds Show', self.showFunds)
        self.m_checkboxShowFunds.SetValue(self.showFunds)

        if self.showFunds:
            self.m_buttonReloadFunds.Enable()


    def OnCheckBoxShowFunds(self, event):
        event.Skip()
        self.VisualGetAccountFunds()


    def VisualGetAccountFunds(self):
        self.showFunds = self.m_checkboxShowFunds.GetValue()
        self.config.WriteBool('Funds Show', self.showFunds)

        if self.showFunds:
            self.m_buttonReloadFunds.Enable()
            self.LoadFunds()
            # self.DisplayFunds()
        else:
            message = Message(timeout=0)
            self.thAccountFunds.passMessage(message)
            self.m_staticTextFundsTotal.SetLabel('')
            self.m_staticTextFundsUk.SetLabel('')
            self.m_staticTextFundsAus.SetLabel('')
            self.m_buttonReloadFunds.Disable()


    def OnButtonClickReloadFunds(self, event):
        event.Skip()
        self.LoadFunds()


    def LoadFunds(self):
        self.funds.reset()
        message = Message(timeout=self.fundsRefresh)
        self.thAccountFunds.passMessage(message)
        # self.GetAccountFunds(exchangeId=bfpy.ExchangeUK)
        # self.GetAccountFunds(exchangeId=bfpy.ExchangeAus)
        self.m_staticTextFundsTotal.SetLabel('-- Loading --')
        self.m_staticTextFundsUk.SetLabel('-- Loading --')
        self.m_staticTextFundsAus.SetLabel('-- Loading --')


    def GetAccountFunds(self, exchangeId, modId=None):
        message = Message(action='getAccountFunds', exchangeId=exchangeId, modId=modId)
	self.thMisc.passMessage(message)


    def OnGetAccountFunds(self, event):
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessages(exception)
                if message.exchangeId == bfpy.ExchangeUK:
                    staticText = self.m_staticTextFundsUk
                elif message.exchangeId == bfpy.ExchangeAus:
                    staticText = self.m_staticTextFundsAus
                if hasattr(message, 'modId') and message.modId is not None:
                    staticText.SetLabel('--- ---')
            return

        if hasattr(message, 'modId') and message.modId:
            if message.modId in self.bfModules:
                # If the module is still active notify
                response.exchangeId = message.exchangeId
                self.bfModules[message.modId].onGetAccountFunds(response)

            # We don't want the display updated by the modules
            return

        if not self.showFunds:
            # Skip delayed messages
            return

        self.funds.updateWallet(message.exchangeId, response)
        self.DisplayFunds()


    def DisplayFunds(self):
        self.m_staticTextFundsTotal.SetLabel('%.2f (%.2f)' % \
                                           (self.funds.availBalance, self.funds.exposure))

        if bfpy.ExchangeUK in self.funds.wallets:
            wallet = self.funds.wallets[bfpy.ExchangeUK]
            staticText = self.m_staticTextFundsUk
            staticText.SetLabel('%.2f (%.2f)' % (wallet.availBalance, wallet.exposure))

        if bfpy.ExchangeAus in self.funds.wallets:
            wallet = self.funds.wallets[bfpy.ExchangeAus]
            staticText = self.m_staticTextFundsAus
            staticText.SetLabel('%.2f (%.2f)' % (wallet.availBalance, wallet.exposure))


    def TransferFunds(self, sourceWalletId, targetWalletId, amount):
        message = Message(action='transferFunds', sourceWalletId=sourceWalletId, \
                                  targetWalletId=targetWalletId, amount=amount)
	self.thMisc.passMessage(message)

        self.LogMessages('Funds Transfer of %.2f %s from %s wallet to %s wallet' %
                         (message.amount,
                          self.currency,
                          self.exchangeName[message.sourceWalletId],
                          self.exchangeName[message.targetWalletId]))


    def OnTransferFunds(self, event):
        self.m_bpButtonAus2UK.Enable()
        self.m_bpButtonUK2Aus.Enable()
        message, response, exception = self.SplitEventResponse(event)

        if not response:
            if exception:
                self.LogMessagesError('Funds transfer of %.2f %s from %s wallet to %s wallet appears to have failed. Please check the wallets' %
                                      (message.amount,
                                       self.currency,
                                       self.exchangeName[message.sourceWalletId],
                                       self.exchangeName[message.targetWalletId]))
                self.LogMessages(exception)
            return

        self.LogMessages('Funds transfer of %.2f %s from %s wallet to %s wallet completed successfully' %
                         (message.amount,
                          self.currency,
                          self.exchangeName[message.sourceWalletId],
                          self.exchangeName[message.targetWalletId]))
        
        self.VisualGetAccountFunds()


    def OnButtonClickUK2Aus(self, event):
        try:
            amount = float(self.m_textCtrlTransferFunds.GetValue())
        except:
            wx.MessageBox( 'Invalid Amount to Transfer', "Transfer Funds")
            return

        sourceWalletId = bfpy.ExchangeUK
        targetWalletId = bfpy.ExchangeAus

        self.m_bpButtonAus2UK.Disable()
        self.m_bpButtonUK2Aus.Disable()

        self.TransferFunds(sourceWalletId, targetWalletId, amount)

    def OnButtonClickAus2UK(self, event):
        try:
            amount = float(self.m_textCtrlTransferFunds.GetValue())
        except:
            wx.MessageBox( 'Invalid Amount to Transfer', "Transfer Funds")
            return

        sourceWalletId = bfpy.ExchangeAus
        targetWalletId = bfpy.ExchangeUK

        self.m_bpButtonAus2UK.Disable()
        self.m_bpButtonUK2Aus.Disable()

        self.TransferFunds(sourceWalletId, targetWalletId, amount)

