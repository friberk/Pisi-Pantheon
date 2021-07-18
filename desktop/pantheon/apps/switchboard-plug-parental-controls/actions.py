#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i -e '/systemd_dep/d' meson.build data/meson.build")
    
    mesontools.configure("-Dsystemdunitdir=no")

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.removeDir("/usr/no")
    pisitools.dodoc("COPYING", "README.md")
