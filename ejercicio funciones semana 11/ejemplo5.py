'''5.	Escriba el programa que contenga una función la cual retorne el factorial de un número capturado por teclado'''
import os
os.system('cls')

def factorial(numero):
    if numero == 0:
         return 1
    n = 1
    for i in range(numero):
         n *= i+1
    return n
         
         


while True:
        try:
            factor = int(input('Ingrese el número para calcular el factorial: '))
            if factor >= 0:
                break
            else:
                print('Ingrese un número válido')
        except Exception:
            print('Ingrese un valor válido!')

print(f'el factorial de {factor} es : {factorial(factor)}')