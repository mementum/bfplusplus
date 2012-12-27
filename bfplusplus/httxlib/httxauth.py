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
#
# NOTES:
#
#   The authdigest code has been adapted from Python 2.6.5 httplib code
#   making it apt for 1st authentication and 2nd-nth authentication
#   and cleaning other dependencies like parsing of the header fields
#   get_cnonce and get_algorithm_impls are also part of the httplib
#   implementation
#
###############################################################################

'''
Authentication functions to answer to Basic and Digest HTTP authentication
challenges
'''

from base64 import b64encode

from httxutil import *

def authbasic(username, password, authchallenge):
    '''
    Given a username and a password return an HTTP Basic Authentication
    challenge.

    The authchallenge parameter is just for harmony with authdigest
    and for potentially defining a plug-in interface for other
    authentications
        
    @param username: The username to reply to the challenge
    @type username: str
    @param password: The password to reply to the challenge
    @type password: str
    @return: A tuple containing a base64 encoded challenge and
             a string with a cache-able challenge for future responses
             The second value can be None
    @rtype: tuple (str, str|None)
    '''
    # Remove the trailing end of line
    # base64auth = base64encode('%s:%s' % (username, password))[:-1]
    base64auth = b64encode('%s:%s' % (username, password)).rstrip()

    return (base64auth, None)


def authdigest(username, password, challenge, request, nonce_count):
    '''
    Given a username, password, a list of challenge fields, a request
    a sequence number (nonce_count) return a Diget Auth challenge
    answer

    If username is None, then challenge will contain a username key with
    the username and the password parameter will be the cached value of
    the HA1 (see the function below) to be used

    @param username: The username to reply to the challenge or None to
                     indicate that the password contains a HA1 cache
    @type username: str|None
    @param password: The password to reply to the challenge or a HA1 cache
    @type password: str
    @param challenge: Dictionary with the parameters in the challenge
    @type challenge: dict
    @param request: The request that has generated the auth challenge
    @type request: L{HttxRequest}
    @param nonce_count: Sequence value if this not the first time such
                        a request has been seen. Used by Digest auth to
                        prevent replay attacks
    @type nonce_count: int
    @return: A tuple containing a digest answer  and
             a string with a cache-able challenge for future responses
             Both values can be None if a specific non-supported variant
             of the Digest Auth is used
    @rtype: tuple (str|None, str|None)
    '''
    try:
        realm = challenge['realm']
        nonce = challenge['nonce']
    except KeyError:
        return (None, None)

    qop = challenge.get('qop')
    algorithm = challenge.get('algorithm', 'MD5')
    # mod_digest doesn't send an opaque, even though it isn't supposed to be optional
    opaque = challenge.get('opaque', None)

    H, KD = get_algorithm_impls(algorithm)
    if H is None:
        return (None, None)

    entdig = None

    if not username:
        username = challenge['username']
        HA1 = password
    else:
        A1 = "%s:%s:%s" % (username, realm, password)
        HA1 = H(A1)
        
    # XXX selector: what about proxies and full urls
    A2 = "%s:%s" % (request.get_method(), request.get_selector())
    if qop == 'auth':

        # client nonce - cnonce
        cnonce = get_cnonce(nonce_count, nonce)

        ncvalue = '%08x' % nonce_count
        noncebit = "%s:%s:%s:%s:%s" % (nonce, ncvalue, cnonce, qop, H(A2))

        respdig = KD(HA1, noncebit)
    elif qop is None:
        respdig = KD(HA1, "%s:%s" % (nonce, H(A2)))
    else:
        # XXX handle auth-int.
        # raise URLError("qop '%s' is not supported." % qop)
        return (None, None)

    # XXX should the partial digests be encoded too?

    base = 'username="%s", realm="%s", nonce="%s", uri="%s", response="%s"' \
           % (username, realm, nonce, request.get_selector(), respdig)
    if opaque:
        base += ', opaque="%s"' % opaque
    if entdig:
        base += ', digest="%s"' % entdig
    base += ', algorithm="%s"' % algorithm
    if qop:
        base += ', qop=auth, nc=%s, cnonce="%s"' % (ncvalue, cnonce)

    return (base, HA1)
