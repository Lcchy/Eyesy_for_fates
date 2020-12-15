#!/bin/bash

systemctl stop eyesy_norns-python.service
systemctl stop eyesy-web.service
systemctl stop eyesy-web-socket.service
# systemctl stop eyesy-pd.service

echo Stoping norns
~/sidekick/patches/Norns/stop.sh