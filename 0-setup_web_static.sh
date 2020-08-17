#!/usr/bin/env bin
# Installs NGINX and sets up the initial file structure for the rest of the project
#	- Creates a symbolic link between the shared/ and releases/ folders
#	- Gives the ownership of the data/ folder to user and group called 'ubuntu'
#	- Update NGINX conf file to serve content from /data/web_static/current/ as /data/web_static/current/
sudo apt-get install nginx
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/current
mkdir -p /data/web_static/releases/test
echo "I'm Alive!" > /data/web_static/shared/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed '/^\tserver_name*/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart 
