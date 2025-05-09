import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, jsonify,request,Response
from flask_cors import CORS
import json
import io
import os

def mover_carpeta(dir1:str):
    carpeta=os.getcwd()
    if not carpeta.endswith(dir1):
        nueva_carpeta=carpeta.split(f"Proyecto_talento_tech")[0]
        ruta = os.path.join(nueva_carpeta, 'Proyecto_talento_tech',dir1)           
        os.chdir(ruta)

def set_json(ruta, data):
    with open(ruta, 'w') as txt:
        json.dump(data, txt, indent=1)

def get_json(ruta):
    with open(ruta, 'r') as f:        
        return json.load(f)
    
    
data = get_json('json/cuestionario.json')
resultados = []
llaves = list(data[0].keys())

for item in data:
    if item["tipo_recoleccion"] == "casa":
        item["tipo_recoleccion"] = "Si"
    elif item["tipo_recoleccion"] == "punto_fijo":
        item["tipo_recoleccion"] = "No"


for llave in llaves:
    si_count = sum(1 for respuesta in data if respuesta[llave] == "Si")
    no_count = sum(1 for respuesta in data if respuesta[llave] == "No")
    resultados.append([si_count, no_count])