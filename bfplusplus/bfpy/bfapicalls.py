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

import types

import bfglobals
import bfprocessors
import bfsoap
import bftransport
import bftypes


class ApiCall(object):
    '''
    Non-data descriptor class to be installed in L{ApiService}

    @type soappattern: string
    @cvar soappattern: basic string pattern with substitution patterns to form
                       the final soap message

    @type instanceCache: dict
    @ivar instanceCache: cache for instances during descriptor operation
    @type pattern: string
    @ivar pattern: holds the prepared soap message patter
    @type ns1: string
    @ivar ns1: namespace where this call was defined
    @type ns2: string
    @ivar ns2: namespace where types for this call are defined
    @type nsxsd: string
    @ivar nsxsd: namespace where types for this call are defined formatted for type parsing
    @type headers: dict
    @ivar headers: customized headers for this specific operation
    '''

    soappattern = '''<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns1="$$ns1$$" xmlns:ns2="$$ns2$$">
<soap:Header/>
<soap:Body>
<ns1:$$operation$$>
$$request$$
</ns1:$$operation$$>
</soap:Body>
</soap:Envelope>'''

    def __init__(self, apitype, ns1, ns2, operation, result='Result', **kwargs):
        '''
        Initializes most of the pattern and the HTTP request, leaving just the last second
        specific value substitutions for the soap call

        @type ns1: string
        @param ns1: namespace where the call was defined
        @type ns2: string
        @param ns2: namespace where the types used by the call were defined
        @type operation: string
        @param operation: name of the call
        '''
        self.apitype = apitype
        self.__name__ = '_' + operation + '_'
        
        self.instanceCache = dict()

        self.pattern = self.soappattern

        self.ns1 = ns1
        self.ns2 = ns2
        self.nsxsd = '{' + ns2 + '}'
        self.pattern = self.patternSub('ns1', self.ns1)
        self.pattern = self.patternSub('ns2', self.ns2)

        self.operation = operation
        self.pattern = self.patternSub('operation', self.operation)

        self.result = result

        self.headers = dict()
        self.headers['Content-type'] = 'text/xml; charset=utf-8'
        self.headers['User-agent'] = bfglobals.libstring
        self.headers['SoapAction'] = '"%s"' % self.operation

        if 'arrays' in kwargs:
            self.arrays = bfprocessors.ArrayFix(kwargs['arrays'])
        else:
            self.arrays = None


    def decodeComplex(self, element, xstype, valtype):
        '''
        Decodes a SOAP complex type from Betfair referring to the type namespace (ns2 instance variable)

        @type element: elementTree.element
        @param element: xml element containing the type to be parsed 
        @type xstype: string
        @param xstype: namespace to which the type belongs in the xsd schema
        @type valtype: string
        @param valtype: type of the element

        @return: a tuple with False|True indicating if the type could be decoded
                 and the actual result of the decoding
        @rtype: tuple
        '''
        if xstype == self.nsxsd and valtype.startswith('ArrayOf'):
            return (True, bfsoap.decode_array(element, [self.decodeComplex], [self.decodeSimplex]))

        return (False, None)


    def decodeSimplex(self, element, xstype, valtype):
        '''
        Decodes a SOAP simple type from Betfair referring to the type namespace (ns2 instance variable)

        @type element: elementTree.element
        @param element: xml element containing the type to be parsed 
        @type xstype: string
        @param xstype: namespace to which the type belongs in the xsd schema
        @type valtype: string
        @param valtype: type of the element

        @return: a tuple with False|True indicating if the type could be decoded
                 and the actual result of the decoding
        @rtype: tuple
        '''
        if xstype == self.nsxsd and 'Enum' in valtype:
                return (True, element.text)

        return (False, None)


    def patternSub(self, name, value):
        '''
        Initializes most of the pattern and the HTTP request, leaving just the last second
        specific value substitutions for the soap call

        @type name: string
        @param name: pattern name to be substituted in the soap message
        @type value: string
        @param value: the string to put into the soap message
        '''
        return self.pattern.replace('$$%s$$' % name, value)


    def __get__(self, instance, owner):
        '''
        Non-data descriptor implementation.

        It returns a method type pointing to itself. This forces the invocation of __call__

        @type instance: instance of class
        @param instance: instance that calls the descriptor
        @type owner: class
        @param owner: the class that holds the descriptor
        '''
        return self.instanceCache.setdefault(instance, types.MethodType(self, instance, owner))


    def __call__(self, instance, request):
        '''
        Invoked as method by L{ApiService} instances. It receives the instance and a request

        It finishes preparation of the soap message with the value of the request object and
        also the preparation of the http request.

        Invokes the http request, the parsing of the soap and return the "Result" part of the
        entire response

        @type instance: an object
        @param instance: object that is invoking the descriptor
        @type request: L{ApiDataType}
        @param request: the request to be sent to the servers
        '''
        # 'Calling' the request delivers the content
        httpreq = bftransport.BfTransportRequest(instance.endPointUrl, self.patternSub('request', request()))
        httpreq.headers.update(self.headers)
        reply = instance.transport.send(httpreq)

        response = bfsoap.soap_process(reply.message, [self.decodeComplex], [self.decodeSimplex])
        response = getattr(response, self.result)

        if self.arrays:
            self.arrays(response)

        return response


class ApiCallGlobal(ApiCall):
    '''
    Specialized version of L{ApiCall} for Global calls
    '''
    ns1 = 'http://www.betfair.com/publicapi/v3/BFGlobalService/'
    ns2 = 'http://www.betfair.com/publicapi/types/global/v3/'

    def __init__(self, operation, result='Result', **kwargs):
        '''
        Initializes the parent class

        @type operation: string
        @param operation: name of the call
        '''
        ApiCall.__init__(self, 'global', self.ns1, self.ns2, operation=operation, result=result, **kwargs)


class ApiCallExchange(ApiCall):
    '''
    Specialized version of L{ApiCall} for Exchange calls
    '''
    ns1 = 'http://www.betfair.com/publicapi/v5/BFExchangeService/'
    ns2 = 'http://www.betfair.com/publicapi/types/exchange/v5/'

    def __init__(self, operation, result='Result', **kwargs):
        '''
        Initializes the parent class

        @type operation: string
        @param operation: name of the call
        '''
        ApiCall.__init__(self, 'exchange', self.ns1, self.ns2, operation=operation, result=result, **kwargs)


class ApiCallVendor(ApiCall):
    '''
    Specialized version of L{ApiCall} for Vendor calls
    '''
    ns1 = 'http://www.betfair.com/adminapi/v2/VendorService/'
    ns2 = 'http://www.betfair.com/adminapi/types/v2/'

    def __init__(self, operation, result='Result', **kwargs):
        '''
        Initializes the parent class

        @type operation: string
        @param operation: name of the call
        '''
        ApiCall.__init__(self, 'vendor', self.ns1, self.ns2, operation=operation, result=result, **kwargs)
