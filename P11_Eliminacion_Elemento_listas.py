######          del()
#del() funciona con posiciones de los elementros
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

print("\tMetodo del()")
print(colores)

#Eliminacion de azul
del colores[1]
print(colores)

#Eliminacion de marron
del colores[3]
print(colores)

#Eliminacion de negro
del colores[-4]
print(colores)

#Eliminacion de rosa
del colores[-3]
print(colores)

######          remove()
#remove() funciona con el contenido especifico de la variable "palabra"

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

print("\n\tMetodo remove()")
print(colores)

#Eliminacion de amarillo
colores.remove('amarillo')
print(colores)

#Eliminacion de rojo
colores.remove('rojo')
print(colores)

######          pop()
#pop() Unicamente elimina el ultimo elemento

#Tambien puede guardar el elemento borrado en otra variable
#Para guardarlo se requiere la posicion especifica del elemento
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

print("\n\tMetodo pop()")
print(colores)

Color=[' ', ' ']
Color1=colores.pop(1)
Color2=colores.pop(-2)

print(colores)
print("Los colores eliminados y almacenados son: "+Color1+' y '+Color2)