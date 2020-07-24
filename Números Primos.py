#Números primos

def es_primo(a):
    primo = True
    if a < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        primo = False
    for i in range(2, a):  #un rango desde el dos hasta el numero que nosotros elijamos
         if a % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
          primo = False
    return primo    #de lo contrario devuelve Verdadero

print(es_primo())  #para probarlo llamamos a la función
