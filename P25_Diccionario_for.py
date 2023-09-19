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
#x pasara por 'Categoria' 'Modelo', y 'Precio'
#Cuando pase por el print, imprimirá sus caracteristicas
print('\tTeclado 1\n')
for x in  teclado1:
    print(teclado1[x])

print('\n\tTeclado 2\n')
for x in teclado2:
    print(teclado2[x])
