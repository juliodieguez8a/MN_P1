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
    
    print (fecha,ingreso)
    linea=txt.readline()
txt.close()

#OBTENEMOS INFORMACION DE info.txt
inf=open('info.txt','r')
f_min=inf.readline().replace("\n","")
print(f_min)
f_min=datetime.strptime(f_min,"%Y-%m-%d").date()
f_max=inf.readline().replace("\n","")
print(f_max)
f_max=datetime.strptime(f_max,"%Y-%m-%d").date()
inf.close()

print ("Se mostraran los ingresos en el intervalo de tiempo seleccionado\n"+
    "la fecha debe encontrarse entre 01/01/2012 y 31/07/2015")
#Ingreso de fechas limite
#==============================================================================
# f_min=input("Ingrese fecha de inicio dd/mm/aaaa: ")
# f_min=datetime.strptime(f_min,"%d/%m/%Y").date()
# f_max=input("Ingrese fecha de final  dd/mm/aaaa: ")
# f_max=datetime.strptime(f_max,"%d/%m/%Y").date()
#==============================================================================

#determinar el indice de la fechas maxima y minima
i_min=fechas.index(f_min)
i_max=fechas.index(f_max)

#la grafica tiene como eje x el rango dado por los indices
x=range (i_min, i_max+1)

#la grafica tiene en y el ingreso
y=[]
y2=[]

#inicializar variables
ingreso=0
ingreso_max=0.0

for i in x:
    ingreso_actual=ingresos[i]
    
    #tomamos el valor maximo para la grafica
    if ingreso_actual != None:
        ingreso_max=max(ingreso_max,ingreso_actual)
    y2.append(ingreso_actual)    
    
#==============================================================================
#     #COLAPSA CUANDO SON MUCHOS DATOS
#     #ingreso es lo que lleva mas el nuevo ingreso
#     ingreso+=ingreso_actual
#     y.append(ingreso)
#==============================================================================
    


#==============================================================================
# #GRAFICAR
# plot(x,y)
# #Definir caracteristicas de grafica
# axis([i_min,i_max+1,0,ingreso])
# grid()
# title("ingresos acumulados entre\n"+str(f_min)+" y "+str(f_max))
# xlabel("x")
# ylabel("y")
# 
# show()
#==============================================================================

#CREAR FIGURA
#GRAFICAR
plot(x,y2)
#Definir caracteristicas de grafica
axis([i_min,i_max+1,0,ingreso_max])
grid()
title("ingresos  entre\n"+str(f_min)+" y "+str(f_max))
xlabel("x")
ylabel("y")

savefig('foo.png')