#!/usr/bin/env bash
# Script that installs, configures and starts Nginx web server
# shellcheck disable=SC2230

# Install Nginx if it is not already installed
if [[ "$(which nginx | grep -c nginx)" == '0' ]]; then
	sudo apt-get update
	sudo apt-get -y install nginx
	sudo service nginx start
fi

# Keep configuration from previous scripts
mkdir -p /var/www/html /var/www/error
chmod -R 755 /var/www
echo 'Hello World!' > /var/www/html/index.html
echo -e "Ceci n\x27est pas une page" > /var/www/error/404.html

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
FAKE_HTML="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
echo -e "$FAKE_HTML" > /data/web_static/releases/test/index.html

# Remove existing symbolic link if it exists
[ -d /data/web_static/current ] && rm -rf /data/web_static/current

# Create a new symbolic link to /data/web_static/releases/test/
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update the configuration(add location alias)
UPDATE_CNF="server {
	listen 80 default_server;
	listen [::]:80 default_server;
	server_name _;
	index index.html index.htm;
	error_page 404 /404.html;
	add_header X-Served-By \$hostname;
	location / {
		root /var/www/html/;
		try_files \$uri \$uri/ =404;
	}
	location /hbnb_static/ {
		alias /data/web_static/current/;
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me) {
		rewrite ^ https://github.com/abdi8-GitHub permanent;
	}
	location = /404.html {
		root /var/www/error/;
		internal;
	}
}
"
bash -c "echo -e '$UPDATE_CNF' > /etc/nginx/sites-available/default"

# Create a symbolic link for the new configuration file
ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

# Restart Nginx changes will take effect
sudo service nginx restart

# Exis Success
exit 0
