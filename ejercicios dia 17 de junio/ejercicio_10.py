import os

# Asegura que el script use su propia carpeta como ruta base
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Abrir el archivo
archivo = open("ventas.csv", "r", encoding="utf-8")
lineas = archivo.readlines()[1:]
archivo.close()

result = []
nombres = []
unidades = []  # Aquí almacenaremos las unidades por producto

# Recorrer cada línea del documento.csv
for linea in lineas:
    lista = linea.strip().split(";")
    producto = lista[1]
    nomb = producto.upper()
    nombres.append(nomb)

    cantidad = float(lista[2])
    precio_unitario = float(lista[3])

    resultado = cantidad * precio_unitario
    result.append(resultado)
    unidades.append(cantidad)  # Guardamos la cantidad vendida

# Resultados generales
print("======================================================================")
print("                            TOTAL RECAUDADO                           ")
print("======================================================================")
print(f"$ {sum(result)}")
print("=======================================================================")
print("                  BUSCAR UNIDADES DE UN PRODUCTO                       ")
print("========================================================================")
# Preguntar por las unidades de un producto
while True:
    prod = input("Ingrese el nombre del producto que busca: ").upper()

    if prod in nombres:
        indice = nombres.index(prod)
        uni = unidades[indice]
        print(f"===============================================================")
        print(f"---------------------PRODUCTO---------------------------------")
        print(f"\n{prod}")
        print(f"----------------------UNIDADES--------------------------------")
        print(f"\n{uni}")
        break
    else:
        print(" Producto no encontrado. Intente de nuevo.\n")
