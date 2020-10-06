
#1
#Obtener el promedio y la desviación standard de una lista
import statistics
# Importamos la librerías para ocupar la operacion de desviación estandard poblacional.
# Ya que ocupadatodos los dato de la lista como todos los datos existentes.
def promedio_std(lista):# debes modificar todos los elementos de la función
  x = sum(lista)/len(lista)
  y = statistics.pstdev(lista)
  return (x,y)
# cuidando el retorno, nombre y argumentos
lista= [84, 18, 74, 38, 9, 72, 36, 98, 47, 90, 30, 95, 91, 16, 97, 11, 29, 55, 57]
print("El promedio y desviación standard de la lista son respectivamente: ",promedio_std(lista))

#Colores Preferidos 

def color_frecuente(lista):
    contador = {}
    for color in lista:
        if color in contador:
            contador[color] += 1 # incrementamos si existe el color
        else:
            contador[color] = 1 # creamos un nuevo item con el key del color y el valor inicial de 1
    m = max(contador.values()) # obtenemos el max de repeticiones
    key_color = [key for       key, value in contador.items() if value == m] # seleccionamos los colores que cumplen con el maximo
    if len(key_color) > 1: # verificamos si existe mas de un maximo
        key_color = min(key_color, key= lambda x: prioridad.index(x)) # obtenemos el elemento segun la prioridad
    else:
         key_color = key_color[0]
    return key_color, m

prioridad = ["azul","rojo","verde","amarillo"]
lista = ['rojo', 'rojo', 'azul', 'azul']
print(color_frecuente(lista))