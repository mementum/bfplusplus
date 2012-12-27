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
HttxConnection connecting object. L{HttxConnection} implementation
@var _httpsconnection: if ssl is active it will hold a reference to the class type
                       to create https capable connections
@type _httpsconnection: class
'''

from collections import deque
from copy import deepcopy
from cStringIO import StringIO
from httplib import HTTPConnection
try:
    from httxs import HttxsConnection as _httpsconnection
except ImportError:
    _httpsconnection = None

from socket import error as SocketError, IPPROTO_TCP, TCP_NODELAY
from ssl import CERT_NONE
from urlparse import urlsplit
import sys
if sys.platform == 'win32':
    from time import clock as tclock
else:
    from time import time as tclock

from httxauth import authbasic, authdigest
from httxbase import HttxBase
from httxcompression import httxdecompress
from httxerror import SocketException, RedirectError, MaxRedirectError, ExternalRedirectError
from httxutil import parse_keqv_list, parse_http_list


class HttxConnection(HttxBase):
    '''
    Connection connecting object. The HttxConnection is responsible for creating
    and managing an underlying httplib.HTTPConnection or a L{HttxsConnection} (for HTTPS)
    to perform the actual connection

    The creation of the underlying connection is based upon a dictionary holding the
    class types indexed by the connection scheme (http or https)

    The connection handles automatically redirection, authentication (auth and digest)
    and decompression (gzip, bzip2, deflate)

    The behaviour can be altered through by managing the options

    @ivar connFactory: class variable holding the dictionary of connection
                       classes used to instantiate connections
    @type connFactory: dict

    @ivar url: url used to set the net location to which connections will
               connect
    @type url: str
    @ivar parsed: it holds the result of urlsplit(url) for practical purposes
    @type parsed: namedtuple from urlsplit
    @ivar redircount: count of redirections so far performed
    @type redircount: int
    @ivar lastreq: Last L{HttxRequest} request issued
    @type lastreq: L{HttxRequest}
    @ivar auxhttx: Reference to the auxiliary connection used for either
                   authentication or rediretion if needed
    @type auxhttx: L{HttxConnection}
    @ivar conn: actual connection object
    @type conn: httplib.HTTPConnection or L{HttxsConnection} - subclass of
                httplib.HTTPSConnection
    @ivar timestamp: last time the connection was used
    @type int
    '''
    connFactory = dict(http=HTTPConnection)
    if _httpsconnection:
        connFactory['https'] = _httpsconnection

    def __init__(self, url = None, **kwargs):
        '''
        Constructor. It delegates construction to the base class
        L{HttxBase} and initializes the member variables with the help
        of the L{createconnection} method

        @param kwargs: keywords arguments passed to L{HttxBase}
        @see: L{HttxOptions}
        '''
        HttxBase.__init__(self, **kwargs)

        self.redircount = kwargs.get('redircount', 0)
        self.lastreq = None
        self.auxhttx = None
        self.createconnection(url)


    def __deepcopy__(self, memo):
        '''
        Deepcopy support.

        @param memo: standard __deepcopy__ parameter to avoid circular references
        @type memo: dict
        @see L{clone}
        @return: a cloned object
        @rtype: L{HttxConnection}
        '''
        return self.clone()
    

    def clone(self, options=None):
        '''
        Clone the object using the supplied options or a new set of options if
        given.

        An equivalente set of L{HttxConnection} objects will be replicated

        A new set of options will separate the clone object from the original
        object, since they will no longer share cookies, user/password/realm
        combinations or https certificates

        To support a maximum redirection count, a redircount parameter is passed
        along during the construction of the clone

        @param options: options for the cloned object
        @type options: L{HttxOptions}
        @return: a cloned object
        @rtype: L{HttxConnection}
        '''
        if not options:
            options = self.options.clone()
        return self.__class__(self.url, redircount=self.redircount, options=options)


    @property
    def sock(self):
        '''
        Property to support easy and quick access to the underlying sock object
        from the underlying connection.

        The sock object is used in the library to index active connections inc
        cache
        '''

        # @return: The opaque type to reference this connection
        # @rtype: opaque type (a Python sock)
        return self.conn.sock


    def createconnection(self, url):
        '''
        Helper function to enable delayed creation of the underlying connection
        if needed. Called from the L{__init__} and from L{request} in order
        to ensure an underlying connection is created

        It initializes the member variables: I{url}, I{parsed}, L{conn}, I{clock}

        In the case of https connections it will also set variables in the
        underlying connection object to ensure certificates and validation
        are used if requested and appropriate for the domain

        @param url: url to open a connection to
        @type url: str
        '''
        if not url:
            self.conn = None
            return

        self.url = url
        self.parsed = urlsplit(self.url)

        self.conn = self.connFactory[self.parsed.scheme](self.parsed.hostname, self.parsed.port, timeout=self.options.timeout)

        if self.parsed.scheme == 'https':
            key_file, cert_file = self.options.certkeyfile.find_certkey(self.url) 
            self.conn.key_file = key_file
            self.conn.cert_file = cert_file
            
            self.conn.cert_reqs = self.options.certreq.find_cert_req(self.url)
            if self.conn.cert_reqs != CERT_NONE:
                self.conn.ca_certs = self.options.cacert.find_ca_cert(self.url)

        # Force HTTPConnection to connect to have the sock object available
        try:
            self.conn.connect()
        except SocketError, e:
            raise SocketException(*e.args)

        # Set TCP_NODELAY
        try:
            self.conn.sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
        except:
            # It may not be supported on all systems
            pass

        self.timestamp = tclock()


    def request(self, httxreq):
        '''
        Send the L{HttxRequest} httxreq to the specified server inside the request
        It does so by creating a connection if needed, then setting headers with
        helper functions for ompression, cookies and authentication and then
        relaying the call to the underlying connection
        
        @param httxreq: Request to be executed
        @type httxreq: L{HttxRequest}
        @return: sock
        @rtype: opaque type for the caller (a Python sock)
        '''
        # Create the connection if needed
        if not self.conn:
            self.createconnection(httxreq.get_full_url())

        # Add the appropriate headers for the outgoing request
        self.addkeepalive(httxreq)
        self.adddecompress(httxreq)
        self.addcookies(httxreq)
        self.addauth(httxreq)
        self.adduseragent(httxreq)
        self.addcontent(httxreq)

        # Decide if which is the url to send to the server
        if self.parsed.netloc != httxreq.netloc or self.options.sendfullurl:
            # connection is proxying or the user wants to send the full url
            url = httxreq.get_full_url()
        else:
            # use the short version of the url (less problematic if not proxying)
            url = httxreq.get_selector()

        # Execute the request
        try:
            self.conn.request(httxreq.get_method(), url, httxreq.body, httxreq.allheaders)
        except SocketError, e:
            raise SocketException(*e.args)

        # If no exception, we may save the request to be used by getresponse
        self.lastreq = httxreq

        # Update the timestamp
        self.timestamp = tclock()

        # Async applications need something to wait on. Return our socket
        return self.conn.sock


    def getresponse(self, sock):
        '''
        Recover a L{HttxResponse}

        The sock parameter is not used but the function follows the abstract
        definition of L{HttxBase} and the implementations of L{HttxManager}
        and L{HttxNetLocation}

        Checks for authentication requests or redirectionare made. If the
        options allow to process those requests, new requests (with potentially
        new connections) are launched and the connection is marked as active
        to avoid any other part of the library to reuse it

        Decompression of content and cookie extraction is also performed
        
        @param sock: The opaque type returned by L{request}
        @type sock: opaque (a Python sock)
        @return: response
        @rtype: L{HttxResponse} (compatible with httplib HTTPResponse)
        '''

        # if we have an AUXHTTX and it's not SELF -> REDIR was made
        if self.auxhttx and self.auxhttx is not self:

            # Get the response from the redirecting connection
            response = self.auxhttx.getresponse(sock)

            # Remove the redirection unless the process is not over
            # The auxhttx could now be further redirecting or authenticating
            if not response.isactive():
                self.auxhttx = None

            return response

        # No auxiliary connection for redirection or is auxhttx is self (auth)
        try:
            response = self.conn.getresponse()
        except SocketError, e:
            raise SocketException(*e.args)

        if self.options.sendfullurl:
            # FIXME: Some HTTP/1.1 servers may close the connection upon receiving
            # the full url instead of keeping it open. Can I detect it and do
            # a (re)"connect" to overcome te problem?
            pass

        # Extract the cookies and try to decompress the body
        self.extractcookies(response)
        self.decompress(response)

        # Check for AUTH
        if response.isauth():
            if self.auxhttx:
                # we were awaiting auth and got auth back, clear auxhttx and return the auth request
                self.auxhttx = None
                return response

            return self.authenticate(response)

        # clean any possible remaining auxhttx flag
        self.auxhttx = None

        # Check for REDIRection
        if response.isredir():
            return self.redirect(response)

        return response


    def addcookies(self, httxreq):
        '''
        Add a Cookie header to httxreq if needed
        It uses a urllib2 cookiejar from the options set
        
        @param httxreq: Request to be executed
        @type httxreq: L{HttxRequest}
        '''
        if self.options.cookies:
            self.options.cookiejar.add_cookie_header(httxreq)


    def adddecompress(self, httxreq):
        '''
        Add a content-encoding header to httxreq if needed and set in the options
        
        @param httxreq: Request to be executed
        @type httxreq: L{HttxRequest}
        '''
        if self.options.decompression:
            httxreq.add_header('Accept-Encoding', self.options.decompmethods.join())


    def addauth(self, httxreq):
        '''
        Add a WWW-Authenticate or Proxy-Authenticate header to httxreq
        if needed and set in the options

        It uses a L{HttxAuthCache} from the options
        
        @param httxreq: Request to be executed
        @type httxreq: L{HttxRequest}
        '''
        parsed = urlsplit(httxreq.get_full_url())

        headername, headerval = self.options.authcache.get(parsed.geturl())

        if headername is not None:
            httxreq.add_unredirected_header(headername, headerval)


    def addkeepalive(self, httxreq):
        '''
        Adds the Connection Keep-Alive header

        @param httxreq: Request to be executed
        @type httxreq: L{HttxRequest}
        '''
        if self.options.connkeepalive:
            httxreq.add_header('Connection', 'Keep-Alive')


    def adduseragent(self, httxreq):
        '''
        Adds the UserAgent header if needed to

        @param httxreq: Request to be executed
        @type httxreq: L{HttxRequest}
        '''
        if self.options.useragent:
            httxreq.add_header('User-Agent', self.options.useragent)


    def addcontent(self, httxreq):
        '''
        Add headers to httxreq if data is transmitted, borrowed from urllib2.

        @param httxreq: Request to be executed
        @type httxreq: L{HttxRequest}
        '''
        if httxreq.body and httxreq.ispost() and not httxreq.has_header('Content-Type'):
            httxreq.add_unredirected_header('Content-Type', 'application/x-www-form-urlencoded')


    def extractcookies(self, response):
        '''
        Perform cookie extraction from a response into a urllib2 cookiejar
        in the options set

        @param response: A response being processed
        @type response: L{HttxResponse}
        '''
        if self.options.cookies:
            self.options.cookiejar.extract_cookies(response, self.lastreq)


    def decompress(self, response):
        '''
        Perform body decompression if enabled by the options and present
        in the response

        @param response: A response being processed
        @type response: L{HttxResponse}
        '''
        if not self.options.decompression and not self.options.autodecompression:
            return

        httxdecompress(response)


    def redirect(self, response):
        '''
        Perform redirection if the response requests it and enabled by the
        options set

        @param response: A response being processed
        @type response: L{HttxResponse}
        @return: The same response with a new sock if redirection is
                          done to an external site
        @rtype: L{HttxResponse}
        '''
        if not self.options.redirect:
            # redirection is disabled -- return the original response
            return response

        if self.redircount == self.options.maxredirects:
            # already redirected the maximum number of times
            raise MaxRedirectError(response, 'Reached the maximum number of redirects')

        if self.lastreq.ispost() and not response.isredirpost():
            raise RedirectError(response, '307 redirection code for a POST request')

        if self.lastreq.ispost() and response.isredirpostrfc2616() and not self.options.rfc2616postredir:
            return response

        locationurl = response.getheader('location', None)

        if not locationurl:
            raise RedirectError(response, 'Redirect error: missing location header')

        parsed = urlsplit(locationurl)

        # Fix relative redirect urls
        if not parsed.scheme or not parsed.netloc:
            parsed = list(parsed)
            parsed[:2] = self.lastreq.scheme, self.lastreq.netloc
            parsed = SplitResult(*parsed)
            locationurl = urlunsplit(parsed)

        if not self.options.externalredirect and self.lastreq.netloc != parsed.netloc:
            # if the redirect netloc is not the one requested and external is not allowed - bail out
            raise ExternalRedirectError(response, 'External redirect not allowed')

        # check if this connection was acting in proxy mode by comparing the netloc passed to the constructor
        # with that passed in the request
        if self.parsed.netloc != self.lastreq.netloc:
            auxhttxurl = self.url
        else:
            auxhttxurl = locationurl

        # create a new connection with the redirection count increased
        auxhttx = self.__class__(auxhttxurl, redircount=self.redircount + 1, options=self.options)

        # Create a clone of the request with the new url
        redirreq = self.lastreq.clone(locationurl)

        # send the request and store the socket in the response
        response.sock = auxhttx.request(redirreq)

        self.auxhttx = auxhttx

        return response


    def authenticate(self, response):
        '''
        Perform authentication if the response requests it and enabled by the
        options set

        @param response: A response being processed
        @type response: L{HttxResponse}
        @return: The same response preocessed 
        @rtype: L{HttxResponse}
        '''
        authheaderserver = {401:'www-authenticate', 407:'proxy-authenticate'}
        authheaderclient = {401:'authorization', 407:'proxy-authorization'}

        if not self.options.auth:
            return response

        if response.isauthuser() and not self.options.authuser:
            return response

        if response.isauthproxy() and not self.options.authproxy:
            return response

        authheader = response.getheader(authheaderserver[response.status])
        authscheme, authchallenge = authheader.split(' ', 1)
        authscheme = authscheme.lower()
        authchallenge = parse_keqv_list(parse_http_list(authchallenge))

        realm = authchallenge['realm']
        username, password = self.options.passmanager.find_user_password(realm, self.lastreq.get_full_url())

        # None is "not empty strings"
        if username is None or password is None:
            return response

        authanswer = None
        authcachedata = None

        if authscheme == 'basic':
            authanswer, authcachedata = authbasic(username, password, authchallenge)

        elif authscheme == 'digest':
            if 'nonce' in authchallenge:
                nonce_count = self.options.authcache.getnoncecount(authchallenge['nonce'])
                authanswer, authcachedata = authdigest(username, password, authchallenge, self.lastreq, nonce_count)

        else:
            # XXX Pluggable authhandlers
            # authhandler = self.options.authhandler.get(authscheme)
            # authanswer, authcachedata = authhandler(username, password, authchallenge)
            pass

        if not authanswer:
            return response

        authorization = '%s %s' % (authscheme, authanswer)

        # Create a clone of the request with the new url
        authreq = self.lastreq
        authreq.add_unredirected_header(authheaderclient[response.status], authorization)

        response.sock = self.request(authreq)
        self.auxhttx = self

        # store it together with the authorization string - with parsed.url
        parsed = urlsplit(authreq.get_full_url())
        self.options.authcache.set(parsed.geturl(), authheaderclient[response.status], authscheme, authcachedata)

        return response
