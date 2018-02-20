import matplotlib.pylab as plt
import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift
from scipy.signal import get_window

fs = 44100

f = 10000

Ts = 1/fs

t = np.arange(0, 1, Ts)

A = np.sin(2*np.pi * f * t)

n = len(A) # length of the signal

'''
n = 256
n = 512
n = 1024
'''

k = np.arange(n)

T = n/fs

frq = k/T # two sides frequency range

frq = frq[range(int(n/2))] # one side frequency range

Y = fft(A)/n #fft computing and normalization

Y = Y[range(int(n/2))]

fig, ax = plt.subplots(2,1)

ax[0].plot(t,A)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,np.abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')

plt.show()


'''
plt.plot(window)
plt.title("Hamming window")
plt.ylabel("Amplitute")
plt.xlabel("Sample")
plt.show()
'''
