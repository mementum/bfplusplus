#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of HttxLib
#
# HttxLib is an HTTP(s) Python library suited multithreaded/multidomain
# applications
#
# Copyright (C) 2010-2011  Daniel Rodriguez (aka Daniel Rodriksson)
# Copyright (C) 2011  Sensible Odds Ltd
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/httxlib/
#
# HttxLib is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HttxLib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HttxLib. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
'''
urllib2 compatible Request object with additional functionality

It can therefore be supplied to urllib2 objects (like a CookieJar)
'''

from urllib2 import Request
from urlparse import urlparse, urlsplit


class HttxRequest(Request):
    '''
    A subclass of urllib2 Request to retain compatibility and make it usable
    for cookies and whatever may be needed

    @ivar parsed: It holds the result of the urlsplit(url) done in the constructor
                  for practical purposes
    @type parsed: namedtuple result of urlsplit (check the Python docs)
    '''

    def __init__(self, url, data=None, headers=None, origin_req_host=None, unverifiable=False):
        '''
        Constructor. It delegates construction to the base class
        Request and initializes the member variables

        It performs an additional call of Request.get_type and Request.get_host
        to ensure that the Request object is properly initialized. Because this
        is done by the urllib2 library, but we are just using the request

        @param url: url to be requested in the HTTP request
        @type url: str
        @param data: data for the HTTP request body (which enforces a POST)
        @type data: str
        @param headers: dictionary of header name/header value
        @type headers: dict
        @param origin_req_host: request host of the origin transaction as per
                                RFC 2965 - Host name or IP address of the host
        @type origin_req_host: str
        @param unverifiable: if the request was not verified/requested by the end
                             user and it is rather automatic (redirection, download
                             of a picture inside a web page) - RFC 2965
        @type unverifiable: bool
        '''
        if headers is None:
            headers = dict()
        Request.__init__(self, url, data, headers, origin_req_host, unverifiable)
        self.parsed = urlsplit(url)
        # Done to force split of the url fields inside the request
        self.get_type()
        self.get_host()


    @property
    def allheaders(self):
        '''
        Property to return all the headers to be sent in a request

        urllib2 distinguishes amongst normal headers and headers that will
        not be used if the original request is redirected

        Therefore it is impossible to request all headers in just one call

        Although Request has a utility function, it returns a list of tuples
        rather than a dictionary

        This property returns a dictionary
        '''
        hdrs = self.unredirected_hdrs.copy()
        hdrs.update(self.headers)
        return hdrs


    @property
    def method(self):
        '''
        Property to have a handy alias for Request.get_method
        '''
        return self.get_method()


    def ispost(self):
        '''
        Utility function to avoid cluttering external code with
        string comparisons

        @return: if the request will be a POST request
        @rtype: bool
        '''
        return self.get_method() == 'POST'


    def isget(self):
        '''
        Utility function to avoid cluttering external code with
        string comparisons

        @return: if the request will be a GET request
        @rtype: bool
        '''
        return self.get_method() == 'GET'


    @property
    def scheme(self):
        '''
        Property to have a handy alias for Request.get_type or
        parsed.scheme
        '''
        # return self.get_type()
        return self.parsed.scheme


    @property
    def netloc(self):
        '''
        Property to have a handy alias for Request.get_host or
        parsed.netloc
        '''
        # return self.get_host()
        return self.parsed.netloc


    @property
    def body(self):
        '''
        Property to have a handy alias for Request.get_data
        '''
        return self.get_data()


    def clone(self, url=None):
        '''
        Clone a request with a change of url to support redirection

        By using the normal/unredirected header separation in Request it is
        easy to clone for a redirection by only supplying the new headers
        to the class

        @param url: url to redirect to if needed. Default of None for no
                    redirection
        @type url: str|None
        @return: a cloned object
        @rtype: L{HttxRequest}
        '''

        # The only non-cloned thing: unredirected_headers and this is possibly how it has to be
        if not url:
            url = self.get_full_url()
            headers = self.allheaders
        else:
            headers = self.headers

        return self.__class__(url, self.data, headers, self.origin_req_host, self.unverifiable)


    def __deepcopy__(self, memo):
        '''
        Deepcopy support.

        @param memo: standard __deepcopy__ parameter to avoid circular references
        @type memo: dict
        @return: a cloned object
        @rtype: L{HttxRequest}
        '''
        return self.clone()
