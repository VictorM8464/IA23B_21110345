######      len()
#Longitud del elemento
teclado={
    'Categoria': 'Teclado',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
    }
print('Longitud del diccionario: ', len(teclado))

######      del
#Eliminar todo o parte del diccionario

del teclado['Precio']
print('\nEliminacion del Precio:\n', teclado)

######      Añadir nuevas claves y valores

teclado['Precio']='89,99'
teclado['Color']='Blanco'
print('\nImplementar cosas al diccionario:\n', teclado)

######      Ejercicio

teclado1={
    'Categoria': 'Teclado',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
    }

teclado2={
    'Categoria': 'Teclado',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
    }

del teclado1
del teclado2['Categoria']
del teclado2['Precio']
print('\nEjercicio\n', teclado2)
