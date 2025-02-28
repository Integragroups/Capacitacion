# Voy hacer una practica de interfaces
""" Se va utilizar TkInter, sin enbargo hay otras librerias que son más modernas
    como son wxPython, PyQT, y """
from tkinter import *  #Carga todas las definciones de la biblioteca tkinter: Menús, Ventanas, scrolls, y demás
class Interfaz:
    def __init__(self, contenedor):
        self.lbltitulo=Label(contenedor,text="Ingreso de datos: ",bg="orange")
        self.nombre=Label(contenedor,text="Nombre: ",bg="White", fg="black")
        self.txtnombre=Entry(contenedor)
        self.apellido=Label(contenedor,text="Apellido: ",bg="White", fg="black")
        self.txtapellido=Entry(contenedor)
        self.edad=Label(contenedor,text="Edad: ",bg="White", fg="black")
        self.txtedad=Entry(contenedor)
        self.activo=Checkbutton(contenedor,text="Activo:" )
        self.guardar=Button(contenedor,text="Guardar", command=self.saludar )
        self.cancelar=Button(contenedor,text="Cancelar" )
        self.lbltitulo.pack(side=TOP,fill=X)
        self.nombre.pack() 
        self.txtnombre.pack() 
        self.apellido.pack()
        self.txtapellido.pack()
        self.edad.pack()
        self.txtedad.pack()
        self.activo.pack()
        self.guardar.pack()
        self.cancelar.pack()

    def saludar(self):
        print("Hola") 


ventana=Tk() # Crea el primer objeto de la clase TK, en el se ecnuentra los elemento necesarios para iniciar
            # el motor gráfico del SO
miInterfaz=Interfaz(ventana)
ventana.mainloop() #Inicia un ciclo infinito que permite al programa monitorear las acciones en la ventana