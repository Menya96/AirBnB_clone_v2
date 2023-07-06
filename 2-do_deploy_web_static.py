#!/usr/bin/python3
'''
Module: '2-do_deploy_web_static'
Fabric script to distribute archive file to web server
'''

from fabric.api import local, run, put, env
import os.path

env.hosts = ['52.73.28.65', '54.90.18.103']


def do_deploy(archive_path):
    '''Deploy to a web server'''
    if os.path.isfile(archive_path) is False:
        return False
    file = os.path.basename(archive_path)
    folder = file.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder)
    flag = False
    try:
        put(archive_path, "/tmp/{}".format(file))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm -rf /tmp/{}".format(file))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        flag = True
    except Exception:
        flag = False
    return flag
