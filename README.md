# pooAlgoritmosConPython

## Creando un ambiente virtual en python en Linux

__Creacion de ambiente virtual:__

`python3 -m venv nombre_venv`

__Activar el ambiente virtual:__

`source nombre_venv/bin/activate`

__Desactivar el entorno virtual:__

Estando en la carpeta del entorno virtual: 
`deactivate` 

__Ignorar la el ambiente virtual en .gitignore__

En el git ignore se debe agregar:

`venv/` que seria en __mejor nombre a ponerle al entorno virtual__
o `nombre_del_entorno_virtual/`

## Usando pip en el entorno virtual 

__pip__ es el __npm__ de javascript

`pip freeze` nos muestra los modulos instalados

#### Mostrando las dependencias instaladas

`pip freeze > requirements.txt` Copia las dependecias instaladas en un archivo .txt para que los demas devs puedan instalarlas.

`pip install -r requirements.txt` Instala todas las dependencias que sean necesarias para el proyecto.