#*args nos permite meter los valores que sean dentro de nuestra funcion
#Esto lo arregla como si fuera una lista o tupla

#       Ejercicio 1
def colores(*args):
    y=0
    for x in args:
        y+=1
    
    print("Tiene ", y , " Argumentos")

print('\tPrimer ejercicio\n')
colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marron', 'naranja')

#       Ejercicio 2

def favorito(*args):
    print('El color ', args[1] , ' es mi favorito.\nEl color', args[0] , ' tampoco esta mal.')
    
print('\n\tSegundo ejercicio\n')
favorito('negro', 'rojo')

#       Ejercicio 3

def suma(*args):
    res=0
    y=len(args)
    for x in range(y):
        res=res+args[x]
        
    print('El resultado de la suma es: ', res)
    
print('\n\tTercer ejercicio\n')
suma(12, 45, 71, 60, 42)    