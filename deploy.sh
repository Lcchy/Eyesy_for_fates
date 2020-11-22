#!/bin/bash

set -ex

# Add nodejs Debian package as source.
# Note the need to allow releaseinfo changes. See https://askubuntu.com/questions/989906/explicitly-accept-change-for-ppa-label
curl -sL https://deb.nodesource.com/setup_14.x | sed -e 's/apt-get /apt-get --allow-releaseinfo-change /g' | sudo bash -

# Debian packages
sudo apt install -y python-pygame python-liblo python-alsaaudio python-pip nodejs

# Python packages
sudo pip install psutil cherrypy numpy JACK-Client

# Node packages
cd web/node && npm install && cd ../..

# Move service files into place and make sure perms are set correctly.
sudo chmod 644 systemd/*
sudo cp systemd/* /etc/systemd/system


# Move PD into place.
cp pd/externals/*.pd_linux ../../pdexternals

# Reload services.
sudo systemctl daemon-reload
