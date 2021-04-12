
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.system("sed -i -e 's:getgroups:lightdm_&:' tests/src/libsystem.c")
    #shelltools.system("sed -i s/systemd/elogind/ data/pam/*")
    
    autotools.configure("--prefix='/usr' --sbindir='/usr/bin' --sysconfdir='/etc' \
                         --localstatedir='/var' --libexecdir='/usr/lib/lightdm' \
                         --with-greeter-user='root' \
                         --with-greeter-session='lightdm-gtk-greeter' \
                         --disable-static \
                         --enable-vala")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
