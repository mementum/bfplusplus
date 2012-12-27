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
Implementation of Exceptions raised by HttxLib

Because HttxLib is built on top of httplib, all exceptions derive from
HTTPException to enable a catch-all case
'''

from httplib import HTTPException


class SocketException(HTTPException):
    '''
    A class representing a socket exception like closed connection,
    timeout, dns failure resolution and others

    HTTPException is HTTP centered, but the HttxLib wants to isolate
    the user from having to install their own except for a socket
    exception and therefore socket errors are caught
    '''

    def __init__(self, *args):
        '''
        Constructor. Passes the args to Exception as explicitly stated
        in the HTTPException definition in httplib.py

        @param args: list of arguments
        @type args: tuple
        '''
        Exception.__init__(self, *args)


# Alias
HttxSocketException = SocketException


class HttxException(HTTPException):
    '''
    A class representing a HTTP related exceptions raised by HttxLib

    @ivar response: response that has triggered the exception
    @type response: L{HttxResponse}
    '''

    def __init__(self, response, *args):
        '''
        Constructor. Passes the args to Exception as explicitly stated
        in the HTTPException definition in httplib.py

        @param response: response that has triggered the exception
        @type response: L{HttxResponse}
        @param args: list of arguments
        @type args: tuple
        '''
        Exception.__init__(self, *args)
        self.response = response


class RedirectError(HttxException):
    '''
    A class representing a redirection error (like missing location header,
    not allowed in a POST request and others)
    '''

    def __init__(self, response, *args):
        '''
        Constructor. Delegates construction to the base class L{HttxException}

        @param response: response that has triggered the exception
        @type response: L{HttxResponse}
        @param args: list of arguments
        @type args: tuple
        '''
        HttxException.__init__(self, response, *args)


class MaxRedirectError(RedirectError):
    '''
    A class representing an error because the configure maxiumum number
    of redirections has been reached
    '''

    def __init__(self, response, *args):
        '''
        Constructor. Delegates construction to the base class L{HttxException}

        @param response: response that has triggered the exception
        @type response: L{HttxResponse}
        @param args: list of arguments
        @type args: tuple
        '''
        HttxException.__init__(self, response, *args)


class ExternalRedirectError(RedirectError):
    '''
    A class representing an error because external redirections are disabled
    but the response redirected to an external host
    '''
    def __init__(self, response, *args):
        '''
        Constructor. Delegates construction to the base class L{HttxException}

        @param response: response that has triggered the exception
        @type response: L{HttxResponse}
        @param args: list of arguments
        @type args: tuple
        '''
        HttxException.__init__(self, response, *args)

