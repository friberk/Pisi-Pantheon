#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    mesontools.configure("-Dsystemdunitdir=/tmp")

def build():
    mesontools.build()

def install():
    mesontools.install()
    shelltools.system("rm -rf /var/pisi/sysprof-3.36.0-1/install/tmp")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README.md")

