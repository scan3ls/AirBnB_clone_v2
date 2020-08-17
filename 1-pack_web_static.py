#!/usr/bin/python3
"""https://www.usmanjabbar.com/"""


def do_pack():
    """
    ---------------
    METHOD: DO_PACK
    ---------------
    DESCRIPTION:
        Creates a tar compressed file
        locally containing the content
        from /web_static/ and returns the
        path of where the compressed file
        has been stored.
    NOTES:
        - Output tar files are stored inside
        the versions/ directory.
        - Output file would be called
        "web_static_" + "current time" + ".tgz"
        - If the compression fails, None's returned.
    """
    from fabric.api import local
    from datetime import datetime as time

    file = "web_static_" + time.now().strftime("%Y%m%d%H%M%S") + ".tgz"

    local('mkdir -p versions')

    try:
        local('tar -cvzf versions/{} web_static/'.format(file))
        path = "versions/" + file
        return path
    except Exception:
        return None
