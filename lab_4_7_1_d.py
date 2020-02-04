import numpy as np
import math
from matplotlib import pyplot as plt
 
# Parametros de la senal analiada
f=3566.
Fsamp= 9000. # la frecuencia de muestreo
# La senal discreta 
N=280
n=np.linspace(0,N-1,N)
t=n/Fsamp
signal=np.exp(1.j*2.*math.pi*f*t)
fourier=np.fft.fft(signal)
fourier_mejor=np.fft.fftshift(fourier)
 
# calculos para relacional la senal discreta con el mundo real
Fmin=-Fsamp/2.
Fresol=Fsamp/N
Fmax=-Fmin-Fresol
f=np.linspace(Fmin,Fmax,N)
 
plt.plot(f,fourier_mejor)
plt.show()
