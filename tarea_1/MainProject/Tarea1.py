import os

def main():
    menu()
    
    textoPrincipal = "hola hola mi nombre es kevin"

    #Creamos y almacenamos los textos en una lista
    mainTextList = list()
    path = "tarea_1/archivosDeTesteo/Libros_txt_utf-8/"
    mainTextList.append( open(path+"El_Arbol_De_La_Colina.txt").read() )
    # mainTextList.append( open(path+"El_Caos_Reptante.txt").read() )
    # mainTextList.append( open(path+"En_El_Mar_Remoto.txt").read() )
    # mainTextList.append( open(path+"Lazarillo_de_Tormes.txt").read() )
    # mainTextList.append( open(path+"Para_Leer_Al_Atardecer.txt").read() )
    # mainTextList.append( open(path+"Una_corta_historia_del_eBook.txt").read() )

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

def limpiarTexto(text):
    characters = ",;:.\n!\"'"
    for character in characters:
        text = text.replace(character, "")
    return text

def alert(text):
    aux = "─"
    fix = aux*(int(len(text)/2))
    print(f"┌{fix*2} •✧✧• {fix*2}┐")
    #print(f"-{fix}ALERTA{fix}- ")
    print(f"    {fix + text + fix}")
    print(f"└{fix*2} •✧✧• {fix*2}┘")
    print("")

def menu():
    
    while(True):
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

