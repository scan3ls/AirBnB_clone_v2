#!/usr/bin/env python3
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
    from datetime.datetime import now as time
    from os.path import isdir

    file = "web_static_" + time().strftime("%Y%m%d%H%M%S") + ".tgz"

    local('mkdir -p ./versions')

    try:
        local('tar -cfv {} ./versions/'.format(file))
        path = "versions/" + file
        return path
    except:
        return None
