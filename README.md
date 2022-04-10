# PythonDataScience_Cource

- Proyecto procesamiento de textos con python nativo
  - Introduccion
  - uso del programa

## Proyecto procesamiento de textos con python nativo
### Introduccion

Procesado de texto con python
Licencia MIT
Copyright (c) 2020, Kevin C. Pablo B.

La aplicacion se trata de un gestor con el cual puedes saber alguna informacion sobre textos que se le entregen por consola, ademas puede realizar modificaciones a este texto tales como reemplazar una palabra especifica o buscar la frecuencia de una palabra en el texto, adicionalmente el programa puede generar un txt el cual contiene las modifiaciones.

### Uso del programa

Al correr el programa por consola recibira como parametro de entrada un archivo (.txt) el cual sera utilizado en la ejecucion

-----

python Tarea1.py El_Arbol_De_La_Colina.txt

-----

una vez iniciado se desplegara un menu con las siguientes opciones.

｡☆✼★━━━━━━  MENU DE OPCIONES  ━━━━━━★✼☆｡

Que deseas hacer?  
 1.- Ver cantidad de lineas  
 2.- Ver cantidad de palabras  
 3.- Ver cantidad de palabras no repetidas  
 4.- Ver cantidad de caracteres con espacio  
 5.- Ver cantidad de caracteres sin espacio  
 6.- Ver cantidad de veces que se repite una palabra  
 7.- Cambiar una palabra en un texto  
 8.- Salir  

｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡

Luego de realizar cualquier opcion sin incluir la de salir, el programa pregunta al usuario si quiere realizar otra accion, finalmente si seleccionas que no quieres realizar otra opcion el programa se intentara finalizar.

```python

def limpiarTexto(text):
    #quite el /n de characters
    characters = ",;:.!\"'"
    for character in characters:
        text = text.replace(character, "")
        #text = text.upper()
    return text

```
-----
