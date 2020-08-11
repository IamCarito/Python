#Cálculo de Fechas

import datetime
from datetime import date

hoy = datetime.date.today()
print(hoy) #Reviso que el formato de fecha por defecto de Pyhton es YYYY-MM-DD
print(hoy.strftime('%d/%m/%y')) #Doy Formato que yo quiero ej 30-07-20

#Variables
ani_nac =int(input(print("Su año de nacimiento es : ")))
mes_nac =int(input(print("Su mes de nacimiento es : ")))
dia_nac =int(input(print("Su dia de nacimiento es : ")))
d = date.today()

#Calcular Edad Por Año
edadxanio =  (d.year)- (ani_nac)
print("\n OPCIÓN 1 : Cálculo solo con años")
print("Lo cálculo a la rápida usted tiene ", str(edadxanio),"años" ) # Valor no exacto no considera los meses o los días.

#Calcular Edad por Mes
#Si la fecha de nacimiento es menor a la fecha actual significa que aún no cumple años entonces : 
edadxmes =  edadxanio -1
#Forma Larga Con Condicionales
print ("\n OPCION 2 : Cálculo Largo con condicionales")
if mes_nac > d.month :
    print(" Usted aún no cumple años, así que tiene ", str(edadxmes), " años")
elif dia_nac > d.day :
    print(" Usted aún no cumple años, así que tiene ", str(edadxmes), " años")
else :
    # mes_nac <= d.month
    print(" Usted está o estuvo de cumpleaños, así que tiene ", str(edadxanio), " años") 

#Calcular Fecha Función
print("\n OPCION 3 : Cálculo con función y año gregoriano")
#Le indicamos que la variable contenga la fecha de nadimiento ingresada anteriormente.
fecha_nac = date(ani_nac,mes_nac,dia_nac)
def calcular_edad (fecha_nac):
    #Ya sabemos que el cálculo de la edad por año
    dif_fechas = d - fecha_nac
    dif_dias = dif_fechas.days
    edad_1 = dif_dias /365.25  #365.25 son los días de un año gregoriano si no sabé que es googlealo
    edad =int(edad_1)
    return edad

print("Su edad es : ", str(calcular_edad(fecha_nac)))

print("Eso sería chau nos vimoh, ESTUVO IZI PISI")