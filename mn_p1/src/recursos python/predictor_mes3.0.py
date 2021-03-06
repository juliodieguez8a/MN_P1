# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:48:47 2016

@author: Julio
"""
from pylab import *
from datetime import datetime, timedelta
import numpy as np


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

f_proy=inf.readline().replace("\n","")
f_proy=datetime.strptime(f_proy,"%Y-%m-%d").date()

inf.close()

#fecha de inicio
dia=1
mes=f_proy.month-6
anio=f_proy.year
if (mes<=0):
    mes=mes+12
    anio=anio-1

f_inicio=f_proy.replace(anio,mes,dia)
#indice de inicio de datos a tomar
i_inicio=fechas.index(f_inicio)


print (f_inicio)
print (f_inicio-timedelta(days=1))

#indice de inicio de datos a tomar
i_inicio=fechas.index(f_inicio)



try:
    i_proy=fechas.index(f_proy)-1
except:
    i_proy=len(fechas)-1


#print (f_proy-deltatime(days=1))

#determinar el indice de la fechas maxima y minima
i_min=fechas.index(f_min)
i_max=fechas.index(f_max)

#la grafica tiene como eje x el rango dado por los indices
#x=range (i_min, i_max+1)

x=range (i_inicio, i_proy+1)

#la grafica tiene en y el ingreso
y=[]
y_date=[]

#inicializar variables
ingreso=0
ingreso_max=0.0
ingreso_semana=[0,0,0,0,0,0,0]
for i in x:
    ingreso_actual=ingresos[i]
    dia=fechas[i].weekday()
    ingreso_semana[dia]+=ingresos[i]
    #tomamos el valor maximo para la grafica
    if ingreso_actual != None:
        ingreso_max=max(ingreso_max,ingreso_actual)
    y.append(ingreso_actual)   
    y_date.append(fechas[i])
    

factor=[]
maximo_semana=max(ingreso_semana)

for i in ingreso_semana:
    factor.append(i/maximo_semana)

y_ajustado=[]
x2=range(0,len(y))

for i in x2:
    dia=y_date[i].weekday()
    y_ajustado.append(y[i]/factor[dia])
    
    
#print (y_ajustado)
    
    

    
parte=(int)(len(y_ajustado)/6)

print (parte)

#mes de resulado
#suma los 6 meses
m=[]
#m[numero de mes][numero de dia]
for i in range(0,cant):
    m.append(y_ajustado[i*parte:(1+i)*parte])

desviacion=np.std(y_ajustado)

resultado=[]
resultado1=[]
resultado2=[]
for i in range(0,parte):
    dia= (f_proy+timedelta(days=i)).weekday()
    dato=(m1[i]+m2[i]+m3[i]+m4[i]+m5[i]+m6[i])*factor[dia]/6
    resultado.append(dato)
    resultado1.append(dato+desviacion)
    resultado2.append(dato-desviacion)

#print(resultado)

#CREAR FIGURA
#GRAFICAR
plot(range(1,len(resultado1)+1),resultado1)
plot(range(1,len(resultado2)+1),resultado2)

try:
    #REAL
    y2=[]
    x=range (i_proy+1, i_proy+31)
    
    #inicializar variables
    ingreso=0
    ingreso_max=0.0
    
    for i in x:
        ingreso_actual=ingresos[i]
        y2.append(ingreso_actual)    
        
    
    plot(range(1,len(resultado2)+1),y2)
except:
    print ("no hay datos reales")

#Definir caracteristicas de grafica

grid()
title("Proyección de ingresos  entre\n"+str(f_proy.month)+"-"+str(f_proy.year))
xlabel("dia")
ylabel("ingresos")



savefig('foo.png')






#next_month = datetime.datetime(mydate.year + (mydate.month / 12), ((mydate.month % 12) + 1), 1)