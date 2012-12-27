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
Extensions of a L{HttxPassManager} to be used to hold paths
to certificate files or values for certificate validation

The locking semantics are all implemented in the L{HttxPassManager}
'''

try:
    from ssl import CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED
except ImportError:
    CERT_NONE = 0
    CERT_OPTIONAL = 1
    CERT_REQUIRED = 2

from urlparse import urlsplit

from httxpassmanager import HttxPassManager


class HttxCertKeyManager(HttxPassManager):
    '''
    A subclass of L{HttxPassManager} to hold paths to private key and
    certificate files to be used in client validation in https connections

    Usually the certificate file contains the private key too, but if this
    is not the case, the path to the file containing the private key has to
    also be supplied

    The class stores the cert_file/private_key_file tuple for a given url

    A catch_all empty string can be used to validate against any url

    The storage functionality is implemented by the HTTPPasswordManagerWithDefaultRealm
    used by L{HttxPassManager} and using a default Realm of None
    '''

    def __init__(self):
        '''
        Constructor. It delegates construction to the base class
        L{HttxPassManager}
        '''
        HttxPassManager.__init__(self)


    def add_certkey(self, url, certfile, keyfile):
        '''
        Add paths to the certificate and private key

        @param url: url to be matched for certificate/private key files
        @type url: str
        @param certfile: path to the certificate file
        @type certfile: str
        @param keyfile: path to the private key file if not contained in the
                        certificate file
        @type keyfile: str
        '''
        parsed = urlsplit(url)
        self.add_password(None, parsed.netloc, certfile, keyfile)


    def find_certkey(self, url):
        '''
        Retrieves a tuple of (certfile, keyfile) for a given url

        @param url: url to be matched for certificate/private key files
        @type url: str
        @return: tuple of (certfile, keyfile) that may be None
        @rtype: tuple
        '''
        parsed = urlsplit(url)
        certfile, keyfile = self.find_user_password(None, parsed.netloc)
        return certfile, keyfile



class HttxCertReqManager(HttxPassManager):
    '''
    A subclass of L{HttxPassManager} to hold the requirement for server
    certificate validation in https connections.

    It stores the requirement on a per url basis by transforming the
    enumeration value into a string on storage and undoing the operation
    on retrieval

    A catch_all empty string can be used to validate against any url

    @ivar certReqs: mapping of enumeration to string for storage
    @type certReques: dict
    @ivar certReqsInv: inverse mapping of enumeration to string for storage
    @type certRequesInv: dict
    '''

    certReqs = {CERT_NONE: 'CERT_NONE', CERT_OPTIONAL: 'CERT_OPTIONAL', CERT_REQUIRED: 'CERT_REQUIRED'}
    certReqsInv = {'CERT_NONE': CERT_NONE, 'CERT_OPTIONAL': CERT_OPTIONAL, 'CERT_REQUIRED': CERT_REQUIRED}

    def __init__(self):
        '''
        Constructor. It delegates construction to the base class
        L{HttxPassManager}
        '''
        HttxPassManager.__init__(self)


    def add_cert_req(self, url, cert_req):
        '''
        Add validation requirement for the given url

        @param url: url to be matched for certificate/private key files
        @type url: str
        @param cert_req: validation requirement from SSL
                         CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED
        @type cert_req: str
        '''
        parsed = urlsplit(url)
        self.add_password(None, parsed.netloc, self.certReqs[cert_req], '')


    def find_cert_req(self, url):
        '''
        Retrieve validation requirement for the given url

        @param url: url to be matched for certificate/private key files
        @type url: str
        @return: the validation requirement
        @rtype: int
        '''
        parsed = urlsplit(url)
        cert_req, emptyField = self.find_user_password(None, parsed.netloc)
        return self.certReqsInv[cert_req] if cert_req is not None else CERT_NONE


class HttxCACertManager(HttxPassManager):
    '''
    A subclass of L{HttxPassManager} to hold the path to a file containing
    the root (chain of) certificate(s) to be used in server certificate
    validation

    It stores the requirement on a per url basis by transforming the
    enumeration value into a string on storage and undoing the operation
    on retrieval

    It is separate from the Validation Requirement storage because this
    file may be use for all servers, but validation may not be required
    for all servers

    A catch_all empty string can be used to validate against any url
    '''
    
    def __init__(self):
        '''
        Constructor. It delegates construction to the base class
        L{HttxPassManager}
        '''
        HttxPassManager.__init__(self)


    def add_ca_cert(self, url, cacert):
        '''
        Add a path to a file with a root (chain of) certificates
        for the given url

        @param url: url to be matched for certificate/private key files
        @type url: str
        @param cacert: path to a file containing the certificates
        @type cacert: str
        '''
        parsed = urlsplit(url)
        self.add_password(None, parsed.netloc, cacert, '')


    def find_ca_cert(self, url):
        '''
        Retrieve the path to a file containing the root certificates
        for the given url

        @param url: url to be matched for certificate/private key files
        @type url: str
        @return: the path to the file with the root certificates or None
        @rtype: str|None
        '''
        parsed = urlsplit(url)
        cacert, emptyField = self.find_user_password(None, parsed.netloc)
        return cacert
