#/bin/bash

# make sure the log file exists
touch /tmp/video.log

echo Starting Vncserver
vncserver -localhost no

amixer cset numid=11 on

echo Starting Eyesy
systemctl start eyesy_cast-python.service
systemctl start eyesy-web.service
systemctl start eyesy-web-socket.service
systemctl start eyesy-pd.service