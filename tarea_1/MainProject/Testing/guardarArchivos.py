
def guardarTxt(text, name, rute):
    with open(name, "w") as f:
        f.write(rute+text)

guardarTxt("adolfito", "secreto.txt", "hola/")