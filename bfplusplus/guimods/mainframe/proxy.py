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

import threads.threadbase as threadbase

if True:
    def init(self):
        useProxy = self.config.ReadBool('Use Proxy', False)
        self.config.WriteBool('Use Proxy', useProxy)
        self.m_checkBoxUseProxy.SetValue(useProxy)

        proxyHost = self.config.Read('Proxy Host', 'myproxy.com')
        self.config.Write('Proxy Host', proxyHost)
        self.m_textCtrlProxyHost.SetValue(proxyHost)

        proxyPort = self.config.Read('Proxy Port', '8888')
        self.config.Write('Proxy Port', proxyPort)
        self.m_textCtrlProxyPort.SetValue(proxyPort)

        self.proxydict = dict()

        if useProxy:
            proxyHostPort = 'http://%s:%s' % (proxyHost, proxyPort)
            self.proxydict['http'] = proxyHostPort
            self.proxydict['https'] = proxyHostPort


    def OnCheckBoxUseProxy(self, event):
        useProxy = self.m_checkBoxUseProxy.GetValue()

        self.proxydict = dict()

        if useProxy:
            proxyHost = self.m_textCtrlProxyHost.GetValue()
            try:
                proxyPort = int(self.m_textCtrlProxyPort.GetValue())
            except:
                self.m_checkBoxUseProxy.SetValue(False)
                return

            proxyHostPort = 'http://%s:%d' % (proxyHost, proxyPort)
            self.proxydict['http'] = proxyHostPort
            self.proxydict['https'] = proxyHostPort

            self.config.Write('Proxy Host', proxyHost)
            self.config.Write('Proxy Port', str(proxyPort))

        self.config.WriteBool('Use Proxy', useProxy)
        with threadbase.ThreadBase.masterLock:
            bftransport = threadbase.ThreadBase.bfClientMaster.transport
        # bftransport = self.bfClient.transport
        bftransport.setproxy(self.proxydict)
