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
    def init(self):

        self.mischandler = {
            'login': self.OnLogin, 'getEvents': self.OnGetEvents,
            'getMarket': self.OnGetMarket, 'getAccountFunds': self.OnGetAccountFunds,
            'transferFunds': self.OnTransferFunds, 'getCurrentBets': self.OnGetCurrentBets,
            'getAllMarkets': self.OnGetAllMarkets, 'module': self.OnMessageFromModule,
            'placeBets': self.OnPlaceBets, 'cancelBets': self.OnCancelBets,
            'cancelBetsByMarket': self.OnCancelBetsByMarket,
            'updateBets': self.OnUpdateBets, 'seekUpdates': self.OnSeekUpdates,
            'runnerActionBitmap': self.OnRunnerActionBitmap,
            'runnerActionTradedVolume': self.OnRunnerActionTradedVolume,
            'runnerActionCompletePrices': self.OnRunnerActionCompletePrices,
            }


    def OnMisc(self, event):
        try:
            self.mischandler[event.message.action](event)
        except KeyError:
            # Some actions may go unhandled - 
            pass


    def SplitEventResponse(self, event):
        return (event.message, event.message.response, event.message.exception)


