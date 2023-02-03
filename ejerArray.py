# Deseo agragar en una lista a los clientes que vayan llegando al restaurante
#cliente=[]
#seleccion= 1
#while seleccion==1:
#    print('*******************************')
#    print('Seleccione: ')
#    print('1 para agregar un nuevo cliente')
#    print('0 para cerrar el programa')
#    seleccion=int(input('Ingrese su seleecion: '))
#    if seleccion ==1:
#        cliente.append(input('Ingrese el nombre del cliente: '))
#print(cliente)


# es lo mimos si lo escribimos asi
clientes = []
seleccion = 1
while seleccion == 1 :
    print('**********************************')
    print('Seleccione:')
    print('1 para agregar un nuevo cliente')
    print('0 para cerrar el programa')
    seleccion = int(input('Ingrese su seleccion: '))

    if seleccion == 1 :
        nombreCliente = input('ingrese el nombre del cliente: ')
        clientes.append(nombreCliente)
        
print(clientes)
