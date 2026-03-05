import requests
import json

profesores_url = ("https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/materias2526-2.json")

response = requests.get(profesores_url)

if response.status_code == 200:
    data = response.json()
    print("Datos JSON Adquiridos")
    print(data[1])
else:
    print(f"Ocurrio un error inesperado, codigo de error {response.status_code}")