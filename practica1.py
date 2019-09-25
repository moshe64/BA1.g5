import math as m
import numpy as np

xa = 0.4
ya = 1.3
za = xa + ya
ha = m.cos(xa)

xb = np.array((25, 50, 20, 15, -10))
yb = np.array((2, 30, 42, 11, 22))
zb = xb + yb
hb = np.cos(xb)

t = np.linspace(0,1,10)
g = np.exp(2.*m.pi*1.j*t)

print'Suma con numeros escalares: ', za
print'Coseno con numero escalar: ', ha

print'Suma con numeros vectores: ', zb
print'Coseno con numero vector: ', hb

print'Exponencial: ', g

