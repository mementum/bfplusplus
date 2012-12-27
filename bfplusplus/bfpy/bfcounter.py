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
Implementation of a Data Counter/Throttler to implemente Betfair Data Charges
weight counting
'''
from __future__ import with_statement

import threading
import time
import sys

'''
time.clock seems to work find under Windows, keeping wallclock time
but seems to really only report CPU time under Linux/Unix and therefore
is not counting time spent in calls like time.sleep if they have not
been implemented with a CPU approach
'''
if sys.platform == 'win32':
    tclock = time.clock
else:
    tclock = time.time


class DataRequest(object):
    '''
    Basic request information holder

    @ivar tstamp: time when the request was made (from time.clock())
    @type tstamp: float
    @ivar weight: contribution to the data charges count
    @type weight: int
    '''
    
    __slots__ = ['__weakref__', 'tstamp', 'weight']

    def __init__(self, tstamp, weight):
        '''
        Initializes the request data holder

        @param tstamp: time when the request was made (from time.clock())
        @type tstamp: float
        @param weight: contribution to the data charges count
        @type weight: int
        '''
        self.tstamp = tstamp
        self.weight = weight


class DataCounter(object):
    '''
    Implements data count and throttling for a configured maximum number
    of data requests made in a second

    @ivar lock: thread lock controller to enable counter sharing
    @type lok: threading.Lock
    @ivar maxRequests: maximum number of concurrent requests
    @type maxRequests: int
    @ivar timeGuard: extra time to add to blocking time if blocking is needed
    @type timeGuard: float
    @ivar reqs: list of last requests made (purged if needed on next weight addition)
    @type reqs: list
    @ivar weight: current data charges weight (recalculated on next weight addition)
    @type weight: int
    '''

    __slots__ = ['__weakref__', 'lock', 'maxRequests', 'timeGuard', 'reqs', 'weight']

    def __init__(self, maxRequests=20, timeGuard=0.01):
        '''
        Initializes the request data holder

        @param maxRequests: maximum number of concurrent requests
        @type maxRequests: int
        @param timeGuard: extra time to add to blocking time if blocking is needed
        @type timeGuard: float
        '''
        self.lock = threading.Lock()
        self.maxRequests = maxRequests
        self.reqs = list()
        self.weight = 0
        self.timeGuard = timeGuard


    def add(self, weight, maxRequests=-1):
        '''
        Adds a weight to the list, purging the list of requests, recalculating the
        weight and deciding if blocking for an amount of time is needed

        If no weight is given (0) or maxRequests is set to (0) no action is performed

        @param weight: new weight to add to the list
        @type weight: int
        @param maxRequests: override value for maxrequests. -1 (do not override)
        @type maxRequests: int
        '''
        if maxRequests < 0:
            maxRequests = self.maxRequests

        if not maxRequests or not weight:
            return

        with self.lock:
            tnow = tclock()

            # purge the request list of requests older than 1 second
            while self.reqs:
                req = self.reqs[0]
                if tnow - req.tstamp > 1.0:
                    self.reqs.pop(0)
                    self.weight -= req.weight
                else:
                    break

            self.reqs.append(DataRequest(tnow, weight))
            self.weight += weight

            if self.weight > maxRequests:
                # All remaining requests happened within one second
                # see how much has to be waited until we may issue another request
                excess = self.weight - maxRequests

                for req in self.reqs:
                    excess -= req.weight

                    if excess <= 0:
                        throttle = 1.0 - (tnow - req.tstamp)
                        break

                # Execute the throttle with a small guard
                time.sleep(throttle + self.timeGuard)
