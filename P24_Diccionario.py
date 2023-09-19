#Los diccionarios nos sirven para poner diferentes caracteristicas con una especificacion

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
#Consulta del apartado 'Modelo' del diccionario teclado1
print('Teclado 1')
Consulta=teclado1['Modelo']
print(Consulta)

print('Teclado 2')
print(teclado2['Modelo'])
print(teclado2['Precio'])