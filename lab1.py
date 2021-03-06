import matplotlib.pyplot as plt
import numpy as np

x = np.sin(np.array([1, 0, -1], dtype=np.float32))
print(x)

m1 = [[0, 1, 2, 3, 2, 1, 0, -1, -2, -3],
      [0, 1, 2, 3, 2, 1, 0, -1, -2, -3]]

array2 = np.array(m1, dtype=np.float32)
print(array2.shape)

m2 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, .1, .2, .3, 2, 1, 0, .1, .2, .3]]

m3 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, .1, .2, .3, 0, 1, 0, .1, .2, .3]]


a1 = np.array(m2, dtype=np.float32)
plt.plot(a1[0, :], a1[1, :], 'r-x')
plt.show()

a2 = np.array(m3, dtype=np.float32)
plt.plot(a2[0, :], a2[1, :], 'r-x')
plt.show()

#print(np.max(a1[1]))
#print(np.argmax(a1[1]))

f = 2 #frequency of the signal
fs = 100 #sample rate

t = np.arange(-1,1+1/fs,1/fs)

A = np.sin(2*np.pi*f*t)

plt.plot(t,A)

plt.title('Sine Wave')
plt.xlabel('Time(s)', fontsize=16)

plt.ylabel('Amplitude', fontsize=16)

plt.grid(True,which='both')

plt.axhline(y=0, color='k')

plt.show()

plt.show()

xslice = A[A.size//2+1::]
plt.plot(t[A.size//2+1::],xslice,'o-r')
plt.grid(True,which='both')
plt.show()

from wave import open as open_wave
fp = open_wave("C:/Users/Michael Hernandez/Downloads/196959__margo-heston__i-see-nine-apples-m.wav", 'r')
strframes = fp.readframes(fp.getnframes())
fp.close()
ys = np.fromstring(strframes, dtype=np.int16)
ts = np.arange(len(ys)) / fp.getframerate()

fig,ax =plt.subplots()
ax.plot(ts,ys,'-r')
ax.set_xlabel('time(s)', fontsize=16)
ax.set_ylabel('amplitute', fontsize=16)
plt.show()







