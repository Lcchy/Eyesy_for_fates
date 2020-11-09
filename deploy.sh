#!/bin/bash

# copy files
sudo cp systemd/eyesy-python.service /lib/systemd/system

cp pd/*.pd_linux ../../pdexternals

sudo systemctl daemon-reload
