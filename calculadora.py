import numpy as np
import math as m
from sympy import integrate, Symbol, limit, oo, sqrt, Rational, log, exp, cos, sin, tan, \
    pi, asin, together, root, S

class Basica:
	
	def __init__(self, x, y, a, b):
		self.x = x
		self.y = y
		self.a = a
		self.b = b
		self.sumar = 0
		self.restar = 0
		self.dividir = 0
		self.multiplicar= 0	

	def suma(self,x,y):
		self.sumar = x + y
		print(self.sumar)
	
	def resta(self,x,y):
		self.restar = x - y
		print(self.restar)

	def division(self,x,y):
		self.dividir = x/y
		print(self.dividir)

	def producto(self,x,y):
		self.multiplicar = x*y
		print(self.multiplicar)

class Cientifica(Basica):
		
	def media(self,x):
		self.E = sum(x)/len(x)
		print(self.E)

	def media_c(self,x):
		self.Ec = sum(x**2)/len(x)
		print(self.Ec)

	def varianza(self,x):
		E = sum(x)/len(x)
		self.V = sum((x - E)**2)/len(x)
		print(self.V)

	def des_estandar(self,x):
		E = sum(x)/len(x)
		V = sum((x - E)**2)/len(x)
		self.De = m.sqrt(V)
		print(self.De)

	def correlacion(self,x,y):
		self.Co = sum(x*y)/len(x*y)
		print(self.Co)

	def RMS(self,x):
		Ec = sum(x**2)/len(x)
		self.Rms = m.sqrt(Ec)
		print(self.Rms)
	
	def integral(self,x,y,a,b):
		self.inte = integrate(y, (x, a, b)) 
		print(self.inte)

	def limite(self,x,y,a):
		self.lim = limit(y, x, a)
		print(self.lim)

print("Menú:")
print("1: Sumar")
print("2: Restar")
print("3: Multiplicar")
print("4: Dividir")
print("5: Media de una variable aleatoria")
print("6: Media cuadratica de una variable aleatoria")
print("7: Varianza de una variable aleatoria")
print("8: Desviacion estandar de una variable aleatoria")
print("9: Correlacion entre dos variables aleatorias")
print("10: Valor RMS de una variable aleatoria")
print("11: Promedio de tiempo de una señal")
print("12: Promedio de tiempo de un proceso estocrastico")
print("13: Integral de una funcion")
print("14: Limite de una funcion")
print("15: Salir")

n = int(input("Digite que operacion desea realizar: "))
while n<1 or n>15:
	n = int(input("El numero que digito no es valido vuelva a introducirlo: "))

while n>0 or n<16:
	if n<11:
		a = 0
		b = 0
		lx0 = []
		ly0 = []
		k = int(input("Ingrese el tamaño de las variables: "))

		for i in range(k):
			x0 = float(input("Introduzca los valores de la primer variable : " ))
			lx0.append(x0) 

		for i in range(k):
			y0 = float(input("Introduzca los valores de la segunda variable: "))
			ly0.append(y0)
	
		x = np.asarray(lx0)
		y = np.asarray(ly0)
		
		calculadora=Cientifica(x,y,a,b)

		if n==1:
			calculadora.suma(x,y)
			n = int(input("Digite otra opcion que quiera realizar: "))

		if n==2:
			calculadora.resta(x,y)
			n = int(input("Digite otra opcion que quiera realizar: "))

		if n==3:
			calculadora.producto(x,y)
			n = int(input("Digite otra opcion que quiera realizar: "))

		if n==4:
			calculadora.division(x,y)
			n = int(input("Digite otra opcion que quiera realizar: "))

		if n==5:
			calculadora.media(x)
			n = int(input("Digite otra opcion que quiera realizar: "))

		if n==6:
			calculadora.media_c(x)
			n = int(input("Digite otra opcion que quiera realizar: "))

		if n==7:
			calculadora.varianza(x)
			n = int(input("Digite otra opcion que quiera realizar: "))

		if n==8:
			calculadora.des_estandar(x)
			n = int(input("Digite otra opcion que quiera realizar: "))

		if n==9:
			calculadora.correlacion(x,y)
			n = int(input("Digite otra opcion que quiera realizar: "))

		if n==10:
			calculadora.RMS(x)
			n = int(input("Digite otra opcion que quiera realizar: "))

	if n==11:
		x = Symbol("x")
		b = float(input("Ingrese el periodo de la señal: "))
		a = -b
		ly0 = []
		k = int(input("Ingrese el numero de muestras de la señal: "))
		for i in range(k):
			y0 = float(input("Introduzca los valores de la señal: "))
			ly0.append(y0)	

		y = np.asarray(ly0)
		calculadora=Cientifica(x,y,a,b)
		t = sum(y)/2*b
		calculadora.limite(x,t,oo)
		n = int(input("Digite otra opcion que quiera realizar: "))
	
	if n==12:
		m = int(input("Ingrese el numero de muestras del proceso: "))
		lt = []
		for i in range(m):
			x = Symbol("x")
			b = float(input("Ingrese el periodo de la señal: "))
			a = -b
			ly0 = []
			k = int(input("Ingrese el numero de muestras de la señal: "))
			for i in range(k):
				y0 = float(input("Introduzca los valores de la señal: "))
				ly0.append(y0)	

			y = np.asarray(ly0)
			calculadora=Cientifica(x,y,a,b)
			t = sum(y)/2*b
			calculadora.limite(x,t,oo)
			lt.append(t)
		print(lt)
		n = int(input("Digite otra opcion que quiera realizar: "))		
	

	if n==13:
		x = Symbol("x")
		y = input("Ingrese la funcion que depende de x: ")
		a = float(input("Ingrese el limite inferior: "))
		b = float(input("Ingrese el limite superior: "))
		calculadora=Cientifica(x,y,a,b)
		calculadora.integral(x,y,a,b)
		n = int(input("Digite otra opcion que quiera realizar: "))

	if n==14:
		x = Symbol("x")
		y = input("Ingrese la funcion que depende de x: ")
		a = input("Ingrese el numero al que tiende x: ")
		b = 0
		calculadora=Cientifica(x,y,a,b)
		calculadora.limite(x,y,a)
		n = int(input("Digite otra opcion que quiera realizar: "))

	if n==15:
		break
	
print("Fin del script")
