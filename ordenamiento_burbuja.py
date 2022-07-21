import random

# O(n**2)

def ordenamiento_de_burbuja(lista):
  n = len(lista) 
  for i in range(n): 
    for j in range(0, n - i - 1):

      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j] # ? Aqui se hace el "swaping" de python, lista[j + 1] toma el lugar de lista[j]

  return lista


if __name__ == "__main__":

  tamano_de_lista = int(input('De que tamano sera la lista? '))

  lista = [random.randint(0, 100) for i in range(tamano_de_lista)]    # aqui estamos usando comprehentions
  print(lista)

  lista_ordernada = ordenamiento_de_burbuja(lista)
  print(lista_ordernada)
