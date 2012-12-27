#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of BfPy
#
# BfPy is a Python library to communicate with the Betfair Betting Exchange
# Copyright (C) 2010 Daniel Rodriguez (aka Daniel Rodriksson)
# Copyright (C) 2011 Sensible Odds Ltd.
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/bfpy/
#
# BfPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BfPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BfPy. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
'''
BfPy exceptions
'''

class BfError(Exception):
    '''
    Base BfPy exception class. Any exception launched by the library
    will be a subclass of this

    @ivar requestName: (arg0) request to the API that generated the error
    @type requestName: str
    @ivar name: alias for requestName. For non API exceptions it shall hold
                a meaningful name
    @type name: str
    @ivar response: (arg1) response the API sent
    @type response: response object
    @ivar object: alias to response for non API exceptions, holding the
                  object/exception that was captured
    @type object: object/Exception
    @ivar text: (arg2) descriptive text for the exception
    @type text: str
    @ivar errorCode: (arg3) for API based exceptions, which errorCode was generated
    @type errorCode: str (Betfair enum)
    '''

    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the Exception constructor
        and unpacks the args into meaningful variables

        @param args: standard Python args
        @type args: list/tuple
        '''
        Exception.__init__(self, *args)
        self.requestName = args[0]
        self.name = args[0]
        self.response = args[1]
        self.object = args[1]
        self.text = args[2]
        self.errorCode = args[3]


class BfPythonError(BfError):
    '''
    Derived from BfError, holding potential Python errors (like missing method
    or syntax errors)
    '''

    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the base class constructor
        '''
        BfError.__init__(self, *args)


class BfTransportError(BfError):
    '''
    Derived from BfError, to hold error generated by BfTransport
    '''
    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the base class constructor
        '''
        BfError.__init__(self, *args)


class BfNetworkError(BfTransportError):
    '''
    Derived from BfError, to hold network errors
    '''

    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the base class constructor
        '''
        BfTransportError.__init__(self, *args)


class BfHttpError(BfTransportError):
    '''
    Derived from BfError, to hold error errors at Http level
    '''

    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the base class constructor
        '''
        BfTransportError.__init__(self, *args)


class BfHtmlError(BfTransportError):
    '''
    Derived from BfError, to hold error errors at Html level
    (You find yourself behind the proxy of a hotel and the proxy returns
    200 OK but of course not the expected XML response)
    '''

    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the base class constructor
        '''
        BfTransportError.__init__(self, *args)


class BfBetfairError(BfError):
    '''
    Derived from BfError. Catch all for Betfair API specific errors
    '''

    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the base class constructor
        '''
        BfError.__init__(self, *args)


class BfApiError(BfBetfairError):
    '''
    Derived from the Betfair Catch-all exceptions for API errors
    '''

    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the base class constructor
        '''
        BfBetfairError.__init__(self, *args)


class BfServiceError(BfBetfairError):
    '''
    Derived from the Betfair Catch-all exceptions for Service errors
    '''

    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the base class constructor
        '''
        BfBetfairError.__init__(self, *args)


class BfApplicationError(BfBetfairError):
    '''
    Derived from the Betfair Catch-all exceptions for application specific
    errors. Not used in the library
    '''

    def __init__(self, *args):
        '''
        Constructor. Saves the args by calling the base class constructor
        '''
        BfBetfairError.__init__(self, *args)

