#!/usr/bin/env bash
# prep web static
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test/
echo -e "<!doctype html>
<html>
  <head>
  </head>
  <body>
    testy testy
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
file="/etc/nginx/sites-available/default"
has_alias="$(grep '/hbnb_static/' /etc/nginx/sites-available/default  -c)"
if [ "$has_alias" -eq 0 ]
    then
        sudo sed -i '/^\tserver_name _;/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $file
else
        # pass
        :
fi
sudo service nginx restart
