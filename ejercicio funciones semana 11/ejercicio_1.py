'''
1.	Crear un programa que dado un monto para presupuesto anual de una fábrica calcule el porcentaje de dinero que le corresponde a cada departamento. 
El cálculo se realizará en una función que recibe como argumento el monto.
Recursos Humanos	50%
Manufactura			25%
Empaquetado		   15%
Publicidad			10
'''
import os
os.system('cls')

def porcentaje(monto,porcentaje):
    return monto * (porcentaje/100)


while True:
    try:
        presupuesto = int(input('ingrese el presupuesto anual: '))
        if presupuesto > 0:
            break
        else:
            print('ingrese un numero valido')
    except Exception:
        print('ingrese un valor valido!')
    

print('-----------TOTAL-----------------') 

print(f'\nel monto destinado a recursos humanos es {porcentaje(presupuesto,50):.2f}')

print(f'\nel monto destinado a Manufactura es {porcentaje(presupuesto,25):.2f}')

print(f'\nel monto destinado a empaquetado es {porcentaje(presupuesto,15):.2f}')

print(f'\nel monto destinado a publicidad es {porcentaje(presupuesto,10):.2f}')

