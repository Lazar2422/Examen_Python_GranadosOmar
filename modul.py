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
    edad=input("Edad del usuario: ")
    direccion=input("Direccion del usuario: ")
    contacto=input("Numero de telefono: ")
    tipodeplan=input("Tipo de plan: ")
def leerUsuarios():
    diccionario=abrirJSON("clientes")
    for i in range(len(diccionario["usuarios"])):
        print("ID:",diccionario["usuarios"][i]["ID"])
        print("Nombre:",diccionario["usuarios"][i]["Nombre"])
        print("Apellido:",diccionario["usuarios"][i]["Apellido"])
        print("Edad:",diccionario["usuarios"][i]["Edad"])
        print("Direccion:",diccionario["usuarios"][i]["Direccion"])
        print("Contacto:",diccionario["usuarios"][i]["Telefono"])
        print("Categoria: ",diccionario["usuarios"][i]["Categoria"])
        print("Planes adquiridos: ")
        for q in range(len(diccionario["usuarios"][i]["Planes"])):
            print("Tipo de plan: ",diccionario["usuarios"][i]["Planes"][q]["Nombre"])
            print("Tipo de plan: ",diccionario["usuarios"][i]["Planes"][q]["Tamano"])
            print("Duracion: ",diccionario["usuarios"][i]["Planes"][q]["Duracion"])
            print("Precio: ",diccionario["usuarios"][i]["Planes"][q]["Precio"])
def editarUsuarios():
    diccionario=abrirJSON("clientes")
    iden=input("Ingrese el id del usuario que desea editar: ")
    for i in range(len(diccionario["usuarios"])):
        if diccionario["usuarios"][i]["ID"]==iden:
            print("1 para editar nombre || 2 para editar apellido || 3 para editar edad || 4 para editar direccion || 5 para editar contacto || 6 para agregar plan || 7 para editar categoria ")
            opcion=input(": ")
            if opcion=="1":
                diccionario["usuarios"][i]["nombre"]=input("Nombre del usuario: ")
            elif opcion=="2":
                diccionario["usuarios"][i]["apellido"]=input("Apellido del usuario: ")
            elif opcion=="3":
                diccionario["usuarios"][i]["edad"]=input("Edad del usuario: ")
            elif opcion=="4":
                diccionario["usuarios"][i]["direccion"]=input("Direccion del usuario: ")
            elif opcion=="5":
                diccionario["usuarios"][i]["Telefono"]=input("Numero de telefono: ")
            elif opcion=="6":
                planes=abrirJSON("planes")
                print("Planes disponibles: ")
                for k in range (len(planes["planes"])):
                    if k==0:
                        nome="Internet Fibra optica"
                    elif k==1:
                        nome="Prepago"
                    elif k==2:
                        nome="Postpago"
                    print("Presione ",k+1," para plan ", nome)
                plan=input(": ")
                if plan=="1":
                        rutaces="Internet fibra optica"
                        for q in range (len(planes["planes"][0][rutaces])):
                            print("Plan ",q+1)
                            print("Velocidaad: ",planes["planes"][i][rutaces][q]["Velocidad"])
                            if diccionario["usuarios"][i]["Categoria"]=="cliente leal":
                                pre=planes["planes"][0][rutaces][q]["Precio"]
                                precio=pre*0.2
                            else:
                                precio=planes["planes"][0][rutaces][q]["Precio"]
                            print("Precio: ",precio)
                        numeroplan=int(input("Seleccione el numero del plan: "))
                        diccionario["usuarios"]["Planes"].append({planes["planes"][numeroplan-1]})
                        print("Ingrese el numero del plan a añadir")
                        añad=int(input(": "))-1
                        nuevo=planes["planes"][0][rutaces][añad]
                        diccionario["usuarios"][i]["Planes"].append(nuevo)
                elif plan=="2":
                        rutaces="Prepago"
                        for q in range(len(planes["planes"][1][rutaces])):
                            print("Plan ", q+1)
                            print("Duracion: ", planes["planes"][1][rutaces][q]["Duracion"])
                            if diccionario["usuarios"][i]["Categoria"]=="cliente leal":
                                pre=planes["planes"][1][rutaces][q]["Precio"]
                                precio=pre*0.2
                                print("Tamano: x2 ", planes["planes"][1][rutaces][q]["Tamano"])
                            else:
                                print("Tamano: ", planes["planes"][1][rutaces][q]["Tamano"])
                                precio=planes["planes"][1][rutaces][q]["Precio"]
                            print("Precio: ",precio)
                        print("Ingrese el numero del plan a añadir")
                        añad=int(input(": "))-1
                        nuevo=planes["planes"][1][rutaces][añad]
                        diccionario["usuarios"][i]["Planes"].append(nuevo)
                elif plan=="3":
                        rutaces="Postpago"
                        for q in range(len(planes["planes"][2][rutaces])):
                            print("Plan ", q+1)
                            print("Duracion: ", planes["planes"][1][rutaces][q]["Duracion"])
                            if diccionario["usuarios"][i]["Categoria"]=="cliente leal":
                                pre=planes["planes"][2][rutaces][q]["Precio"]
                                precio=pre*0.2
                                print("Tamano: x2", planes["planes"][2][rutaces][q]["Tamano"])
                            else:
                                print("Tamano: ", planes["planes"][2][rutaces][q]["Tamano"])
                                precio=planes["planes"][2][rutaces][q]["Precio"]
                            print("Precio: ",precio)    
                        print("Ingrese el numero del plan a añadir")
                        añad=int(input(": "))-1
                        nuevo=planes["planes"][2][rutaces][añad]
                        diccionario["usuarios"][i]["Planes"].append(nuevo)
            elif opcion=="7":
                print("Ingrese el numero de años que ha estado en la empresa")
                años=int(input(": "))
                if años<5:
                    categoria="cliente nuevo"
                elif años<10:
                    categoria="cliente regular"
                elif años>=10:
                    categoria="cliente leal"
                diccionario["usuarios"][i]["Categoria"]=categoria
    guardarJSON("clientes",diccionario)


def eliminarUsuarios():
    diccionario=abrirJSON("usuarios")
    print("Ingrese el id del usuario a eliminar ")
    id=input(": ")
    for i in range(len(diccionario["usuarios"])):
        if id==diccionario["usuarios"][i]["ID"]:
            diccionario["usuarios"].pop(i)
def menuUser():
    f=True
    while f==True:
        print("Que desea hacer?")
        print("1 para agregar usuario || 2 para leer usuarios || 3 para editar usuarios || 4 para eliminar usuarios || 5 para salir")
        opcion=input(": ")
        if opcion=="1":
            agergarUsuario()
        elif opcion=="2":
            leerUsuarios()
        elif opcion=="3":
            editarUsuarios()
        elif opcion=="4":
            eliminarUsuarios()
        elif opcion=="5":
            f=False
        else:
            print("Opcion invalida")
def menuinterfaz():
    tru=True
    while tru==True:
        print("Bienvenido, a que modulo desea ingresar?")
        print("1 modulo de usuario || 2 modulo de planes || 3 historial de usuarios || 4 para modulo de reportes || 5 para salir")
        opt=input(":")
        if opt=="1":
            menuUser()
