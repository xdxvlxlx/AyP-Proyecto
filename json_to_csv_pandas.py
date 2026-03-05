import requests_api as api
import pandas as pd

json_file = api.data_profesores

x = pd.DataFrame(json_file)
#print(x)
x.to_csv("profesores_pandas.csv", index=False, sep=";")