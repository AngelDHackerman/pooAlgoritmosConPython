# Polimorfismo es similar a la herencia pero cambiando el comportamiento de las clases. 

class Persona:
  
  def __init__(self, nombre):
    self.nombre = nombre

  def avanza (self):
    print('Ando caminando')


class Ciclista(Persona):

  def __init__(self, nombre):
    super().__init__(nombre)

  def avanza(self):
    print('Ando moviendome en mi bicileta')


def main():
  persona = Persona('Angel')
  persona.avanza()

  ciclista = Ciclista('Daniel')
  ciclista.avanza()


if __name__ == "__main__":
  main()