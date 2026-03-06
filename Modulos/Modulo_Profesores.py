from . import requests_api as api
import json

class Profesores():
    def __init__(self, Nombre, Apellido, Cedula, Email, Max_Carga, Materias):
        self.nombre = Nombre
        self.apellido = Apellido
        self.cedula = Cedula
        self.email = Email
        self.max_carga = Max_Carga
        self.materias = Materias

    def info_profe(self):
        print(self.nombre, self.apellido, self.cedula, self.email, self.max_carga, self.materias)

    def ver_profesores_fromapi():
        x = 0
        for i in api.data_profesores:
            x += 1
            #print(json.dumps(requests_api.data_profesores[:]["Nombre"], indent=2))
            print(x, i["Nombre"], i["Apellido"])

    def specific_profesor_fromapi():
        x = int(input("Ingrese el numero de cedula del docente: "))
        for i in api.data_profesores:
            if x == i["Cedula"]:
                print("Informacion del Docente:\n",json.dumps(i, indent=1), end="")
                            
    def add_profesor_fromapi():
        data = api.data_profesores

        Nombre = input("Ingrese el nombre del profesor: ")
        Apellido = input("Ingrese el apellido del profesor: ")
        Cedula = input("Ingrese la cedula del profesor: ")
        Email = input("Ingrese el correo del profesor: ")
        Max_Carga = input("Ingrese la carga maxima de materias del profesor: ")
        Materias = input("Ingrese los codigos de las materias del profesor: ")
        new_profesor = {
            "Cedula":Cedula,
            "Email":Email,
            "Apellido":Apellido,
            "Nombre":Nombre,
            "Max Carga":Max_Carga,
            "Materias":[Materias]
        }
        data.append(new_profesor)
        print(api.data_profesores)
    #info_profesores()
    #specific_profesor()
    def del_profesor_fromapi():
        x = int(input("Ingrese el numero de cedula del docente a eliminar: "))
        for i in api.data_profesores:
            
            if x == i["Cedula"]:
                print("Informacion del Docente:\n",json.dumps(i, indent=1), end="")
        y = input("Esta seguro que quiere eliminar este docente de la lista? (Y/N): ")
        if y == "Y" or "y":
            for i in api.data_profesores:
                print(api.data_profesores.index(i))
########################corregir
        else:
            print("No se elimino el docente de la lista")
            pass

def crear_objeto_fromapi():
    x = -1
    data = api.data_profesores
    for newobject in data:
        x += 1
        newobject = Profesores(data[x]["Nombre"],data[x]["Apellido"],data[x]["Cedula"],data[x]["Email"],data[x]["Max Carga"],data[x]["Materias"])
        newobject.info_profe()
#crear_objeto()