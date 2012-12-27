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
HttxLib Set with locking semanctics to store the allowed compression values
'''

from copy import deepcopy

from httxobject import HttxObject


class HttxCompressionSet(HttxObject):
    '''
    HttxLib Set with locking semanctics to store the allowed compression values

    @ivar compressionset: holds the unique values
    @type cache: set
    '''

    def __init__(self, *args):
        '''
        Constructor. It delegates construction to the base class
        L{HttxObject} and initializes the member variables

        @param args: iterable of allowed compression values
        @type args: list|tuple
        '''
        HttxObject.__init__(self)
        self.compressionset = set(args)


    def __deepcopy__(self, memo):
        '''
        Deepcopy support.

        @param memo: standard __deepcopy__ parameter to avoid circular references
        @type memo: dict
        @return: a cloned object
        @rtype: L{HttxCompressionSet}
        '''
        clone = self.__class__()
        with self.lock:
            clone.compressionset = deepcopy(self.compressionset)
        return clone


    def __str__(self):
        '''
        Conversion to string

        @return: a string containing the allowed compression types
        @rtype: str
        '''
        return str(self.compressionset)


    def add(self, elem):
        '''
        Add a compression type to the set

        @param elem: a compression type (like gzip)
        @type elem: str
        '''
        with self.lock:
            self.compressionset.add(elem)


    def remove(self, elem):
        '''
        Remove a compression type from the set.

        It mimics remove from Python set

        @param elem: a compression type (like gzip)
        @type elem: str
        '''
        with self.lock:
            self.compressionset.remove(elem)


    def discard(self, elem):
        '''
        Discard a compression type from the set

        It mimics discard from Python set

        @param elem: a compression type (like gzip)
        @type elem: str
        '''
        with self.lock:
            self.compressionset.discard(elem)


    def clear(self):
        '''
        Clear the set
        '''
        with self.lock:
            self.compressionset.clear()


    def update(self, other):
        '''
        Update the set with another set

        @param other: another set to use in the update
        @type other: set
        '''
        with self.lock:
            self.compressionset.update(other)


    def join(self, sep = ', '):
        '''
        Utility function to return the values in the set as a string
        separated by sep

        @param sep: separator in the returned string
        @type sep: str
        @return: string composed of the set elements separated by sep
        @rtype: str
        '''
        with self.lock:
            return sep.join(self.compressionset)
