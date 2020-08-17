#!/usr/bin/python3
"""usmanjabbar.com"""

def do_deploy(archive_path):
    """
    -----------------
    METHOD: DO_DEPLOY
    -----------------
    DESCRIPTION:
        This method distributes and
        deploys an archive of web_static
        files
    ARGS:
        - Takes in a string with the path
        to the archive file
    NOTES:
        - If the archive_path doesn't exist,
        returns False
    """
    from fabric.api import env, run, put
    from os.path import isfile

    web01, web02 = '35.196.94.233', '54.160.230.10'
    env.hosts = [web01, web02]

    # Check if that file actually exists
    if not isfile(archive_path):
        return False

    try:
        # Extract the file name from the var 'archive_path'
        archive = archive_path.split('/')[-1]

        # Upload, uncompress and delete the archive from the web servers
        put(archive, '/tmp/')
        out_path = '/data/web_static/releases/{}'.format(archive.split('.')[1])
        run('mkdir -p {}'.format(out_path))
        run('tar -xzvf /tmp/{} -C {}'.format(archive, out_path))
        run('rm /tmp/{}'.format(archive))

        # Del symbolic link 'current' and link extracted folder to current
        run('rm /data/web_static/current')
        run('ln -sf /data/web_static/current {}'.format(out_path))

        # All good, return True
        return True

    except:
        return False
