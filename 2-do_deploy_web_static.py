#!/usr/bin/python3
'''
Module: '2-do_deploy_web_static'
Fabric script to distribute archive file to web server
'''

from fabric.api import local, run, put, env
import os.path

env.hosts = ['52.73.28.65', '54.90.18.103']


def do_deploy(archive_path):
