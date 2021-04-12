#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt
#
# TODO: ADD GDATA AND GNOME ONLINE ACCOUNTS SUPPORT

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr   \
                          -DSYSCONF_INSTALL_DIR=/etc    \
                          -DENABLE_VALA_BINDINGS=ON     \
                          -DENABLE_INSTALLED_TESTS=ON   \
                          -DENABLE_GOOGLE=OFF           \
                          -DWITH_OPENLDAP=OFF           \
                          -DWITH_KRB5=OFF               \
                          -DENABLE_INTROSPECTION=ON     \
                          -DENABLE_CANBERRA=ON          \
                          -DENABLE_WEATHER=ON           \
                          -DENABLE_GTK=ON               \
                          -DENABLE_OAUTH2=ON            \
                          -DENABLE_GOA=OFF              \
                          -DWITH_SYSTEMDUSERUNITDIR=NO  \
                          -DENABLE_GTK_DOC=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "ChangeLog", "HACKING", "MAINTAINERS", "NEWS", "README")

