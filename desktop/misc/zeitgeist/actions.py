#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --disable-maintainer-mode \
                         --enable-fts \
                         --enable-datahub \
                         --enable-telepathy \
                         --enable-downloads-monitor \
                         --enable-explain-queries")

    # fix for unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/lib/systemd")
    pisitools.dodoc("COPY*", "README", "ChangeLog", "NEWS", "AUTHORS")
