print("*** PREGUNTA 1 ***")
#Crea una Función que reciba 2 String como parametros.\n Que retorne 1 String de largo
#Que contenga las 2 primeras letras del 1er string y las 2 últimas del segundo string

def mesclador(string_a, string_b):
    if len(string_a)<3 or len(string_b)<3 :
        print("El largo de las palabras a ingresar debe ser mayor a 2 caracteres")
    else:
        uno=(string_a[:2])
        #print(uno)
        dos=(string_b[-2:])
        #print(dos)
        mix= uno + dos
    return mix
#Prueba
#print("\nPrueba función mesclador string_a = hola, string_b = chao ")
print(mesclador("Funciones","Strings"))

print("\n ***PREGUNTA 2***")
#Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que consista del primero,
#pero con el segundo string intercalado entre cada letra del primero.
def intercarlar(string_a,string_b):
    i=0
    largo =len(string_a)
    j= ""
    while i<largo:
        j = j+ string_a[i] + string_b
        i = i +1
    return j
print("\nPrueba función intercalar  string_a = hola, string_b = chao ")
print(intercarlar("hola","chao"))

print("***PREGUNTA 3***")
# Escriba una función que reciba un string consistente de unos y ceros y retorne
# la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.
# Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1 (ya que hay 6 unos y 5 ceros)

def ocurrencias(string):
    numeros = string
    ceros = numeros.count('0')
    unos = numeros.count('1')
    ocu = unos-ceros
    return ocu

print(ocurrencias("11001100000011"))

print("***PREGUNTA 4***")
#Escriba una funcion que reciba un string s y un numero n como parámetros y retorne:
#el mismo string s, pero sin el indice n, por ejemplo si s = "Hasta Luego" debe retonar "Hasa Luego"
def remover_enesimo(s,n):
    saco = s[n]
    nuevo = s.replace(saco,"")
    return nuevo

print(remover_enesimo("Hasta Luego",3))

print("***PREGUNTA 5***")
#Escriba una función que  reciba un string  como parámetro y retorne el string,
#Pero cada elemento que estuviese en mayúscula reemplazarlo por "$"
def reemplazo(string):
    texto = string
    mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for letra in mayus:
        texto = texto.replace(letra,"$")
    return texto

print(reemplazo("CaroLiNa"))
