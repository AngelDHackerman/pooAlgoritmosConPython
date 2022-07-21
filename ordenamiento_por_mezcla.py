
# * Este es el favorito del profesor, pero tambien es uno de los mas complejos

import random

def ordenamiento_por_mezcla(lista):
  pass


if __name__ == "__main__":
  tamano_de_lista = int(input('De que tamano sera la lista?: '))

  lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
  print(lista)
  print('-' * 2)

  lista_ordenada = ordenamiento_por_mezcla(lista)
  print(lista_ordenada)