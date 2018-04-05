# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pylab as py
import scipy.interpolate as sc


Dias=[]
Dinero=[]
Anios = np.array([1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016])
TotalAnios = np.linspace(1999,2016,18)
ResultadoDia = []

x=0
y=0


indice=0

with open("/Users/Danny/Documents/GitHub/Metodos/MetodosNumericos/Diciembre.txt") as f:
    Contenido = f.read().splitlines()

while(indice<len(Contenido)):
    Contenedor = ""
    Contenedor = Contenido[indice]
    nuevoContenedor = Contenedor.split()
    DiasString=nuevoContenedor[0]
    DineroString=nuevoContenedor[1]
    X=float(DiasString)
    Y=float(DineroString)
    indice=indice+1
    Dias.extend([X])
    Dinero.extend([Y])

listaDias=np.array(Dias)
listaDinero=np.array(Dinero)


IndiceActual=0
Contador=0
Resultado = 0

n1 = 0
n2 = 18

#Polinomio=np.polyfit(Anios,listaDinero[n1:n2],3)
#ConversionPolinomio = np.poly1d(Polinomio)
#Resultado = ConversionPolinomio(2017)
#
#ResultadoDia.extend([Resultado])

Polinomio=np.polyfit(Anios,listaDinero[n1+19:n2+19],3)
ConversionPolinomio = np.poly1d(Polinomio)
Resultado = ConversionPolinomio(2017)


ResultadoDia.extend([Resultado])
print(ResultadoDia)
    
    
    
#plt.plot(TotalAnios,Polinomio)
#plt.ylabel("Valores en Y:")
#plt.xlabel("Valores en X:")
#plt.title("Grafica generada, Ejercicio #1:")
#plt.grid()
#plt.show ()

