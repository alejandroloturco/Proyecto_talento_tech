from funciones import *

si_count = []
no_count = []
for i in range(1,len(resultados)):
    si_count.append(resultados[i][0])
    no_count.append(resultados[i][1])

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
mover_carpeta('graficas')

x = np.arange(len(preguntas))            
            
# Dividir a la mitad
mid = len(x) // 2
x1, y1, z1= x[:mid], si_count[:mid], no_count[:mid]
x2, y2, z2= x[mid:], si_count[mid:], no_count[mid:]


width = 0.35
# Primer gráfico

fig, ax = plt.subplots(figsize=(12, 6))
barras_si1 = ax.bar(x1 - width/2, y1, width, label='Sí', color='green')
barras_no1 = ax.bar(x1 + width/2, z1, width, label='No', color='yellow')
ax.set_ylabel('Cantidad de respuestas')
ax.set_title('Resultados del formulario sobre uso de aceite de cocina')
ax.set_xticks(x1)
ax.set_xticklabels(preguntas[:(len(preguntas)//2)], rotation=45, ha='right')
ax.legend()
plt.tight_layout()
plt.savefig('output2.png')
plt.close()



fig, ax2 = plt.subplots(figsize=(12, 6))
barras_si2 = ax2.bar(x2 - width/2, y2, width, label='Sí', color='green')
barras_no2 = ax2.bar(x2 + width/2, z2, width, label='No', color='yellow')
ax2.set_ylabel('Cantidad de respuestas')
ax2.set_title('Resultados del formulario sobre uso de aceite de cocina')
ax2.set_xticks(x2)
ax2.set_xticklabels(preguntas[(len(preguntas)//2):], rotation=45, ha='right')
ax2.legend()
plt.tight_layout()
plt.savefig('output3.png')
plt.close()
