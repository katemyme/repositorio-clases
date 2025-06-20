import os

# Asegura que el script use su propia carpeta como ruta base
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Abrir archivo CSV original
with open("notas.csv", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()[1:]

# Listas para guardar datos
nombres = []
promedios = []

# Procesar cada línea
for linea in lineas:
    lista = linea.strip().split(";")  # separa por punto y coma
    nombre = lista[0]
    notas = []
    for n in lista[1:]:
        notas.append(float(n))
    promedio = sum(notas) / len(notas)
    nombres.append(nombre)
    promedios.append(promedio)

# Guardar promedios en archivo de salida
with open("promedio.txt", "w", encoding="utf-8") as archivo2:
    archivo2.write("Nombres  Promedio\n")
    for i in range(len(nombres)):
        archivo2.write(f"{nombres[i]}: | {promedios[i]:.2f}\n")