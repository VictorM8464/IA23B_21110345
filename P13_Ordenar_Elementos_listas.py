######          sort()
#sort() acomoda los elemtos alfabeticamente A-Z
print("\tMetodo sort()")

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron','lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colores)

colores.sort()
print(colores)

######          sort(reverse=True)
#sort(reverse=True) acomoda los elemtos alfabeticamente inversamente Z-A
print("\n\tMetodo sort(reverse=True)")

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron','lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colores)

colores.sort(reverse=True)
print(colores)

######          sorted()
#sorted() funciona como sort(), pero este no modifica las posiciones de los elementos
#solo los acomoda para otra funcion
print("\n\tMetodo sorted()")

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron','lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colores)
print(sorted(colores))
print(colores)