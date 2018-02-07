import matplotlib.pyplot as plt
import numpy as np
import librosa

f = 0.5
fs = 770

t = np.arange(-1,1+1/fs,1/fs)
A = np.sin(2*np.pi*f*t)

plt.plot(t,A)

plt._show()
