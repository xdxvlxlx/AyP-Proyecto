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

    def verprofe_temp(self):
        print(self.nombre, self.apellido, self.cedula, self.email, self.max_carga, self.materias)


    def ver_profesores(self):
        x = 0
        for i in api.data_profesores:
            x += 1
            #print(json.dumps(requests_api.data_profesores[:]["Nombre"], indent=2))
            print(x, i["Nombre"], i["Apellido"])

    def specific_profesor():
        x = int(input("Ingrese el numero de cedula del docente: "))
        for i in api.data_profesores:
            if x == i["Cedula"]:
                print("Informacion del Docente:\n",json.dumps(i, indent=1), end="")
                            
    def add_profesor(self):
        data_list = api.data_profesores
        new_profesor = {
            "Cedula":self.cedula,
            "Email":self.email,
            "Apellido":self.apellido,
            "Nombre":self.nombre,
            "Max Carga":self.max_carga,
            "Materias":[self.materias]
        }
        self.nombre = input("Ingrese el nombre del profesor: ")
        self.apellido = input("Ingrese el apellido del profesor: ")
        self.cedula = input("Ingrese la cedula del profesor: ")
        self.email = input("Ingrese el correo del profesor: ")
        self.max_carga = input("Ingrese la carga maxima de materias del profesor: ")
        self.materias = input("Ingrese los codigos de las materias del profesor: ")        
        data_list.append(new_profesor)
    #info_profesores()
    #specific_profesor()

def crear_objeto():
    x = -1
    data = api.data_profesores
    for newobject in data:
        x += 1
        newobject = Profesores(data[x]["Nombre"],data[x]["Apellido"],data[x]["Cedula"],data[x]["Email"],data[x]["Max Carga"],data[x]["Materias"])
        newobject.verprofe_temp()
#crear_objeto()