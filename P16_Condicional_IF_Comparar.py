###### Operadores de Comparacion
    #   > 	    Mayor que
    #   < 	    Menor que
    #   >=  	Mayor o igual que
    #   <=  	Menor o igual que
    #   ==  	Igual que
    #   !=  	Diferente que

num1 = 15
num2 = 20

#Cambia el operador para que la condición sea True.
if num1 <= num2:
	print('Se ejecuta el if.')

num1 = 1450
num2 = 60

#Cambia el operador para que la condición sea True.
if num1 > num2:
	print('Se ejecuta el if.')
	
#Haz que el siguiente condicional se convierta en False sin cambiar el operador.
num1 = 1450
num2 = 60 + 1390

if num1 != num2:
	print('Se ejecuta el if.')
	
######          Condicional IF Else

color = "rojo"

if color != "rojo":
    print("El color no es rojo.")
else:
    print("El color es rojo.")