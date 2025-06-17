'''2.	Una compañía de seguros tiene contratados a n vendedores. 
Cada uno hace tres ventas a la semana. 
Su política de pagos es que un vendedor recibe un sueldo base, y un 10% extra por comisiones de sus ventas. 
El gerente de su compañía desea saber cuánto dinero obtendrá en la semana cada vendedor por concepto de comisiones por las tres ventas realizadas,
 y cuanto tomando en cuenta su sueldo base y sus comisiones. 
Utilice una función para calcular la comisión por las tres ventas realizadas.'''

import os
os.system('cls')

import random

while True:
    try:
        n_vendedores = int(input('ingrese la cantidad de vendedores: '))
        if n_vendedores> 0:
            break
        else:
            print('ingrese un número válido')
    except Exception:
        print('ingrese un valor válido!')

lista_ventas = [[round(random.randint(4000, 10_000) * 0.10, 2) for j in range(3)] for i in range(n_vendedores)]

for i in lista_ventas:
    print(*i)

def suma_comision():
    suma_lista = []
    for i in range(len(lista_ventas)):
        suma = sum(lista_ventas[i])
        suma_lista.append(suma)
        
    return suma_lista

totales = suma_comision()

while True:
    try:
        salario_base = int(input('ingrese el salario base de los vendedores: '))
        if salario_base > 0:
            break
        else:
            print('ingrese un número válido')
    except Exception:
        print('ingrese un valor válido!')
     
for i in range(n_vendedores):
    print(f'el vendedor {i+1} ha ganado {totales[i]} en comisiones')
    
total_a_pagar = [salario_base + comision for comision in totales]

print()
print()

for i in range(n_vendedores):
    print(f'la cantidad a pagar al vendedor {i+1} es: {total_a_pagar[i]:.2f}')
            

    

        
            
    

    