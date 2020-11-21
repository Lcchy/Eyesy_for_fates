#/bin/bash

# make sure the log file exists
touch /tmp/video.log

echo Starting Vncserver
vncserver -localhost no

echo Starting norns
~/sidekick/patches/Norns/run.sh

echo Starting Eyesy
systemctl start eyesy_norns_cast-python.service
systemctl start eyesy-web.service
systemctl start eyesy-web-socket.service
systemctl start eyesy-pd.service