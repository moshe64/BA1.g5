import numpy as np
import math
from matplotlib import pyplot as plt
 
# Parametros de la senal de interes
fo=1000. # es una frecuencia fundamental
k=2
f=k*fo # es la frecuencia de la senoidal
N=8
 
# La senal discreta 
n=np.linspace(0,N-1,N)
signal=np.exp(1.j*2.*math.pi*k*n/N)
fourier=np.fft.fft(signal)
fourier_mejor=np.fft.fftshift(fourier)

# calculos para relacional la senal discreta con el mundo real
T=1./fo 
Tsamp=T/N
Fsamp=1./Tsamp
Fmin=-Fsamp/2.
Fresol=Fsamp/N
Fmax=-Fmin-Fresol
f=np.linspace(Fmin,Fmax,N)
 
plt.stem(f,fourier_mejor)  # plt.plot(f,fourier_mejor)
plt.show()

