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
HttxLib authcache object to enable cached (or partially cached) authentication
answer to authentication requests

A namedtuple I{AuthCache} is defined for storage in the cache with the
following fields:

  - {headername} if WWW-Authenticate or Proxy-Authenticate was sent
  - {scheme} if Basic, Digest or other
  - {answer} Previous answer
  - {cachedata} Specific data cached to be used if a new auth request is seen
'''

from collections import defaultdict, namedtuple
from copy import deepcopy

from httxobject import HttxObject

# Authorization cache type
AuthCache = namedtuple('AuthCache', 'headername, scheme, answer, cachedata')


class HttxAuthCache(HttxObject):
    '''
    An object that caches data from and for authentication requests

    @ivar cache: holds the cache entries
    @type cache: dict
    @ivar noncecache: holds specifically sequestial nonce values for
                      digest authentication
    @type noncecache: defaultdict(int)
    '''

    def __init__(self):
        '''
        Constructor. It delegates construction to the base class
        L{HttxObject} and initializes the member variables
        '''
        HttxObject.__init__(self)
        self.cache = dict()
        self.noncecache = defaultdict(int)


    def __deepcopy__(self, memo):
        '''
        Deepcopy support.

        @param memo: standard __deepcopy__ parameter to avoid circular references
        @type memo: dict
        @return: a cloned object
        @rtype: L{HttxAuthCache}
        '''
        clone = self.__class__()
        with self.lock:
            clone.cache = deepcopy(self.cache, memo)
            clone.noncecache = deepcopy(self.noncecache, memo)

        return clone


    def getnoncecount(self, nonce):
        '''
        Get a new nonce_count value for nonce

        This will increment the cached value and return and cache the
        incremented value

        @param nonce: nonce value in digest auth requests
        @type nonce: str
        @return: a sequentally incremented nonce_count
        @rtype: int
        '''
        with self.lock:
            self.noncecache[nonce] += 1
            return self.noncecache[nonce]


    def set(self, url, headername, scheme, answer, cachedata):
        '''
        Set a new entry in the cache

        @param headername: WWW-Authenticate or Proxy-Authenticate as sent
        @type headername: str
        @param scheme: Basic, Digest or other types of auth
        @type scheme: str
        @param answer: Answer sent to the server
        @type answer: str
        @param cachedata: Specific data cached to be used if a new auth request is seen
        @type cachedata: str
        '''
        with self.lock:
            self.cache[url] = AuthCache(headername, scheme, answer, cachedata)


    def get(self, url):
        '''
        Get a cache entry for a url

        The search is done hierarchically, because once authorized in an url
        all sub-urls (same domain and same initial) path will likely send
        the same authorization request

        @param url: url for the http request
        @type url: str
        @return: A tuple with the headername to be sent and the header content
                 Both values can be None to indicate that no entry was found
        @rtype: tuple
        '''
        urllen = len(url)
        authcache = None

        with self.lock:
            cachekeys = self.cache.keys()
        cachekeys.sort(reverse=True)

        for cachekey in cachekeys:
            if len(cachekey) > urllen or not url.startswith(cachekey):
                continue

            with self.lock:
                authcache = self.cache[cachekey]
            break

        headername = None
        headerval = None

        if authcache:

            if authcache.scheme == 'basic':
                authanswer = authcache.answer

            elif authcache.scheme == 'digest':

                authchallenge = parse_keqv_list(parse_http_list(authcache.answer))

                nonce = authchallenge['nonce']
                nonce_count = self.getnoncecount(nonce)
                authanswer = authdigest(None, authcache.cachedata, authchallenge, httxreq, nonce_count)

            headerval = '%s %s' % (authcache.scheme, authanswer)
            headername = authcache.headername

        return (headername, headerval)
