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
BfPy global variables and functions module.

@var libname: name of this library
@type libname: string
@var version: the version number of the library
@type version: float
@var libstring: the combined library name and version number
@type libstring: string

@type freeApiId: int
@var freeApiId: default Betfair product Id, the one for the free API
@type Global: int
@var Global: endPoint id (internal) for the Global Betfair endpoint service
@type Exchange: int
@var Exchange: endPoint id (internal) to point out that a call goes to an Exchange
@type ExchangeUK: int
@var ExchangeUK: endPoint id (Betfair) for the UK Exchange Betfair endpoint service
@type ExchangeAus: int
@var ExchangeAus: endPoint id (Betfair) for the Aus Exchange Betfair endpoint service
@type Exchanges: list
@var Exchanges: list of available Exchange endpoints
@type EndPoints: list
@var EndPoints: list of available Betfair EndPoints
@type EndPointUrls: list
@var EndPointUrls: list of available Betfair EndPoint Urls

@type wsdlDefs: dict
@var wsdlDefs: mapping of EndPoints to the WSDL contents

@type eventRootId: int
@var eventRootId: default parentEventId to identify ActiveEventTypes in the joint
                  call that unifies GetActiveEventTypes and GetEvents

@type preProcess: bool
@var preProcess: default library behaviour: process (easing use) the user requests
                 before sending them to Betfair
@type postProcess: bool
@var postProcess: default library behaviour: process (easing use) Betfair answers
                  before sending them to Betfair
@type catchAllExceptions: bool
@var catchAllException: catch and return as BfPythonError any possible error generated
                        along the library once a service has been called

@type separateCounters: bool
@var separateCounters: use separate counters (per exchange/endpoint) to throttle requests
                      of calls that fall under the DataRequest (default: False)
'''

libname = 'BfPy'
version = 1.11
libstring = '%s %s' % (libname, str(version))

freeApiId = 82

Vendor = -1
Global = 0
Exchange = 1
ExchangeUK = 1
ExchangeAus = 2

Exchanges = [ExchangeUK, ExchangeAus]
EndPoints = [Vendor, Global, ExchangeUK, ExchangeAus]

EndPointUrls = {
    Vendor: 'https://api.betfair.com/admin-api/v2/VendorService',
    Global: 'https://api.betfair.com/global/v3/BFGlobalService',
    ExchangeUK: 'https://api.betfair.com/exchange/v5/BFExchangeService',
    ExchangeAus: 'https://api-au.betfair.com/exchange/v5/BFExchangeService',
    }

try:
    import bfwsdl
except ImportError:
    wsdlDefs = dict()
else:
    wsdlDefs = {
        Vendor: bfwsdl.BFVendorService,
        Global: bfwsdl.BFGlobalService,
        ExchangeUK: bfwsdl.BFExchangeService,
        ExchangeAus: bfwsdl.BFExchangeServiceAus,
        }
    
eventRootId = -1

preProcess = True
postProcess = True

catchAllExceptions = True

separateCounters = False
