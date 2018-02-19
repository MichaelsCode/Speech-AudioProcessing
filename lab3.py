import matplotlib.pylab as plt
import numpy as np
from scipy.fftpack import fft

fs = 44100

f = 10000

Ts = 1/fs

t = np.arange(0, 1, Ts)

A = np.sin(2*np.pi * f * t)

n = len(A) # length of the signal

k = np.arange(n)

T = n / fs

plt.plot(t,A)

plt.title('Sine Wave')
plt.xlabel('Time(s)', fontsize=16)

plt.ylabel('Amplitude', fontsize=16)

plt.grid(True,which='both')

plt.axhline(y=0, color='k')
frq = k/T # two sides frequency range

frq = frq[range(int(n/2))] # one side frequency range

Y = np.fft.fft(A)/n #fft computing and normalization

Y = Y[range(int(n/2))]

fig, ax = plt.subplots(2,1)

ax[0].plot(t,A)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')

plt.show()


