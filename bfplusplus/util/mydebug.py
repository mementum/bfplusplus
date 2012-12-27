#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of Bfplusplus
#
# Bfplusplus is a graphical interface to the Betfair Betting Exchange
# Copyright (C) 2010 Daniel Rodriguez (aka Daniel Rodriksson)
# Copyright (C) 2011 Sensible Odds Ltd.
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/bfplusplus/
#
# Bfplusplus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Bfplusplus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Bfplusplus. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import inspect

def PrintInfo():

    print "Line: " + str(inspect.currentframe().f_back.f_lineno)
    # + " - Function: " + str(inspect.currentframe().f_back.f_function)
    

    if False:
        l_frameList = inspect.getouterframes(inspect.currentframe())

        #print l_frameList[1]
        l_fi = inspect.getframeinfo(l_frameList[1])

        print "Line: " + str(l_fi[1]) + "Function: " + str(l_fi[2])
        pass
    # end if
    pass
# end def
