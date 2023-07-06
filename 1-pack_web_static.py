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
        local("tar -cvzf {} web_static".format(file_name))
    except Exception:
        return None
    return file_name
