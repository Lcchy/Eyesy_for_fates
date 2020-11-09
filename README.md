# EYESY_OS_fates

The operating system for the EYESY video synthesizer device - remixed.

Adaptation of the Critter&Guitari Eyesy video synth in order to run it on Fates (or norns shield) as a Sidekick App.

### Installation :
```
 sudo apt install python-pygame python-liblo python-alsaaudio
 git clone https://github.com/Lcchy/Eyesy_for_fates Eyesy
 cd Eyesy
 ./deploy.sh
 ```
 
### Usage:
 - connect a display to the first hdmi out
 - boot up the fates
 - select Eyesy in Sidekick and control the video output via the hardware buttons
 
![text](hardware_usage.png)

 
 I also exposed various controls to midi:
  
  | Midi CC    | 21,22,23,24 | 25               | 26, 27               | 28                | 29, 30              | 31        | 32           | 33              | 34                         | 35       | 36         | 37             | 38                       |
|-------|-------------|------------------|----------------------|-------------------|---------------------|-----------|--------------|-----------------|----------------------------|----------|------------|----------------|--------------------------|
| Control | Mode Params | Background Color | Previous, Next Scene | Auto Clear Toggle | Previous, Next Mode | Info Disp | Send Trigger | Take Screenshot | Save or delete (long hold) | ShiftKey | Input Gain | Trigger Source | Midi In Channel (init 1) |

ETC Manual : https://github.com/critterandguitari/ETC_Manual/blob/master/manual.md

### Rem:
- I haven't tested the web interface for mode editing, it probably doesn't work
- If you don't connect the display before booting, Eyesy will launch on the fates display which is fun
- Eyesy uses alsa as a backend which means you cannot use other audio processes at the same time

### TODO:
- Make the Open Frameworks engine work
- Move everything to Jack
- Web interface
