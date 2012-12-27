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
BfPy utility classes
'''

import threading
import types

# Code from suds: no changes
def tostr(obj, encoding=None):
    """ get a unicode safe string representation of an obj """
    if isinstance(obj, basestring):
        if encoding is None:
            return obj
        else:
            return obj.encode(encoding)
    if isinstance(obj, tuple):
        s = ['(']
        for item in obj:
            if isinstance(item, basestring):
                s.append(item)
            else:
                s.append(tostr(item))
            s.append(', ')
        s.append(')')
        return ''.join(s)
    if isinstance(obj, list):
        s = ['[']
        for item in obj:
            if isinstance(item, basestring):
                s.append(item)
            else:
                s.append(tostr(item))
            s.append(', ')
        s.append(']')
        return ''.join(s)
    if isinstance(obj, dict):
        s = ['{']
        for item in obj.items():
            if isinstance(item[0], basestring):
                s.append(item[0])
            else:
                s.append(tostr(item[0]))
            s.append(' = ')
            if isinstance(item[1], basestring):
                s.append(item[1])
            else:
                s.append(tostr(item[1]))
            s.append(', ')
        s.append('}')
        return ''.join(s)
    try:
        return unicode(obj)
    except:
        return str(obj)

# Code from suds (removed the 'Object' references
# to do a pretty print of an object
class Printer(object):
    """ 
    Pretty printing of a Object object.
    """
    
    @classmethod
    def indent(cls, n): return '%*s'%(n*3,' ')

    def tostr(self, obj, indent=-2):
        """ get s string representation of object """
        history = []
        return self.process(obj, history, indent)
    
    def process(self, obj, h, n=0, nl=False):
        """ print obj using the specified indent (n) and newline (nl). """
        if obj is None:
            return 'None'
        if isinstance(obj, EmptyObject):
            if len(obj) == 0:
                return '<empty>'
            else:
                return self.print_object(obj, h, n+2, nl)
        if isinstance(obj, dict):
            if len(obj) == 0:
                return '<empty>'
            else:
                return self.print_dictionary(obj, h, n+2, nl)
        if isinstance(obj, (list,tuple)):
            if len(obj) == 0:
                return '<empty>'
            else:
                return self.print_collection(obj, h, n+2)
        if isinstance(obj, basestring):
            return '"%s"' % tostr(obj)
        return '%s' % tostr(obj)
    
    def print_object(self, d, h, n, nl=False):
        """ print complex using the specified indent (n) and newline (nl). """
        s = []
        cls = d.__class__
        if d in h:
            s.append('(')
            s.append(cls.__name__)
            s.append(')')
            s.append('...')
            return ''.join(s)
        h.append(d)
        if nl:
            s.append('\n')
            s.append(self.indent(n))

        s.append('(')
        s.append(cls.__name__)
        s.append(')')
        s.append('{')

        for item in d.__dict__.iteritems():
            # item = self.unwrap(d, item)
            s.append('\n')
            s.append(self.indent(n+1))
            if isinstance(item[1], (list,tuple)):            
                s.append(item[0])
                s.append('[]')
            else:
                s.append(item[0])
            s.append(' = ')
            s.append(self.process(item[1], h, n, True))
        s.append('\n')
        s.append(self.indent(n))
        s.append('}')
        h.pop()
        return ''.join(s)

    def print_dictionary(self, d, h, n, nl=False):
        """ print complex using the specified indent (n) and newline (nl). """
        if d in h: return '{}...'
        h.append(d)
        s = []
        if nl:
            s.append('\n')
            s.append(self.indent(n))
        s.append('{')
        for item in d.items():
            s.append('\n')
            s.append(self.indent(n+1))
            if isinstance(item[1], (list,tuple)):            
                s.append(tostr(item[0]))
                s.append('[]')
            else:
                s.append(tostr(item[0]))
            s.append(' = ')
            s.append(self.process(item[1], h, n, True))
        s.append('\n')
        s.append(self.indent(n))
        s.append('}')
        h.pop()
        return ''.join(s)

    def print_collection(self, c, h, n):
        """ print collection using the specified indent (n) and newline (nl). """
        if c in h: return '[]...'
        h.append(c)
        s = []
        for item in c:
            s.append('\n')
            s.append(self.indent(n))
            s.append(self.process(item, h, n-2))
            s.append(',')
        h.pop()
        return ''.join(s)
    

class EmptyObject(object):
    '''
    Used to implement objects, like those arising from
    compressed answers
    '''
    printer = Printer()
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return self.printer.tostr(self)

    def __len__(self):
        return len(self.__dict__)


class SharedData(object):
    '''
    Non-data descriptor class to be installed in class during class
    instantiation to enable sharing of values on a clone basis if
    wished.

    It implements a pointer-like dictionary to store which instance
    really holds the value for a given instance (an instance can point
    to itself)

    @type lock: threading.lock
    @ivar lock: synchronize get/set from/to dictionaries
    @type instanceval: dict 
    @ivar instanceval: values stored for instances
    @type instancepointers: dict 
    @ivar instancepointers: pointers for instances to find the final value
    '''

    def __init__(self, name):
        '''
        Initializes the descriptor
        '''
        self.name = name
        self.instanceval = dict()
        self.instancepointers = dict()

        self.lock = threading.RLock()


    def __set__(self, instance, value):
        '''
        Stores a value for an instance using the master pointer for that instance

        @type instance: instance
        @param instance: instance that is calling the descriptor
        @type value: any
        @param value: value to be stored for the instance (or pointer the instace is associated with)
        '''
        # Point to itself unless there is a value in the dict and get the pointer
        with self.lock:
            instpointer = self.instancepointers.setdefault(instance, instance)
            self.instanceval[instpointer] = value


    def __get__(self, instance, owner=None):
        '''
        Non-data descriptor implementation.

        If invoked at class level it returns and unbound method pointing that forces the invocation
        of __call__. The invocation has to be done with an instance

        If invoked from an instance it returns the value that is currently stored for such instance
        (directly or through the master pointer)

        @type instance: instance of class
        @param instance: instance that calls the descriptor
        @type owner: class
        @param owner: the class that holds the descriptor
        '''
        if instance is None:
            return types.MethodType(self, None, owner)

        with self.lock:
            # Point to itself unless there is a value in the dict and get the pointer
            instpointer = self.instancepointers.setdefault(instance, instance)
            # Return None to indicate that it wasn't set so far
            return self.instanceval.get(instpointer, None)


    def __call__(self, instance, slave=None):
        '''
        Associates an instance and a slave to share the same value.
        If no slave is passed, the instance associates to itself.

        @type instance: instance
        @param instance: instance that is calling the descriptor
        @type slave: instance
        @param slave: slave pointer that will be associated to slave
        '''
        with self.lock:
            if slave is None:
                self.instancepointers[instance] = instance
            else:
                self.instancepointers[slave] = self.instancepointers.setdefault(instance, instance)

