from funciones import *

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


x = np.arange(len(preguntas))            
y_1 = respuestas_si             
y_2 = respuestas_no             

mover_carpeta('graficas')
# Dividir a la mitad
mid = len(x) // 2
x1, y1, z1= x[:mid], y_1[:mid], y_2[:mid]
x2, y2, z2= x[mid:], y_2[mid:], y_2[mid:]


width = 0.35
# Primer gráficofig, 

fig, ax = plt.subplots(figsize=(12, 11))
barras_si = ax.bar(x1 - width/2, y1, width, label='Sí', color='green')
barras_no = ax.bar(x1 + width/2, z1, width, label='No', color='red')
ax.set_ylabel('Cantidad de respuestas')
ax.set_title('Resultados del formulario sobre uso de aceite de cocina')
ax.set_xticks(x1)
ax.set_xticklabels(preguntas[:(len(preguntas)//2)], rotation=45, ha='right')
ax.legend()
plt.savefig('output2.png')
plt.close()

fig, ax2 = plt.subplots(figsize=(12, 11))
barras_si = ax2.bar(x2 - width/2, y2, width, label='Sí', color='green')
barras_no = ax2.bar(x2 + width/2, z2, width, label='No', color='red')
ax2.set_ylabel('Cantidad de respuestas')
ax2.set_title('Resultados del formulario sobre uso de aceite de cocina')
ax2.set_xticks(x2)
ax2.set_xticklabels(preguntas[(len(preguntas)//2):], rotation=45, ha='right')
ax2.legend()
plt.savefig('output3.png')
plt.close()
