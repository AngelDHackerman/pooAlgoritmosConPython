import time     # ? Este es usado para poder medir el tiempo de nuestro algoritmo.  
import sys      # ! esto es para ver el maximo de recursion permitida en el sistema
sys.setrecursionlimit(100_000_000)    # * Asi cambiamos el limite de recursion permitido. 

def factorial(n):
  respuesta = 1

  while n > 1:
    respuesta *= n
    n -= 1

  return respuesta

def factoria_recursivo(n):
  if n == 1:
    return 1

  return n * factoria_recursivo(n - 1)


if __name__ == "__main__":
  n = 10_000

  comienzo = time.time()    # * Calculando el tiempo de la funcion factorial
  factorial(n)
  final = time.time()
  print(final - comienzo)

  comienzo = time.time()    # * Calculando el tiempo de la funcion factorial_recursivo
  factoria_recursivo(n)
  final = time.time()
  print(final - comienzo)
  print(sys.getrecursionlimit()) # 1000   # ? obtenemos el maximo de recursion permitida