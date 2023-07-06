#!/usr/bin/python3
'''
Module: '1-pack_web_static'
Script that generates a .tgz archive from contents of web_static folder
'''

from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """generates a tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if isdir("versions") is False:
        local("mkdir versions")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(file_name))
    if file_name:
        return file_name
    else:
        return None
