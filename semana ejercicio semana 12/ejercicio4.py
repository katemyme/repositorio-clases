'''Se proporciona un archivo productos.csv donde cada línea contiene el nombre 
de un producto, su precio y la cantidad en stock, separados por comas (ej: Laptop,1200,15). 
Escribe un programa que lea este archivo y muestre la información en un formato legible 
para el usuario, indicando el nombre, precio y stock de cada producto.'''


import os
os.system('cls')

def abrir_csv():
    with open('estudiantes.csv','r',encoding='utf-8-sig') as excel:
        for lineas in excel:
            sucio =lineas.strip().split(";") #split es convertir una cadena en lista con su separador 
            limpio = [dato.replace('[', '').replace(']', '') for dato in sucio] #aca removemos los corchetes de las listas
            print(" | ".join(limpio)) #join lo que hace es convertir esa lista a una cadena y escogemos el separador




abrir_csv()
    