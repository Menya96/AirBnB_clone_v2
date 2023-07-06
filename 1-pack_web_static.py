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
    date = datetime.now()
    if isdir("versions") is False:
        local("mkdir versions")
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            date.second
            )
    try:
        print("Packing web_static to {}".format(file_name))
        local("tar -cvzf {} web_static".format(file_name))
        arch_size = os.stat(file_name).st_size
        print("web_static packed: {} -> {} Bytes".format(file_name, arch_size))
    except Exception:
        return None
    return file_name
