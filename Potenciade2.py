#Determinar cuál e sla pontencia de 2 más alta dentro de un número y que me devuelva el exponente 
def exponente (n): 
    i = 1
    x = 2**i
    while x <= n:
        #print(x)
        i += 1
        x = 2**i
    return i-1

#Por ejemplo la potencia de dos más alta dentro de 65 es 64 que corresponde a 2**6
print(exponente(65))
