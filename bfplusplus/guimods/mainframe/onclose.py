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

if True:
    try:
        import pythoncom
    except ImportError:
        pass

    def OnClose(self, event):
        if self.recordModule:
            try:
                self.UnloadModule(self.recordModule, 'recordnplay.record', appExiting=True)
            except:
                pass

        if self.playModule:
            try:
                self.UnloadModule(self.playModule, 'recordnplay.play', appExiting=True)
            except:
                pass

        if self.excelModule:
            try:
                self.UnloadModule(self.excelModule, 'excelmod.excelmod', appExiting=True)
            except:
                pass
            try:
                pythoncom.CoUninitialize()
            except:
                pass


        for bfModuleName, bfModule in self.bfModulesUser.iteritems():
            try:
                self.UnloadModule(bfModule, bfModuleName, appExiting=True)
            except:
                pass

        self.Destroy()
