from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
N = 3*1024
Fn = np.linspace(0 , 512 , int(N/2))
Fn1,Fn2= np.random.randint(0, 512, 2)
t=np.linspace(0,3,12*1024)
noise= np.sin(2*np.pi*Fn1*t)+np.sin(2*np.pi*Fn2*t)
f=np.array([261.63,293.66,329.63,261.63,329.63,261.63,329.63])
F=np.zeros(7,dtype=int)
T1=np.array([0,0.65,0.9,1.55,1.9,2.35,2.7])
T2=np.array([0.6,0.85,1.3,1.85,2.2,2.65,3])
ans=0
for i in range(7):
   u=np.where(t>T1[i],1,0)
   y=np.where(t>T2[i],1,0)
   res=(np.sin(2*np.pi*F[i]*t)+np.sin(2*np.pi*f[i]*t))*(u-y)
   ans=ans+res
x_fWithoutNoise = fft(ans)
x_fWithoutNoise = 2/N * np.abs(x_fWithoutNoise [0:np.int(N/2)])
ansNoise=ans+noise
x_f = fft(ansNoise)
x_f = 2/N * np.abs(x_f [0:np.int(N/2)])
m = round(max(x_fWithoutNoise))
myNoise=[]
for i in range(len(Fn)):
  if (round(x_f[i]) > m):
     myNoise+=[Fn[i]]
     
Fn1new=round(myNoise[0])
Fn2new=round(myNoise[1])
print(Fn1)
print(Fn1new)
print(Fn2)
print(Fn2new)
ansFinal=ansNoise-(np.sin(2*np.pi*Fn1new*t)+np.sin(2*np.pi*Fn2new*t))
withOutNoise=fft(ansFinal)
withOutNoise = 2/N * np.abs(withOutNoise [0:np.int(N/2)])
plt.subplot(6,2,1)
plt.plot(t,ans)
plt.subplot(6,2,2)
plt.plot(Fn,x_fWithoutNoise)
plt.subplot(6,2,3)
plt.plot(t,ansNoise)
plt.subplot(6,2,4)
plt.plot(Fn,x_f)
plt.subplot(6,2,5)
plt.plot(t,ansFinal)
plt.subplot(6,2,6)
plt.plot(Fn,withOutNoise)
sd.play(ansFinal,3*1024)