import signal

import matplotlib.pyplot as plt
import numpy as np
import librosa
import scipy
from scipy import signal
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
#plt._show() #show plot on IDE

#second signal

fs2 = 44100
f2= 1209.0

t2 = np.linspace(0, 1, 0.002 * fs2, endpoint=False)
A2 = np.sin(2*np.pi*f2*t2)

plt.grid(axis='both') # draw grid on plot
plt.plot(t2,A2) # plotting amplitude A(y axis), time t(y axis)

plt.title('Sine Wave 2') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis

plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
#plt._show() #show plot on IDE

#Signals mixed
result = A + A2 # mix sine waves

plt.title('Sine Wave Mixed') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis

plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
plt.plot((t+t2),result) # plot the sine wave
#plt.show()



#define the keypad and its frequencies
validkeys = '*#0123456789ABCD' #valid keys
rowfreqs = [697, 770, 852, 941] #row frequencies
colfreqs = [1209, 1336, 1477, 1633] #column frequencies
buttons = {'1':(0,0), '2':(0,1), '3':(0,2), 'A':(0,3),
'4':(1,0), '5':(1,1), '6':(1,2), 'B':(1,3),
'7':(2,0), '8':(2,1), '9':(2,2), 'C':(2,3),
'*':(3,0), '0':(3,1), '#':(3,2), 'D':(3,3)} #matrix of buttons

# I could not make this code to work I kept getting the following error: sounds = np.append([np.sin(2 * np.pi * fr * t).astype(np.float32) + np.sin(2 * np.pi * fc * t).astype(np.float32)],axis=0)
#TypeError: append() missing 1 required positional argument: 'values'
def dtmf_encoder(phonenumber):

    dur = 0.5
    Fs= 44100 # sampling rate

    t = np.linspace(0, dur, dur * Fs, endpoint=False)

    sounds = np.zeros(int(phonenumber)) #array of zeros where I intended to append signals

    for key in phonenumber:
        if key.upper() in validkeys:
            r, c = buttons[key]
            fr, fc = rowfreqs[r], colfreqs[c]
    sounds = np.append(np.sin(2 * np.pi * fr * t).astype(np.float32) + np.sin(2 * np.pi * fc * t).astype(np.float32))
    return librosa.output.write_wav('C:/Users/Michael Hernandez/Desktop/sounds.wav', sounds, Fs)

#Tone of digit three

fs = 44100
row_f = 697.0

row_t = np.linspace(0, 1, 0.002 * fs, endpoint=False)
row_A =np.sin(2 * np.pi * row_f * row_t).astype(np.float32)

col_f = 1477.0

col_t = np.linspace(0, 1, 0.002 * fs, endpoint=False)
col_A =np.sin(2 * np.pi * col_f * row_t).astype(np.float32)

b, a = signal.butter(6, 1000, 'low', analog=True)
row_A, col_A = signal.freqs(b,a)

plt.plot(row_A, 20 * np.log10(abs(col_A )))
plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(1000, color='green') # cutoff frequency
plt.show()
