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
Base Object for Connecting objects and primitives
'''

from httxcompressionset import HttxCompressionSet
from httxobject import HttxObject
from httxoptions import HttxOptions

class HttxBase(HttxObject):
    '''
    Base of HttxLib classes that make a connection providing the
    definition and (in some cases) the implementation of primitives

    @ivar options: The shared options for the connection(s)
    @type options: L{HttxOptions}
    '''
    def __init__(self, **kwargs):
        '''
        Contructor

        @param kwargs: keyword arguments for L{HttxOptions}
        @see: L{HttxOptions}
        '''
        HttxObject.__init__(self)

        self.options = kwargs.get('options', HttxOptions())
        self.options.update(**kwargs)


    def setoptions(self, **kwargs):
        '''
        Sets the I{options} at any time during execution

        @param kwargs: keyword arguments for L{options}
        @see: L{HttxOptions}
        '''
        self.options.update(**kwargs)


    def setuseragent(self, useragent):
        '''
        Helper method to set the User-Agent header

        @param useragent: the user agent to fake
        @type useragent: str
        '''
        self.options.update(useragent=useragent)


    def setdecompmethods(self, decompmethods):
        '''
        Helper method to set the decompression methods

        @param decompmethods: desired decompression methods
        @type decompmethods: list
        '''
        self.options.update(decompmethods=HttxCompressionSet(*decompmethods))


    def add_password(self, realm, url, username, password):
        '''
        Sets a I{username} and I{password} for a realm and base url
        @param realm: Realm of application. It can be None
        @type realm: str

        @param url: base url for which to apply. It can be empty to match all
        @type url: str
        @param username: username for realm and base url
        @type username: str
        @param password: username for realm and base url
        @type password: str
        '''
        self.options.passmanager.add_password(realm, url, username, password)


    def add_certkey(self, url, certfile, keyfile):
        '''
        Sets a I{certificate file} and (if needed) a I{private key file}
        to be used for https authentication in the domain given in the url
        The private key file is needed if the private key is not stored in the
        certificate. Please check the Python SSL documentation to learn more

        @param url: url (domain) for which to apply. It can be empty to match all
        @type url: str
        @param certfile: path to the cerfiticate file to be used
        @type certfile: str
        @param keyfile: path to the private key file (if not stored in the cerfiticate)
        corresponding to the certificate
        @type keyfile: str
        '''
        self.options.certkeyfile.add_certkey(url, certfile, keyfile)


    def add_cert_req(self, url, cert_req):
        '''
        Sets the certificate verification level for the server certificate in the given
        url. A (chain of) root certificate(s) has to be supplied with L{add_ca_cert}
        Please check the Python SSL documentation

        @param url: url (domain) for which to apply. It can be empty to match all
        @type url: str
        @param cert_req: verification level
        @type cert_req: enumeration ssl.CERT_NONE, ssl.CERT_OPTIONAL, ssl.CERT_REQUIRED
        @see: L{add_ca_cert}
        '''
        self.options.certreq.add_cert_req(url, cert_req)


    def add_ca_cert(self, url, ca_cert):
        '''
        Sets the path to a file that contains the root (chain) certificate(s) to be used
        if the certificate of the server pointed by url has been requested to be
        verified with L{add_cert_req} and I{ssl.CERT_OPTIONAL} or I{ssl.CERT_REQUIRED}
        was specified
        Please check the Python SSL documentation

        @param url: url (domain) for which to apply. It can be empty to match all
        @type url: str
        @param ca_cert: path to a file containing the root (chain) certificate(s)
        @type ca_cert: str
        @see: L{add_cert_req}
        '''
        self.options.cacert.add_ca_cert(url, ca_cert)


    def setproxy(self, proxy):
        '''
        Set the proxy for the HttxLib connecting object.
        This is the abstract definition. To be implemented by connecting objects
        The proxy can be different for http and https connections.

        @param proxy: proxy servers. Dictionary with scheme:url pairs.
                      '*' as scheme stands for both http and https
        @type proxy: dict
        @raise NotImplemented
        '''
        raise NotImplemented


    def request(self, httxreq):
        '''
        Send the L{HttxRequest} httxreq to the specified server inside the request
        This is the abstract definition. To be implemented by connecting objects

        @param httxreq: Request to be executed
        @type httxreq: L{HttxRequest}
        @return: sock
        @rtype: opaque type for the caller (a Python sock)
        @raise NotImplemented
        '''
        raise NotImplemented


    def getresponse(self, sock):
        '''
        Recover a L{HttxResponse} corresponding to the sock (returned by L{request}
        This is the abstract definition. To be implemented by connecting objects

        @param sock: The opaque type returned by L{request}
        @type sock: opaque (a Python sock)
        @return: response
        @rtype: L{HttxResponse} (compatible with httplib HTTPResponse)
        @raise NotImplemented
        '''
        raise NotImplemented


    def urlopen(self, httxreq):
        '''
        Fecth a url specified in the  L{HttxRequest} httxreq object
        and return it in the form of an L{HttxResponse}

        @param httxreq: Request to be fetched
        @type httxreq: L{HttxRequest}
        @return: response
        @rtype: L{HttxResponse} (compatible with httplib HTTPResponse)
        '''
        sock = self.request(httxreq)

        while True:
            response = self.getresponse(sock)

            # getresponse may have returned but still be active because a
            # redirection or authentication request may be pending
            if not response.isactive():
                break

            # Used the sock inside the response, since it may be different
            sock = response.sock

        return response




    
