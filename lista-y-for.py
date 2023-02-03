# Array o Lista
# Una lista es un tipo de dato que contiene diferentes objetos o valores. Por ejemplo:

miLista = ['valor1', 2 , True]
print(miLista) #imprimo miLista 
# salida: ['valor1', 2 , True]

# Vamos a imprimir el True
# las listas inician en posicion 0, esto quiere decir que la posicion de 'valor1' es 0
# por ejemplo la pocision de True en la lista es 2
# entonces para imprimir True, debo de usar la posicion 2 de la lista asi:
print(miLista[2])

# Vamos a imprimir todos los valores de la lista sin conchetes
# para esto tenemos que recorrer la lista e imprimir valor por valor
# para recorrer la lista usamos un ciclo que se ejecute tantas veces como valores tenga la lista
for valor in miLista:
    print(valor)

# Vamos a aniadir un elemento o valor al final de la lista
miLista.append('Este es el nuevo valor')
print(miLista)
# salida: ['valor1', 2 , True, 'Este es el nuevo valor']

# Vamos a extender miLista con una nueva lista
miLista.extend([1,2,3])
print(miLista)
# salida: ['valor1', 2 , True , 'Este es el nuevo valor', 1 , 2 , 3 ]

# Vamos a insertar un valor en miLista, en la posicion 2
miLista.insert(2, 'esta es 2')
print(miLista)
# salida: ['valor1', 2 , 'esta es 2' , True , 'Este es el nuevo valor', 1 , 2 , 3 ]

# Vamos a eliminar de miLista el valor True
miLista.remove(True)
print(miLista)
# salida: ['valor1', 2 , 'esta es 2' , 'Este es el nuevo valor', 1 , 2 , 3 ]

# Vamos a eliminar de miLista el valor de la posicion 3
del miLista[3]
print(miLista)
# salida: ['valor1', 2 , 'esta es 2', 1 , 2 , 3 ]


#Link fuente: https://medium.com/@hgodinez89/operaciones-sobre-listas-en-python-c19853a9d07b


# FOR
# se usa cuando conocemos el numero de iteraciones que tendra el ciclo, por eso usamos las listas como ejemplo
# porque conocemos los valores que tiene la lista

