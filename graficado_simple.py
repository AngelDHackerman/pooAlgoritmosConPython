from bokeh.plotting import figure, output_file, show   # estos import son para visualizar los datos en un HTML

if __name__ == "__main__":
  output_file('graficado_simple.html')
  fig = figure()

  total_vals = int(input('Cuantos valores queres graficar? '))
  x_vals = list(range(total_vals))  # con la funcion list() podemos convertir un valor a una lista rapidamente.
  y_vals = []

  for x in x_vals:
    val = int(input(f'Valor y para {x} '))
    y_vals.append(val)

  fig.line(x_vals, y_vals, line_width=2)
  show(fig)