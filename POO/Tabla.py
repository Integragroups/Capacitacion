# Manejo de Base de datos
import sqlite3 #Importa la clase
conexion=sqlite3.connect('novelas.db') #Crea una conexion
consulta=conexion.cursor() #Crea un cursor
tabla=("CREATE TABLE tabla(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre VARCHAR (30) NOT NULL, autor VARCHAR(40) NOT NULL, year INTEGER(9) NOT NULL);") 
print(tabla)
if (consulta.execute(tabla)): # Ejecuta el cursor
    print("Tabla creada")
else:
        print("Tabla creada")
consulta.close()
conexion.commit()
conexion.close()