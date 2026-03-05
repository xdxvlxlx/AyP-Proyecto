import requests
import json

profesores_url = ("https://raw.githubusercontent.com/xdxvlxlx/AyP-Proyecto/refs/heads/main/profesores.json")
materias_url = ("https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/materias2526-2.json")

response_materias = requests.get(materias_url)
response_profesores = requests.get(profesores_url)

data_materias = response_materias.json()
data_profesores = response_profesores.json()

#print(json.dumps(data_materias, indent=2))

"""
if response.status_code == 200:
    data = response.json()
    print("Datos JSON Adquiridos")
    print(json.dumps(data, indent=1))
    #print(data)
else:
    print(f"A ocurrido un error, codigo {response.status_code}")
"""