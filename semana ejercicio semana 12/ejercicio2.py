''' Desarrolla un programa que pida al usuario el nombre de un archivo de texto. El 
programa deberá leer el archivo y mostrar en pantalla el número total de líneas que contiene. 
Debe manejar el error en caso de que el archivo no exista. '''

import os
os.system('cls')

nombre_archivo = input('ingrese el nombre del archivo que desea abrir: ')

def leer_archivo():
    try:
        with open(f'{nombre_archivo}.txt','r',encoding='utf-8') as archivo:
            list = archivo.readlines()
            print()
            print(f'el archivo tiene {len(list)} lineas ')
            print()
            print('----CONTENIDO DEL ARCHIVO----')
            for lineas in list:
                print(lineas, end= '')
    except FileNotFoundError:
        print('Ingrese un nombre válido')

leer_archivo()


