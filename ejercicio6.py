'''	Escribir el programa que tenga una función, esta devuelva el área de un círculo cuyo radio se le suministra como argumento.'''
import math
import os
os.system('cls')

def circulo_area(radio):
    area = math.pi*(radio)**2
    return area
    
while True:
    try:
        radio = int(input('Ingrese el radio del circulo: '))
        if radio > 0:
            break
        else:
            print('Introduzca un número positivo')
    except Exception:
        print('Ingrese una entrada válida')

print(f'el área del circulo es: {circulo_area(radio):.2f} unidades cuadradas')