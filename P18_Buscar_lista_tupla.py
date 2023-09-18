entrada=input("Introduce el color de tu preferencia\n")
colores=('rojo', 'blanco', 'azul', 'verde')

#para buscar se tiene que poner la variable que comparar, despues 'in'
#y al final la lista o tupla donde va a buscar
if entrada in colores[0]:
    print("El color rojo esta admitido")
elif entrada in colores[1]:
    print("El color blanco esta admitido")
elif entrada in colores[2]:
    print("El color azul esta admitido")
elif entrada in colores[3]:
    print("El color verde esta admitido")
else:
    print("Color no admitido")