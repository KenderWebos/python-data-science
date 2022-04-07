#Procesado de texto con python
#Licencia MIT
#Copyright (c) 2020, Kevin C. Pablo B.

# -*- coding: utf-8 -*-
import sys
import os

mainTextList = list()
def main():
    
    #Creamos y almacenamos los textos en una lista

    #pdf = "El_Arbol_De_La_Colina.txt"
    path = "../archivosDeTesteo/Libros_txt_utf-8/"
    ruta = rutaFile()
    mainTextList.append( open(ruta).read() )

    menu()


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
def contectFila():
    pass
def rutaFile():
    ruta= "../archivosDeTesteo/Libros_txt_utf-8/"
    doc = str(sys.argv[1])
    return ruta+doc
  
def get_cantidadDeLineas(mainText):
    n_lines =0
    allLines = mainText.split("\n")
    for line in allLines:
        if line != "":
            n_lines= n_lines+1
    return n_lines

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
    wordToChange = " " + wordToChange + " "
    newWorld = " " + newWorld + " "
    a = mainText.replace(wordToChange, newWorld)
    return a

def limpiarTexto(text):
    #quite el /n de characters
    characters = ",;:.!\"'"
    for character in characters:
        text = text.replace(character, "")
        #text = text.upper()
    return text

def alert(text):
    aux = "─"
    fix = aux*(int(len(text)/2))
    print(f"┌{fix} •✧✧• {fix}┐")
    #print(f"-{fix}ALERTA{fix}- ")
    print(f"    { text }")
    print(f"└{fix} •✧✧• {fix}┘")
    print("")

def menu():
    
    mainTextList[0] = limpiarTexto(mainTextList[0])

    while(True):
        os.system("cls")
        print("")
        print("｡☆✼★━━━━━━  MENU DE OPCIONES  ━━━━━━★✼☆｡")
        print("")
        print("Que deseas hacer? \n 1.- Ver cantidad de lineas \n 2.- Ver cantidad de palabras \n 3.- Ver cantidad de palabras no repetidas \n 4.- Ver cantidad de caracteres con espacio \n 5.- Ver cantidad de caracteres sin espacio \n 6.- Ver cantidad de veces que se repite una palabra \n 7.- Cambiar una palabra en un texto \n 8.- Salir \n")
        print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
        print("")

        response = input("Ingrese una opcion: ")

        os.system("cls")
        if(response == "1"):
            alert("la cantidad de lineas del texto es:")
            print(get_cantidadDeLineas(mainTextList[0]), "\n")

        if(response == "2"): 
            alert("la cantidad de palabras repetidas es:")
            print( get_cantidadDePalabras(mainTextList[0]), "\n" )

        if(response == "3"):
            alert("la cantidad de palabras no repetidas es:")
            print( get_cantidadDePalabrasNoRepetidas(mainTextList[0]) )

        if(response == "4"):
            alert("la cantidad de caracteres con espacio es:")
            print( get_cantidadDeCaracteresConEspacio(mainTextList[0]) )
        
        if(response == "5"):
            alert("la cantidad de caracteres sin espacio es:")
            print( get_cantidadDeCaracteresSinEspacio(mainTextList[0]) )

        if(response == "6"):
            wordToFind = input("Ingrese la palabra a buscar: ")
            alert("la cantidad de veces que se repite una palabra es:")
            print( get_cantidadDeVecesQueSeRepitioUnaPalabra(wordToFind, mainTextList[0]) ) 

        if(response == "7"):
            wordToChange = input("Ingrese la palabra a cambiar: ")
            newWorld = input("Ingrese la nueva palabra: ")
            alert("el texto con la palabra cambiada es:")
            print( changeWordInText(wordToChange, newWorld, mainTextList[0]) )

        if(response == "8"):
            os.system("cls")
            alert("Saliendo...")
            os.system("pause")
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

