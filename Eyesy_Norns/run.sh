#/bin/bash

# make sure the log file exists
touch /tmp/video.log

echo Starting norns
sudo systemctl start norns-jack.service
sudo systemctl start norns-crone.service
sudo systemctl start norns-sclang.service
sudo systemctl start eyesy_norns-matron.service
sudo systemctl start norns-maiden.service
sleep 4

echo Starting Eyesy
systemctl start eyesy_norns-python.service
systemctl start eyesy-web.service
systemctl start eyesy-web-socket.service
# systemctl start eyesy-pd.service          # Deactivated to let norns take over the hardware