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
BfClient object implementation.
'''

from bfapi import BfApi, BfService
import bfclientext 


class BfClient(BfApi):
    '''
    The class defines a higher level interface over the L{BfApi} parent class.

    The intention is to have some services redefine/extend the functionality
    in a intelligent manner.
    
    As an example de redefined "getEvents" unifies getActiveEventTypes and getEvents
    (it is used as such in the Bfplusplus application <http://code.google.com/p/bfplusplus>

    The redefintion is made by means of non-data descriptors in the bfclientext
    module

    @ivar serviceDefs: service definitions with non-data descriptors
    @type clients: list

    The following services are redefined here (see L{BfApi} for the originals):

        - getCurrentBets

          Enables 'MU' as parameter for betStatus, by issuing a call with 'M'
          and a call with 'U' and returning a unified answer

          Default values: betStatus='MU'

        - getEvents:

          Unifies getEvents and getActiveTypeEvents. The results of the second
          are aliased to look like the results of the first

          Default values: eventParentId = -1 (return getActiveTypeEvents)
          
        - placeBets

          Hack to enable re-placement of bets if they fail with an "INVALID_PERSISTENCE"
          given that the results from getEvents do not say if a market will turn
          in-play or not

          This is a hack and may be removed

          Default values: _nonIPRePlace=False

    '''

    __metaclass__ = BfService

    # Methods that override base class non-data descriptors, are implemented
    # as non-data descriptors also (simple override doesn't work)
    _serviceDefs = [
        bfclientext.GetEvents(eventParentId=-1),
        bfclientext.GetCurrentBets(betStatus='MU'),
        bfclientext.PlaceBets(_nonIPRePlace=False),
        ]

    def __init__(self, **kwargs):
        BfApi.__init__(self, **kwargs)
