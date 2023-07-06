#!/usr/bin/python3
'''
Module: '1-pack_web_static'
Script that generates a .tgz archive from contents of web_static folder
'''

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    date = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    archive_name = "versions/web_static_{}.tgz".format(date)
    local("tar -czvf {} web_static".format(archive_name))
    if archive_name:
        return archive_name
    else:
        return None
