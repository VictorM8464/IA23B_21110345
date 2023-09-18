
######          Condicional Elif
#input pregunta y almacena la respuesta del usuario

edad = int(input('Cual es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 17:
	print('Eres menor de edad.')
elif edad >= 17 and edad <= 45:
	print('Eres adulto')
elif edad >= 45 and edad <= 100:
	print('Eres mayor de edad.')
elif edad >= 100 and edad <= 120:
	print('Estas muy bien conservado')
else:
	print('Edad no valida.')