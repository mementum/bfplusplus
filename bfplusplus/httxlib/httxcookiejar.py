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
Module implementing a deepcopyable Cookiejar
(Cookiejar is already multithread safe)
'''


from cookielib import CookieJar
from copy import deepcopy

from httxobject import HttxObject


class HttxCookieJar(HttxObject):
    '''
    An CookieJar holder to enable deepcopy semantics with locking.

    CookieJars already lock access to the internals, but cannot be
    deepcopied, which prevents separation of cookiejars into different
    domains as achieved with different HttxOptions

    A light wrapper over CookieJar with a lock for deepcopy and access
    to the internal variable _cookies is needed to achieve deepcopy
    and therefore enable separation of domains

    @ivar cookiejar: CookieJar object holding the cookies
    @type cookiejar: urllib2 CookieJar
    '''

    def __init__(self):
        '''
        Constructor. It delegates construction to the base class
        L{HttxObject} and initializes the member variables
        '''
        HttxObject.__init__(self)
        self.cookiejar = CookieJar()


    def __deepcopy__(self, memo):
        '''
        Deepcopy support.

        The lock prevents access from any other part of the library to this
        CookieJar, enabling a deepcopy of the private variable into the
        private variable of the clone to enable separation of domains
        for CookieJar objects

        The existing RLock in the CookieJar objects forbids direct deepcopy

        @param memo: standard __deepcopy__ parameter to avoid circular references
        @type memo: dict
        @return: a cloned object
        @rtype: L{HttxCookieJar}
        '''
        clone = self.__class__()
        with self.lock:
            # CookieJar has a threading.RLock, so we may not deepcopy it
            # and it has no __deepcopy_ implemented
            clone.cookiejar._cookies = deepcopy(self.cookiejar._cookies, memo)

        return clone


    def add_cookie_header(self, request):
        '''
        Add a cookie header to the request if needed

        This is a simple stub for CookieJar add_cookie_header

        @param request: the request to be manipulated
        @type request: urllib2 compatible Request - L{HttxRequest} 
        '''
        self.cookiejar.add_cookie_header(request)


    def extract_cookies(self, response, request):
        '''
        Extract cookies from the response, using request as a basis to do so

        This is a simple stub for CookieJar extract_cookies

        @param response: the response containing the headers where cookies
                         may be present
        @type response: urllib2 compatible Response - L{HttxResponse} 
        @param request: the request to be manipulated
        @type request: urllib2 compatible Request - L{HttxRequest} 
        '''
        self.cookiejar.extract_cookies(response, request)
    
