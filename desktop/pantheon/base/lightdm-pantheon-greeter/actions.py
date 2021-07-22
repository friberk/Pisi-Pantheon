#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    mesontools.configure("--sbindir=/usr/bin")

def build():
    mesontools.build()

def install():
    mesontools.install()

    shelltools.system("sed -i 's@Exec=io.elementary.greeter@Exec=/usr/bin/io.elementary.greeter@' %s/usr/share/xgreeters/io.elementary.greeter.desktop" 
                        % get.installDIR())
    pisitools.dodoc("LICENSE", "README.md")
