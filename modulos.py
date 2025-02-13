import json

def abrirJSON(ruta):
    dicFinal={}
    with open(f"./{ruta}.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(ruta,dic):
    with open(f"./{ruta}.json",'w') as outFile:
        json.dump(dic,outFile)
def tipoplan():
    plan=abrirJSON("planes")
def agergarUsuario():
    diccionario=abrirJSON("usuarios")
    nombre=input("Nombre del usuario: ")
    apellido=input("Apellido del usuario: ")
    direccion=input("Direccion del usuario: ")
    contacto=input("Numero de telefono: ")
    tipodeplan=input("Tipo de plan: ")

def menu():
    f=True
    while f==True:
        print("Que desea hacer?")
        print("1 para agregar usuario || 2 para leer usuarios || 3 para editar usuarios || 4 para eliminar usuarios || 5 para salir")
        opcion=input(": ")
        match opcion:
            case "1":
                agregarUsuario()
            case "2":
                leerUsuarios()
            case "3":
                editarUsuario()
            case "4":
                eliminarUsuario()
            case "5":
                f=False