#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure(" --prefix=/usr \
                          --libexecdir=/usr/lib/lightdm \
                          --localstatedir=/var \
                          --sbindir=/usr/bin \
                          --sysconfdir=/etc \
                          --disable-static \
                          --disable-tests \
                          --enable-gtk-doc \
                          --with-greeter-user=lightdm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

