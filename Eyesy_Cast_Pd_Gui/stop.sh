#!/bin/bash
amixer cset numid=11 off

systemctl stop eyesy_cast-python.service
systemctl stop eyesy-web.service
systemctl stop eyesy-web-socket.service

pidof pd | xargs -r kill

vncserver -kill :1
