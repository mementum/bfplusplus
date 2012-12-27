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
BfPy transport
'''
#
# Contains classes for http(s) transport implementation
#

from copy import deepcopy
from cStringIO import StringIO
from urlparse import urlparse
from socket import error as SocketError

from httxlib import HttxManager, HttxRequest, HttxSocketException, HttxException


class BfTransportError(Exception):
    def __init__(self, *args):
        Exception.__init__(self, *args)

class BfTransportSocketError(BfTransportError):
    def __init__(self, *args):
        BfTransportError.__init__(self, *args)


class BfTransportHttpError(BfTransportError):
    def __init__(self, *args):
        BfTransportError.__init__(self, *args)


class BfTransportHtmlError(BfTransportError):
    def __init__(self, *args):
        BfTransportError.__init__(self, *args)


class BfTransportRequest(object):
    '''
    Transport neutral class to define a request

    @type url: string
    @ivar url: url to go to
    @type headers: dict
    @ivar headers: specific headers for the call
    @type message: string
    @ivar message: content of the soap message
    '''

    def __init__(self, url, message=None):
        '''
        Inits the transport request

        @type url: string
        @param url: url to go to
        @type message: string
        @param message: content of the soap message
        '''
        self.url = url
        self.headers = dict()
        self.message = message

    def __str__(self):
        '''
        Generates a printable output of a request
        '''
        s = []
        s.append('URL:%s' % self.url)
        s.append('HEADERS: %s' % self.headers)
        s.append('MESSAGE:')
        if self.message is not None:
            s.append(self.message)
        return '\n'.join(s)


class BfTransportReply(object):
    '''
    Transport neutral class to define a Replay

    @type code: int
    @ivar code: status code from the answer
    @type headers: dict
    @ivar headers: specific headers for the call
    @type message: string
    @ivar message: content of the soap message
    '''

    def __init__(self, code, headers, message):
        '''
        Inits the transport request

        @type code: int
        @param code: status code from the answer
        @type headers: dict
        @param headers: specific headers for the call
        @type message: string
        @param message: content of the soap message
        '''
        self.code = code
        self.headers = headers
        self.message = message

    def __str__(self):
        '''
        Generates a printable output of a reply
        '''
        s = []
        s.append('CODE: %s' % self.code)
        s.append('HEADERS: %s' % self.headers)
        s.append('MESSAGE:')
        s.append(self.message)
        return '\n'.join(s)


class BfTransport(object):
    '''
    HTTP transport using httxlib. Provides http/https transport
    with cookies, authentication (basic and digest), redirection,
    certificate support and certificate validation
    and proxy support
    '''

    def __init__(self, httxmanager=None, **kwargs):
        '''
        Initialize the transport.

        If an httxmanager is passed it will be used as the underlying transport
        else a new one will be created

        @param httxmanager: A HttxManager object to do actual transport
        @type httxmanager: HttxManager
        @param kwargs: keyword arguments
        @type kwargs: dict
        '''
        self.httxmanager = httxmanager if httxmanager else HttxManager()


    def setproxy(self, proxydict):
        '''
        Set the proxy options for the transport

        @param proxydict: proxy options
        @type proxydict: dict
        '''
        self.httxmanager.setproxy(proxydict)


    def setuseragent(self, useragent):
        '''
        Set the useragent option for the transport

        @param useragent: the useragent to fake
        @type useragent: str
        '''
        self.httxmanager.setuseragent(useragent)


    def setdecompmethods(self, decompmethods):
        '''
        Set the decompression methods option for the transport

        @param decompmethods: the useragent to fake
        @type decompmethods: list
        '''
        self.httxmanager.setdecompmethods(decompmethods)


    def send(self, request):
        """
        Send a soap request

        @param request: A request
        @type request: Request
        @return: the reply
        @rtype: BfTransportReply
        """
        httxrequest = HttxRequest(request.url, request.message, request.headers)

        try:
            httxresponse = self.httxmanager.urlopen(httxrequest)
        except HttxSocketException, e:
            raise BfTransportSocketError(*e.args)
        except HttxException, e:
            # This error is to mimic the original exception code
            httxresponse = e.response
            raise BfTransportHttpError(httxresponse.reason, httxresponse.status, httxresponse.bodyfile)
        except Exception, e:
            # This will be a non-network, non - HTTP error (python syntax, ...)
            raise e

        else:
            if httxresponse.status < 200 and httxresponse.status >= 300:
                raise BfTransportHttpError(httxresponse.reason, httxresponse.status, httxresponse.bodyfile)

            if not httxresponse.body.startswith('<?xml'):
                raise BfTransportHtmlError('Wrong answer received from server. Please check connection',
                                           httxresponse.status, httxresponse.bodyfile)

        reply = BfTransportReply(200, httxresponse.headers, httxresponse.body)
        return reply


    def __deepcopy__(self, memo):
        """
        Deepcopy support

        It does a copy of itself with the existing HttxManager object
        because the httxmanager is already multithreaded safe
        and can handle multiple connections

        @param memo: Standard deepcopy memo parameter to avoid loops
        @type memo: dict
        @return: a cloned object
        @rtype: HttxTransport
        """
        clone = self.__class__(self.httxmanager)
        return clone


    def clone(self):
        """
        Just an alias for __deepcopy__
        """
        return deepcopy(self)
