#!/bin/bash

sudo cp Eyesy_Cast/eyesy_cast-python.service /etc/systemd/system
sudo cp Eyesy_Norns_Cast/eyesy_norns_cast-python.service /etc/systemd/system

# Reload services.
sudo systemctl daemon-reload

./deploy.sh
