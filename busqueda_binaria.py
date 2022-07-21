import random
# todo: Las busquedas binarias se deben hacer con listas ORDENADAS

def busqueda_binaria(lista, comienzo, final, objetivo):

  if comienzo > final:    # ? Esto significa que el objetivo no existe en nuestra lista ordenada
    return False

  medio = (comienzo + final) // 2     # ? // significa division de enteros, NO va a devolver ningun decimal

  if lista[medio] == objetivo:    # objetivo encontrado
    return True
  elif lista[medio] < objetivo:
    return busqueda_binaria(lista, medio + 1, final, objetivo)  # Reejecutamos la funcion pero con el "comienzo" siendo la mitad + 1
  else:
    return busqueda_binaria(lista, comienzo, medio - 1, objetivo)  # # Reejecutamos la funcion pero con el "final" siendo la mitad - 1


if __name__ == "__main__":
  tamano_de_lista = int(input('De que tamano sera la lista ? '))
  objetivo = int(input('Que numero quieres encontrar? '))

  lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)]) 

  encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

  print(lista)
  print(f'El elemento {objetivo} {"esta" if encontrado else "no esta" } en la lista')   # todo: hace se hace el operador ternario: "esta" if encontrado else "no esta" 