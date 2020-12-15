#!/bin/bash
amixer cset numid=11 off

systemctl stop eyesy_cast-python.service
systemctl stop eyesy-web.service
systemctl stop eyesy-web-socket.service
systemctl stop eyesy-pd.service

vncserver -kill :1
