import json

# Suponiendo que esta es tu estructura JSON
data = {
    "0": [1, 2],
    "1": [3, 4],
    "2": [5, 6],
    "3": [7, 8],
    "4": [9, 10],
    "5": [11, 12],
    "6": [13, 14],
    "7": [15, 16],
    "8": [17, 18],
    "9": [19, 20],
    "10": [21, 22],
    "11": [23, 24],
    "12": [25, 26]
}

# Lista de llaves
keys = list(data.keys())

# Listas para pares e impares
pares = []
impares = []

# Iteramos por los valores
for valores in data.values():
    for v in valores:
        if v % 2 == 0:
            pares.append(v)
        else:
            impares.append(v)

print("Llaves:", keys)
print("Pares:", pares)
print("Impares:", impares)
