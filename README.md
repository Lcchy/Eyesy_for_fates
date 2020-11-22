# EYESY_OS_fates

The operating system for the [EYESY video synthesizer device](https://github.com/critterandguitari/EYESY_OS) - remixed.

Adaptation of the Critter&Guitari Eyesy video synth in order to run it on Fates (or norns shield) as a Sidekick App.

Eyesy Manual : https://www.critterandguitari.com/manual?m=EYESY_Manual#eyesy%E2%84%A2-user-manual

Support thread for this project : https://llllllll.co/t/critter-guitari-video-synth-eyesy-for-fates-working/38144

### Installation :
```
 cd ~/sidekick/patches
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
  
  | Midi CC    | 21,22,23,24 | 25               | 26               | 27               | 28                | 29                | 30              | 31        | 32           | 33              | 34                         | 35       |
  |-------|-------------|------------------|----------------------|-------------------|---------------------|-----------|--------------|-----------------|----------------------------|----------|------------|----------------|
  | Control | Mode Params | Background Color | Scene selection | Save or delete (long hold) | Auto Clear Toggle | Mode Selection | Take Screenshot | Info Disp | Send Trigger | ShiftKey | Input Gain | Trigger Source |

### Web editor
The web editor should be accessible at http://norns.local:8080/

See the Eyesy manual for more details on using the web editor.

### Rem:
- If you don't connect the display before booting, Eyesy will launch on the fates display which is fun
- Eyesy uses alsa as a backend which means you cannot use other audio processes at the same time

### TODO:
- Make the Open Frameworks engine work
- Move everything to Jack
