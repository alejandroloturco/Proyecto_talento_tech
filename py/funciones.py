import matplotlib.pyplot as plt
import numpy as np
import os

def mover_carpeta(dir1:str):
    carpeta=os.getcwd()
    if not carpeta.endswith(dir1):
        nueva_carpeta=carpeta.split(f"Proyecto_talento_tech")[0]
        ruta = os.path.join(nueva_carpeta, 'Proyecto_talento_tech',dir1)                
        os.chdir(ruta)
