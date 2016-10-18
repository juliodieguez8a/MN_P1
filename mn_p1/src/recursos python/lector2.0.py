# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:48:47 2016

@author: Julio
"""
from pylab import *
from datetime import datetime


#listas de datos
fechas=[]
ingresos=[]

#LEER BASE DE DATOS:

try:    
    txt=open('Base_Datos.txt','r')
except:
    input("presione enter para ver muchos errores")
linea=txt.readline()
while linea!="":
    #==================================
    # Obtenemos informacion de la linea
    #==================================
    fecha,ingreso=linea.split(",")
    
    #FECHA
    fecha=datetime.strptime(fecha,"%Y-%m-%d").date()
    fechas.append(fecha)
    
    #INGRESO
    ingreso=(float)(ingreso)
    ingresos.append(ingreso)
    
    linea=txt.readline()
txt.close()

#OBTENEMOS INFORMACION DE info.txt
inf=open('info.txt','r')
f_min=inf.readline().replace("\n","")
f_min=datetime.strptime(f_min,"%Y-%m-%d").date()

f_max=inf.readline().replace("\n","")
f_max=datetime.strptime(f_max,"%Y-%m-%d").date()
inf.close()

#determinar el indice de la fechas maxima y minima
i_min=fechas.index(f_min)
i_max=fechas.index(f_max)

#la grafica tiene como eje x el rango dado por los indices
x=range (i_min, i_max+1)

#la grafica tiene en y el ingreso
y=[]

#inicializar variables
ingreso=0
ingreso_max=0.0

for i in x:
    ingreso_actual=ingresos[i]
    
    #tomamos el valor maximo para la grafica
    if ingreso_actual != None:
        ingreso_max=max(ingreso_max,ingreso_actual)
    y.append(ingreso_actual)    
    

#CREAR FIGURA
#GRAFICAR
plot(x,y)
#Definir caracteristicas de grafica
axis([i_min,i_max+1,0,ingreso_max])
grid()
title("ingresos  entre\n"+str(f_min)+" y "+str(f_max))
xlabel("x")
ylabel("y")

savefig('foo.png')