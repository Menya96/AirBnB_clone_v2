#!/usr/bin/python3
'''
Module: '1-pack_web_static'
Script that generates a .tgz archive from contents of web_static folder
'''

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the archive name using the current date and time
    archive_name = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))

    # Compress the web_static folder into the archive
    result = local("tar -czvf versions/{} web_static".format(archive_name))

    if result.succeeded:
        # Return the archive path if the archive has been correctly generated
        return "versions/{}".format(archive_name)
    else:
        # Return None if the archive generation failed
        return None
