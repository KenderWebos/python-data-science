import os

def main():
    menu()
    textoPrincipal = "Hola Hola mi nombre es kevin"
    print(get_cantidadDeLineas(textoPrincipal))
    print(get_cantidadDePalabras(textoPrincipal))
    print(get_cantidadDePalabrasNoRepetidas(textoPrincipal))
    print(get_cantidadDeCaracteresConEspacio(textoPrincipal))
    print(get_cantidadDeCaracteresSinEspacio(textoPrincipal))
    makeSpace()
    print(get_cantidadDeVecesQueSeRepitioUnaPalabra("Hola", textoPrincipal))
    print(changeWordInText("kevin", "pablo", textoPrincipal))
    
# def get_info():
#     #mainText = open('C:\Users\pc0128\Downloads\El_Arbol_De_La_Colina.txt')
#     #type El_Arbol_De_La_Colina.txt | find /v /c ""

#     mainText = input("agrega tu texto: \n")
#     allWords = mainText.split(" ")
#     print(f"la cantidad de palabras es {len(allWords)}")
#     conjuntoDePalabras = set(allWords)
#     print(f"la cantidad de palabras no repetidas es {len(conjuntoDePalabras)}")

#     print(f"la cantidad de palabras es {len(mainText)}")

#     textoSinEspacio = mainText.replace(" ", "")
#     print(f"la cantidad de palabras es {len(textoSinEspacio)}")

"""
número de líneas, OK
número de palabras en total, OK
número de palabras no repetidas, OK
numero de caracteres con espacio, OK
número de caracteres sin espacio. OK
"""
def makeSpace():
    print("--------------------------------------------------------------------------------")

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
    
    count = get_cantidadDePalabras(mainText)
    a = mainText.replace(wordToFind,"")

    print(a)
    print(get_cantidadDePalabras(a))
    
    # count2 = get_cantidadDePalabras(textoSinLaPalabra)
    # print( get_cantidadDePalabras(textoSinLaPalabra) )

    #hacer el substring por cada palabra
    count = count
    return count

def changeWordInText(wordToChange, newWorld, mainText):
    a = mainText.replace(wordToChange, newWorld) #a =
    return a


def menu():
    print("-----Bienvenido al menu de opciones-----")
    while(True):
        response = input("Que deseas hacer? \n 1.- Ver cantidad de lineas \n 2.- Ver cantidad de palabras \n 3.- Ver cantidad de palabras no repetidas \n 4.- Ver cantidad de caracteres con espacio \n 5.- Ver cantidad de caracteres sin espacio \n 6.- Ver cantidad de veces que se repite una palabra \n 7.- Cambiar una palabra en un texto \n 8.- Salir \n")
        if(response == "1"):
            print("seleccionaste la opcion 1")

        if(response == "8"):
            os.system("cls")
            return

if __name__=="__main__":
    main()

