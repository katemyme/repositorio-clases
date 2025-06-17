'''	Escriba un programa para capturar por teclado el número de horas trabajadas y que envíe dicho valor a una función que determine y retorne el valor a pagar, 
considerando que las primeras 160 horas trabajadas serán a $6.5 y el resto de horas a $7.5.'''
import os
os.system('cls')


def pago_hora(hora):
    if hora > 160:
        pago_hora = hora * 7.5
    if hora <= 160:
        pago_hora = hora * 6.5

    return pago_hora



while True:
        try:
            horas = int(input('Ingrese las horas laborales trabajadas: '))
            if horas > 0:
                break
            else:
                print('Ingrese un número válido')
        except Exception:
            print('Ingrese un valor válido!')
print('-----DINERO A PAGAR-----')
print(f'el dinero a pagar es: ${pago_hora(horas)}')