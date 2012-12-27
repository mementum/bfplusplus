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
Classes for definition and management of API types
'''

import datetime
import types

from bftimezone import LocalTimezone


class ApiParam(object):
    '''
    Non-data descriptor class to be installed in a L{ApiDataType}

    @type name: string
    @ivar name: public name of the "param"
    @type nullable: bool
    @ivar nullable: if the parameter can be nullified upon sending the request
    @type defvalue: any
    @ivar defvalue: if not None the default value will be applied if no other
                    has been later specified
    @type listtype: string
    @ivar listtype: if the para specifies a list type, this defines the 'soap' type
    @type patternList: string
    @ivar patternList: pre-computed listtype pattern for element list substitution
    @type patternFill: string
    @ivar patternFill: pre-computed patter for substitution
    @type patternNull: string
    @ivar patternNull: precomputed pattern for substitution if the value is nullified
    @type instanceval: dict
    @ivar instanceval: holds the assigned value to the param on a per instance basis
    @type instanceCache: dict
    @ivar instanceCache: holds the generated method to be called by holding instances
    '''
    def __init__(self, name, nullable=False, xsd=True, value=None, listtype=None):
        '''
        Initializes the descriptor precomputing the needed patterns

        @type name: string
        @param name: public name of the "param"
        @type nullable: bool
        @param nullable: if the parameter can be nullified upon sending the request
        @type xsd: bool
        @param xsd: if the type is xsd standard or not (to be used with nullable)
        @type value: any
        @param value: to be stored as defvalue
        @type listtype: string
        @param listtype: if the para specifies a list type, this defines the 'soap' type
        '''
        self.instanceCache = dict()
        self.instanceval = dict()

        self.name = name
        self.nullable = nullable
        self.defvalue = value
        self.xsd = xsd
        self.listtype = listtype

        self.patternFill = '<%s>%%s</%s>' % (name, name)

        if self.nullable:
            self.patternNull = '<%s' % name
            if xsd:
                self.patternNull += ' xsi:nil="true"'
            self.patternNull += '/>'

        self.patternList = '<ns2:%s>%%s</ns2:%s>' % (self.listtype, self.listtype)


    def __set__(self, instance, value):
        '''
        Stores the value passed to later generate the exception

        @type instance: instance
        @param instance: instance that is calling the descriptor
        @type value: any
        @param value: value to be stored for substitution in pattern
        '''
        self.instanceval[instance] = value


    def __get__(self, instance, owner=None):
        '''
        Non-data descriptor implementation.

        If invoked at class level it returns and unbound method pointing that forces the invocation
        of __call__. The invocation has to be done with an instance

        If invoked from an instance it returns the value that is currently stored for such instance

        @type instance: instance of class
        @param instance: instance that calls the descriptor
        @type owner: class
        @param owner: the class that holds the descriptor
        '''
        if instance is None:
            return self.instanceCache.setdefault(owner, types.MethodType(self, None, owner))
        return self.instanceval.get(instance, self.defvalue)


    def __call__(self, instance):
        '''
        Returns the pattern for this param

        @type instance: instance
        @param instance: instance that is calling the descriptor

        @return: textual representation of the defined ApiParam type
        @rtype: string

        '''
        value = self.instanceval.get(instance, self.defvalue)

        if value is None and self.nullable:
            # NOTE: A exception could be raised if not "nullable"
            return self.patternNull

        if isinstance(value, (int, long, float, basestring)):
            pattern = str(value)
        elif isinstance(value, bool):
            pattern = str(value).lower()
        elif isinstance(value, (list, tuple)):
            pattern = ''
            for val in value:
                pattern += self.patternList % str(val)
        elif isinstance(value, datetime.datetime):
            localTimezone = LocalTimezone()
            tmpvalue = value - localTimezone.utcoffset(value)
            pattern = tmpvalue.isoformat()
        else:
            pattern = str(value)

        return self.patternFill % pattern


ApiDataTypes = list()

class ApiDataTypeMeta(type):
    '''
    Metaclass for L{ApiDataType} that install L{ApiParam} descriptors
    '''
    def __new__(cls, name, bases, clsdict):
        '''
        Modifies L{ApiDataType} class creation

        @type cls: class
        @param cls: the class to be modifies on creation
        @type name: string
        @param name: name of the class
        @type bases: list
        @param bases: list of base classes for cls
        @type clsdict: dict
        @param clsdict: the dictionary of cls
        '''
        clsdict['_params'] = list()
        if '_apiParams' in clsdict:
            for apiParam in clsdict['_apiParams']:
                clsdict[apiParam.name] = apiParam
                clsdict['_params'].append(apiParam.name)

        newcls = type.__new__(cls, name, bases, clsdict)
        ApiDataTypes.append(newcls)

        return newcls


class ApiDataType(object):
    '''
    Holds L{ApiParam} descriptors to later generate an entire pattern
    for an ApiDataType

    @type pattern: string
    @cvar pattern: pre-computed pattern for the type in the soap call
    @type header: ApiDataType
    @cvar header: a header that ApiDataType instances may carry (most do)
    '''
    __metaclass__ = ApiDataTypeMeta

    apitype = None

    def __init__(self, ns='ns1', name='request'):
        '''
        Initializes the pattern using the given name

        @type name: string
        @param name: name of the type in the soap call
                     if name is None, the pattern will be empty
                     (except for the substitution)
        '''
        self.header = None

        if ns and name:
            name = '%s:%s' % (ns, name)

        if name is not None:
            self.pattern = '<%s>\n%%s</%s>' % (name, name)
        else:
            self.pattern = '\n%s'


    def __call__(self):
        '''
        Returns the final computed pattern for the type
        '''
        subpattern = ''

        if self.header is not None:
            subpattern += self.header()
            subpattern += '\n'

        for param in self._params:
            subpattern += getattr(self.__class__, param)(self)
            subpattern += '\n'

        return self.pattern % subpattern


    def __str__(self):
        '''
        Returns the final computed pattern for the type
        '''
        return self()


    def __unicode__(self):
        '''
        Returns the final computed pattern for the type in unicode
        '''
        return unicode(self()).encode('utf-8')


    def __copy__(self):
        clone = self.__class__()
        for param in self._params:
            setattr(clone, param, getattr(self, param))
        return clone
        

'''ApiDataType definitions'''

class APIRequestHeader(ApiDataType):
    _apiParams = [
        ApiParam('clientStamp'), ApiParam('sessionToken'),
        ]

    def __init__(self):
        ApiDataType.__init__(self, ns=None, name='header')


##############################
# General API - Complete
##############################

class LoginReq(ApiDataType):
    _apiParams = [
        ApiParam('ipAddress'),
        ApiParam('locationId'),
        ApiParam('password'),
        ApiParam('productId'),
        ApiParam('username'),
        ApiParam('vendorSoftwareId'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class LogoutReq(ApiDataType):
    def __init__(self):
        ApiDataType.__init__(self)


class KeepAliveReq(ApiDataType):
    def __init__(self):
        ApiDataType.__init__(self)


##############################
# Read-Only API - Complete
##############################
class ConvertCurrencyReq(ApiDataType):
    _apiParams = [
        ApiParam('amount'),
        ApiParam('fromCurrency', nullable=True),
        ApiParam('toCurrency', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetCurrenciesReq(ApiDataType):
    _apiParams = [
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetCurrenciesV2Req(ApiDataType):
    _apiParams = [
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetEventTypesReq(ApiDataType):
    _apiParams = [
        ApiParam('locale', nullable=True),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetAllMarketsReq(ApiDataType):
    _apiParams = [
        ApiParam('locale', nullable=True),
        ApiParam('eventTypeIds', nullable=True, xsd=False, listtype='int'),
        ApiParam('countries', nullable=True, xsd=False, listtype='Country'),
        ApiParam('fromDate', nullable=True),
        ApiParam('toDate', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetBetReq(ApiDataType):
    _apiParams = [
        ApiParam('betId'),
        ApiParam('locale', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetBetHistoryReq(ApiDataType):
    _apiParams = [
        ApiParam('betTypesIncluded', xsd=False),
        ApiParam('detailed'),
        ApiParam('eventTypeIds', nullable=True, xsd=False, listtype='int'),
        ApiParam('marketId'),
        ApiParam('locale', nullable=True),
        ApiParam('timezone', nullable=True),
        ApiParam('marketTypesIncluded', nullable=True, xsd=False, listtype='MarketTypeEnum'),
        ApiParam('placedDateFrom'),
        ApiParam('placedDateTo'),
        ApiParam('recordCount'),
        ApiParam('sortBetsBy', xsd=False),
        ApiParam('startRecord'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetBetLiteReq(ApiDataType):
    _apiParams = [
        ApiParam('betId'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetBetMatchesLiteReq(ApiDataType):
    _apiParams = [
        ApiParam('betId'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetCompleteMarketPricesCompressedReq(ApiDataType):
    _apiParams = [
        ApiParam('currencyCode', nullable=True),
        ApiParam('marketId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetCurrentBetsReq(ApiDataType):
    _apiParams = [
        ApiParam('betStatus', xsd=False),
        ApiParam('detailed'),
        ApiParam('locale', nullable=True),
        ApiParam('timezone', nullable=True),
        ApiParam('marketId'),
        ApiParam('orderBy', xsd=False),
        ApiParam('recordCount'),
        ApiParam('startRecord'),
        ApiParam('noTotalRecordCount'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetCurrentBetsLiteReq(ApiDataType):
    _apiParams = [
        ApiParam('betStatus', xsd=False),
        ApiParam('marketId'),
        ApiParam('orderBy', xsd=False),
        ApiParam('recordCount'),
        ApiParam('startRecord'),
        ApiParam('noTotalRecordCount'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetDetailedAvailableMktDepthReq(ApiDataType):
    _apiParams = [
        ApiParam('asianLineId'),
        ApiParam('currencyCode', nullable=True),
        ApiParam('locale', nullable=True),
        ApiParam('marketId'),
        ApiParam('selectionId'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetEventsReq(ApiDataType):
    _apiParams = [
        ApiParam('eventParentId'),
        ApiParam('locale', nullable=True),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetInPlayMarketsReq(ApiDataType):
    _apiParams = [
        ApiParam('locale', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketReq(ApiDataType):
    _apiParams = [
        ApiParam('locale', nullable=True),
        ApiParam('marketId'),
        ApiParam('includeCouponLinks'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketInfoReq(ApiDataType):
    _apiParams = [
        ApiParam('marketId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketPricesReq(ApiDataType):
    _apiParams = [
        ApiParam('currencyCode', nullable=True),
        ApiParam('marketId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketPricesCompressedReq(ApiDataType):
    _apiParams = [
        ApiParam('currencyCode', nullable=True),
        ApiParam('marketId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMUBetsReq(ApiDataType):
    _apiParams = [
        ApiParam('betStatus', xsd=False),
        ApiParam('marketId'),
        ApiParam('betIds', nullable=True, xsd=False, listtype='betId'),
        ApiParam('orderBy', xsd=False),
        ApiParam('sortOrder', xsd=False),
        ApiParam('recordCount'),
        ApiParam('startRecord'),
        ApiParam('matchedSince', nullable=True),
        ApiParam('excludeLastSecond'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMUBetsLiteReq(ApiDataType):
    _apiParams = [
        ApiParam('betStatus', xsd=False),
        ApiParam('marketId'),
        ApiParam('betIds', nullable=True, xsd=False, listtype='betId'),
        ApiParam('orderBy', xsd=False),
        ApiParam('sortOrder', xsd=False),
        ApiParam('recordCount'),
        ApiParam('startRecord'),
        ApiParam('matchedSince', nullable=True),
        ApiParam('excludeLastSecond'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketProfitAndLossReq(ApiDataType):
    _apiParams = [
        ApiParam('locale', nullable=True),
        ApiParam('includeSettledBets'),
        ApiParam('includeBspBets'),
        ApiParam('marketID'),
        ApiParam('netOfComission'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketTradedVolumeReq(ApiDataType):
    _apiParams = [
        ApiParam('asianLineId'),
        ApiParam('currencyCode', nullable=True),
        ApiParam('marketId'),
        ApiParam('selectionId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketTradedVolumeCompressedReq(ApiDataType):
    _apiParams = [
        ApiParam('currencyCode', nullable=True),
        ApiParam('marketId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetPrivateMarketsReq(ApiDataType):
    _apiParams = [
        ApiParam('locale', nullable=True),
        ApiParam('eventTypeId'),
        ApiParam('marketType', xsd=False),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetSilksReq(ApiDataType):
    _apiParams = [
        ApiParam('locale', nullable=True),
        ApiParam('markets', nullable=True, xsd=False, listtype='int'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetSilksV2Req(ApiDataType):
    _apiParams = [
        ApiParam('locale', nullable=True),
        ApiParam('markets', nullable=True, xsd=False, listtype='int'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


##############################
# Bet Placement API - Complete
##############################
class PlaceBetsReq(ApiDataType):
    _apiParams = [
        ApiParam('bets', xsd=False, nullable=True, listtype='PlaceBets'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class PlaceBets(ApiDataType):
    _apiParams = [
        ApiParam('asianLineId'),
        ApiParam('betType', xsd=False),
        ApiParam('betCategoryType', xsd=False),
        ApiParam('betPersistenceType', xsd=False),
        ApiParam('marketId'),
        ApiParam('price'),
        ApiParam('selectionId'),
        ApiParam('size', nullable=True),
        ApiParam('bspLiability', nullable=True),
        ]
    def __init__(self):
        ApiDataType.__init__(self, name=None)


class CancelBetsReq(ApiDataType):
    _apiParams = [
        ApiParam('bets', xsd=False, nullable=True, listtype='CancelBets'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class CancelBets(ApiDataType):
    _apiParams = [
        ApiParam('betId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self, name=None)


class CancelBetsByMarketReq(ApiDataType):
    _apiParams = [
        ApiParam('markets', nullable=True, xsd=False, listtype='int'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class UpdateBetsReq(ApiDataType):
    _apiParams = [
        ApiParam('bets', xsd=False, nullable=True, listtype='UpdateBets'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class UpdateBets(ApiDataType):
    _apiParams = [
        ApiParam('betId'),
        ApiParam('newPrice', nullable=True),
        ApiParam('newSize'),
        ApiParam('oldPrice', nullable=True),
        ApiParam('oldSize'),
        ApiParam('newBetPersistenceType', xsd=False),
        ApiParam('oldBetPersistenceType', xsd=False),
        ]
    def __init__(self):
        ApiDataType.__init__(self, name=None)


##############################
# Account Management API - Complete
##############################
class AddPaymentCardReq(ApiDataType):
    _apiParams = [
        ApiParam('cardNumber'),
        ApiParam('cardType', xsd=False),
        ApiParam('startDate', nullable=True),
        ApiParam('expiryDate'),
        ApiParam('issueNumber', nullable=True),
        ApiParam('billingName'),
        ApiParam('nickName'),
        ApiParam('password'),
        ApiParam('address1'),
        ApiParam('address2', nullable=True),
        ApiParam('address3', nullable=True),
        ApiParam('address4', nullable=True),
        ApiParam('town', nullable=True),
        ApiParam('county', nullable=True),
        ApiParam('zipCode', nullable=True),
        ApiParam('country', nullable=True),
        ApiParam('cardStatus', xsd=False),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class DeletePaymentCardReq(ApiDataType):
    _apiParams = [
        ApiParam('nickName'),
        ApiParam('password'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class DepositFromPaymentCardReq(ApiDataType):
    _apiParams = [
        ApiParam('amount'),
        ApiParam('cardIdentifier', nullable=True),
        ApiParam('cv2', nullable=True),
        ApiParam('password', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class ForgotPasswordReq(ApiDataType):
    _apiParams = [
        ApiParam('username'),
        ApiParam('emailAddress'),
        ApiParam('countryOfResidence'),
        ApiParam('forgottenPasswordAnswer1', nullable=True),
        ApiParam('forgottenPasswordAnswer2', nullable=True),
        ApiParam('newPassword', nullable=True),
        ApiParam('newPasswordRepeat', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetAccountFundsReq(ApiDataType):
    def __init__(self):
        ApiDataType.__init__(self)


class GetAccountStatementReq(ApiDataType):
    _apiParams = [
        ApiParam('endDate'),
        ApiParam('itemsIncluded', xsd=False),
        ApiParam('ignoreAutoTransfers'),
        ApiParam('recordCount'),
        ApiParam('startDate'),
        ApiParam('startRecord'),
        ApiParam('locale', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self, name='req')


class GetPaymentCardReq(ApiDataType):
    _apiParams = [
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetSubscriptionInfoReq(ApiDataType):
    _apiParams = [
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class ModifyPasswordReq(ApiDataType):
    _apiParams = [
        ApiParam('password'),
        ApiParam('newPassword'),
        ApiParam('newPasswordRepeat'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class ModifyProfileReq(ApiDataType):
    _apiParams = [
        ApiParam('password'),
        ApiParam('address1', nullable=True),
        ApiParam('address2', nullable=True),
        ApiParam('address3', nullable=True),
        ApiParam('townCity', nullable=True),
        ApiParam('countyState', nullable=True),
        ApiParam('postCode', nullable=True),
        ApiParam('countryOfResidence', nullable=True),
        ApiParam('homeTelephone', nullable=True),
        ApiParam('workTelephone', nullable=True),
        ApiParam('mobileTelephone', nullable=True),
        ApiParam('emailAddress', nullable=True),
        ApiParam('timeZone', nullable=True),
        ApiParam('depositLimit', nullable=True),
        ApiParam('depositLimitFrequency', xsd=False, nullable=True),
        ApiParam('lossLimit', nullable=True),
        ApiParam('lossLimitFrequency', xsd=False, nullable=True),
        ApiParam('nationalIdentifier', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class RetrieveLIMBMessageReq(ApiDataType):
    _apiParams = [
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class SelfExcludeReq(ApiDataType):
    _apiParams = [
        ApiParam('selfExclude'),
        ApiParam('password', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class SetChatNameReq(ApiDataType):
    _apiParams = [
        ApiParam('password'),
        ApiParam('chatName'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class SubmitLIMBMessageReq(ApiDataType):
    _apiParams = [
        ApiParam('password'),
        ApiParam('submitPersonalMessage', xsd=False),
        ApiParam('submitTCPrivacyPolicyChangeMessage', xsd=False),
        ApiParam('submitPasswordChangeMessage', xsd=False),
        ApiParam('submitBirthDateCheckMessage', xsd=False),
        ApiParam('submitAddressCheckMessage', xsd=False),
        ApiParam('submitContactDetailsCheckMessage', xsd=False),
        ApiParam('submitChatNameChangeMessage', xsd=False),
        ApiParam('submitCardBillingAddressCheckItems', nullable=True, xsd=False),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class TransferFundsReq(ApiDataType):
    _apiParams = [
        ApiParam('sourceWalletId'),
        ApiParam('targetWalletId'),
        ApiParam('amount'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class UpdatePaymentCardReq(ApiDataType):
    _apiParams = [
        ApiParam('nickName'),
        ApiParam('password'),
        ApiParam('expiryDate', nullable=True),
        ApiParam('startDate', nullable=True),
        ApiParam('issueNumber', nullable=True),
        ApiParam('address1', nullable=True),
        ApiParam('address2', nullable=True),
        ApiParam('address3', nullable=True),
        ApiParam('address4', nullable=True),
        ApiParam('town', nullable=True),
        ApiParam('county', nullable=True),
        ApiParam('zipCode', nullable=True),
        ApiParam('country', nullable=True),
        ApiParam('cardStatus', xsd=False),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class ViewProfileReq(ApiDataType):
    _apiParams = [
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class ViewProfileV2Req(ApiDataType):
    _apiParams = [
        # According to the docs, the following param exists
        # But not in the WSDL
        ApiParam('requestVersion', xsd=False, nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class ViewReferAndEarnReq(ApiDataType):
    _apiParams = [
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class WithdrawToPaymentCardReq(ApiDataType):
    _apiParams = [
        ApiParam('amount'),
        ApiParam('cardIdentifier', nullable=True),
        ApiParam('password', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


##############################################
# Account Management API - Complete
##############################################
class CreateVendorAccessRequestReq(ApiDataType):
    _apiParams = [
        ApiParam('vendorCustomField'),
        ApiParam('vendorSoftwareId'),
        ApiParam('expiryDate', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class VendorSubscriptionReq(ApiDataType):
    _apiParams = [
        ApiParam('username'),
        ApiParam('vendorCustomField'),
        ApiParam('vendorClientId'),
        ApiParam('vendorSoftwareId'),
        ApiParam('expiryDate', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class CancelVendorAccessRequestReq(ApiDataType):
    _apiParams = [
        ApiParam('accessRequestToken'),
        ApiParam('vendorSoftwareId'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetVendorUsersReq(ApiDataType):
    _apiParams = [
        ApiParam('vendorSoftwareId'),
        ApiParam('username', nullable=True),
        ApiParam('usernameSearchModifier', xsd=False),
        ApiParam('vendorCustomField', nullable=True),
        ApiParam('customFieldSearchModifier', xsd=False),
        ApiParam('expiryDateFrom', nullable=True),
        ApiParam('expiryDateTo', nullable=True),
        ApiParam('status', xsd=False),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetVendorAccessRequestsReq(ApiDataType):
    _apiParams = [
        ApiParam('vendorSoftwareId'),
        ApiParam('status', xsd=False),
        ApiParam('requestDateFrom', nullable=True),
        ApiParam('requestDateTo', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetSubscriptionInfoReq(ApiDataType):
    _apiParams = [
        ApiParam('username'),
        ApiParam('vendorClientId'),
        ApiParam('vendorSoftwareId'),
        ]

    apitype='vendor'

    def __init__(self):
        ApiDataType.__init__(self)


class GetVendorInfoReq(ApiDataType):
    _apiParams = [
        ]

    def __init__(self):
        ApiDataType.__init__(self)
