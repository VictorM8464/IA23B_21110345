#La condicion if se puede escribir en la misma linea
x = 100
y = 200

if x < y: print('x es menor que y.')

#Este es una modo para añadir tambien el else a la condicion
x = 10000
y = 200

print('x es menor que y.') if x < y else print('x no es menor que y')

#El or nos ayuda que la condicion tenga dos opciones que se pueden cumplir
x=34
if x<0 or x>0: 
    print("Tu numero no es igual a 0")
else:
    print("Tu numero es 0")

#El and pone dos o mas condiones que se DEBEN cumplir
edad=21
sexo='H'
if edad>=18 and sexo=='H': 
    print("Eres lo que estamos buscando")
else:
    print("No te podemos contratar")