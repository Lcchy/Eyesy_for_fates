#!/bin/bash

vncserver -kill :1

systemctl stop eyesy_norns_cast-python.service
systemctl stop eyesy-web.service
systemctl stop eyesy-web-socket.service
systemctl stop eyesy-pd.service

echo Starting norns
~/sidekick/patches/Norns/stop.sh