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
BfApi object implementation.
'''

from copy import copy
from datetime import datetime

import bfglobals
import bfcounter
import bfdirect
import bferror
from bfservice import GlobalServiceDef, ExchangeServiceDef, VendorServiceDef, GlobalObject, ExchangeObject
from bfprocessors import *
import bftransport
from bfutil import SharedData


class BfService(type):
    '''
    Metaclass for L{BfApi} to initialize the non-data descriptor based
    methods on instantiation
    '''

    def __new__(mcs, name, bases, clsdict):
        '''
        On L{BfApi} instantiation the service definitions present in
        the class variable I{_serviceDefs} are added to the dictionary of the
        instance to generate non-data descriptor based methods
        that allow the invocation of the Betfair API Services
        '''
        if '_serviceDefs' in clsdict:
            for serviceDef in clsdict['_serviceDefs']:
                clsdict[serviceDef.methodName] = serviceDef

        if '_sharedArgs' in clsdict:
            for sharedArg in clsdict['_sharedArgs']:
                clsdict[sharedArg.name] = sharedArg

        return type.__new__(mcs, name, bases, clsdict)
    

class BfApi(object):
    '''
    The class implements a unified communication interface with the Betfair API Services
    EndPoints (Global, ExchangeUK, ExchangeAus)

    This is done by defining the the services and object retrieval methods by means of
    non-data descriptors. The descriptors are added to the class by the metaclass {BfService}

    The class can be configured to avoid any pre/post-processing of the requests and answers
    by changing the module L{preProcess} and L{postProcess} variables or passing them as
    named arguments to the constructor

    @type preProcess: bool
    @ivar preProcess: whether service requests will undergo pre-processing
    @type preProcess: bool
    @ivar postProcess: whether service requests will undergo post-processing
    @type postProcess: bool
    @ivar maxRequests: maximum number of requests to issue to Bf in 1 second
                       (20 is maximum before data charges kick-in)
                       maxRequests = 0 to unlimit the number of requests
    @type maxRequests: int
    @ivar transport: a reference to the L{BfTransport} used to communicate (HTTP)
                     with the Betfair servers
    @type transport: L{BfTransport}

    @ivar _serviceDefs: service definitions with non-data descriptors
    @type _serviceDefs: list

    @ivar _sharedData: shared variables (amongst clones) definition
    @type _serviceDefs: list

    The description below states if a service diverts from the standard
    behaviour and what default values have may be assigned to some variables
    to ease the usage of the services.

    The Betfair API Documentation has to be checked to call those services.

    To call a service, pass the name of the fields the service request object
    has in the Betfair docs, as named parameters. If a service request needs a
    "username" parameters, simply: service(username=myusername)

    For Exchange services, pass the exchangeId as the first parameter. It must
    be unnamed. The reason is "consistency". All Exchange services will always
    have the exchangeId as the first parameter

    The following services are defined:

        - login
          Default values:
          productId=82, vendorSoftwareId=0, ipAddress='0', locationId=0

          If a sucessfull login has been achieved, calling the function with no
          parameters will perform a re-login

        - logout
        - keepAlive

        - convertCurrency
        - getActiveEventTypes
        - getAllCurrencies
        - getAllCurrenciesV2
        - getAllEventTypes
        - getAllMarkets
        - getBet
        - getBetHistory
          Default values:
          detailed=False, orderBy='BET_ID', eventTypesId=None,
          marketId=0, marketTypesIncluded=['A', 'L', 'O', 'R'],
          startRecord=0, recordCount=0,
          placedDateFrom=now() - 1 day, placedDateTo=now(), 

        - getBetLite
        - getBetMatchesLite
        - getCompleteMarketPricesCompressed
        - getCurrentBets
          Default values:
          detailed=False, orderBy='NONE',
          marketId=0, recordCount=0,
          startRecord=0, noTotalRecordCount=True

        - getCurrentBetsLite
          Default values:
          detailed=False, orderBy='NONE',
          marketId=0, recordCount=1000,
          startRecord=0, noTotalRecordCount=True

          Unlike getCurrentBets recordCount=0 does not return all
          current bets

        - getDetailAvailableMarketDepth
          Default values:
          asianLineId=0
          
        - getEvents
        - getMarket:
          Default values: includeCouponLinks=False

        - getInPlayMarkets  
        - getMarketInfo
        - getMarketPrices
        - getMarketPricesCompressed

        - getMarketProfitAndLoss
          This function is preprocessed to try avoid an error if the user
          passes a "marketId" parameter, given the obvious typo made when
          the service was created at Betfair: it requires a marketID parameter.

          Default values:
          includeBspBets=False,
          includeSettledBets=False, netOfCommission=False,

        - getMarketTradedVolume
          Default values:
          asianLineId=0

        - getMarketTradedVolumeCompressed

        - getMUBets:
          Default values:
          betStatus='MU', excludeLastSecond=False,
          matchedSince=datetime(2000, 01, 01, 00, 00, 00),
          orderBy='BET_ID', recordCount=200,
          sortOrder='ASC', startRecord=0

        - getMUBetsLite:
          Default values:
          betStatus='MU', excludeLastSecond=False,
          matchedSince=datetime(2000, 01, 01, 00, 00, 00),
          orderBy='BET_ID', recordCount=200,
          sortOrder='ASC', startRecord=0

        - getPrivateMarkets  
          Default values:
          marketType='O'

        - getSilks
        - getsilksV2

        - cancelBets
        - cancelBetsByMarket
        - placeBets
        - updateBets

        - addPaymentCard
          Default values:
          cardStatus='UNLOCKED'
          itemsIncluded='EXCHANGE', startRecord=0, recordCount=1000
          startDate=datetime.now() - timedelta(days=1), endDate=datetime.now()),
        - deletePaymentCard  
        - depositFromPaymentCard
        - forgotPassword,
        - getAccountFunds
        - getAccountStatement
          Default values:
          itemsIncluded='EXCHANGE',
          startRecord=0, recordCount=0,
          ignoreAutoTransfers=True,

        - getSubscriptionInfo
        - modifyPassword
        - modifyProfile
        - retrieveLIMBMessage
        - selfExclude
        - setChatName
        - submitLIMBMessage
        - transferFunds
        - updatePaymentCard
        - viewProfile
        - viewProfileV2
        - viewReferAndEarn
        - withdrawToPaymentCard

        - createVendorAccessRequest,
        - cancelVendorAccessRequest,
        - updateVendorSubscription,
          requestName='VendorSubscriptionReq' (non standard definition by Betfair)
          Default parameters:
          username = '' (internal Betfair use, but cannot be set to null)
        - getVendorUsers
          Default parameters:
          usernameSearchModifier='CONTAINS', customFieldSearchModifier='CONTAINS', status='ACTIVE'
        - getVendorAccessRequests
          Default parameters:
          status = ACTIVE
        - getSubscriptionInfo
          Default parameters:
          username = '' (internal Betfair use, but cannot be set to null)
        - getVendorInfo
    '''

    __metaclass__ = BfService

    _sharedArgs = [
        SharedData('username'), SharedData('password'),
        SharedData('productId'), SharedData('vendorSoftwareId'),
        SharedData('currency'), SharedData('rateGBP')
        ]


    def __init__(self,
                 preProcess=bfglobals.preProcess,
                 postProcess=bfglobals.postProcess,
                 maxRequests=20,
                 separateCounters=None,
                 **kwargs):
        '''
        Initializes the processing options, transport and service apis

        @param preProcess: whether service requests will undergo pre-processing
        @type preProcess: bool
        @param postProcess: whether service requests will undergo post-processing
        @type postProcess: bool
        @param maxRequests: maximum number of requests to issue to Bf in 1 second (20 is maximum before data charges)
                            maxRequests = 0 to unlimit the number of requests
        @type maxRequests: int
        '''
        self.preProcess = preProcess
        self.postProcess = postProcess
        self.maxRequests = maxRequests
        self.dataCounter = dict()

        self.separateCounters = separateCounters if separateCounters is not None else bfglobals.separateCounters
        if self.separateCounters:
            for endPoint in bfglobals.EndPoints:
                self.dataCounter[endPoint] = bfcounter.DataCounter(maxRequests)
        else:
            self.dataCounter[0] = bfcounter.DataCounter(maxRequests)

        self.transport = bftransport.BfTransport()
        if 'proxydict' in kwargs:
            self.transport.setproxy(kwargs['proxydict'])

        self.transport.setuseragent(bfglobals.libstring)

        self.apiServices = dict()
        for endPoint in bfglobals.EndPoints:
            self.apiServices[endPoint] = bfdirect.ApiService(endPoint=endPoint, transport=self.transport.clone())


    def clone(self):
        '''
        Returns smartly cloned object.

        All objects are copied, then clients are also "cloned" themselves and
        the sessionToken is ended

        @return: a clone of itself
        @rtype: L{BfApi}
        '''
        obj = copy(self)

        for endPoint, service in self.apiServices.iteritems():
            obj.apiServices[endPoint] = service.clone()

        obj.sessionToken = ''

        # Force clone to use this object values as a reference
        for sharedArg in self._sharedArgs:
            getattr(self.__class__, sharedArg.name)(self, obj)

        return obj


    def getService(self, endPoint, serviceName):
        '''
        Returns a service from an endPoint

        @param endPoint: client to retrieve the service from
        @type endPoint: int
        @param serviceName: name of the service to be retrieved
        @type serviceName: str

        @return: a service to be invoked
        @rtype: directapi method
        '''
        return self.apiServices[endPoint].getService(serviceName)


    def getObject(self, endPoint, objectName, apiHeader=False):
        '''
        Returns an object from an endPoint

        @param endPoint: client to retrieve the service from
        @type endPoint: int
        @param objectName: name of the object to be retrieved
        @type objectName: str
        @param apiHeader: whether to append an APIRequestHeader to the object
        @type apiHeader: bool

        @return: the requested object and whether the object is fetched from the DirectApi
        @rtype: DirectApi method
        '''
        obj = self.apiServices[endPoint].getObject(objectName)
        if apiHeader:
            obj.header = self.apiServices[endPoint].getObject('APIRequestHeader')
            obj.header.clientStamp = 0
            obj.header.sessionToken = self.sessionToken
        return obj


    def getRequest(self, endPoint, requestName, apiHeader=True): 
        '''
        All methods pass a request object to services. Because login does
        not carry a header, we need to know if the header has to be added
        retrieves the header object

        @param endPoint: client to retrieve the service from
        @type endPoint: int
        @param requestName: name of the object to be retrieved
        @type requestName: str
        @param apiHeader: whether to append an APIRequestHeader to the object
        @type apiHeader: bool

        @return: the request object
        @rtype: DirectAPI type
        '''
        return self.getObject(endPoint, requestName, apiHeader)


    def addDataWeight(self, endPoint, weight):
        '''
        Adds the weight to the counter corresponding to the endPoint

        @param endPoint: which endPoint to add weight to
        @type endPoint: int
        @param weight: weight of the call to come
        @type weight: int
        '''
        if self.separateCounters:
            self.dataCounter[endPoint].add(weight, self.maxRequests)
        else:
            self.dataCounter[0].add(weight, self.maxRequests)


    def invoke(self, methodName, service, request, skipErrorCodes):
        '''
        Invokes a service with a given request and with a list of errors
        that do not generate exceptions if returned

        @param methodName: method name that has been used to invoke
        @type methodName: str
        @param service: name of the object to be retrieved
        @type service: method to invoke
        @param skipErrorCodes: error codes that will not generate exceptions
        @type skipErrorCodes: list

        @return: the response object processed
        @rtype: object generated decoding the answer

        @raise BfNetworkError: on network errors
        @raise BfHttpError: if the server does not answer with 200 OK
        @raise BfHtmlError: if the server answered with 200 OK but the
                            XML answer was not found in place (Hotel Proxy example)
        @raise BfApiError: on specific API errors
        @raise BfServiceError: on service errors (unless specified in skipErrorCodes)
        @raise BfPythonError: on other errors (original exception is saved)
        '''
        try:
            response = service(request)
        except bftransport.BfTransportSocketError, e:
            # raise bferror.BfNetworkError(methodName, e.args[0], str(e.args[0]), e.args[0].args)
            raise bferror.BfNetworkError(methodName, e, str(e), e.args)
        except bftransport.BfTransportHttpError, e:
            raise bferror.BfHttpError(methodName, e, str(e), e.args)
        except bftransport.BfTransportHtmlError, e:
            raise bferror.BfHtmlError(methodName, e, str(e), e.args)
        except Exception, e:
            if bfglobals.catchAllExceptions:
                # Catch all - to ensure a consistent error reporting from the library
                raise bferror.BfPythonError(methodName, e, str(e), e.args)

        # Analyze API errorCodes
        if response.header.errorCode != 'OK':
            raise bferror.BfApiError(methodName, response, str(response), response.header.errorCode)

        # Analyze Service errorCodes - keepAlive (at least) has no "errorCode" field
        if hasattr(response, 'errorCode'):
            if response.errorCode != 'OK' and response.errorCode not in skipErrorCodes:
                raise bferror.BfServiceError(methodName, response, str(response), response.errorCode)

        # Save the latest session token
        self.sessionToken = response.header.sessionToken

        return response


    class MinStake(object):
        '''
        Placeholder class for minimum bets if the getAllCurrencies family cannot be used

        @ivar minimumStake: Minimum Stake for regular markets
        @type minimumstake: float
        @ivar minimumRangeStake: Minimum Stake for Range markets
        @type minimumRangestake: float
        @ivar minimumBSPLayLiability: Minimum lay stake for BSP markets
        @type minimumBSPLayLiability: float
        '''

        def __init__(self, minimumStake, minimumRangeStake, minimumBSPLayLiability):
            '''
            Init the object instance variables with the provided values
            '''
            self.rateGBP = None # Unknown unless full API is used
            self.minimumStake = minimumStake
            self.minimumRangeStake = minimumRangeStake
            self.minimumBSPLayLiability = minimumBSPLayLiability

    MinBets = {
        'AUD': MinStake(5.0, 3.0, 30.0),
        'CAD': MinStake(6.0, 3.0, 30.0),
        'DKK': MinStake(30.0, 15.0, 150.0),
        'EUR': MinStake(2.0, 2.0, 20.0),
        'HKD': MinStake(25.0, 15.0, 125.0),
        'NOK': MinStake(30.0, 15.0, 150.0),
        'SGD': MinStake(6.0, 1.0, 30.0),
        'SEK': MinStake(30.0, 15.0, 150.0),
        'GBP': MinStake(2.0, 1.0, 10.0),
        'USD': MinStake(4.0, 2.0, 20.0),
        }

    @staticmethod
    def getMinStakes(currency, which=None):
        '''
        Returns the minimum stakes for standard bets, range and BSP liability

        Useful for Free API applications that cannot call getAllCurrencies(V2)

        @param currency: the currency for which the minimum stakes are sought
        @type currency: str (3 letter code)
        @param which: indicates if a specific stake should be returned
        @type which: str

        @returns: the minimum stakes (minimumStake, minimumRangeStake, minimumBSPLayLiability
        @rtype: L{MinStake}
        '''
        minBets = BfApi.MinBets[currency]
        if not which:
            return minBets

        return getattr(minBets, which)


    _serviceDefs = [
        # ######################
        # API Object Retrieval
        # ######################
        GlobalObject('BFEvent', eventId=-1, eventName=''),
        ExchangeObject('Market'),
        ExchangeObject('Runner'),
        ExchangeObject('MarketPrices'),
        ExchangeObject('RunnerPrices'),
        ExchangeObject('Price'),
        ExchangeObject('PlaceBets', betCategoryType='E', bspLiability=0.0),
        ExchangeObject('CancelBets'),
        ExchangeObject('UpdateBets'),
        
        # ######################
        # General API Services
        # ######################
        GlobalServiceDef('login', apiHeader=False, preProc=[PreProcLogin()], postProc=[ProcLogin()],
                         productId=bfglobals.freeApiId, vendorSoftwareId=0, ipAddress='0', locationId=0),
        GlobalServiceDef('logout'),
        GlobalServiceDef('keepAlive'),

        # ######################
        # Read-Only API Services
        # ######################
        GlobalServiceDef('convertCurrency'),
        GlobalServiceDef('getActiveEventTypes', requestName='GetEventTypesReq', skipErrorCodes=['NO_RESULTS']),
        GlobalServiceDef('getAllCurrencies', requestName='GetCurrenciesReq'),
        GlobalServiceDef('getAllCurrenciesV2', requestName='GetCurrenciesV2Req', postProc=[ProcGetAllCurrenciesV2()]),
        GlobalServiceDef('getAllEventTypes', requestName='GetEventTypesReq', skipErrorCodes=['NO_RESULTS']),
        ExchangeServiceDef('getAllMarkets', postProc=[ProcAllMarkets()]),
        ExchangeServiceDef('getBet', skipErrorCodes=['NO_RESULTS'], weight=1),
        ExchangeServiceDef('getBetHistory', skipErrorCodes=['NO_RESULTS'], preProc=[PreBetHistory()], weight=-1,
                           marketId=0, detailed=False, marketTypesIncluded=['A', 'L', 'O', 'R'],
                           recordCount=100, sortBetsBy='BET_ID', startRecord=0),
        ExchangeServiceDef('getBetLite', skipErrorCodes=['NO_RESULTS'], weight=1),
        ExchangeServiceDef('getBetMatchesLite', skipErrorCodes=['NO_RESULTS'], weight=1),
        ExchangeServiceDef('getCompleteMarketPricesCompressed',
                           skipErrorCodes=['EVENT_CLOSED', 'EVENT_SUSPENDED', 'EVENT_INACTIVE'],
                           preProc=[PreCompleteMarketPricesCompressed()],
                           postProc=[ProcMarketPricesCompressed(True)], weight=1),
        ExchangeServiceDef('getCurrentBets', skipErrorCodes=['NO_RESULTS'], postProc=[ProcCurrentBets()],
                           weight=-1,
                           detailed=False, orderBy='NONE', marketId=0, recordCount=0, startRecord=0, noTotalRecordCount=True),
        ExchangeServiceDef('getCurrentBetsLite', skipErrorCodes=['NO_RESULTS'], weight=-1,
                           orderBy='NONE', marketId=0, recordCount=1000, startRecord=0, noTotalRecordCount=True),
        ExchangeServiceDef('getDetailAvailableMarketDepth', serviceName='getDetailAvailableMktDepth',
                           requestName='GetDetailedAvailableMktDepthReq', skipErrorCodes=['NO_RESULTS', 'SUSPENDED_MARKET'],
                           weight=1, asianLineId=0),
        GlobalServiceDef('getEvents', skipErrorCodes=['NO_RESULTS']),
        ExchangeServiceDef('getInPlayMarkets', postProc=[ProcAllMarkets()]),
        ExchangeServiceDef('getMarket', postProc=[ProcMarket()], includeCouponLinks=False),
        ExchangeServiceDef('getMarketInfo'),
        ExchangeServiceDef('getMarketPrices', postProc=[ProcMarketPrices()], weight=1),
        ExchangeServiceDef('getMarketPricesCompressed', postProc=[ProcMarketPricesCompressed()], weight=1),
        ExchangeServiceDef('getMarketTradedVolume', skipErrorCodes=['NO_RESULTS', 'MARKET_CLOSED'], weight=1, asianLineId=0),
        ExchangeServiceDef('getMarketTradedVolumeCompressed', skipErrorCodes=['EVENT_SUSPENDED', 'EVENT_CLOSED'],
                           preProc=[PreMarketTradedVolumeCompressed()],
                           postProc=[ProcMarketTradedVolumeCompressed()], weight=1),
        ExchangeServiceDef('getMUBets', skipErrorCodes=['NO_RESULTS'], weight=-1,
                           betStatus='MU', excludeLastSecond=False,
                           matchedSince=datetime(2000, 01, 01, 00, 00, 00),
                           orderBy='BET_ID', recordCount=200, sortOrder='ASC', startRecord=0),
        ExchangeServiceDef('getMUBetsLite', skipErrorCodes=['NO_RESULTS'], weight=-1,
                           betStatus='MU', excludeLastSecond=False, matchedSince=datetime(2000, 01, 01, 00, 00, 00),
                           orderBy='BET_ID', recordCount=200, sortOrder='ASC', startRecord=0),
        ExchangeServiceDef('getMarketProfitAndLoss', skipErrorCodes=['MARKET_CLOSED', 'INVALID_MARKET'],
                           preProc=[PreProcMarketProfitAndLoss()], postProc=[ProcMarketProfitAndLoss()], weight=1,
                           includeBspBets=False, includeSettledBets=False, netOfCommission=False),
        ExchangeServiceDef('getPrivateMarkets', skipErrorCodes=['NO_RESULTS'], preProc=[PreProcPrivateMarkets()], marketType='O'),
        ExchangeServiceDef('getSilks'),
        ExchangeServiceDef('getSilksV2'),

        # ######################,
        # Bet Placement API Services
        # ######################
        ExchangeServiceDef('cancelBets'),
        ExchangeServiceDef('cancelBetsByMarket'),
        ExchangeServiceDef('placeBets'),
        ExchangeServiceDef('updateBets'),

        # ######################
        # Acount Management API Services
        # ######################
        GlobalServiceDef('addPaymentCard', cardStatus='UNLOCKED'),
        GlobalServiceDef('deletePaymentCard'),
        GlobalServiceDef('depositFromPaymentCard'),
        GlobalServiceDef('forgotPassword'),
        ExchangeServiceDef('getAccountFunds'),
        ExchangeServiceDef('getAccountStatement', skipErrorCodes=['NO_RESULTS'], preProc=[PreAccountStatement()],
                           itemsIncluded='EXCHANGE', startRecord=0, recordCount=1, ignoreAutoTransfers=True),
        GlobalServiceDef('getPaymentCard'),
        GlobalServiceDef('getSubscriptionInfo'),
        GlobalServiceDef('modifyPassword'),
        GlobalServiceDef('modifyProfile'),
        GlobalServiceDef('retrieveLIMBMessage'),
        GlobalServiceDef('selfExclude'),
        GlobalServiceDef('setChatName'),
        GlobalServiceDef('submitLIMBMessage'),
        GlobalServiceDef('transferFunds'),
        GlobalServiceDef('updatePaymentCard'),
        GlobalServiceDef('viewProfile'),
        GlobalServiceDef('viewProfileV2'),
        GlobalServiceDef('viewReferAndEarn', skipErrorCodes=['NO_RESULTS']),
        GlobalServiceDef('withdrawToPaymentCard'),

        # ######################
        # Vendor API Services
        # ######################
        VendorServiceDef('createVendorAccessRequest'),
        VendorServiceDef('cancelVendorAccessRequest'),
        VendorServiceDef('updateVendorSubscription', requestName='VendorSubscriptionReq', username=''),
        VendorServiceDef('getVendorUsers', usernameSearchModifier='CONTAINS', customFieldSearchModifier='CONTAINS', status='ACTIVE'),
        VendorServiceDef('getVendorAccessRequests', status='ACTIVE'),
        VendorServiceDef('getSubscriptionInfoVendor', requestName='GetSubscriptionInfoReqVendor', username=''),
        VendorServiceDef('getVendorInfo'),
        ]
