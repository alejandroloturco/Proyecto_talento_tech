from funciones import *

data = get_json('json/cuestionario.json')
resultados = []
llaves = list(data[0].keys())
for item in data:
    if item["tipo_recoleccion"] == "casa":
        item["tipo_recoleccion"] = "si"
    elif item["tipo_recoleccion"] == "punto_fijo":
        item["tipo_recoleccion"] = "no"


for llave in llaves:
    si_count = sum(1 for respuesta in data if respuesta[llave] == "Si")
    no_count = sum(1 for respuesta in data if respuesta[llave] == "No")
    resultados.append([si_count, no_count])



