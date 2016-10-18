# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:48:47 2016

@author: Julio, Boggdan
"""
from pylab import *
import numpy as np
from datetime import datetime

#Uso de numpy para el promedio de los datos
#Usa de numpy para el calculo de la desviacion estandar       

#Dia se define como 1 lunes y 7 domingo
def pronosticoDias(dia):
    diasIngreso=[] 
    for i in range(i_min,i_max+1,1):
        codigoDia = datetime.isoweekday(fechas[i])
        if codigoDia == dia:
            diasIngreso.append(ingresos[i])
    promedio = np.mean(diasIngreso)
    return diasIngreso, promedio
    
def pronosticoAbril(Fmin,Fmax):
    diasPronostico = []
    intSup = []
    intInf = []
    for i in range(Fmin,Fmax,1):
        diasPronostico.append(ingresos[i])
    promedio = np.mean(diasPronostico)
    desviacion = np.std(diasPronostico)
    for i in range(len(diasPronostico)-31,len(diasPronostico),1):
        intSup.append(diasPronostico[i]+desviacion)
        intInf.append(diasPronostico[i]-desviacion)
    return intSup, intInf, promedio, desviacion
        

def intervalo(promedio, desviacion):
    intSup = promedio+desviacion
    intInf = promedio-desviacion
    return intSup,intInf
    
def convertirDate(ano,mes,dia): 
    date = (ano+"-"+mes+"-"+dia)
    lookDate = datetime.strptime(date,"%Y-%m-%d").date()
    return lookDate
    
    
def buscadorIndiceMin(anno,mes):
    date = (anno+"-"+mes+"-"+"01")
    lookDate = datetime.strptime(date,"%Y-%m-%d").date()
    lookI = fechas.index(lookDate)
    return lookI
    
def buscadorIndiceMax(indice,mes,cMes = 0):
    mes = mes + cMes
    for i in range(indice+1,len(fechas),1):
        if fechas[i].month == mes:
            if fechas[i].day == 1:
                return i-1

#fmin1 fmax1 El periodo mas alejado a la prediccion
#fmin2 fmax2 El periodo mas cercano a la prediccion aunque sea un ano de diferencia
def pronosticadorPresentePasado(fmin1,fmax1,fmin2,fmax2):
    diasPronostico = []
    intSup = []
    intInf = []
    for i in range(fmin1,fmax1,1):
        diasPronostico.append(ingresos[i])
    for i in range(fmin2,fmax2,1):
        diasPronostico.append(ingresos[i]+ajuste)
    promedio = np.mean(diasPronostico)
    desviacion = np.std(diasPronostico)
    Vmin = buscadorIndiceMin("2014","05")
    Vmin = fmax2-Vmin
    print( range(len(diasPronostico)-Vmin,len(diasPronostico),1))
    for i in range(len(diasPronostico)-Vmin-1,len(diasPronostico),1):
        if diasPronostico[i] < desviacion:
            intSup.append(diasPronostico[i]+desviacion)
            intInf.append(diasPronostico[i])
        else:
            intSup.append(diasPronostico[i]+desviacion)
            intInf.append(diasPronostico[i]-desviacion)
    print(diasPronostico[60:90])
    return intSup, intInf, promedio, desviacion
    
def promedio(min,max):
    pingresos = []
    for i in range(min,max+1,1):
        pingresos.append(ingresos[i])
    promedio = np.mean(pingresos) 
    return promedio

#Año 2014
i2014 = fechas.index(convertirDate("2014","01","01"))
f2014 = fechas.index(convertirDate("2014","12","31"))
promedio2014 = promedio(i2014,f2014)

#Año 2015
i2015 = fechas.index(convertirDate("2015","01","01"))
f2015 = fechas.index(convertirDate("2015","03","31"))
promedio2015 = promedio(i2015,f2015)


ajuste = promedio2015-promedio2014



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
    
#    print (fecha,ingreso)
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
pronostico = inf.readline().replace("\n","")
pronostico = (int)(pronostico)
pronostico = (str)(pronostico)
print(pronostico)
inf.close()

print ("Se mostraran los ingresos en el intervalo de tiempo seleccionado\n"+
    "la fecha debe encontrarse entre 01/01/2013 y 31/03/2015")


#determinar el indice de la fechas maxima y minima
i_min=fechas.index(f_min)
i_max=fechas.index(f_max)

#la grafica tiene como eje x el rango dado por los indices
x=range (i_min, i_max+1)

#la grafica tiene en y el ingreso
y=[]

#Inicializar variables
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
#plot(x,y)
#Definir caracteristicas de grafica
#axis([i_min,i_max+1,0,ingreso_max])
#grid()
#title("Ingresos  entre\n"+str(f_min)+" y "+str(f_max))
#xlabel("x")
#ylabel("y")




print(fechas[850].month)

#dias,promedio = pronosticoDias(2)
#print(dias)
#print(promedio)

if pronostico == "4":
    FMin = 1096
    FMax = 1185
    x = range(FMax-31,FMax,1)
    superior, inferior, prom, desv = pronosticoAbril(FMin,FMax)
    plot(x,superior,x,inferior)
    grid()
    savefig('foo.png')
elif pronostico == "5":
    anio = "2014"
    nmes = int(pronostico) - 1
    mes = "0"+str(nmes)
    print(mes)
    indiceMin = buscadorIndiceMin(anio,mes)
    indiceMax = buscadorIndiceMax(indiceMin,int(pronostico))
    fmin = fechas.index(convertirDate("2015","02","01"))
    fmax = fechas.index(convertirDate("2015","03","31"))
    superior, inferior, prom, desv =  pronosticadorPresentePasado(fmin,fmax,indiceMin,indiceMax)
    x = range(indiceMin,indiceMax+1,1)
    plot(x,superior,x,inferior)
    grid()
    savefig('foo.png')
elif pronostico == "6":
    anio = "2014"
    nmes = int(pronostico) - 2
    mes = "0"+str(nmes)
    indiceMin = buscadorIndiceMin(anio,mes)
    indiceMax = buscadorIndiceMax(indiceMin,int(pronostico))
    fmin = fechas.index(convertirDate("2015","03","01"))
    fmax = fechas.index(convertirDate("2015","03","31"))
    superior, inferior, prom, desv =  pronosticadorPresentePasado(fmin,fmax,indiceMin,indiceMax)
    indiceMin2 = buscadorIndiceMin(anio,"05")
    x = range(indiceMin2,indiceMax+1,1)
    plot(x,superior,x,inferior)
    grid()
    savefig('foo.png')
elif pronostico == "7":
    anio = "2014"
    nmes = int(pronostico) - 2
    mes = "0"+str(nmes)
    indiceMin = buscadorIndiceMin(anio,mes)
    indiceMax = buscadorIndiceMax(indiceMin,int(pronostico))
    print(indiceMin)
    print(indiceMax)
    fmin = fechas.index(convertirDate("2015","03","01"))
    fmax = fechas.index(convertirDate("2015","03","31"))
    superior, inferior, prom, desv =  pronosticadorPresentePasado(fmin,fmax,indiceMin,indiceMax)
    indiceMin2 = buscadorIndiceMin(anio,"05")
    x = range(indiceMin2,indiceMax+1,1)
    plot(x,superior,x,inferior)
    grid()
    print("Prueba",ingresos[indiceMin:indiceMax])
    print(fechas[881],ingresos[881])
    print(fechas[881])
    savefig('foo.png')


        