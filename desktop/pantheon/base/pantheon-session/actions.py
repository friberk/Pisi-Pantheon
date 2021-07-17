#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools

def setup():
    mesontools.configure("-Dpatched-ubuntu-autostarts=false")

def build():
    mesontools.build()

def install():
    mesontools.install()
