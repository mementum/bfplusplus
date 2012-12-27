#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of BfPy
#
# BfPy is a Python library to communicate with the Betfair Betting Exchange
# Copyright (C) 2010 Daniel Rodriguez (aka Daniel Rodriksson)
# Copyright (C) 2011 Sensible Odds Ltd.
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/bfpy/
#
# BfPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BfPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BfPy. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
'''
BfPy Timezone classes. Adapted (if needed) from the Python documentation to make
them more generic
'''

from datetime import datetime, timedelta, tzinfo
import time as _time

class LocalTimezone(tzinfo):
    '''
    System specific local timezone.

    As seen in the Python docs (with mods)
    '''
    zero = timedelta(0)
    def __init__(self):
        self.stdOffset = timedelta(seconds=-_time.timezone)
        if _time.daylight:
            self.dstOffset = timedelta(seconds=-_time.altzone)
        else:
            self.dstOffset = self.stdOffset

        self.dstDiff = self.dstOffset - self.stdOffset

    def utcoffset(self, dt):
        '''
        Return the offset to UTC (GMT) for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        return self.dstOffset if self._isdst(dt) else self.stdOffset

    def dst(self, dt):
        '''
        Return the daylight savings offset for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        return self.dstDiff if self._isdst(dt) else LocalTimezone.zero

    def tzname(self, dt):
        '''
        Return the name of this timezone for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        return _time.tzname[self._isdst(dt)]

    def _isdst(self, dt):
        '''
        Private function to find out if the system reports
        to be in DST mode for the given datetime

        @param dt: datetime to see offset against
        @type dt: datetime
        '''
        tt = (dt.year, dt.month, dt.day,
              dt.hour, dt.minute, dt.second,
              dt.weekday(), 0, -1)
        stamp = _time.mktime(tt)
        tt = _time.localtime(stamp)
        return tt.tm_isdst > 0
