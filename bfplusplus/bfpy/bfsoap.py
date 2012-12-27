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

# This file contains parts and functions, modified, adapted and extended if needed,
# from the ElementSoap Library. The license is below
# Please visit: http://effbot.org/

# --------------------------------------------------------------------
# The ElementSoap Library is
#
# Copyright (c) 1999-2007 by Secret Labs AB
# Copyright (c) 1999-2007 by Fredrik Lundh
#
# By obtaining, using, and/or copying this software and/or its
# associated documentation, you agree that you have read, understood,
# and will comply with the following terms and conditions:
#
# Permission to use, copy, modify, and distribute this software and its
# associated documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appears in all
# copies, and that both that copyright notice and this permission notice
# appear in supporting documentation, and that the name of Secret Labs
# AB or the author not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
# 
# SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO
# THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS.  IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# --------------------------------------------------------------------

'''
Soap processing
'''

import base64
from cStringIO import StringIO
from datetime import datetime
try:
    from xml.etree.cElementTree import Element, SubElement, QName, iterparse
except ImportError:
    from xml.etree.ElementTree import Element, SubElement, QName, iterparse

from bftimezone import LocalTimezone
from bfutil import EmptyObject

# SOAP 1.1 namespaces
NS_SOAP_ENV = "{http://schemas.xmlsoap.org/soap/envelope/}"
NS_SOAP_ENV_body = NS_SOAP_ENV + 'Body'
NS_SOAP_ENC = "{http://schemas.xmlsoap.org/soap/encoding/}"
NS_XSI = "{http://www.w3.org/2001/XMLSchema-instance}"
NS_XSI_type = NS_XSI + 'type'
NS_XSI_nil = NS_XSI + 'nil'
NS_XSD = "{http://www.w3.org/2001/XMLSchema}"

SOAP_ENCODING = "http://schemas.xmlsoap.org/soap/encoding/"


def soap_process(httpbody, complexDecoders, simplexDecoders):
    response = namespace_parse(StringIO(httpbody))
    response = response.find(NS_SOAP_ENV_body)[0]

    fix_xsi_types(response)
    # look_for_fault(response)

    return decode(response, complexDecoders, simplexDecoders)

# Extracted from SoapService
def fix_xsi_types(response):
    # fixup any XSI_type attributes
    # FIXME: only do this if envelope uses known soapencoding
    for elem in response.getiterator():
        type = elem.get(NS_XSI_type)
        if type:
            elem.set(NS_XSI_type, namespace_qname(elem, type))


# Extracted from SoapService
def look_for_fault(response):
    # look for fault descriptors
    if response.tag == NS_SOAP_ENV + "Fault":
        faultcode = response.find("faultcode")
        if faultcode is not None:
            raise SoapFault(
                namespace_qname(faultcode, faultcode.text),
                response.findtext("faultstring"),
                response.findtext("faultactor"),
                response.find("detail")
                )
        else:
            # workaround: TGWebServices uses namespaced Fault sub-
            # element names
            faultcode = response.find(NS_SOAP_ENV + "faultcode")
            # TODO: manage the soapactor... :(
            raise SoapFault(
                namespace_qname(faultcode, faultcode.text),
                response.findtext(NS_SOAP_ENV + "faultstring"),
                'Server', #response.findtext(NS_SOAP_ENV + "faultactor"),
                response.findtext(NS_SOAP_ENV + "detail")
                )

##
# (Experimental) Element decoder for the standard SOAP encoding
# scheme.  This function only decodes individual elements.  Use {@link
# decode} to handle nested data structures.
#
# NOTE: Modified to support "nullifiable" types and support custom
# types which are not complex (example: Enums ...)
#
# @param element Element.
# @return A Python object, or None if the element argument was None.
# @throws ValueError If the element has an unknown type.


def convertTime(dtString):
    dt = datetime.strptime(dtString.split('.')[0], '%Y-%m-%dT%H:%M:%S')
    localTimezone = LocalTimezone()
    try:
        utcoffset = localTimezone.utcoffset(dt)
    except:
        # Fails with the dates from getSubscriptionInfo
        utcoffset = localTimezone.utcoffset(datetime.now())

    dt += utcoffset
    dt.replace(tzinfo=localTimezone)
    return dt


XSDTYPES = {
    'string': lambda x: x or '',
    'int': lambda x: int(x),
    'integer': lambda x: int(x),
    'long': lambda x: long(x),
    'double': lambda x: float(x),
    'float': lambda x: float(x),
    'boolean': lambda x: x == 'true',
    # 'dateTime': lambda x: datetime.strptime(x.split('.')[0], '%Y-%m-%dT%H:%M:%S'),
    'dateTime': convertTime,
    }

def decode_element(element, simplexDecoders):
    if element is None:
        return None

    if element.get(NS_XSI_nil) is not None:
        return None

    xsitype = element.get(NS_XSI_type)
    if xsitype is None:
        raise ValueError("type %s not supported" % type)

    xstype, valtype = xsitype.split('}')
    xstype += '}'

    if xstype == NS_XSD:
        return XSDTYPES[valtype](element.text)
    
    for simplexDecoder in simplexDecoders:
        decoded, retval = simplexDecoder(element, xstype, valtype)
        if decoded:
            return retval
        
    raise ValueError("type %s not supported" % type)

##
# (Experimental) Decoder for the standard SOAP encoding scheme.  This
# function supports SOAP arrays, and maps custom types to Python
# dictionaries (using accessor names as keys, and decoded elements
# as values).
#
# NOTE: Modified to return an object rather than a dictionary for
# custom/complex types
#
# @param element Element.
# @return A Python object structure.
# @throws ValueError If a subelement has an unknown type.


# Added this function to abstract the creation of an array
def decode_array(element, complexDecoders, simplexDecoders):
    value = []
    for elem in element:
        value.append(decode(elem, complexDecoders, simplexDecoders))
    return value


def decode(element, complexDecoders, simplexDecoders):
    if element.get(NS_XSI_nil) is not None:
        return None

    xsitype = element.get(NS_XSI_type)
    if xsitype is not None:
        xstype, valtype = xsitype.split('}')
        xstype += '}'

        for complexDecoder in complexDecoders:
            decoded, retval = complexDecoder(element, xstype, valtype)
            if decoded:
                return retval

        # is it a primitive type?
        try:
            return decode_element(element, simplexDecoders)
        except ValueError:
            if xsitype and xsitype.startswith(NS_XSD):
                raise # unknown primitive type
            
    # assume it's a structure
    value = EmptyObject()
    for elem in element:
        # Set the name of the instance attribute without namespace
        setattr(value, elem.tag.split('}')[-1], decode(elem, complexDecoders, simplexDecoders))
    return value

##
# Namespace-aware parser.  This parser attaches a namespace attribute
# to all elements.
#
# @param source Source (a file-like object).
# @return A 2-tuple containing an annotated element tree, and a qname
#     resolution helper.  The helper takes an element and a QName, and
#     returns an expanded URL/local part string.

def namespace_parse(source):
    events = ("start", "end", "start-ns", "end-ns")
    ns = []
    context = iterparse(source, events=events)
    for event, elem in context:
        if event == "start-ns":
            ns.append(elem)
        elif event == "end-ns":
            ns.pop()
        elif event == "start":
            elem.set("(xmlns)", tuple(ns))
    return context.root


##
# Convert a QName string to an Element-style URL/local part string.
# Note that the parser converts element tags and attribute names
# during parsing; this method should only be used on attribute values
# and text sections.
#
# @param element An element created by the {@link namespace_parse}
#     function.
# @param qname The QName string.
# @return The expanded URL/local part string.
# @throws SyntaxError If the QName prefix is not defined for this
#     element.

def namespace_qname(element, qname):
    prefix, local = qname.split(":")
    for p, url in element.get("(xmlns)"):
        if prefix == p:
            return "{%s}%s" % (url, local)
    raise SyntaxError("unknown namespace prefix (%s)" % prefix)
