#!/bin/bash

systemctl stop eyesy_norns-python.service
systemctl stop eyesy-web.service
systemctl stop eyesy-web-socket.service
# systemctl stop eyesy-pd.service

echo Stoping norns
mv ~/dust/data/system.state /tmp/ ; sed 's/norns.state.clean_shutdown = false/norns.state.clean_shutdown = true/' < /tmp/system.state > ~/dust/data/system.state
sudo systemctl stop norns-maiden.service
sudo systemctl stop eyesy_norns-matron.service
sudo systemctl stop norns-sclang.service
sudo systemctl stop norns-crone.service
sudo systemctl stop norns-jack.service
sleep 1