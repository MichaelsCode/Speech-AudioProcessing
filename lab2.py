import matplotlib.pyplot as plt
import numpy as np
import librosa
import scipy as sp
import scipy.signal
import scipy.io.wavfile

#s ine wave formula A sin(wt)


fs = 44100 # sampling rate
f = 770.0# frequency of the signal
t = np.linspace(0, 0.5, 0.002 * fs, endpoint=False) #time calculation (x axis)

A =np.sin(2 * np.pi * f * t).astype(np.float32)  # amplitude calculation (y axis)

plt.grid(axis='both') # draw grid on plot
plt.plot(t,A) # plotting amplitude A(y axis), time t(y axis)
plt.title('Sine Wave') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis

plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
plt._show() #show plot on IDE

#second signal

fs2 = 44100
f2= 1209

t2 = np.linspace(0, 1, 0.002 * fs2, endpoint=False)
A2 = np.sin(2*np.pi*f2*t2)

plt.grid(axis='both') # draw grid on plot
plt.plot(t2,A2) # plotting amplitude A(y axis), time t(y axis)

plt.title('Sine Wave 2') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis

plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
plt._show() #show plot on IDE

#Signals mixed
result = A + A2 # mix sine waves

plt.title('Sine Wave Mixed') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis

plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
plt.plot((t+t2),result) # plot the sine wave
plt.show()



#define the keypad and its frequencies
validkeys = '*#0123456789ABCD'
rowfreqs = [697, 770, 852, 941]
colfreqs = [1209, 1336, 1477, 1633]
buttons = {'1':(0,0), '2':(0,1), '3':(0,2), 'A':(0,3),
'4':(1,0), '5':(1,1), '6':(1,2), 'B':(1,3),
'7':(2,0), '8':(2,1), '9':(2,2), 'C':(2,3),
'*':(3,0), '0':(3,1), '#':(3,2), 'D':(3,3)}

def dtmf_encoder(phonenumber):

    dur = 0.5
    silencedur = 0.1
    Fs= 44100


    t = np.linspace(0, dur, dur * Fs, endpoint=False)
    silence = np.zeros(int(silencedur * Fs))

    sounds = np.zeros()
    for key in phonenumber:
        if key.upper() in validkeys:
            r, c = buttons[key]
            fr, fc = rowfreqs[r], colfreqs[c]
    # print key, fr, fc
    sounds = np.append(np.sin(2 * np.pi * fr * t).astype(np.float32) + np.sin(2 * np.pi * fc * t).astype(np.float32))
    sounds = np.append(silence)
    np.concatenate(sounds[:-1])  # drop last silence period
    librosa.output.write_wav('C:/Users/Michael Hernandez/Desktop/sounds.wav', sounds, Fs)
    return  np.concatenate(sounds[:-1])

dtmf_encoder('12')