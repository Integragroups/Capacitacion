# Creación de Clase
class Persona:
    def __init__(self, edad, nombre):
        self.edad=edad
        self.nombre=nombre
        print("Se ha creado ", self.nombre, " de ", self.edad)
        
    def Hablar( self, ** palabras):  # Recibe un diccionario como palabras
        for frase in palabras:      # Se itera la frase palabras
            print(self.nombre, '->',palabras[frase] )

hombre1=Persona(30, "Maria")
hombre1.Hablar(T1="Hola amigos", T2="Como están")

hombre2=Persona(20, "Andres")
hombre2.Hablar(T1="Hola amigos", T2="Me llamaron")
