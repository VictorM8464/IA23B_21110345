#Valor incial de x -> 0
x = 0

while x <= 30:
	x += 1
	
	#Salto de ejecucion
	if x == 4 or x == 6 or x == 10:
		print('Se salto el valor ', x, ' de x')
		continue
	if x== 15:
		print('Se rompio la ejecucion del bucle cuando x valia: ', x)
		#break nos permite salir del bucle directamente
		break
	print(x)