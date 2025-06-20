# Lectura de archivo poema.txt línea por línea   
try:
        with open("poema.txt", "r", encoding="utf-8") as archivo:
         for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print(" el archivo 'poema.txt' no se encontro.")
except Exception as e:  
    print(f"ocurrio un error: {e}") 
exit