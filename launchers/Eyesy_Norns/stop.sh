#!/bin/bash

systemctl stop eyesy_norns-python.service
systemctl stop eyesy-web.service
systemctl stop eyesy-web-socket.service
systemctl stop eyesy-pd-no-hw-ctl.service

echo Stoping norns
bash /home/we/sidekick/patches/Norns/stop.sh
sleep 1
