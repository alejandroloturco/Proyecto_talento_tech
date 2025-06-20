from funciones import *

visitantes = ["Registrados", "No Registrados"]
# Lista de ejemplo con porcentaje  de visitantes en el orden de Registrados, No Registrados
visitas = [resultados[0][0],resultados[0][1]]
#Colores alusivos a la tematica de la pagina
colores = ["#549C3C", "#FFD33B"]
explode = (0.05, 0)  # Destaca ligeramente el primer segmento (Registrados)

plt.figure(figsize=(5, 5))  # Tamaño del gráfico
plt.pie(
    visitas,
    labels=visitantes,
    colors=colores,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

plt.title("Visitantes Totales", fontsize=16, fontweight='bold')
plt.tight_layout()

mover_carpeta('graficas')
plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.close()


