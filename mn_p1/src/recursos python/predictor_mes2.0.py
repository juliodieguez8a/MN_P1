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

meses_atras=12

#fecha de inicio
dia=1
mes=f_proy.month-meses_atras
anio=f_proy.year
if (mes<=0):
    mes=mes+12
    anio=anio-1

f_inicio=f_proy.replace(anio,mes,dia)
#indice de inicio de datos a tomar
i_inicio=fechas.index(f_inicio)


#print (f_inicio)
#print (f_inicio-timedelta(days=1))

#indice de inicio de datos a tomar
i_inicio=fechas.index(f_inicio)


#CUANDO LA FECHA ANTERIOR NO ESTA EN LA BASE DE DATOS
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
    


parte=(int)(len(y_ajustado))
for i in range (1,meses_atras+1):
    if parte/i>28 and parte/i<32:
        parte=parte/i
        cant=i

#===========================
meses_adelante=1

#fecha de inicio
dia=1
mes=f_proy.month+meses_adelante
anio=f_proy.year
if (mes>12):
    mes=mes-12
    anio=anio+1

f_ultima=f_proy.replace(anio,mes,dia)
f_ultima=(f_ultima-timedelta(days=1))

print (f_ultima)
print (f_ultima.day)

#cant=f_ultima.day

#print (cant)
#indice de inicio de datos a tomar
#i_inicio=fechas.index(f_inicio)


#print (f_inicio)
#print (f_inicio-timedelta(days=1))

#==========================


#canidad de dias
parte=(int)(parte)
print (parte)

m=[]
#m[numero de mes][numero de dia]
for i in range(0,cant):
    m.append(y_ajustado[i*parte:(1+i)*parte])
        
    
#mes de resulado
#suma los 6 meses

desviacion=np.std(y_ajustado)

resultado=[]
resultado1=[]
resultado2=[]



#PARA DESVIACION ESTANDAR POR CADA UNO DE LOS DIAS DEL MES
desviaciones=[]

#parte cantidad de dias
#cant cantidad de meses
for n_dia in range (0,parte):
    datos_dia=[]
    for n_mes in range(0,cant):
        datos_dia.append(m[n_mes][n_dia])
    desviaciones.append(np.std(datos_dia))
    
#PARTE cantidad de dias en que se divide
for i in range(0,parte):
    #indice de dia de la semana
    dia= (f_proy+timedelta(days=i)).weekday()
    dato=0
    for n in range(0,cant):
        dato+=m[n][i]
        #datos.append(m[n][i])
    #1.03 factor de crecimiento
    dato=(dato)*factor[dia]*(1.03)/cant
    resultado.append(dato)
    #resultado1.append(dato+desviacion)
    #resultado2.append(dato-desviacion)
    
    resultado1.append(dato+desviaciones[i]*factor[dia]*1.03)
    resultado2.append(dato-desviaciones[i]*factor[dia]*1.03)



#print (desviaciones)


#print(resultado)

#CREAR FIGURA
#GRAFICAR


try:
    #REAL
    y2=[]
    x=range (i_proy+1, i_proy+parte+1)
    
    #inicializar variables
    ingreso=0
    ingreso_max=0.0
    
    for i in x:
        ingreso_actual=ingresos[i]
        y2.append(ingreso_actual)    

#==============================================================================
#     e=(minimosCuadrados(y2,resultado))**(1/2)
#     print (e)    
#     
#     print(np.corrcoef(y2,resultado))
#     e1=[]
#     e2=[]
#     print (y2)
#     for i in range(0,parte):
#         e1.append(resultado[i]+e)
#         e2.append(resultado[i]-e)
#     
#     plot(range(1,len(resultado1)+1),e1)
#     plot(range(1,len(resultado2)+1),e2)    
#==============================================================================
    
    #GRAFICA DATOS REALES
    plot(range(1,len(resultado1)+1),resultado1)
    plot(range(1,len(resultado2)+1),resultado2)    
    plot(range(1,len(resultado2)+1),y2)
    correlacion=np.corrcoef(y2,resultado)

    print (correlacion[0][1])
    print(np.corrcoef(y2,resultado))
    
    
    
    
except:
    print ("no hay datos reales")
    plot(range(1,len(resultado1)+1),resultado1)
    plot(range(1,len(resultado2)+1),resultado2)

#Definir caracteristicas de grafica

grid()
title("Proyección de ingresos  de:\n"+str(f_proy.month)+"-"+str(f_proy.year))
xlabel("dia")
ylabel("ingresos")
axis([0, 31, 0, max(resultado1)])

savefig('foo.png')

txt=open('DatosMes.txt','w')
try:
    txt.write('R^2:{:{width}.{prec}f}\n'.format(correlacion[0][1], width=13, prec=4))
except:
    print("no hay datos reales para obtener correlacion")

txt.write('dia -- pronostico -- desv.estandar'+'\n')
for i in range(0,len(resultado)):
    linea='{:2d}'.format(i+1)
    linea+='  {:{width}.{prec}f}'.format(resultado[i], width=13, prec=2)
    linea+='{:{width}.{prec}f}\n'.format(desviaciones[i], width=13, prec=2)
    
    txt.write(linea)
    #txt.write(((str)(i+1))+', '+((str)(resultado[i]))+', '+((str)(desviaciones[i]))+'\n')
txt.close()
