#**kwargs nos permite ingresas diccionarios a nuestras funciones

def colores(**kwargs):
    print("Este es el color ", kwargs['color1'], '.')
    
colores(color1='rojo', color2='azul', color3='amarillo')