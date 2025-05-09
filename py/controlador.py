from flask import Flask, jsonify,request,Response
from flask_cors import CORS
import os
import json
import matplotlib.pyplot as plt
import io
app=Flask(__name__)
CORS(app)
name = 'py/clientes.json'

carpeta=os.getcwd()
print('aqui: '+carpeta)
if not carpeta.endswith(f"\Proyecto_talento_tech"):
        carpeta=carpeta.split(f"\infoPacs")[0]
        os.chdir(carpeta)
        

if not os.path.exists('py'):
    os.makedirs('py')

if not os.path.exists(name):
    with open('aqui.json', 'w') as f:
        json.dump([], f)