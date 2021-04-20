#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()
    shelltools.system("rm /var/pisi/gsignon-1.2.0-1/install/usr/share/dbus-1/services/com.google.code.AccountsSSO.SingleSignOn.service")

    pisitools.dodoc("COPYING.LIB", "README.md")

