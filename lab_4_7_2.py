import numpy as np
import math
from matplotlib import pyplot as plt

# Parametros de la senal analiada
f=float(input("Ingrese el valor de la frecuencia de la senal: "))
Fsamp=float(input("Ingrese el valor de la frecuencia de muestreo: ")) # la frecuencia de muestreo

# La senal discreta 
N=float(input("Ingrese el numero de puntos N de la fft: "))
n=np.linspace(0,N-1,N)
t=n/Fsamp

print("Las senales a las que le puede efectuar la fft: ")
print("1. Senal coseno")
print("2. Senal exponencial")
n=int(input("Elija cual senal: "))
while n<1 or n>2:
    print("La opcion no es valida introduzca otra")
    n=int(input("Elija cual senal: "))

if n==1:
    signal=np.cos(2.*math.pi*f*t)

if n==2:
    signal=np.exp(1.j*2.*math.pi*f*t)
        
fourier=abs(np.fft.fft(signal))**2
fourier_mejor=np.fft.fftshift(fourier)
 
# calculos para relacional la senal discreta con el mundo real
Fmin=-Fsamp/2.
Fresol=Fsamp/N
Fmax=-Fmin-Fresol
f=np.linspace(Fmin,Fmax,N)
 
plt.plot(f,fourier_mejor)
plt.show()
