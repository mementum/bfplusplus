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
BfApi method extensions to be inserted in BfClient
'''

from copy import copy
from operator import attrgetter
import time

from bfapi import BfApi
import bfglobals
from bfservice import ServiceDescriptor


class GetEvents(ServiceDescriptor):
    '''
    Implements a non-data descriptor for BfClient to extend the getEvents
    service method by unifying getActiveEventTypes and getEvents to be able
    to directly recurse downwards the list of events from a fictitious
    eventRootId (-1)
    '''

    def __init__(self, **kwargs):
        '''
        Initializes the non-data descritor by invoking the base class
        L{ServiceDescriptor}

        @param kwargs: keyword arguments to implement default arguments
                       for the method
        @type kwargs: dict
        '''
        ServiceDescriptor.__init__(self, 'getEvents', **kwargs)


    def __call__(self, instance, *args, **kwargs):
        '''
        Returns getActiveEventTypes and getEvents in a single call.
        The events returned by getActiveEventTypes are aliased to look like
        an answer from getEvents

        @param instance: object whose method is being called
        @type instance: object (a L{BfApi} subclass)

        @returns: Betfair API answer
        @rtype: parsed answer
        '''
        callArgs = self.kwargs.copy()
        callArgs.update(**kwargs)
        eventParentId = callArgs.get('eventParentId')

        if eventParentId == bfglobals.eventRootId:
            response = instance.getActiveEventTypes()
            # Alias the .id and .name attributes to those of an event
            for event in response.eventTypeItems:
                event.eventTypeId = event.id
                event.eventId = event.id
                del event.id
                event.eventName = event.name
                del event.name

            # Create the eventItems and marketItems alias
            response.eventItems = response.eventTypeItems
            del response.eventTypeItems
            response.marketItems = list()

            return response

        return BfApi.getEvents(instance, eventParentId=eventParentId)


class GetCurrentBets(ServiceDescriptor):
    '''
    Implements a non-data descriptor for BfClient to extend the getCurrentBets
    service method by allowing betStatus to be MU (return both Matched and
    UnMatched bets in a single call) Betfair does not allow it, which is
    odd.
    '''
    def __init__(self, **kwargs):
        '''
        Initializes the non-data descritor by invoking the base class
        L{ServiceDescriptor}

        @param kwargs: keyword arguments to implement default arguments
                       for the method
        @type kwargs: dict
        '''
        ServiceDescriptor.__init__(self, 'getCurrentBets', **kwargs)


    def __call__(self, instance, *args, **kwargs):
        '''
        Method implementation to allow MU (default also in the call) to be returned

        @param instance: object whose method is being called
        @type instance: object (a L{BfApi} subclass)
        @param args: unnamed args
        @type args: tuple
        @param kwargs: named args
        @type kwargs: dict

        @returns: Betfair API answer
        @rtype: parsed answer
        '''
        currentBetsArgs = self.kwargs.copy()
        currentBetsArgs.update(**kwargs)

        if currentBetsArgs['betStatus'] != 'MU':
            return BfApi.getCurrentBets(instance, *args, **currentBetsArgs)

        currentBetsArgs['betStatus'] = 'M'
        mResponse = BfApi.getCurrentBets(instance, *args, **currentBetsArgs)
        currentBetsArgs['betStatus'] = 'U'
        uResponse = BfApi.getCurrentBets(instance, *args, **currentBetsArgs)

        mResponse.totalRecordCount += uResponse.totalRecordCount
        mResponse.bets.extend(uResponse.bets)

        orderBy = kwargs.get('orderBy', 'NONE')

        if orderBy == 'PLACED_DATE':
            mResponse.bets.sort(key=attrgetter('placedDate', 'betStatus'))
        else:
            # According to the docs the only other combination for M and U is 'NONE'
            # so do a sensible ordering on betId and betStatus
            mResponse.bets.sort(key=attrgetter('betId', 'betStatus'))

        return mResponse
            

class PlaceBets(ServiceDescriptor):
    '''
    Implements a non-data descriptor for BfClient to extend the placeBets
    to re-place a bet if the betPersistence has not been speficied.

    This is a hack to support Bfplusplus, given that the "marketSummary" returned
    by getEvents does not state if a market will turn in-ply or not. A call
    to getAllMarkets is needed to find out.

    This hack will be removed
    '''
    def __init__(self, **kwargs):
        '''
        Initializes the non-data descritor by invoking the base class
        L{ServiceDescriptor}

        @param kwargs: keyword arguments to implement default arguments
                       for the method
        @type kwargs: dict
        '''
        ServiceDescriptor.__init__(self, 'placeBets', **kwargs)

    
    def __call__(self, instance, *args, **kwargs):
        '''
        if the parameter nonIPRePlace is passed to the call with a True
        value, bets not placed due to an "INVALID_PERSISTENCE" error
        will be returned

        @param instance: object whose method is being called
        @type instance: object (a L{BfApi} subclass)
        @param args: unnamed args
        @type args: tuple

        @returns: Betfair API answer
        @rtype: parsed answer
        '''
        placeBetsArgs = self.kwargs.copy()
        placeBetsArgs.update(**kwargs)
        nonIPRePlace = placeBetsArgs.pop('_nonIPRePlace')

        response = BfApi.placeBets(instance, *args, **placeBetsArgs)

        if response.betResults and nonIPRePlace:
            placeBets = placeBetsArgs.get('bets')
            toRePlaceBets = list()
            for i, betResult in enumerate(response.betResults[:]):
                placeBet = placeBets[i]
                if betResult.resultCode == 'INVALID_PERSISTENCE' and placeBet.betPersistenceType == 'IP':
                    # This can be a simple copy because placeBet is made of Simple types
                    # newPlaceBet = deepcopy(placeBet)
                    newPlaceBet = copy(placeBet)
                    newPlaceBet.betPersistenceType = 'NONE'
                    toRePlaceBets.append(newPlaceBet)
                    response.betResults.pop(i)

            if toRePlaceBets:
                placeBetsArgs['bets'] = toRePlaceBets
                rePlaceResponse = BfApi.placeBets(instance, *args, **placeBetsArgs)
                response.betResults.extend(rePlaceResponse.betResults)

        return response
