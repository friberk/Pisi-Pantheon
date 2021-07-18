#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Degl_device=true \
                          -Dwayland_eglstream=true \
                          -Dudev=true \
                          -Dnative_backend=true \
                          -Dprofiler=false \
                          -Dintrospection=true \
                          -Dxwayland_initfd=disabled \
                          -Dinstalled_tests=false")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.removeDir("/lib")
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/share")
    pisitools.removeDir("/usr/libexec")

    pisitools.dodoc("NEWS", "README.md", "COPYING")
