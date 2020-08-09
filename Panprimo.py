# La siguiente función es para determinar si un número en pandigital y además los 3 últimos digitos del mismo son primos
# Los números pandigitales son aquellos que contienen todos los dígitos del 0 al 9 

# Número Primo 
#numero = 2424643
#print(numero%1000)

def es_primo(numero):
    a=numero%1000
    primo = True
    if a < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        primo = False
    for i in range(2, a): 
        if a % i == 0:  
            primo = False
    return primo    #de lo contrario devuelve Verdadero

    #Valido Primo con los 3 último números
#print(es_primo(2424643))

def pandig (numero):
    ceronueve =["0","1","2","3","4","5","6","7","8","9"]
    pan=str(numero)
    pandigital = True
    for i in ceronueve:
        if  i not in pan:
            pandigital = False
    return pandigital

    #Válido Pandigital 
#print(pandig(12345678190))
#print(pandig(2424643))

def pandigital_primo (numero):
    if es_primo(numero)== True and pandig(numero)==True:
        return True
    else:
        return False

print(pandigital_primo(1234567890769))