#!/bin/bash

set -ex

# make sure the log file exists 
touch /tmp/video.log
# killall -q node
pidof node | xargs -r kill
cd node
node websockettailer.js &
cd ..
# redirect 80 -> 8080
sudo iptables -A PREROUTING -t nat -p tcp --dport 80 -j REDIRECT --to-ports 8080
cherryd -i cpapp -c prod.conf 

