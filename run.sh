#/bin/bash
echo starting Eyesy
cd ~/sidekick/patches/Eyesy

# make sure the log file exists
touch /tmp/video.log

amixer cset numid=11 on

systemctl start eyesy-python.service
systemctl start eyesy-web.service
systemctl start eyesy-web-socket.service

/usr/bin/pd -alsamidi -nogui -noaudio -path /home/we/sidekick/pdexternals pd/main.pd
