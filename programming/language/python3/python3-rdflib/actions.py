#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules

def setup():
    pass

def build():
    pythonmodules.compile(pyVer = '3')

def install():
    pythonmodules.install(pyVer = "3")
