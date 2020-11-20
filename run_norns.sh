#/bin/bash
echo starting Eyesy

# make sure the log file exists
touch /tmp/video.log

systemctl start eyesy_norns-python.service
systemctl start eyesy-web.service
systemctl start eyesy-web-socket.service
systemctl start eyesy-pd.service
