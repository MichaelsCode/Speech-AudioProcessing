import matplotlib.pylab as plt
import numpy as np
from scipy.fftpack import fft


Fs = 10000
Ts = 1.0/Fs

t = np.arange(0,1,Ts)

ff = 1

y = np.sin(2*np.pi*ff*t)

plt.plot(t,y)

plt.title('Sine Wave')
plt.xlabel('Time(s)', fontsize=16)

plt.ylabel('Amplitude', fontsize=16)

plt.grid(True,which='both')

plt.axhline(y=0, color='k')

plt.show()


