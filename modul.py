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
    diccionario=abrirJSON("clientes")
    nombre=input("Nombre del usuario: ")
    apellido=input("Apellido del usuario: ")
    edad=input("Edad del usuario: ")
    direccion=input("Direccion del usuario: ")
    contacto=input("Numero de telefono: ")
    tipodeplan=[]
    categoria="Cliente nuevo"
    id=str(len(diccionario["usuarios"])+1)
    diccionario["usuarios"].append({"ID":id,"Nombre":nombre,"Apellido":apellido,"Edad":edad,"Direccion":direccion,"Telefono":contacto,"Planes":tipodeplan,"Categoria":categoria})
    guardarJSON("clientes",diccionario)
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
                    nome=planes["planes"][k]["Nombre"]
                    print("Presione ",k+1," para plan ", nome)
                plan=input(": ")
                if plan=="1":
                        for q in range (len(planes["planes"][0]["Planes"])):
                            print("Plan ",q+1)
                            print("Velocidaad: ",planes["planes"][0]["Planes"][q]["Velocidad"])
                            if diccionario["usuarios"][i]["Categoria"]=="cliente leal":
                                pre=planes["planes"][0]["Planes"][q]["Planes"]["Precio"]
                                precio=pre*0.2
                            else:
                                precio=planes["planes"][0]["Planes"][q]["Precio"]
                            print("Precio: ",precio)
                        numeroplan=int(input("Seleccione el numero del plan: "))
                        print("Ingrese el numero del plan a añadir")
                        añad=int(input(": "))-1
                        nuevo=planes["planes"][0]["Planes"][añad]
                        diccionario["usuarios"][i]["Planes"].append(nuevo)
                elif plan=="2":
                        for q in range(len(planes["planes"][1]["Planes"])):
                            print("Plan ", q+1)
                            print("Duracion: ", planes["planes"][1]["Planes"][q]["Duracion"])
                            if diccionario["usuarios"][i]["Categoria"]=="cliente leal":
                                pre=planes["planes"][1]["Planes"][q]["Precio"]
                                precio=pre*0.2
                                print("Tamano: x2 ", planes["planes"][1]["Planes"][q]["Tamano"])
                            else:
                                print("Tamano: ", planes["planes"][1]["Planes"][q]["Tamano"])
                                precio=planes["planes"][1]["Planes"][q]["Precio"]
                            print("Precio: ",precio)
                        print("Ingrese el numero del plan a añadir")
                        añad=int(input(": "))-1
                        nuevo=planes["planes"][1]["Planes"][añad]
                        diccionario["usuarios"][i]["Planes"].append(nuevo)
                elif plan=="3":
                        for q in range(len(planes["planes"][2]["Planes"])):
                            print("Plan ", q+1)
                            print("Duracion: ", planes["planes"][2]["Planes"][q]["Duracion"])
                            if diccionario["usuarios"][i]["Categoria"]=="cliente leal":
                                pre=planes["planes"][2]["Planes"][q]["Precio"]
                                precio=pre*0.2
                                print("Tamano: x2", planes["planes"][2]["Planes"][q]["Tamano"])
                            else:
                                print("Tamano: ", planes["planes"][2]["Planes"][q]["Tamano"])
                                precio=planes["planes"][2]["Planes"][q]["Precio"]
                            print("Precio: ",precio)    
                        print("Ingrese el numero del plan a añadir")
                        añad=int(input(": "))-1
                        nuevo=planes["planes"][2]["Planes"][añad]
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
def menuplanes():
    planes=abrirJSON("planes")
    print("Que desea hacer?")
    print("1 para añadir planes || 2 para editar planes || 3 para eliminar planes || 4 para salir")
    opcion=input(":")
    if opcion=="1":
        for i in range(len(planes["planes"])):
            print("Servicio ",i+1, planes["planes"][i]["Nombre"])
        nombre=int(input("A cual servicio quiere añadir planes? "))-1
        if planes["planes"][nombre]["Nombre"]=="Internet fibra optica":
            velocidad=input("Ingrese la velocidad del plan")
            precio=int(input("Ingrese el precio del plan: "))
            planes["planes"][nombre]["Planes"].append({"Nombre":"fibra optica","Velocidad":velocidad,"Precio":precio})
        else:
            tamaño=input("Ingrese el tamaño del plan: ")
            duracion=input("Ingrese la duracion del plan")
            precio=input("Ingrese el precio del plan: ")
            if nombre==1:
                planes["planes"][nombre]["Planes"].append({"Nombre":"Prepago","Tamano":tamaño,"Duracion":duracion,"Precio":precio})
            else:
                planes["planes"][nombre]["Planes"].append({"Nombre":"Postpago","Tamano":tamaño,"Duracion":duracion,"Precio":precio})
    if opcion=="2":
        if opcion=="1":
            for i in range(len(planes["planes"])):
                print("Servicio ",i+1, planes["planes"][i]["Nombre"])
            nombre=int(input("A cual servicio quiere editar planes? "))-1
            for i in range(len(planes["planes"][nombre]["Planes"])):
                print("Presione ", i+1, " para editar el plan ", i+1)
            numeroplan=input(": ")
            if planes["planes"][nombre]["Nombre"]=="Internet fibra optica":
                velocidad=input("Ingrese la velocidad del plan")
                precio=int(input("Ingrese el precio del plan: "))
                planes["planes"][nombre]["Planes"][numeroplan]["Velocidad"]=velocidad
                planes["planes"][nombre]["Planes"][numeroplan]["Precio"]=precio
            else:
                tamaño=input("Ingrese el tamaño del plan: ")
                duracion=input("Ingrese la duracion del plan")
                precio=input("Ingrese el precio del plan: ")
                planes["planes"][nombre]["Planes"][numeroplan]["Tamano"]=tamaño
                planes["planes"][nombre]["Planes"][numeroplan]["Duracion"]=duracion
                planes["planes"][nombre]["Planes"][numeroplan]["Precio"]=precio
            guardarJSON("planes",planes)
    if opcion=="3":
        for i in range(len(planes["planes"])):
            print("Servicio ",i+1, planes["planes"][i]["Nombre"])
        nombre=int(input("A cual servicio quiere eliminar un plan? "))-1
        for i in range(len(planes["planes"][nombre]["Planes"])):
            print("Presione ", i+1, " para editar el plan ", i+1)
        numeroplan=input(": ")
        planes["planes"][nombre]["Planes"].pop(numeroplan)
        guardarJSON("planes",planes)
    if opcion=="4":
        print("Adios ")
def reportes():
    diccionario=abrirJSON("clientes")
    planes=abrirJSON("planes")
    print("Numero de servicios ofrecidos por lal empresa: ", len(planes["planes"]))
    print("Servicios adquiridos por los clientes: ")
    for i in range (len(diccionario["usuarios"])):
        for q in range(len(diccionario["usuarios"][i]["Planes"])):
            print(diccionario["usuarios"][i]["Planes"][q]["Nombre"])
            print(diccionario["usuarios"][i]["Planes"][q]["Tamano"])
            print(diccionario["usuarios"][i]["Planes"][q]["Duracion"])
            print(diccionario["usuarios"][i]["Planes"][q]["Precio"])
            print("")
def menuinterfaz():
    tru=True
    while tru==True:
        print("Bienvenido, a que modulo desea ingresar?")
        print("1 modulo de usuario || 2 modulo de planes || 3 para modulo de reportes || 4 para salir")
        opt=input(":")
        if opt=="1":
            menuUser()
        if opt=="2":
            menuplanes()
        if opt=="3":
            reportes()
        if opt=="4":
            tru=False
