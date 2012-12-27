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
Net Location connecting object L{HttxNetLocation} implementation
'''

from collections import deque
import sys
if sys.platform == 'win32':
    from time import clock as tclock
else:
    from time import time as tclock

from httxbase import HttxBase
from httxconnection import HttxConnection


class HttxNetLocation(HttxBase):
    '''
    Net Location Connecting object. The HttxNetLocation is responsible for creating
    and managing a set of L{HttxConnection} connection objects that will 
    perform the actual connection

    L{HttxConnection} connections will be created on demand and re-used if possible.
    Active connections will be kept in a cache, whilst non-active will be kept
    in a double queue (next in use to be popped from the right, and after usage
    they wll be appended to the left

    Due to the threading nature, a in-operation cache may hold connections during
    manipulation

    @ivar url: url used to set the net location to which connections will
               connect
    @type url: str
    @ivar httxconnque: The double queue holding non-active connections
    @type options: collections.deque
    @ivar httxconnache: Cache of connections with a pending request/response
    @type options: dict
    @ivar inopcache: Temporary in-operation cache for connections during request/response
    @type options: set
    '''

    def __init__(self, url, **kwargs):
        '''
        Constructor. It delegates construction to the base class
        L{HttxBase} and initializes the member variables

        @param url: url to open a connection to
        @type url: str
        @param kwargs: keywords arguments passed to L{HttxBase}
        @see: L{HttxOptions}
        '''
        HttxBase.__init__(self, **kwargs)

        self.url = url

        # For connections currently with no pending network activity
        self.httxconnque = deque()
        # For connections with pending network activity
        self.httxconncache = dict()
        # Temporary cache after creation and before usage
        self.inopcache = set()


    def __deepcopy__(self, memo):
        '''
        Deepcopy support.

        @param memo: standard __deepcopy__ parameter to avoid circular references
        @type memo: dict
        @return: a cloned object
        @rtype: L{HttxNetLocation}
        @see L{clone}
        '''
        return self.clone()
    

    def clone(self, options=None, connections=True):
        '''
        Clone the object using the supplied options or a new set of options if
        given.

        An equivalente set of L{HttxConnection} objects will be replicated

        A new set of options will separate the clone object from the original
        object, since they will no longer share cookies, user/password/realm
        combinations or https certificates

        @param options: options for the cloned object
        @type options: L{HttxOptions}
        @param connections: whether to clone the existing connections
        @type connections: bool
        @return: a cloned object
        @rtype: L{HttxNetLocation}
        '''
        if not options:
            options = self.options.clone()
        clone = self.__class__(self.url, options=options)

        with self.lock:
            if connections:
                for conniterable in (self.httxconnque, self.inopcache, self.httxconncache.itervalues()):
                    for httxconn in conniterable:
                        clone.httxconnque.appendleft(httxconn.clone(options))

        return clone


    def request(self, httxreq):
        '''
        Send the L{HttxRequest} httxreq to the specified server inside the request
        It does get a connection or create one and relay the request down to it, taking
        into account the HTTP keepalive timeout
        
        @param httxreq: Request to be executed
        @type httxreq: L{HttxRequest}
        @return: sock
        @rtype: opaque type for the caller (a Python sock)
        '''
        with self.lock:
            try:
                httxconn = self.httxconnque.pop()
                # Check if the HTTP keepalive timeout has been exceeded
                if (tclock() - httxconn.timestamp) >= self.options.keepalive:
                    # Simulate that no connection was available
                    raise IndexError
                # The connection is no longer in any container, it will be discarded
            except IndexError:
                # use self.url and not the request url ... to be able to proxy connections
                httxconn = HttxConnection(self.url, options=self.options)

            # keep a copy of this dangling connecion in a set to avoid missing it if
            # we are cloning an object and some threads find themselves issuing requests
            self.inopcache.add(httxconn)

        sock = httxconn.request(httxreq)

        # Remove the cache from the in-operation cache and place it in the
        # cache for connections with pending network activity
        with self.lock:
            self.inopcache.discard(httxconn)
            self.httxconncache[sock] = httxconn

        return sock


    def getresponse(self, sock):
        '''
        Recover a L{HttxResponse} using the connection that is in the cache
        indexed by sock and calling its getresponse
        
        @param sock: The opaque type returned by L{request}
        @type sock: opaque (a Python sock)
        @return: response
        @rtype: L{HttxResponse} (compatible with httplib HTTPResponse)
        '''
        with self.lock:
            httxconn = self.httxconncache.pop(sock)
            # keep a copy of this dangling connecion in a set to avoid missing it if
            # we are cloning an object and some threads find themselves issuing requests
            self.inopcache.add(httxconn)

        response = httxconn.getresponse(sock)

        # Put it back into the connection queue unless not ready
        with self.lock:
            self.inopcache.discard(httxconn)

            if not response.isactive():
                self.httxconnque.appendleft(httxconn)
            else:
                # Redirecting or authenticating and therefore still with
                # pending network activity. Back to the active conn cache
                self.httxconncache[response.sock] = httxconn

        return response
