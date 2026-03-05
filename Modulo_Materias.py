import requests_api
import json

class Materias():
    def __init__(self, Código, Nombre, Secciones):
        self.codigo = Código
        self.nombre = Nombre
        self.secciones = Secciones