def exponenciacion(numero):
  resultado = numero
  if numero%2==0:
    resultado = numero**3
    #print("Número al cubo : ", resultado)
  else:
    resultado =numero**2
    #print("Número al cuadrado : ", resultado)
  return resultado

print(exponenciacion(4))
