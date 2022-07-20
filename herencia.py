

from cmath import rect


class Rectangulo:

  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def area(self):
    return self.base * self.altura

class Cuadrado (Rectangulo):   # todo: La clase dentro de los parentesis es de donde tomaremos la extencion para esta clase.
  
  def __init__(self, lado):
    super().__init__(lado, lado) # * lado se repite 2 veces porque lado es base y tambien altura.

if __name__ == "__main__":
  rectangulo = Rectangulo(base= 3, altura= 4)
  print(rectangulo.area())    # ? El metodo area vino heredado de la super clase

  cuadrado = Cuadrado(lado= 5)
  print(cuadrado.area())
