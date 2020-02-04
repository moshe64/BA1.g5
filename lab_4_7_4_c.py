import numpy as np
################################################################################
## Escribimos el codigo a probar, sin usar "self" porque esto no es una clase ##
################################################################################
N=128 # N va a ser ahora un parametro del bloque
def work(input_items, output_items):
    in0 = input_items[0]
    out0 = output_items[0]
    out0[:]=abs(np.fft.fftshift(np.fft.fft(in0,N),1)) # ,1 es lo unico que cambio 
    return len(out0)
 
###############################################################################
##              PRUEBAS A LA FUNCION WORK                                    ##
###############################################################################
import math
from matplotlib import pyplot as plt
 
# Deinifimos la senal entrante
f=1378.
Fsamp= 8000. # la frecuencia de muestreo
 
n=np.linspace(0,N-1,N)
t=n/Fsamp
 
# Tambien cambio la manera en que las senales se expresan en las pruebas:
# para presentar la senal como una matriz de prueba, vamos a suponer que cada
# N muestras la senal presenta una pequena desviacion de frec
signal0=np.cos(2.*math.pi*f*t)
signal1=np.cos(2.*math.pi*(f+100)*t)
signal2=np.cos(2.*math.pi*(f-60)*t)
 
# creamos el array 2d para la senal entrante y saliente
in_sig=np.array([signal0,signal1,signal2])    # array 3xN
out_sig=np.array([0.]*N)                      # array 1xN
out_sig=np.array([out_sig, out_sig, out_sig]) # arrat 3xN
 
# Pasamos a array 3d las dos senales ya que es necesario introducir la dimension
# que en GNU radio debe ser destinada para identificar las posibles entradas y salidas
# que puede tener un bloque
in_sig= np.array([in_sig])   # array 1x3xN
out_sig=np.array([out_sig])  # array 1x3xN
 
# Por fin comprobamos la funcion
d=work(in_sig,out_sig)
 
# calculos para graficar
Fmin=-Fsamp/2.
Fresol=Fsamp/N
Fmax=-Fmin-Fresol
f=np.linspace(Fmin,Fmax,N)
plt.plot(f,out_sig[0][0]) # para imprimir la salida 0, paquete 0
plt.show()

