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
Utility module to perform decompression of an http body
'''

from bz2 import decompress as bz2decompress
from gzip import GzipFile
from zlib import decompress as zlibdecompress, error as zliberror, MAX_WBITS as zlibMAX_WBITS

def httxdecompress(response):
    '''
    Decompression of the body from response.

    The supported compression types are gzip, bzip2 and deflate

    @param response: the response from the http server containing the body
    @type response: L{HttxResponse}
    '''

    decompmethod = response.getheader('content-encoding')

    if not decompmethod:
        return

    if decompmethod == 'gzip':
        gzipper = GzipFile(fileobj=response.bodyfile)
        response.body = gzipper.read()

    elif decompmethod == 'deflate':
        try:
            response.body = zlibdecompress(response.body)
        except zliberror:
            # Many web sites fail to send the first bytes of the header
            # possibly it is a header-stripped gzip file
            response.body = zlibdecompress(response.body, -zlibMAX_WBITS)

    elif decompmethod == 'bzip2':
        response.body = bz2decompress(response.body)
