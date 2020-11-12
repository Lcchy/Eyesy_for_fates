#/bin/bash
echo starting Eyesy
cd ~/sidekick/patches/Eyesy

amixer cset numid=11 on

systemctl start eyesy-python.service

/usr/bin/pd -alsamidi -nogui -noaudio -path /home/we/sidekick/pdexternals pd/main.pd