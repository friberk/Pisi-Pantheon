#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt
# TODO: ADD AUTOAR, GSPELL, HIGHLIGHT AND MAPS SUPPORT

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr       \
                          -DSYSCONF_INSTALL_DIR=/etc        \
                          -DENABLE_INSTALLED_TESTS=ON       \
                          -DENABLE_PST_IMPORT=OFF           \
                          -DENABLE_YTNEF=OFF                \
                          -DENABLE_ALARM_NOTIFY_MODULE=ON   \
                          -DENABLE_WEATHER=ON               \
                          -DENABLE_CANBERRA=ON              \
                          -DENABLE_AUTOAR=OFF               \
                          -DENABLE_CONTACT_MAPS=OFF         \
                          -DENABLE_TEXT_HIGHLIGHT=OFF       \
                          -DENABLE_GSPELL=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "ChangeLog", "HACKING", "MAINTAINERS", "NEWS", "README.md")

