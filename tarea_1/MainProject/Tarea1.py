import os

def main():
    print("Iniciando...")
    get_info()

def get_info():
    #mainText = open('C:\Users\pc0128\Downloads\El_Arbol_De_La_Colina.txt')
    #type El_Arbol_De_La_Colina.txt | find /v /c ""

    mainText = input("agrega tu texto: \n")
    allWords = mainText.split(" ")
    print(f"la cantidad de palabras es {len(allWords)}")
    conjuntoDePalabras = set(allWords)
    print(f"la cantidad de palabras no repetidas es {len(conjuntoDePalabras)}")

    print(f"la cantidad de palabras es {len(mainText)}")

    textoSinEspacio = mainText.replace(" ", "")
    print(f"la cantidad de palabras es {len(textoSinEspacio)}")

def countWord(wordToFind, mainText):
    count = 0

    mainText = input("agrega tu texto: \n")
    allWords = mainText.split(" ")
    print(f"la cantidad de palabras es {len(allWords)}")
    conjuntoDePalabras = set(allWords)
    print(f"la cantidad de palabras no repetidas es {len(conjuntoDePalabras)}")

    textoConLaPalabra = len(mainText)
    textoSinLaPalabra = len( mainText.replace(wordToFind,"") )

    #hacer el substring por cada palabra

    count = textoConLaPalabra - textoSinLaPalabra
    return 0

def changeWordInText(wordToChange, newWorld, mainText):
    mainText.replace(wordToChange, newWorld) #a =
    return mainText


def menu():
    pass

if __name__=="__main__":
    main()

"""
número de líneas,
número de palabras en total, 
número de palabras no repetidas, 
numero de caracteres conespacio, 
número de caracteres sin espacio.
"""