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
import glob
import imp
import os
import types
import sys

import wx

import MainFrame
import guimods.mainframe

import util.flushfile

def Run():
    mainApp = MainApp(0)
    mainApp.MainLoop()


class MainApp(wx.App):
    beta = False
    BetBuddyName = 'Bfplusplus'
    BetBuddyVersion = '1.05'

    modClasses = [
        (MainFrame.MainFrame, guimods.mainframe)
        ]


    def OnInit(self):
        self.loadOk = False
        self.loadMsg = ''

        self.LoadAllGuiModules()

        try:
            betaFeatures = 'betafunc'
            __import__(betaFeatures)
        except Exception, e:
            if self.beta:
                print str(e)

        try:
            bfverification = 'bfverification'
            __import__(bfverification)
        except Exception, e:
            if self.beta:
                print str(e)

        # This should avoid getting a dialog warning if an image can't be loaded or is not
        # found when loading an HTML fragment in the Market Info tab
        if self.beta:
            wx.Log_SetActiveTarget(wx.LogStderr())
        else:
            wx.Log_SetActiveTarget(wx.LogStderr())
            # wx.Log_SetActiveTarget(wx.LogBuffer())

        frame = MainFrame.MainFrame(None)
    
        if not self.loadOk:
            wx.MessageBox('Please report the following error\n\n%s' % self.loadMsg, 'Load Error')
            frame.Destroy()
        else:
            self.SetTopWindow(frame)
            frame.Show(True)

        return True


    def LoadAllGuiModules(self):
        for modClass, modMod in self.modClasses:
            self.loadOk, self.loadMsg = self.LoadGUIModules(modClass, modMod)
            if not self.loadOk:
                break


    def LoadGUIModules(self, modClass, modMod):
        def getter(mangledFuncName):
            return lambda self, *args, **kwargs: getattr(self, mangledFuncName)(*args, **kwargs)

        setattr(modClass, 'initlist', list())
        modClassInit = getattr(modClass, 'initlist')

        for modAttrName in dir(modMod):
            modAttr = getattr(modMod, modAttrName)
            if not isinstance(modAttr, types.ModuleType):
                continue
            
            try:
                # Re-using the return value from reload breaks executable generation
                # it seems the PyInstaller reload hook doesn't fully mimic the original reload
                # Anyhow, the module is reloade and therefore the original reference can be
                # used
                # modAttr = reload(modAttr)
                reload(modAttr)
                # print "Reloading modAttrName %s" % modAttrName
            except Exception, e:
                if not self.beta:
                    return False, str(e)
                continue

            for funcAttrName in dir(modAttr):
                funcAttr = getattr(modAttr, funcAttrName)
                if not isinstance(funcAttr, types.FunctionType) or funcAttrName.startswith('__'):
                    continue
                if funcAttrName == 'init':
                    modClassInit.append(funcAttr)
                    continue

                if self.beta:
                    mangledFuncName = '%sxxx' % funcAttrName
                    setattr(modClass, mangledFuncName, funcAttr)
                    setattr(modClass, funcAttrName, getter(mangledFuncName))
                else:
                    setattr(modClass, funcAttrName, funcAttr)

        return True, ''


    def LoadGUIModules2(self, baseModPath, modClass):
        def getter(mangledFuncName):
            return lambda self, *args, **kwargs: getattr(self, mangledFuncName)(*args, **kwargs)

        className = modClass.__name__.lower()

        guiModPath = '%s/%s' % (baseModPath, className)
        guiModName = '%s.%s' % (baseModPath, className)
        modNameParts = [baseModPath, className]

        for modDepth in xrange(len(modNameParts)):
            modChainName = '.'.join(modNameParts[:modDepth + 1])
            if modChainName not in sys.modules:
                guiModule = imp.new_module(modChainName)
                sys.modules[modChainName] = guiModule

        if not os.path.isdir(guiModPath):
            return False, "Module directory '%s' not found" % guiModPath

        modFullFileNames = glob.glob('%s/*.py' % guiModPath)

        setattr(modClass, 'initlist', list())
        modClassInit = getattr(modClass, 'initlist')

        for modFullFileName in modFullFileNames:
            modBaseFileName = os.path.basename(modFullFileName)

            if modBaseFileName.startswith('__'):
                continue

            modName, modExt = os.path.splitext(modBaseFileName)
            modFullName = '%s.%s' % (guiModName, modName)

            try:
                mod = imp.load_source(modFullName, modFullFileName)
            except Exception, e:
                if not self.beta:
                    return False, str(e)

                print 'exception %s' % str(e)
                continue

            for modattrname in dir(mod):
                modattr = getattr(mod, modattrname)
                if not modattrname.startswith('__') and isinstance(modattr, types.FunctionType):

                    if modattrname == 'init':
                        modClassInit.append(modattr)
                    elif self.beta:
                        mangledFuncName = '%sxxx' % modattrname
                        setattr(modClass, mangledFuncName, modattr)
                        setattr(modClass, modattrname, getter(mangledFuncName))
                    else:
                        setattr(modClass, modattrname, modattr)

        return True, ''
