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

class Funds(object):

    def __init__(self):
        self.wallets = dict()
        self.updateGlobal()


    def updateGlobal(self):
        self.availBalance = 0.0
        self.exposure = 0.0

        for wallet in self.wallets.itervalues():
            self.availBalance += wallet.availBalance
            self.exposure += wallet.exposure


    def updateWallet(self, exchangeId, accountFunds):
        self.wallets[exchangeId] = accountFunds
        self.updateGlobal()


    def reset(self):
        self.wallets.clear()
        self.updateGlobal()
