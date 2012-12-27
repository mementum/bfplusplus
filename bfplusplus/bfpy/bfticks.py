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
This module ease calculations of valid prices and next best prices at a given
distance or the closest next best price

@var priceRanges: valid price ranges and increments for bf
@type priceRanges: tuple of tuples
@var PriceIncs: list of valid prices ordered
@type PriceIncs: list
@var PriceIncsLen: number of valid prices
@type PriceIncsLen: int

@var PriceMin: Minimum valid price (1.01)
@type PriceMin: float
@var PriceMax: Maximum valid price (1000.0)
@type PriceMax: float
'''

from bisect import bisect_left, bisect_right

# list of tuples containing low, high, inc
priceRanges = (
    (1.01, 2.0, 0.01),
    (2.0, 3.0, 0.02),
    (3.0, 4.0, 0.05),
    (4.0, 6.0, 0.10),
    (6.0, 10.0, 0.20),
    (10.0, 20.0, 0.50),
    (20.0, 30.0, 1.0),
    (30.0, 50.0, 2.0),
    (50.0, 100.0, 5.0),
    (100.0, 1000.0, 10.0),
    )

PriceIncs = list()
PriceIncsLen = 0
PriceMin = 1.01
PriceMax = 1000.0

def GeneratePriceIncs():
    '''
    Using L{priceRanges} it generates a list containing
    every possible valid price for Bf
    '''
    for low, high, inc in priceRanges:
        while low < high:
            PriceIncs.append(low)
            low = float('%.2f' % (low + inc))

    PriceIncs.append(high)
    global PriceIncsLen
    PriceIncsLen = len(PriceIncs)

GeneratePriceIncs()


def GetPriceTicks(price, ticks, betType):
    '''
    Returns the next price tick upwards/downwards for a given price
    and bet type

    Back bets increase price upwards
    Lay bets increase price downwards

    @type  price: float
    @param price: base price for next tick
    @type  ticks: int
    @param ticks: number of ticks to move the price
    @type  betType: B|L
    @param betType: bet type (determines the direction)

    @rtype: float
    @return: the passed prices decreased x ticks
    '''
    global PriceIncsLen
    if betType == 'L':
        ticks *= -1

    pIndex = bisect_left(PriceIncs, price) + ticks
    
    if pIndex < 0:
        return PriceMin
    elif pIndex >= PriceIncsLen:
        return PriceMax

    return PriceIncs[pIndex]


def GetClosestTick(price, down):
    '''
    Returns the next (and best) valid price upwards/downwards given a price (which may
    or may not be valid) It is of course limited to PriceMin/PriceMax

    @type  price: float
    @param price: base price for next price
    @type  down: bool
    @param down: go downwards (back bets) if True, else go upwards (lay bets)

    @rtype: float
    @return: the best price upwards/downwards
    '''
    if down:
        if price <= PriceMin:
            return PriceMin
        return PriceIncs[bisect_right(PriceIncs, price) - 1]

    if price >= PriceMax:
        return PriceMax
    return PriceIncs[bisect_left(PriceIncs, price)]


def GetClosestTickDown(price):
    '''
    Utility function to return the closest tick downwards

    @type  price: float
    @param price: base price for next price

    @rtype: float
    @return: the best price downwards
    '''
    return GetClosestTick(price, down=True)


def GetClosestTickUp(price):
    '''
    Utility function to return the closest tick upwards

    @type  price: float
    @param price: base price for next price

    @rtype: float
    @return: the best price upwards
    '''
    return GetClosestTick(price, down=False)
