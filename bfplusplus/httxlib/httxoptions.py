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
Module that implements the domain wide options that connecting objects can share

A set of options apply to a HttxManager and all pending objects.

If a L{HttxManager} is cloned, it can be cloned sharing the options or not. If the options
are shared, so will be the cookies, compression schemes allowed, username and passwords,
certificate files.

If the options are not shared the new L{HttxManager} will be completely separate from
the original.

Since options can be directly instantiated by L{HttxNetLocation} and L{HttxConnection}, the
same logic applies on cloning
'''

from copy import deepcopy

from httxauthcache import HttxAuthCache
from httxcertificates import HttxCertKeyManager, HttxCertReqManager, HttxCACertManager
from httxcookiejar import HttxCookieJar
from httxcompressionset import HttxCompressionSet
from httxobject import HttxObject
from httxpassmanager import HttxPassManager


class HttxOption(object):
    '''
    A class representing an individual option.

    The class is implemented as a descriptor. The class locks access
    automatically on access (read/write) to the storage by using the
    lock from the instance object accessing the option.

    @ivar name: Name of the option
    @type name: str
    @ivar defvalue: Default value of the option
    @type defvalue: Opaque type. Each option may have different types
    @ivar storage: Actual storage for the option value(s) on a per
                   instance (descriptor) basis
    @type storage: dict
    '''

    __slots__ = ['name', 'defvalue', 'storage', '__weakref__']

    def __init__(self, name, defvalue):
        '''
        Constructor.
        Initializes the member variables

        @param name: Name of the option
        @type name: str
        @param defvalue: Default value of the option
        @type defvalue: Opaque type. Each option may have different types
        '''
        self.name = name
        self.defvalue = defvalue
        self.storage = dict()


    def __get__(self, instance, owner):
        '''
        Descriptor get

        @param instance: instance that wants to access the storage
        @type instance: object instance
        @param owner: Not used but needed for descriptor implementation
        @type owner: Not used
        @return: the value of the requested option (the default value if
                 the option had not been set yet
        @rtype: Opaque type. Each option may have different types
        '''
        with instance.lock:
            # XXX is deepcopy really needed?
            return self.storage.setdefault(instance, deepcopy(self.defvalue))


    def __set__(self, instance, value):
        '''
        Descriptor set

        @param instance: instance that wants to access the storage
        @type instance: object instance
        @param value: Value to set
        @type value: Opaque type. Each option may have different types
        '''
        with instance.lock:
            # XXX is deepcopy really needed?
            self.storage[instance] = deepcopy(value)


class HttxOptionsMeta(type):
    '''
    Metaclass for L{HttxOptions} to initialize the list of options
    on instantiation
    '''

    def __new__(mcs, name, bases, dict):
        '''
        On L{HttxOptions} instantiation the options present in the
        class variable I{defoptions} are added to the dictionary of the
        instance to start them with the default value
        '''
        for defoption in dict['defoptions']:
            dict[defoption.name] = defoption

        return type.__new__(mcs, name, bases, dict)


class HttxOptions(HttxObject):
    '''
    Class implementing a set of options per domain to be held by HttxLib
    connecting objects like L{HttxManager}, L{HttxNetLocation} and L{HttxConnection}

    @ivar defoptions: list of L{HttxOption} definitions
    @type defoptions: tuple

      - timeout
        Default value: 15 seconds
        Timeout for network operations

      - keepalive
        Default value: 90 seconds
        Timeout for HTTP keepalive

      - connkeepalive
        Default value: True
        Timeout for HTTP Send the 'Connection: Keep-Alive' header
        
      - sendfullurl
        Default value: False
        HTTP 1.1 allows this, but some servers may crash if they receive the full url

      - proxy
        Default value: None
        A dictionary of scheme:url tuples can be set to use proxy servers
        scheme can be * for any scheme or have the http/https values

      - compression
        Default value: False
        If True the body of a POST will be sent compressed. This is supported
        by very few servers

      - compmethod
        Default value: HttxCompressionSet('gzip')
        Method to use when sending compressed requests

      - decompression
        Default value: True
        Request compressed answers and decompress the body of an HTTP answer

      - autodecompression
        Default value: True
        Even if compression was not requested, decompressed answers that
        contain a compressed body

      - decompmethod
        Default value: HttxCompressionSet('gzip', 'deflate', 'bzip2')
        Methods to use when requesting compressed answers

      - useragent
        Default value: ''
        Sets the user agent header value

      - redirect
        Default value: True
        Allows or disallows redirection support

      - externalredirect
        Default value: True
        Allows or disallows external redirection support

      - maxredirect
        Default value: 3
        Maximum number of redirects to follow

      - rfc2616postredir
        Default value: True
        If a redir after a post as specified in RFC 2616 should be followed

      - cookies
        Default value: True
        Allows or disallows cookie support

      - cookiejar
        Default value: HttxCookieJar
        For internal storage of cookies in a HttxOptions domain

      - auth
        Default value: True
        Allows or disallows authentication support

      - authuser
        Default value: True
        Allows or disallows www authentication support

      - authproxy
        Default value: True
        Allows or disallows proxy authentication support

      - passmanager
        Default value: HttxPassManager
        Internal storage of username/password credentials for realm and urls

      - authcache
        Default value: HttxAuthCache
        Internal storage of authentication answers for reuse

      - certkeyfile
        Default value: HttxCertKeyManager
        Internal storage of certificate/private key pair of path to files
        containing the certificates and private keys for client
        validation
        Being empty at the beginning, no files will be used in client validation

      - certreq
        Default value: HttxCertReqManager
        Internal storage of requirement of validation for server certificates
        Being empty at the beginning, no validation will be performed

      - cacert
        Default value: HttxCACertManager
        Internal storage of root (chain of) certificates(s) for server
        certificate validation.
        Being empty at the beginning, no validation can be performed
    '''

    defoptions = (
        HttxOption('timeout', 15),
        HttxOption('keepalive', 90),
        HttxOption('connkeepalive', True),
        HttxOption('sendfullurl', False),
        HttxOption('proxy', None),
        HttxOption('compression', False),
        HttxOption('compmethod', HttxCompressionSet('gzip')),
        HttxOption('decompression', True),
        HttxOption('autodecompression', True),
        HttxOption('decompmethods', HttxCompressionSet('gzip', 'deflate', 'bzip2')),
        HttxOption('useragent', ''),
        HttxOption('redirect', True),
        HttxOption('externalredirect', True),
        HttxOption('maxredirects', 3),
        HttxOption('rfc2616postredir', True),
        HttxOption('cookies', True),
        HttxOption('cookiejar', HttxCookieJar()),
        HttxOption('auth', True),
        HttxOption('authuser', True),
        HttxOption('authproxy', True),
        HttxOption('passmanager', HttxPassManager()),
        HttxOption('authcache', HttxAuthCache()),
        HttxOption('certkeyfile', HttxCertKeyManager()),
        HttxOption('certreq', HttxCertReqManager()),
        HttxOption('cacert', HttxCACertManager()),
        )

    __metaclass__ = HttxOptionsMeta


    def __init__(self):
        '''
        Constructor. It delegates construction to the base class
        L{HttxObject}
        '''
        HttxObject.__init__(self)


    def __deepcopy__(self, memo):
        '''
        Deepcopy support.

        @param memo: standard __deepcopy__ parameter to avoid circular references
        @type memo: dict
        @return: a cloned object
        @rtype: L{HttxOptions}
        '''
        clone = self.__class__()

        # lock is un(deep)copyable
        # copy the attributes we want: options
        for defoption in self.defoptions:
            setattr(clone, defoption.name, deepcopy(getattr(self, defoption.name)))

        return clone


    def clone(self):
        '''
        Alias for deepcopy, for consistency with the rest of objects

        @return: a cloned object
        @rtype: L{HttxOptions}
        '''
        return deepcopy(self)


    def update(self, **kwargs):
        '''
        Given a set of keyword arguments update the value of options

        @param kwargs: keyword args
        @type kwargs: dict
        '''
        for option in kwargs:
            if hasattr(self, option):
                setattr(self, option, kwargs[option])
