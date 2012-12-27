#! /bin/sh
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
# to create spec
# python ../pyinstaller/Makespec.py -s -w bfplusplus.pyw -o exe

find . -name '*~' -exec rm -f {} \;
find . -name '*.pyc' -exec rm -f {} \;
# find . -name '*.pyo' -exec rm -f {} \;

rm -rf bin

mkdir -p bin/pkg
cp scripts/bfplusplus.spec bin/pkg

python -OO ../pyinstaller/Build.py -y bin/pkg/bfplusplus.spec
mv logdict* bin/pkg

cp LICENSE LICENSE.LGPL LICENSE.APACHE CREDITS README GAMBLING bin/pkg/dist/bfplusplus

