# Creación de Clase
class Persona:
    def __init__(self):
        self.edad=18
        self.nombre="Juan"
        print("Se ha creado ", self.nombre, " de ", self.edad)
        
    def Hablar( self, palabras="No se que decir"):
        print(self.nombre, '->',palabras)

hombre=Persona()
hombre.Hablar("Hola amigos")
hombre.Hablar()
