import matplotlib.pyplot as plt
import numpy as np
import librosa
import scipy.signal


#s ine wave formula A sin(wt)
import result as result

f = 2 # frequency of the signal
fs = 770 # sample rate

t = np.arange(-1,1+1/fs,1/fs) # time calculation

A = np.sin(2*np.pi*f*t)# amplitude calculation

sinewave1 = np.array((t,A))
print(sinewave1.shape)

plt.grid(axis='both') # draw grid on plot
plt.plot(t,A) # plotting amplitude A(y axis), time t(y axis)

plt.title('Sine Wave') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis

plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
plt._show() #show plot on IDE

#second signal

f2 = 1
fs2= 1209

t2 = np.arange(-1,1+1/fs2,1/fs2)
A2 = np.sin(2*np.pi*f2*t2)

sinewave2 = np.array((t2,A2))
print(sinewave2.shape)


print(plt.plot(t2,A2))

plt.grid(axis='both') # draw grid on plot
plt.plot(t2,A2) # plotting amplitude A(y axis), time t(y axis)

plt.title('Sine Wave 2') #plot title
plt.xlabel('Time(s)', fontsize=16)#plot label for x axis

plt.ylabel('Amplitude', fontsize=16)#plot label for y axis
plt._show() #show plot on IDE

#x =  np.arange(-1,1+1/fs,1/fs) + np.arange(-1,1+1/fs2,1/fs2)
#y = np.sin(2*np.pi*f*t) + np.sin(2*np.pi*f2*t2)

#plt.plot(x,y)


