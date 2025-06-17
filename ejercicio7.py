'''Programa para pasar tres argumentos reales a una función que devolverá el menor de ellos'''
from typing import List
import os
os.system('cls')

def menor(numeros: List[int]) -> int:
    n = numeros[0]
    for i in numeros:
       if n > i:
        n = i 
        

    return n

numeros = []
for i in range(3):
   numero = int(input(f'Ingrese el número {i+1}: '))
   numeros.append(numero)

print(f'el menor número es {menor(numeros)}')