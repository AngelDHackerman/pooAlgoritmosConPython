# Definicion

class Persona:
                                    # todo: self es el this de python
  def __init__(self, nombre, edad): # ? __init__ es el constructor de la clase, self es un parametro inicial obligatorio de las clases y metodos dentro de las clases
    self.nombre = nombre # * Asi se inicializan las variables de instancia
    self.edad = edad

  def saluda(self, otra_persona):
    print(f'Hola {otra_persona}, me llamo {self.nombre}')
    return f'Hola {otra_persona}, me llamo {self.nombre}' # ? f'texto{variables}' es la interpolacion de python

# Uso

david = Persona('David', 35)
erika = Persona('Erika', 32)

david.saluda('Ericka')