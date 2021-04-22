#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--prefix=/usr \
                         --with-libsecret \
                         --with-libsoup \
                         --with-gtksourceview  \
                         --with-goocanvas  \
                         --disable-static \
                         --enable-json \
                         --with-graphviz \
                         --with-ui \
                         --enable-system-sqlite")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
