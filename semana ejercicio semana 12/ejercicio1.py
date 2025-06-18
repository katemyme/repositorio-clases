'''Escribe un programa que funcione como un diario simple. Cada vez que se 
ejecute, debe solicitar al usuario una entrada de texto y la guardará, junto con la fecha y hora 
actual, en un archivo llamado diario.txt. Cada nueva entrada debe añadirse al final del 
archivo sin borrar las anteriores. '''

from  datetime import datetime
import os
os.system('cls')


dia_actual = datetime.now()
fecha_formateada = dia_actual.strftime('%d-%m-%Y %H:%M')

def agregar_lineas(nueva_entrada):
    with open('diario.txt','a', encoding='utf-8') as diario:
        diario.write(f'{fecha_formateada}\n')
        diario.write('Querido Diario:\n')
        diario.write(f'{nueva_entrada}\n')
        diario.write('\n')
        

def leer_diario():
    with open('diario.txt','r',encoding='utf-8') as diario:
        contenido = diario.read()
        print('----CONTENIDO DEL DIARIO----')
        print(contenido)

nueva_entrada = input('Querido Diario: ')

agregar_lineas(nueva_entrada)

while True:
    peticion = input('Desea ver el contenido del diario (si/no): ').strip().lower()
    if peticion in ['si','sí']:
        leer_diario()
    elif peticion == 'no':
        break
    else:
        print('ingrese una repuesta válida')










