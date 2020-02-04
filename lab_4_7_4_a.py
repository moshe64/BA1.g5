import numpy as np
import math
from matplotlib import pyplot as plt
################################################################################
## Escribimos el codigo a probar, sin usar "self" porque esto no es una clase ##
################################################################################
def work(input_items, output_items):
    in0 = input_items[0]
    out0 = output_items[0]
    out0[:]=abs(np.fft.fftshift(np.fft.fft(in0,N)))
    return len(out0)
###############################################################################
##              PRUEBAS A LA FUNCION WORK                                    ##
###############################################################################
 
# Deinifimos la senal entrante
f=1378.
Fsamp= 8000. # la frecuencia de muestreo
N=128 
n=np.linspace(0,N-1,N)
t=n/Fsamp
in_sig=np.cos(2.*math.pi*f*t)
out_sig=np.array([0.]*N) # se crea  un vector de N ceros

# Pasamos a array 2d las dos senales ya que es mecesario introducir la dimension
# que en GNU radio debe ser destinada para identificar las posibles entradas y salidas
# que puede tener un bloque
in_sig= np.array([in_sig])
out_sig=np.array([out_sig])
# Por fin comprobamos la funcion
d=work(in_sig,out_sig)
# calculos para graficar
Fmin=-Fsamp/2.
Fresol=Fsamp/N
Fmax=-Fmin-Fresol
f=np.linspace(Fmin,Fmax,N)
plt.plot(f,out_sig[0])
plt.show()

