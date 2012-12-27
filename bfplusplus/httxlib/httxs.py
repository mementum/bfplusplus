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
Reimplementation of HTTPSConnection to allow for certificate validation
'''

import socket

try:
    from httplib import HTTPSConnection
    import ssl
except ImportError:
    pass
else:
    class HttxsConnection(HTTPSConnection):
        '''
        Reimplementation of HTTPSConnection to allow certificate validation

        HTTPSConnection omitted this possibilitiy which is supported by the
        Python ssl library and the wrap_socket functionality

        HTTPSConnection is subclassed, receives two new member variables
        and overrides connect to better call ssl.wrap_socket

        Please read the Python 2.6 documentation on SSL and certificate validation

        @ivar cert_reqs: It dictates if certificate validation will be done.
                         It uses the ssl: CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED
                         values from the ssl module
        @type cert_reqs: enumeration
        @ivar ca_certs: Path to the file containing the root (chain of)
                        certificate(s)
        @type ca_certs: str
        '''

        def __init__(self, host, port=None, key_file=None, cert_file=None,
                     strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
            '''
            Constructor. It delegates construction to the base class
            HTTPConnection and initializes the new member variables
            with the default values from the Python documentation

            @param host: host to connect to
            @type host: str
            @param port: port to connect to. use None for the default HTTP port
            @type port: int|None
            @param key_file: path to private key_file or None if stored in cert_file
            @type key_file: str|None
            @param cert_file: path to certificate to be used for validation or None
            @type cert_file: str|None
            @param strict: n/a
            @type strict: Unknown
            @param timeout: default time for network operations
            @type timeout: float
            '''
            HTTPSConnection.__init__(self, host, port, key_file, cert_file, strict, timeout)
            self.cert_reqs = ssl.CERT_NONE
            self.ca_certs = None

        def connect(self):
            '''
            Establishes the connection (ssl) to a host on a port and with
            the parameters given in the constructor

            Overrides the default HTTPSConnection.connect and uses the
            cert_reqs and ca_certs member variables to enable certificate
            validation if set to do so
            '''
            sock = socket.create_connection((self.host, self.port), self.timeout)
            if self._tunnel_host:
                self.sock = sock
                self._tunnel()
            self.sock = ssl.wrap_socket(sock,
                                        self.key_file, self.cert_file,
                                        cert_reqs=self.cert_reqs, ca_certs=self.ca_certs)

