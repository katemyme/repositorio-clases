'''Crea un programa que permita al usuario crear una lista de compras. El programa 
solicitará al usuario que ingrese productos uno por uno y los guardará en un archivo llamado 
compras.txt. El usuario indicará que ha terminado de añadir productos introduciendo la 
palabra "fin". '''


def escribir_producto():
    with open('lista_de_compras.txt','w',encoding='utf-8') as lista:
        while True:
            producto = input('Ingrese el nombre del producto: ')
            if producto in ['fin','FIN','Fin']:
                print('Se han guardado correctamente sus productos!')
                break
            else:
                lista.write(f'{producto}\n')
            
            


        
escribir_producto()      