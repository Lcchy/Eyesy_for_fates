import alsaaudio, audioop
import time
import math

inp = None
etc = None
trig_this_time = 0
trig_last_time = 0
sin = [0] * 100

def init (etc_object) :
    global inp, etc, trig_this_time, trig_last_time, sin
    etc = etc_object
    #setup alsa for sound in
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
    inp.setchannels(2) 
    inp.setrate(6000)       # Original value of 11025 was giving error.. OR 44100
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(300)  # OR 1024
    trig_last_time = time.time()
    trig_this_time = time.time()
    
    for i in range(0,100) :
        sin[i] = int(math.sin(2 * 3.1459 * i / 100) * 32700)

def recv() :
    global inp, etc, trig_this_time, trig_last_time, sin
    # get audio
    l,data = inp.read()
    peak = 0
    if l > 0:
        try :
            ldata = audioop.tomono(data, 2, 1, 0)
            rdata = audioop.tomono(data, 2, 0, 1)
            for i in range(0,100) :
                avg_l = 0
                avg_r = 0

                idx = i * 3
                avg_l +=audioop.getsample(ldata,2,idx)
                avg_r +=audioop.getsample(rdata,2,idx)

                idx += 1
                avg_l +=audioop.getsample(ldata,2,idx)
                avg_r +=audioop.getsample(rdata,2,idx)

                idx += 1
                avg_l +=audioop.getsample(ldata,2,idx)
                avg_r +=audioop.getsample(rdata,2,idx)

                avg_l = avg_l / 3
                avg_r = avg_r / 3

                avg = (avg_l + avg_r) / 2

                # scale it
                avg = int(avg * etc.audio_scale)
                avg_l = int(avg_l * etc.audio_scale)
                avg_r = int(avg_r * etc.audio_scale)

                if (avg > 20000) :
                    trig_this_time = time.time()
                    if (trig_this_time - trig_last_time) > .05:
                        if etc.audio_trig_enable: etc.audio_trig = True
                        trig_last_time = trig_this_time
                if avg > peak :
                    etc.audio_peak = avg
                    peak = avg
                # if the trigger button is held
                if (etc.trig_button) :
                    etc.audio_in[i] = sin[i]
                    etc.audio_left[i] = sin[i] 
                    etc.audio_right[i] = sin[i] 
                else :
                    etc.audio_in[i] = avg
                    etc.audio_left[i] = avg_l
                    etc.audio_right[i] = avg_r

        except :
            pass
        l,data = inp.read()

