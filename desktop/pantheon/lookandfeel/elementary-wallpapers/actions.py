#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("mv 'backgrounds/Pisi-Crocus-Ancyrensis-(C)Mustafa-Orhon.jpg' 'backgrounds/Mustafa Orhon.jpg'")

    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dosym("/usr/share/backgrounds/Mustafa Orhon.jpg", "/usr/share/backgrounds/elementaryos-default")
    pisitools.dodoc("README.md", "LICENSE.md")
