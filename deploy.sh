#!/bin/bash

# copy files
sudo cp systemd/eyesy-python.service /lib/systemd/system

sudo systemctl daemon-reload
