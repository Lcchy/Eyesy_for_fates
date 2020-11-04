#/bin/bash
echo starting Eyesy
cd ~/sidekick/patches/Eyesy

sudo systemctl start eyesy-python.service

/usr/bin/pd -alsamidi -noaudio -path /home/we/sidekick/pdexternals pd/main.pd #-nogui