#La tupla y las listas son parecidas solo que se abren con () en vez de []
#Las listas se pueden modificar y las tuplas no

colores = ('rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(colores[1])

numeros = (10, 1, 5, 11)
print(numeros[0] + numeros[2] + numeros[3] - numeros[1])

######      Convertir Tupla -> Lista
tupla = ('rojo', 'azul', 'verde', 'amarillo')
lista = list(tupla)
print(lista)
print(type(lista))

######      Convertir Lista -> Tupla
lista= ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
tupla= tuple(lista)
print(tupla)
print(type(tupla))