# Creación de Clase
class Persona:
    def __init__(self, edad, nombre):
        self.edad=edad
        self.nombre=nombre
        print("Se ha creado ", self.nombre, " de ", self.edad)
        
    def Hablar( self, palabras="No se que decir"):
        print(self.nombre, '->',palabras)

hombre1=Persona(30, "Maria")
hombre1.Hablar("Hola amigos")

hombre2=Persona(20, "Andres")
hombre2.Hablar("Hola amigos")
