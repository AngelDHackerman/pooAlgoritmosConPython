

def morral(tamano_morral, pesos, valores, n):
  
  if n == 0 or tamano_morral == 0:  # si ya no tengo mas elementos o ya no tengo espacio, regresara 0
    return 0

  if pesos[n - 1] > tamano_morral:  # Si el peso es mayor al disponible en el morral, dejamos ese elemnto y nos pasamos al siguiente.
    return morral(tamano_morral, pesos, valores, n - 1)

  return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
            morral(tamano_morral, pesos, valores, n - 1))


if __name__ == "__main__":
  valores = [60, 100, 120]
  pesos = [10, 20, 30]
  tamano_morral = 50
  n = len(valores)

  resultado = morral(tamano_morral, pesos, valores, n)
  print(resultado)