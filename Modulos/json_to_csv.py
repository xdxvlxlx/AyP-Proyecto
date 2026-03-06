from . import requests_api as api
import csv

#json.dumps(api.data_profesores, indent=1)
json_file = api.data_profesores

fieldnames = json_file[0].keys()

with open("profesores.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    for data in json_file:
        writer.writerow(data)