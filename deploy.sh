#!/bin/bash

# copy files
sudo rm -f /lib/systemd/system/eyesy-python.service
sudo chmod 644 systemd/eyesy-python.service
sudo cp systemd/eyesy-python.service /etc/systemd/system

cp pd/*.pd_linux ../../pdexternals

sudo systemctl daemon-reload