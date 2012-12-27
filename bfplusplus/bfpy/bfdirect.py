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
Definition of direct construction API call and services
and metaclass to install them in an API provider
'''

import copy
import types

import bfapicalls
import bfglobals
import bftypes

class ApiServiceMeta(type):
    '''
    Metaclass for L{ApiService} that install L{ApiCall} and L{ApiDataType}
    as descriptors and values into a dictionary to enable ApiService to
    return the values via member retrieval or with getService and getObject
    '''

    def __new__(cls, name, bases, clsdict):
        '''
        Modifies L{ApiService} class creation

        @type cls: class
        @param cls: the class to be modifies on creation
        @type name: string
        @param name: name of the class
        @type bases: list
        @param bases: list of base classes for cls
        @type clsdict: dict
        @param clsdict: the dictionary of cls
        '''
        for apiCall in clsdict['_ApiCalls']:
            if apiCall.operation not in clsdict:
                clsdict[apiCall.operation] = apiCall
            else:
                apitype = apiCall.apitype[0].upper() + apiCall.apitype[1:]
                clsdict[apiCall.operation + apitype] = apiCall

        clsdict['objects'] = dict()
        for apiType in bftypes.ApiDataTypes:
            if apiType.apitype:
                suffix = apiType.apitype[0].upper() + apiType.apitype[1:]
            else:
                suffix = ''
            clsdict['objects'][apiType.__name__ + suffix] = apiType

        return type.__new__(cls, name, bases, clsdict)


class ApiService(object):
    '''
    Holds L{ApiCall} descriptors and L{ApiDataType} classes to enable
    direct interaction with a Betfair service

    @type _ApiCalls: list
    @cvar _ApiCalls: list of ApiCalls to install

    @type endPointUrl: string
    @ivar endPointUrl: url to the service
    @type transport: L{BfTransport}
    @ivar transport: transport (over http) object
    '''

    __metaclass__ = ApiServiceMeta

    _ApiCalls = [
        # General API - Complete
        bfapicalls.ApiCallGlobal('login'),
        bfapicalls.ApiCallGlobal('logout'),
        bfapicalls.ApiCallGlobal('keepAlive'),

        # Read-Only API - Complete
        bfapicalls.ApiCallGlobal('convertCurrency'),
        bfapicalls.ApiCallGlobal('getActiveEventTypes', arrays='eventTypeItems'),
        bfapicalls.ApiCallGlobal('getAllCurrencies', arrays='currencyItems'),
        bfapicalls.ApiCallGlobal('getAllCurrenciesV2', arrays='currencyItems'),
        bfapicalls.ApiCallGlobal('getAllEventTypes', arrays='eventTypeItems'),
        bfapicalls.ApiCallExchange('getAllMarkets'),
        bfapicalls.ApiCallExchange('getBet', arrays='bet.matches'),
        bfapicalls.ApiCallExchange('getBetHistory'),
        bfapicalls.ApiCallExchange('getBetLite'),
        bfapicalls.ApiCallExchange('getBetMatchesLite', arrays='matchLites'),
        bfapicalls.ApiCallExchange('getCompleteMarketPricesCompressed'),
        bfapicalls.ApiCallExchange('getCurrentBets', arrays='bets'),
        bfapicalls.ApiCallExchange('getCurrentBetsLite', arrays='betLites'),
        bfapicalls.ApiCallExchange('getDetailAvailableMktDepth', arrays='priceItems'),
        bfapicalls.ApiCallGlobal('getEvents', arrays=['eventItems', 'marketItems']),
        bfapicalls.ApiCallExchange('getInPlayMarkets'),
        bfapicalls.ApiCallExchange('getMarket', arrays=['market.runners', 'market.eventHierarchy']),
        bfapicalls.ApiCallExchange('getMarketInfo'),
        bfapicalls.ApiCallExchange('getMarketPrices', arrays=['marketPrices.runnerPrices',
                                                              'marketPrices.runnerPrices.bestPricesToBack',
                                                              'marketPrices.runnerPrices.bestPricesToLay']),
        bfapicalls.ApiCallExchange('getMarketPricesCompressed'),
        bfapicalls.ApiCallExchange('getMarketProfitAndLoss', arrays='annotations'),
        bfapicalls.ApiCallExchange('getMarketTradedVolume', arrays='priceItems'),
        bfapicalls.ApiCallExchange('getMarketTradedVolumeCompressed'),
        bfapicalls.ApiCallExchange('getMUBets', arrays='bets'),
        bfapicalls.ApiCallExchange('getMUBetsLite', arrays='betLites'),
        bfapicalls.ApiCallExchange('getPrivateMarkets', arrays='privateMarkets'),
        bfapicalls.ApiCallExchange('getSilks', arrays=['marketDisplayDetails', 'marketDisplayDetails.racingSilks']),
        bfapicalls.ApiCallExchange('getSilksV2', arrays=['marketDisplayDetails', 'marketDisplayDetails.racingSilks']),

        # Bet Placement API - Complete
        bfapicalls.ApiCallExchange('cancelBets', arrays='betResults'),
        bfapicalls.ApiCallExchange('cancelBetsByMarket', arrays='results'),
        bfapicalls.ApiCallExchange('placeBets', arrays='betResults'),
        bfapicalls.ApiCallExchange('updateBets', arrays='betResults'),

        # Account Management API - Complete
        bfapicalls.ApiCallGlobal('AddPaymentCard'),
        bfapicalls.ApiCallGlobal('DeletePaymentCard'),
        bfapicalls.ApiCallGlobal('DepositFromPaymentCard'),
        bfapicalls.ApiCallGlobal('forgotPassword'),
        bfapicalls.ApiCallExchange('getAccountFunds'),
        bfapicalls.ApiCallExchange('getAccountStatement', arrays='items'),
        bfapicalls.ApiCallGlobal('getPaymentCard', arrays='paymentCardItems'),
        bfapicalls.ApiCallGlobal('getSubscriptionInfo', arrays=['subscriptions', 'subscriptions.services']),
        bfapicalls.ApiCallGlobal('modifyPassword'),
        bfapicalls.ApiCallGlobal('modifyProfile'),
        bfapicalls.ApiCallGlobal('transferFunds'),
        bfapicalls.ApiCallGlobal('retrieveLIMBMessage', arrays='retrieveCardBillingAddressCheckItems'),
        bfapicalls.ApiCallGlobal('selfExclude'),
        bfapicalls.ApiCallGlobal('setChatName'),
        bfapicalls.ApiCallGlobal('submitLIMBMessage'),
        bfapicalls.ApiCallGlobal('updatePaymentCard'),
        bfapicalls.ApiCallGlobal('viewProfile'),
        bfapicalls.ApiCallGlobal('viewProfileV2'),
        bfapicalls.ApiCallGlobal('viewReferAndEarn'),
        bfapicalls.ApiCallGlobal('withdrawToPaymentCard'),

        # Vendor API - Complete
        bfapicalls.ApiCallVendor('createVendorAccessRequest'),
        bfapicalls.ApiCallVendor('cancelVendorAccessRequest'),
        bfapicalls.ApiCallVendor('updateVendorSubscription'),
        bfapicalls.ApiCallVendor('getVendorUsers', arrays='vendorUsers'),
        bfapicalls.ApiCallVendor('getVendorAccessRequests', arrays='vendorAccessRequests'),
        bfapicalls.ApiCallVendor('getSubscriptionInfo'),
        bfapicalls.ApiCallVendor('getVendorInfo', arrays='vendorInfo'),
        ]


    def __init__(self, endPoint, transport):
        '''
        Constructor of ApiService
        
        @type endPoint: int
        @param endPoint: which enpoint will do the call
        @type transport: L{BfTransport}
        @param transport: transport (over http) object
        '''
        self.endPointUrl = bfglobals.EndPointUrls[endPoint]
        self.transport = transport


    def clone(self):
        '''
        Returns an L{ApiService} cloned

        @rtype: L{ApiService}
        @returns: a clone of itself
        '''
        obj = copy.copy(self)
        obj.transport = self.transport.clone()
        return obj


    def getObject(self, name):
        '''
        Returns an L{ApiDataType} by name

        @type name: string
        @param name: the object to be returned

        @rtype: ApiDataType
        @returns: the sought object
        '''
        return self.objects[name]()


    def getService(self, name):
        '''
        Returns an L{ApiCall} by name

        @type name: string
        @param name: the api call to be returned

        @rtype: ApiCall
        @returns: the sought service name
        '''
        return getattr(self, name)
