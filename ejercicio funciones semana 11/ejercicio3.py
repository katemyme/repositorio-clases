'''3.	Escribir un programa que permita ingresar los salarios de una cantidad indicada de empleados,
 debe presentar al final el total que se debe pagar a cada empleado y el descuento de renta considerando que es del 10% sobre cada salario.
 Utiliza una función para el cálculo del descuento.'''

#hay un problema al digitar espacio y validaciones en el ciclo for

import os
os.system('cls')

def salario_neto(salario_bruto):
   salario_neto = salario_bruto*0.90
   return salario_neto

def cantidad_empleados():
    lista_salario = []
    
    while True:
        try:
            n_cantidad = int(input('Ingrese la cantidad de empleados: '))
            if n_cantidad > 0:
                break
            else:
                print('Ingrese un número válido')
        except Exception:
            print('Ingrese un valor válido!')

    for i in range(n_cantidad):
        while True:
            try:
                salario_emp = int(input(f'Ingrese el salario del empleado {i+1}: '))
                if salario_emp > 0:
                    break
                else:
                    print('Ingrese un número válido')
            except Exception:
                print('Ingrese un valor válido!')

        salario_final = salario_neto(salario_emp)
        lista_salario.append(salario_final)

    return lista_salario
   
cantidad_empleado = cantidad_empleados()
print()
print('------------SALARIO DE LOS EMPLEADOS-------------')
print()
for i in range(len(cantidad_empleado)):
   print(f'el salario del empleado {i+1} es {cantidad_empleado[i]}')
   
    


    


  
