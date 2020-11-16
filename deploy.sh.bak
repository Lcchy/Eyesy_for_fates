#!/bin/bash

set -ex

# copy files
sudo rm -f /lib/systemd/system/eyesy-python.service     #In case it is reinstalling

services=("eyesy-python.service" "eyesy-web.service" "eyesy-web-socket.service" "eyesy-pd.service")
for i in "${services[@]}"
do
  sudo chmod 644 systemd/$i
  sudo cp systemd/$i /etc/systemd/system
done

cp pd/*.pd_linux ../../pdexternals

sudo systemctl daemon-reload
