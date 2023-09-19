#Definicion de nuestra clase
class Usuario:
    #Definicion de los objetos de la clase
    nombre=''
    apellidos=''
    
    #Definicion de las funciones de la clase
    def imprimir(self):
        #self se refiere a los objetos que tiene la clase
        #Ya que la funcion esta en la clase Usuario, usará los objetos dentro de la misma
        print('Nombre: ', self.nombre, '\nApellidos: ', self.apellidos)
        
#Definicion de una variable a uns clase
#Ahora la variable tiene todas las propiedades de la clase
usuario001=Usuario()

#llenamos los objetos de nuestra variable
usuario001.nombre='Victor Abel'
usuario001.apellidos='Moreno Magana'
#llamamos la funcion de nuestra variable
usuario001.imprimir()