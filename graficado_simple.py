from bokeh import figure, output_file, show   # estos import son para visualizar los datos en un HTML

if __name__ == "__main__":
  output_file('graficado_simple.html')
  fig = figure()

  total_vals = int(input('Cuantos valores queres graficar?'))
  x_vals = list(range(total_vals))  # con la funcion list() podemos convertir un valor a una lista rapidamente.