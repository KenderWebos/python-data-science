# -*- coding: utf-8 -*-
import imp
import os
import sys

def main():
    #menu()
    
    textoPrincipal = "hola hola mi nombre es kevin"

    #Creamos y almacenamos los textos en una lista
    pdf = "El_Arbol_De_La_Colina.txt"
    mainTextList = list()
    path = "../archivosDeTesteo/Libros_txt_utf-8/"
    mainTextList.append( open(rutaFile()).read() )
    print(mainTextList)

    # makeSpace()
    # print(get_cantidadDeLineas(textoPrincipal))
    # print(get_cantidadDePalabras(textoPrincipal))
    # print(get_cantidadDePalabrasNoRepetidas(textoPrincipal))
    # print(get_cantidadDeCaracteresConEspacio(textoPrincipal))
    # print(get_cantidadDeCaracteresSinEspacio(textoPrincipal))
    # makeSpace()
    # print(get_cantidadDeVecesQueSeRepitioUnaPalabra("Hola", textoPrincipal))
    # print(changeWordInText("kevin", "pablo", textoPrincipal))


# ｡☆✼★━━━━━━  TO DO  ━━━━━━★✼☆｡
"""
número de líneas, OK
número de palabras en total, OK
número de palabras no repetidas, OK
numero de caracteres con espacio, OK
número de caracteres sin espacio. OK

número de veces que se repite una palabra, OK

cambiar una palabra en el texto, OK
"""

# ｡☆✼★━━━━━━  FUNCIONES  ━━━━━━★✼☆｡
def makeSpace():
    print("--------------------------------------------------------------------------------")

def rutaFile():
    ruta= "../archivosDeTesteo/Libros_txt_utf-8/"

    doc = str(sys.argv[1])
    return ruta+doc
    
  
def get_cantidadDeLineas(mainText):
    allLines = mainText.split("\n")
    return len(allLines)

def get_cantidadDePalabras(mainText):
    allWords = mainText.split(" ")
    return len(allWords)

def get_cantidadDePalabrasNoRepetidas(mainText):
    allWords = mainText.split(" ")
    conjuntoDePalabras = set(allWords)
    return len(conjuntoDePalabras)

def get_cantidadDeCaracteresConEspacio(mainText):
    return len(mainText)

def get_cantidadDeCaracteresSinEspacio(mainText):
    textoSinEspacio = mainText.replace(" ", "")
    return len(textoSinEspacio)

def get_cantidadDeVecesQueSeRepitioUnaPalabra(wordToFind, mainText):
    
    conjunto = mainText.split(" ")
    diccionarioDePalabras = dict()

    for palabra in conjunto:
        if palabra in diccionarioDePalabras:
            diccionarioDePalabras[palabra] += 1
        else:
            diccionarioDePalabras[palabra] = 1

    return (diccionarioDePalabras[wordToFind])
    
    #hacer el substring por cada palabra
    #queriamos hacer que contara las palabras antes de quitar una en especifico y ver cuando da la resta

def changeWordInText(wordToChange, newWorld, mainText):
    a = mainText.replace(wordToChange, newWorld) #a =
    return a

def limpiarTexto(text):
    characters = ",;:.\n!\"'"
    for character in characters:
        text = text.replace(character, "")
        text.upper()
    return text

# def alert(text):
#     aux = "─"
#     fix = aux*(int(len(text)/2))
#     print(f"┌{fix*2} •✧✧• {fix*2}┐")
#     #print(f"-{fix}ALERTA{fix}- ")
#     print(f"    {fix + text + fix}")
#     print(f"└{fix*2} •✧✧• {fix*2}┘")
#     print("")

def alert(text):
    aux = "─"
    fix = aux*(int(len(text)/2))
    print(f"┌{fix} •✧✧• {fix}┐")
    #print(f"-{fix}ALERTA{fix}- ")
    print(f"    { text }")
    print(f"└{fix} •✧✧• {fix}┘")
    print("")

def menu():
    
    while(True):
        os.system("cls")
        print("")
        print("｡☆✼★━━━━━━  MENU DE OPCIONES  ━━━━━━★✼☆｡")
        print("")
        print("Que deseas hacer? \n 1.- Ver cantidad de lineas \n 2.- Ver cantidad de palabras \n 3.- Ver cantidad de palabras no repetidas \n 4.- Ver cantidad de caracteres con espacio \n 5.- Ver cantidad de caracteres sin espacio \n 6.- Ver cantidad de veces que se repite una palabra \n 7.- Cambiar una palabra en un texto \n 8.- Salir \n")
        print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
        print("")

        alert("esta funcion puede mostrar textos de alerta para el usuario")
        alert("me encanta esta funcion porque puedo mostrar contenido que se ve graficamente")
        alert("pero tiene un pequeño bug")

        response = input("Ingrese una opcion: ")

        os.system("cls")
        if(response == "1"):
            print("seleccionaste la opcion 1")
            alert("esto ocurre cuando se realiza la funcion get_cantidadDeLineas")

        if(response == "2"):
            print("seleccionaste la opcion 2")
            alert("esto ocurre cuando se realiza la funcion get_cantidadDeLineas")    

        if(response == "8"):
            os.system("cls")
            return

        response = input("quieres realizar otra accion? (si/no): ")
        if(response == "si"):
            os.system("cls")
        else:
            os.system("cls")
            alert("Ejecucion terminada. Hasta luego")
            return

if __name__=="__main__":
    main()

