import requests_api
import json

class Profesores():
    def __init__(self, Nombre, Cedula, Email, Max_Carga, Materias):
        self.nombre = Nombre
        self.cedula = Cedula
        self.email = Email
        self.max_carga = Max_Carga
        self.materias = Materias

    def info_profesores():
        #x = len(requests_api.data_profesores)
        #for y in range(1, x+1):
        #    print(y)

        x = 0
        for i in requests_api.data_profesores:
            x += 1
            #print(json.dumps(requests_api.data_profesores[:]["Nombre"], indent=2))
            print(x, i["Nombre"], i["Apellido"])

    def specific_profesor():
        x = int(input("Ingrese el numero de cedula del docente: "))
        for i in requests_api.data_profesores:
            if x == i["Cedula"]:
                print("Informacion del Docente:\n",i)
            
    
    #info_profesores()
    specific_profesor()

    