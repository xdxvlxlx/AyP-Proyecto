from Modulos import *

Modulo_Profesores.crear_objeto()

while True:
    x = input("1. Profesores\n2. Materias\n3. Generacion de horarios\n4. Modificacion de Horarios\n5. Salir\n")
    if x == "1":
        y = input("\n1. Ver lista de profesores\n2. Ver un profesor especifico\n3. Agregar profesor a una lista\n4. Eliminar profesor de una lista (WIP)\n5. Volver al menu anterior\n")
        if y == "1":
            print("Lista de Profesores:")
            Modulo_Profesores.Profesores.ver_profesores()
            input("\nPresione Enter para volver\n")
        if y == "2":
            Modulo_Profesores.Profesores.specific_profesor()
            input("\nPresione Enter para volver\n")
        if y == "3":
            Modulo_Profesores.Profesores.add_profesor()
        if y == "4":
            pass
        if y == "5":
            pass
    elif x == "2":
        pass
    elif x == "3":
        pass
    elif x == "4":
        pass
    elif x == "5":
        print("Programa finalizado")
        break
