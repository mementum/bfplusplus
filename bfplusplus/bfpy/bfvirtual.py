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
Implementation of Virtual Prices Calculation.
'''

from collections import defaultdict
from copy import deepcopy
from decimal import Decimal, ROUND_UP, ROUND_DOWN

import bfticks
from bfutil import EmptyObject

TWOPLACES = Decimal(10) ** -2

def VirtualPrices(marketPrices, minGBPStake=2.0, rateGBP=None, freeApi=False):
    '''
    Please bear in mind that:

      - It is (so far 2011-05-19) to know if the website is presenting Virtual Prices
        or not to the user (and this seems to be linked to the activation/non-activation
        of Cross Matching in some markets

      - An exact representation of Virtual Prices requires knowing which exchange rate
        is being applied by Betfair between GBP and the currency of the logged in user

    This is because Bf is not presenting bets of less than 2 GBP to the users and
    the calculated virtual bets have to be converted to GBP to understand if they
    can be presented

    Because the getAllCurrencies(V2) call is not available to the FreeAPI, the FreeAPI
    users would see these bets
    Returns the next price tick upwards/downwards for a given price
    and bet type

    Calculation of virtual prices for a marketPrices object (can be found as
    response.marketPrices calling getMarkePrices and getMarketPricesCompressed)

    This should only be applied to Match Odds markets

    @type  marketPrices: complex object
    @param marketPrices: prices received from getAllMarkets(Compressed)
    @type  minGBPStake: float
    @param minGBPStake: what the current minimum stake is for GBP
    @type  rateGBP: float
    @param rateGBP: current exchange rate applied to see if a bet goes under
                    the minGBPStake
    @type freeApi: boolean
    @param freeApi: if True and not rateGBP has been given it will return
                    any valid virtual price calculated even if under the
                    minimumGBPStake
    '''
    for rPrice0 in marketPrices.runnerPrices:
        rPrice0.vBets = defaultdict(list)

        # 1. Save a copy of the prices - because we'll modify them
        runnerPrices = deepcopy(marketPrices.runnerPrices)

        betTypes = [('L', 'bestPricesToLay'), ('B', 'bestPricesToBack')]
        for vBetType, attrName in betTypes:
            while True:
                sumOdds = 0.0
                prodStakes = dict()

                # 2.Go over all runners to calculate the virtual prices
                for rPrice in runnerPrices:
                    bestPricesTo = getattr(rPrice, attrName)
                    if rPrice0.selectionId != rPrice.selectionId and bestPricesTo:
                        bestPrice = bestPricesTo[0]
                        sumOdds += 1.0 / bestPrice.price
                        prodStakes[rPrice.selectionId] = bestPrice.price * bestPrice.amountAvailable

                # Before any operation, check if there was any price, if not we are over
                if not prodStakes:
                    break

                # Create the Virtual Bet
                vBet = EmptyObject()
                vBet.betType = vBetType # It's a lay in the exchange, available to be layed
                vBet.depth = 0 # not really known at this moment

                try:
                    vBet.price = 1.0 / (marketPrices.numberOfWinners - sumOdds)
                except:
                    break

                if vBet.price < 1.01 or vBet.price > 1000.0:
                        break

                # Use decimal arithmetic to ensure that the price is properly adjusted
                vBet.price = str(vBet.price)
                rounding = ROUND_DOWN if vBetType == 'L' else ROUND_UP
                vBet.price = float(Decimal(vBet.price).quantize(TWOPLACES, rounding=rounding))

                # Adjust to an existing price tick
                vBet.price = bfticks.GetClosestTick(vBet.price, down=(vBetType == 'L'))

                # Calculate the maximum possible payout of the virtual bet
                maxPayOutKey = min(prodStakes, key=lambda x: prodStakes.get(x))
                maxPayOut = prodStakes[maxPayOutKey]
                # Adjustment done against the "adjusted price" and not the "calculated price"
                vBet.amountAvailable = round(maxPayOut / vBet.price, 2)

                # Only insert the vBet if it will show up (above the minimum GBP bet)
                if rateGBP is not None:
                    if (vBet.amountAvailable / rateGBP) >= minGBPStake:
                        rPrice0.vBets[vBetType].append(vBet)
                elif freeApi:
                    # Or if freeApi wants to see all bets
                    rPrice0.vBets[vBetType].append(vBet)

                for rPrice in runnerPrices:
                    bestPricesTo = getattr(rPrice, attrName)
                    if rPrice0.selectionId != rPrice.selectionId and bestPricesTo:
                        if rPrice.selectionId == maxPayOutKey:
                            del bestPricesTo[0]
                        else:
                            bestPrice = bestPricesTo[0]
                            bestPrice.amountAvailable -= round(maxPayOut / bestPrice.price, 2)
                            if bestPrice.amountAvailable <= 0.0:
                                del bestPricesTo[0]

    # Now merge the vBets of the runners with the normal bets
    betTypes = [('L', 'bestPricesToBack'), ('B', 'bestPricesToLay')]
    for rPrice in marketPrices.runnerPrices:
        for vBetType, attrName in betTypes:
            oBets = getattr(rPrice, attrName)
            vBets = rPrice.vBets[vBetType]

            # Save a copy of the original bets
            setattr(rPrice, attrName + 'Orig', deepcopy(oBets))
            # Put an empty list as the placeholder for merged bets
            bestPricesTo = list()
            setattr(rPrice, attrName, bestPricesTo)

            while len(bestPricesTo) < 3 and vBets and oBets:
                vBet = vBets[0]
                oBet = oBets[0]

                if (vBetType == 'L' and vBet.price > oBet.price) or \
                   (vBetType == 'B' and vBet.price < oBet.price):
                    bestPricesTo.append(vBets.pop(0))
                elif vBet.price == oBet.price:
                    vBet.amountAvailable += oBet.amountAvailable
                    bestPricesTo.append(vBets.pop(0))
                    while vBets and vBets[0].price == oBet.price:
                        bestPricesTo[-1].amountAvailable += vBets[0].amountAvailable
                        del vBets[0]
                    oBets.pop(0)
                else:
                    bestPricesTo.append(oBets.pop(0))

            # Top if needed
            while len(bestPricesTo) < 3 and vBets:
                bestPricesTo.append(vBets.pop(0))
            while len(bestPricesTo) < 3 and oBets:
                bestPricesTo.append(oBets.pop(0))

