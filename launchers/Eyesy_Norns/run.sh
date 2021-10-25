#/bin/bash

# make sure the log file exists
touch /tmp/video.log

echo Starting norns
bash /home/we/sidekick/patches/Norns/run.sh
sleep 4

echo Starting Eyesy
systemctl start eyesy_norns-python.service
systemctl start eyesy-web.service
systemctl start eyesy-web-socket.service
systemctl start eyesy-pd-no-hw-ctl.service
