#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of Bfplusplus
#
# Bfplusplus is a graphical interface to the Betfair Betting Exchange
# Copyright (C) 2010  Daniel Rodriguez (aka Daniel Rodriksson)
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

import compileall
compileall.compile_dir('./bfplusplus', force=True)

a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'),
              os.path.join(HOMEPATH,'support/useUnicode.py'),
              'bfplusplus/bfplusplus.pyw'],
             excludes=['betafunc'],
             pathex=None,
             hookspath=['./scripts/hooks'])

pyz = PYZ(a.pure + [('bfverification', './bfplusplus/bfverification.pyo', 'PYSOURCE')])

exe = EXE(pyz,
          a.scripts + [('OO', '', 'OPTION')],
          console=False,
          debug=False,
          name=os.path.join('build/pyi.win32/bfplusplus', 'bfplusplus.exe'),
          exclude_binaries=1,
          strip=False,
          upx=False,
          icon='bfplusplus/icons/bfplusplus.ico'
          )

datadirs = ['bfmodules', 'icons']
treeFiles = list()
for datadir in datadirs:
    treeFiles.extend(Tree('bfplusplus/%s' % datadir, prefix='%s/' % datadir, excludes=['*~']))

coll = COLLECT(exe,
               a.binaries,
               treeFiles,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name=os.path.join('dist', 'bfplusplus'))
