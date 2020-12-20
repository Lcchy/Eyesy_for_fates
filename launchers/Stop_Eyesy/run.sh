#!/bin/bash

amixer cset numid=11 off

systemctl stop eyesy-python.service
systemctl stop eyesy_cast-python.service
systemctl stop eyesy-web.service
systemctl stop eyesy-web-socket.service
systemctl stop eyesy-pd.service

vncserver -kill :1

pidof pd | xargs -r kill

python3 /home/we/fates_deploy/scripts/osc_sender.py --message_path "/sk/activate" --message 1
