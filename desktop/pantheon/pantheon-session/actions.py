#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-Dpatched-ubuntu-autostarts=false")

def build():
    mesontools.build()

def install():
    mesontools.install()
    shelltools.system('sed -i "s|/usr/lib/gnome-settings-daemon/|/usr/libexec/|g" {}/etc/xdg/autostart/*'.format(get.installDIR()))
