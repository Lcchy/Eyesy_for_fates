# EYESY_OS_fates

The operating system for the EYESY video synthesizer device - remixed.

Adaptation of the Critter&Guitari Eyesy video synth in order to run it on Fates (or norns shield) as a Sidekick App.

Installation :
 - clone this repo into '~/sidekick/patches'
 - run 'deploy.sh'
 
Usage:
 - connect a display to the first hdmi out
 - boot up the fates
 - select Eyesy in Sidekick and control the video output via the hardware buttons
 
![text](hardware_usage.png)

Rem:
- I haven't tested the web interface for mode editing, it probably doesn't work
- If you don't connect the display before booting, Eyesy will launch on the fates display which is fun
- Eyesy uses alsa as a backend which means you cannot use other audio processes at the same time

TODO:
- Map Midi controls for all parameters
- Make the Open Frameworks engine work
- Move everything to Jack
- Web interface
