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

from collections import defaultdict

class DataProcessor(object):
    def __init__(self, api, **kwargs):
        # Ideally the application will only start this module if
        # it has been able to detect this modules
        try:
            # wxPython initializes some ole/com components and
            # multi-threaded mode is not possible
            # sys.coinit_flags = 0
            import pythoncom
            pythoncom.CoInitialize()
            self.pcom = pythoncom
            import win32com.client
            self.w32com = win32com.client
        except ImportError:
            pass

        self.api = api
        self.mComp = None
        self.market = None

        self.numRunners = 0

        self.workbooks = dict()
        self.sheets = defaultdict(dict)
        
        self.baseRow = 1
        self.baseCol = 1


    def getExcelSheets(self):
        comName='Microsoft Excel'
        self.workbooks = dict()
        self.sheets = defaultdict(dict)
        rot = self.pcom.GetRunningObjectTable()
        rotenum = rot.EnumRunning()
        while True:
            monikers = rotenum.Next()
            if not monikers:
                break
            obj = rot.GetObject(monikers[0])
            try:
                queryInterface = obj.QueryInterface(self.pcom.IID_IDispatch)
                comObject = self.w32com.Dispatch(queryInterface)
                if comName in str(comObject):
                    ctx = self.pcom.CreateBindCtx(0)
                    wbname = monikers[0].GetDisplayName(ctx, None);
                    if not wbname.startswith('!'):
                        self.workbooks[wbname] = comObject
                        for sheet in comObject.Sheets:
                           self.sheets[wbname][sheet.Name] = sheet
            except:
                # Possibly - no query interface supported
                pass

        self.api.modMessage('getExcelSheets', sheets=self.sheets)


    def doExit(self, appExiting=False):
        if not appExiting:
            self.api.logMessage('End of Excel Betting')

    def play(self):
        pass

    def pause(self):
        pass

    def getParams(self):
        pass

    def setParams(self, params):
        pass

    def processData(self, message):
        if hasattr(message, 'subAction'):
            if message.subAction == 'getExcelSheets':
                self.getExcelSheets()
                return

            elif message.subAction == 'setActiveCell':
                cell = message.cell
                cellBoundary = cell.find('0123456789')
                # Reminder: Excel order is -> (row, col) and starting at (1, 1)
                # For A1 -> (1,1) for A2 -> (2, 1)
                self.baseRow = int(cell[cellBoundary:])
                self.baseCol = ord(cell[0:cellBoundary].lower()) - ord('a') + 1
                return

            elif message.subAction == 'openExcel':
                try:
                    app = self.w32com.Dispatch("Excel.Application")
                    app.Visible = True
                    app.Workbooks.Add(None)
                except:
                    pass
                return

        workbooks = message.workbooks
        sheets = message.sheets

        mComp = message.marketComp
        market = mComp.market
        
        if not self.mComp or \
               (mComp.marketId != self.mComp.marketId and
                mComp.exchangeId != self.mComp.exchangeId):

            self.cleanSheets(workbooks, sheets)
            self.mComp = mComp
            self.market = market
            self.numRunners = len(self.mComp.runners)
            self.initSheets(workbooks, sheets)

        self.fillSheets(workbooks, sheets)
        # self.triggerBetting(workbooks, sheets)


    def cleanSheets(self, workbooks, sheets):
        if self.mComp is None:
            return

        tlRow = self.baseRow
        tlCol = self.baseCol

        brRow = tlRow + self.priceOffVert + 2 * self.numRunners
        bfCol = tlCol + self.headersLength - 1

        for wbname, status in workbooks.iteritems():
            if not status:
                continue
            for sheetname, status in sheets[wbname].iteritems():
                if not status:
                    continue
                sheet = self.sheets[wbname][sheetname]

                try:
                    rng = sheet.Range(sheet.Cells(tlRow, tlCol),
                                      sheet.Cells(brRow, brCol))
                    rng.Value = ''
                except Exception, e:
                    # Don't let 1 sheet ruin the others
                    # print "Sheet: %s - Error: %s" % (str(sheet), str(e))
                    pass

    mInfos = {'Market Id': 'marketId', 'Exchange Id': 'exchangeId',
              'Market Name': 'name', 'Menu Path': 'menuPath',}

    headers = ['Name', 'Back 3', 'Back 2', 'Back 1',
               'Lay 1', 'Lay 2', 'Lay 3', 'Compensations', 'Reference',
               'Bet Ref', 'Bet to Place', 'Price', 'Size']

    headersLength = len(headers)
    # len(mInfos) + blank + headers (1 line)
    priceOffVert =  len(mInfos) +  2
    # After Name
    priceOffHorz = 1
    
    def initSheets(self, workbooks, sheets):
        col = self.baseCol

        for wbname, status in workbooks.iteritems():
            if not status:
                continue
            for sheetname, status in sheets[wbname].iteritems():
                if not status:
                    continue
                sheet = self.sheets[wbname][sheetname]

                row = self.baseRow

                try:

                    # Top header
                    row += 0
                    for name, attrName in self.mInfos.iteritems():
                        sheet.Cells(row, col + 0).Value = name
                        sheet.Cells(row, col + 1).Value = getattr(self.mComp, attrName)
                        row += 1

                    # Blank line
                    row += 1

                    # Prices header
                    row + 1
                    for i, header in enumerate(self.headers):
                        sheet.Cells(row, col + i).Value = header

                    # Runner names
                    row += 1
                    for i, runner in enumerate(self.mComp.runners):
                        sheet.Cells(row + 2 * i, col + 0).Value = runner.name
                        sheet.Cells(row + 2 * i + 1, col + 0).Value = ''
                except:
                    pass


    def fillSheets(self, workbooks, sheets):
        # Offset from headers
        row = self.baseRow + self.priceOffVert
        col = self.baseCol + self.priceOffHorz

        firstRow = row

        for wbname, status in workbooks.iteritems():
            if not status:
                continue
            for sheetname, status in sheets[wbname].iteritems():
                if not status:
                    continue
                sheet = self.sheets[wbname][sheetname]

                row = firstRow

                try:
                    if False:
                        numRunners = len(self.mComp.runners)
                        rng = sheet.Range(sheet.Cells(row, col),
                                          sheet.Cells(row + 2 * numRunners, col + 7))
                        rng.Value = ''

                    for runner in self.mComp.runners:

                        runnerPrices = self.mComp.runnerPrices[runner.selectionId]

                        # Fill cells with back prices
                        for i, bestPrice in enumerate(runnerPrices.bestPricesToBack):
                            sheet.Cells(row, col + 2 - i).Value = bestPrice.price
                            sheet.Cells(row + 1, col + 2 - i).Value = bestPrice.amountAvailable

                        # Clear cells with no back prices
                        for i in range(3 - len(runnerPrices.bestPricesToBack)):
                            sheet.Cells(row, col + i).Value = ''
                            sheet.Cells(row + 1, col + i).Value = ''

                        # Fill cells with lay prices
                        for i, bestPrice in enumerate(runnerPrices.bestPricesToLay):
                            sheet.Cells(row, col + 3 + i).Value = bestPrice.price
                            sheet.Cells(row + 1, col + 3 + i).Value = bestPrice.amountAvailable

                        # Clear cells with no lay prices
                        for i in range(3 - len(runnerPrices.bestPricesToLay)):
                            sheet.Cells(row, col + 5 - i).Value = ''
                            sheet.Cells(row + 1, col + 5 - i).Value = ''

                        row += 2
                except:
                    pass
