import matplotlib.pylab as plt
import numpy as np

f = 1
fs = 10000

t = np.arange(-1,1+1/fs,1/fs)

A = np.sin(2*np.pi*f*t)

plt.plot(t,A)

plt.title('Sine Wave')
plt.xlabel('Time(s)', fontsize=16)

plt.ylabel('Amplitude', fontsize=16)

plt.grid(True,which='both')

plt.axhline(y=0, color='k')

plt.show()