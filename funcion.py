import numpy as np
import math as m

def suma(x,y):
	s = x + y
	return(s)

def resta(x,y):
	r =  x - y
	return(r)

lx0 = []

ly0 = []

n = int(input("Ingrese el tamaño de los vectores: "))

for i in range(n):
	x0 = float(input("Introduzca los valores del primer vector : " ))
	
	lx0.append(x0) 
	
for i in range(n):
	y0 = float(input("Introduzca los valores del segundo vector: "))

	ly0.append(y0)

x = np.asarray(lx0)

y = np.asarray(ly0)

print("La suma de los vectores es: ", suma(x,y))

print("La resta de los vectores es: ", resta(x,y))
	
