import signal

import matplotlib.pyplot as plt
import numpy as np
import librosa
import scipy
from scipy import signal
import scipy.io.wavfile

'#s ine wave formula A sin(wt)'


fs = 44100 # sampling rate
f = 770 # frequency of the signal
t = np.linspace(0, 0.5, fs, endpoint=True) #time calculation (x axis)

A =np.sin(2 * np.pi * f * t).astype(np.float32)  # amplitude calculation (y axis)

plt.grid(axis='both') # draw grid on plot
plt.axis([0,0.02,-1,1])
plt.plot(t,A) # plotting amplitude A(y axis), time t(y axis)
plt.title('Sine Wave') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis

plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
plt._show() #show plot on IDE

#second signal

fs2 = 44100
f2= 1209

t2 = np.linspace(0, 1, fs2, endpoint=True)
A2 = np.sin(2*np.pi*f2*t2)

plt.grid(axis='both') # draw grid on plot
plt.axis([0,0.02,-1,1])W
plt.plot(t2,A2) # plotting amplitude A(y axis), time t(y axis)

plt.title('Sine Wave 2') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis

plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
plt._show() #show plot on IDE

#Signals mixed
times = np.array(t + t2)
result = np.array(A + A2)
sine_wave_mixed = np.array([result,times])
librosa.output.write_wav('/home/michael/Documents/sinewavemixed.wav', result, fs)

#result = A + A2 # mix sine waves
plt.grid(axis='both') # draw grid on plot
#plt.axis([0,result.size,-1,1])
plt.plot(times,result) # plotting amplitude A(y axis), time t(y axis)
plt.title('Sine Wave Mixed') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis
plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
plt.show()

#define the keypad and its frequencies
validkeys = '*#0123456789ABCD' #valid keys
rowfreqs = [697, 770, 852, 941] #row frequencies
colfreqs = [1209, 1336, 1477, 1633] #column frequencies
buttons = {'1':(0,0), '2':(0,1), '3':(0,2), 'A':(0,3),
'4':(1,0), '5':(1,1), '6':(1,2), 'B':(1,3),
'7':(2,0), '8':(2,1), '9':(2,2), 'C':(2,3),
'*':(3,0), '0':(3,1), '#':(3,2), 'D':(3,3)} #matrix of buttons

def dtmf_encoder(phonenumber):

    dur = 0.5
    Fs= 44100 # sampling rate

    t = np.linspace(0, dur, dur * Fs, endpoint=False)

    for key in phonenumber:
        if key.upper() in validkeys:
            r, c = buttons[key]
            fr, fc = rowfreqs[r], colfreqs[c]
    sounds = np.array(np.cos(2 * np.pi * fr * t).astype(np.float32) + np.cos(2 * np.pi * fc * t).astype(np.float32))
    librosa.output.write_wav('/home/michael/Documents/sounds.wav', sounds, Fs)
    return

dtmf_encoder('5') #run the function

#Tone of digit three

fs = 44100
row_f = 697

row_t = np.linspace(0, 0.5, 0.5 * fs, endpoint=False)
row_A =np.sin(2 * np.pi * row_f * row_t).astype(np.float32)

col_f = 1477

col_t = np.linspace(0, 0.5, 0.5 * fs, endpoint=False)
col_A =np.sin(2 * np.pi * col_f * row_t).astype(np.float32)

digit3 = np.array(np.sin(2 * np.pi * row_f * row_t).astype(np.float32) + np.sin(2 * np.pi * col_f * row_t).astype(np.float32))

librosa.output.write_wav('/home/michael/Documents/digit3.wav', digit3, fs)

b, a = signal.butter(6, 1000/(fs/2), 'low', analog=True,output='ba') #here I'm using a filter order 6 and cutoff at 1000

row_A, col_A = signal.freqs(b, a) #here I'm applying the butterworth filter.

plt.plot(row_A, 20 * np.log10(abs(col_A)))
plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(1000, color='green') # cutoff frequency
plt.show()

signal_filtered = np.array(row_A,col_A)
#librosa.output.write_wav('/home/michael/Documents/digit3filtered.wav', signal_filtered, fs)
