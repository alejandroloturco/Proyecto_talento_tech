import matplotlib.pyplot as plt
import numpy as np

# Nombres cortos de las preguntas (para el eje X)
preguntas = [
    "Reutiliza aceite",
    "Lo tira al desagüe",
    "Conoce puntos recolección",
    "Sabe que contamina",
    "Entregaría aceite",
    "Interés ecológico",
    "Cocina en casa",
    "Usa más aceite",
    "Separa residuos",
    "Quiere recipiente",
    "Preferencia recolección",
    "Pagaría por recolección"
]

# Respuestas simuladas (número de personas que respondieron Sí / No)
respuestas_si = [12, 5, 7, 18, 15, 14, 17, 8, 13, 16, 10, 6]
respuestas_no = [8, 15, 13, 2, 5, 6, 3, 12, 7, 4, 10, 14]

# Crear el gráfico de barras
x = np.arange(len(preguntas))
width = 0.35  # ancho de las barras

fig, ax = plt.subplots(figsize=(12, 6))
barras_si = ax.bar(x - width/2, respuestas_si, width, label='Sí', color='green')
barras_no = ax.bar(x + width/2, respuestas_no, width, label='No', color='red')

# Etiquetas y formato
ax.set_ylabel('Cantidad de respuestas')
ax.set_title('Resultados del formulario sobre uso de aceite de cocina')
ax.set_xticks(x)
ax.set_xticklabels(preguntas, rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.show()
