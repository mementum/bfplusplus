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

from base64 import b64encode
import sys

import wx

import bfpy
from util import AesHelper

if True:
    def InitConstants(self):
        self.config = wx.Config('Bfplusplus', 'Bfplusplus');
        self.config.SetRecordDefaults(True)

        self.aes = AesHelper('bfplusplus++bfplusplus++')

        # Do version checking
        lastVersion = float(self.config.Read('version', '0.30'))
        self.config.Write('version', self.version)

        if lastVersion < 0.31:
            # Convert usernames to encrypted forms
            usernames = self.config.Read('Usernames', '[]')
            usernames = eval(usernames)

            if usernames:
                usernames = [b64encode(self.aes.encrypt(username)) for username in usernames]
                self.config.Write('Usernames', str(usernames))

            username = self.config.Read('Username', '')
            if username:
                username = b64encode(self.aes.encrypt(username))
                self.config.Write('Username', username)

        if lastVersion < 0.38:
            try:
                self.config.DeleteEntry('Single Click Stakes Index', False)
                self.config.DeleteEntry('Single Click Stakes', False)
            except:
                pass

        # Needed for some other module inits
        winDC = wx.ClientDC(self)
        self.avgCharWidth = winDC.GetCharWidth()

        # Regular constants
        self.annSep = {'O': '', 'A': '/', 'MW': '/'}
        self.mktTyp = {'O': 'Odds', 'A': 'Asian', 'R': 'Range', 'L': 'Line'}

        self.toBool = {'True': True, 'False': False}

        self.persistenceEnum = {True: 'IP', False: 'NONE'}
        self.persistenceType = {'IP': True, 'NONE': False}
        self.persistenceTypeStr = {'IP': 'Yes', 'NONE': 'No'}

        self.betTypeLegend = {'L': 'Lay', 'B': 'Back'}

        self.betStatusLegend = {'M': 'Matched', 'U': 'Unmatched'}

        self.backLegend = {'O': 'Back', 'A': 'Back', 'R': 'Sell', 'L': 'Sell'}
        self.layLegend = {'O': 'Lay', 'A': 'Lay', 'R': 'Buy', 'L': 'Buy'}

        self.exchangeName = {bfpy.ExchangeUK: 'UK', bfpy.ExchangeAus: 'Aus'}

        self.monthNames = ('January', 'February', 'March', 'April',
                           'May', 'June', 'July', 'August',
                           'September', 'October', 'November', 'December')
        self.monthShortNames = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        self.weekdayNames = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                             'Friday', 'Saturday', 'Sunday')
        self.weekdayShortNames = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
