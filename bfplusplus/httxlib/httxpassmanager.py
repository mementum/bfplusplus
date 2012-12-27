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
HttxLib password manager implementation
'''

from copy import deepcopy
from urllib2 import HTTPPasswordMgrWithDefaultRealm

from httxobject import HttxObject


class HttxPassManager(HttxObject):
    '''
    An object manages username and password for url and realms
    with locking semantics to be used in L{HttxOptions}

    @ivar passmanager: storage for username, password credentials
    @type passmanager: HTTPPasswordMgrWithDefaultRealm
    '''

    def __init__(self):
        '''
        Constructor. It delegates construction to the base class
        L{HttxObject} and initializes the member variables
        '''
        HttxObject.__init__(self)

        self.passmanager = HTTPPasswordMgrWithDefaultRealm()


    def  __deepcopy__(self, memo):
        '''
        Deepcopy support.

        @param memo: standard __deepcopy__ parameter to avoid circular references
        @type memo: dict
        @return: a cloned object
        @rtype: L{HttxPassManager}
        '''
        clone = self.__class__()
        with self.lock:
            clone.passmanager = deepcopy(self.passmanager)
        return clone


    def add_password(self, realm, url, user, passwd):
        '''
        Stub replica for HTTPPasswordManagerWithDefaultRealm to
        add a username and a password for a real, url combination

        @param realm: where the credentials should be applied
                      None is a catch-all value
        @type realm: str|None
        @param url: base url for application of username, password
                    if realm matches. It can be empty to catch-all
        @type url: str
        @param user: username
        @type user: str
        @param passwd: username
        @type passwd: str
        '''
        with self.lock:
            self.passmanager.add_password(realm, url, user, passwd)


    def find_user_password(self, realm, url):
        '''
        Stub replica for HTTPPasswordManagerWithDefaultRealm to
        retrieve username, password for the given realm and url

        @param realm: where the credentials should be applied
                      None is a catch-all value
        @type realm: str|None
        @param url: base url for application of username, password
                    if realm matches. It can be empty to catch-all
        @return: tuple with the username, password values. It can be
                 None, None if not found
        @rtype: tuple
        '''
        with self.lock:
            return self.passmanager.find_user_password(realm, url)
