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
This module implements a series of hacks to the HTTPResponse class to enable
extra functionaliy (and practical in some cases) for the HttxLib

Rather than creating a new class and given that HTTPResponse is already well
suited for usage in CookieJars (except for the missing info method), extending
the class seems suitable.

Subclassing is not possible, because the HTTPResponse is instantiated inside
httplib.

Creating a class and instantiating it out of the data stored in the HTTPResponse
would be possible but data would have to be copied for each response.

This alternative seems the better: patching the class definition at the start of
the program and therefore be able to use the instantiated HTTPResponse everywhere
'''

from cStringIO import StringIO
from httplib import HTTPResponse


def httxinit(self, sock, debuglevel=0, strict=0, method=None):
    '''
    It replaces the HTTPResponse.__init__ to allow to add and initialize
    a member variable at object instantiation

    Sock is the opaque type (actually a Python sock object) used in HttxLib
    to index connecting objects with pending network activity
    '''
    self._httxinit(sock, debuglevel=debuglevel, strict=strict, method=method)
    self.sock = None

HTTPResponse._httxinit = HTTPResponse.__init__
HTTPResponse.__init__ = httxinit



def httxredirecting_or_authenticating(self):
    '''
    Utility function to check if a response is underdoing a redirection
    or authentication and network activity is pending
    redirection
    
    @return: if the response is underdoing a redirection or authentication
             and network activity is pending
    @rtype: bool
    '''
    return self.redirecting() or self.authenticating()

def httxisredir(self):
    '''
    Utility function to check if a response is requesting redirection
    
    @return: if the response is a request to redirect
    @rtype: bool
    '''
    return self.status in (301, 302, 303, 307)

def httxisredirget(self):
    '''
    Utility function to check if the redir codes are good for a GET request

    @return: if the redir codes are good for a GET request
    @rtype: bool
    '''
    return self.status in (301, 302, 303, 307)

def httxisredirpost(self):
    '''
    Utility function to check if the redir codes are good for a POST request

    @return: if the redir codes are good for a POST request
    @rtype: bool
    '''
    return self.status in (301, 302, 303)

def httxisredirpostrfc2616(self):
    '''
    Utility function to check if the redir codes are good for a POST request
    according to RFC 2616

    @return: if the redir codes are good for a POST request
             according to RFC 2616
    @rtype: bool
    '''
    return self.status in (301, 302)

def httxisauth(self):
    '''
    Utility function to check if a response is requesting authentication

    @return: if a response is requesting authentication
    @rtype: bool
    '''
    return self.status in (401, 407)
    
def httxredirecting(self):
    '''
    Utility function to check if a response indicates that pending network
    activity exists, because a new request has been isssued following a
    redirect request

    @return: if a response is undergoing network activity because a
             redirection request has been sent
    @rtype: bool
    '''
    return self.sock and self.isredir()

def httxauthenticating(self):
    '''
    Utility function to check if a response indicates that pending network
    activity exists, because a new request has been isssued following an
    authentication request

    @return: if a response is undergoing network activity because an
             authentication request has been sent
    @rtype: bool
    '''
    return self.sock and self.isauth()

def httxisauthuser(self):
    '''
    Utility function to check if the requested authentication is www-authenticate

    @return: if the requested authentication is www-authenticate
    @rtype: bool
    '''
    return self.status == 401

def httxisauthproxy(self):
    '''
    Utility function to check if the requested authentication is proxy-authenticate

    @return: if the requested authentication is proxy-authenticate
    @rtype: bool
    '''
    return self.status == 407


HTTPResponse.redirecting = httxredirecting
HTTPResponse.authenticating = httxauthenticating
HTTPResponse.isauthuser = httxisauthuser
HTTPResponse.isauthproxy = httxisauthproxy
HTTPResponse.redirecting_or_authenticating = httxredirecting_or_authenticating
HTTPResponse.isactive = httxredirecting_or_authenticating
HTTPResponse.isauth = httxisauth
HTTPResponse.isredir = httxisredir
HTTPResponse.isredirget = httxisredirget
HTTPResponse.isredirpost = httxisredirpost
HTTPResponse.isredirpostrfc2616 = httxisredirpostrfc2616

def httxinfo(self):
    '''
    Utility function to make HTTPResponse fully compatible with CookieJar requirements

    @return: the message object from HTTPResponse
    @rtype: HTTPMessage
    '''
    return self.msg

HTTPResponse.info = httxinfo


def httxbegin(self):
    '''
    Wrapper for HTTPResponse.begin to allow for the body to be read and leave the
    connection free for further re-use
    '''
    # HTTPResponse will return if self.msg has been filled with
    # an object. In such a case we will already have performed
    # a read and have a body attribute available for us
    # If not needed, de-activate the code below
    if self.msg is not None:
        return

    # Call the original begin method
    self._httxbegin()

    # Fill the body with all the content in which will set this
    # response as "closed" (just the response, no the connection)
    # Call the original read method
    self.setbody(self._httxread())


HTTPResponse._httxbegin = HTTPResponse.begin
HTTPResponse.begin = httxbegin


def httxread(self, amt=None):
    '''
    Wrapper for HTTPResponse.read to read the body contents from the
    StringIO object created during httxbegin
    connection free for further re-use

    @param amt: amount of bytes to be read
    @type amt: int or None
    @return: the read bytes 
    @rtype: str
    '''
    # the read method should never be called before begin
    # we assume that begin has been called and therefore we
    # have our file-like object created
    return self._httxbodyfile.read(amt)

HTTPResponse._httxread = HTTPResponse.read
HTTPResponse.read = httxread


# Property alias to manage the body and the creation of the
# body file object
def httxgetbody(self):
    '''
    Utility function for a property get descriptor for body

    @return: the body of the http response
    @rtype: str
    '''
    return self._httxbody

def httxsetbody(self, value):
    '''
    Utility function for a property set descriptor for body

    @param value: the body of the http response to set
    @type value: str
    '''
    self._httxbody = value
    self._httxbodyfile = StringIO(self._httxbody)

HTTPResponse.getbody = httxgetbody
HTTPResponse.setbody = httxsetbody
HTTPResponse.body = property(HTTPResponse.getbody, HTTPResponse.setbody)


# Alias to get the body file object
def httxgetbodyfile(self):
    '''
    Utility function for a property tet descriptor for bodyfile
    '''
    return self._httxbodyfile

HTTPResponse.getbodyfile = httxgetbodyfile
HTTPResponse.bodyfile = property(HTTPResponse.getbodyfile)

# Property alias
HTTPResponse.headers = property(HTTPResponse.getheaders)


# Make a class alias
HttxResponse = HTTPResponse

