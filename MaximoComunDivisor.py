#MCD 
#Máximo Común Divisor
#Número máximo por los que son divisibles 2 números.

#Algoritmo de Euclides
#Si tengo 2 número enteros positivos donde a>b>=0
#Entonces  a =b*q+r  donde q es la cantidad de veces y r es el resto
#mcd(a,b) = mcd(b,r)
def mcd(n1,n2):
    #Creamos la Variable donde guarde el resto (r)
    while True:
        r = n1%n2
        if r == 0:
            return n2
        else:
            #Invertimos los parametros y ver si el resto es 0 ahora.
            n1=n2
            n2=r
#Probamos donde el mcd debería ser  5
print(mcd(10,15))

#Ahora que se entiende el proceso trataré de optimizar parte del código.
def mcd_euclides (n1,n2):
    while n1%n2 != 0 : # indicamos al inicio la condición.
        resto=n1%n2
        n1=n2
        n2=resto
    return n2
    #Nos devolverá n2 cuando la condición no se cumpla y podemos salir del while.
#probamos nuevamente 
print(mcd_euclides(10,15))


