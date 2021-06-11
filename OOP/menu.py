import sqlite3

def insertar():

    db1 = sqlite3.connect('novelas.db')
    print ("Estas en la funcion insertar")
    nombre1 = input("Escribe el nombre de la novela: ")
    autor1 = input("Escribe el nombre del autor: ")
    year1 = str(input("Escribe el anio de publicacion: "))

    insercion = db1.cursor()
    strInsercion = "INSERT INTO tabla(nombre,autor,year) VALUES('"\
            + nombre1 + "','" + autor1 + "'," + year1 + ")"
    print(strInsercion)
    insercion.execute(strInsercion)
    insercion.close()
    db1.commit()
    db1.close()

def consultar():

    db2 = sqlite3.connect('novelas.db')
    print ("Estas en la funcion consultar")
    db2.row_factory = sqlite3.Row
    consulta = db2.cursor()
    consulta.execute("SELECT * FROM tabla")
    filas = consulta.fetchall()
    lista = []
    for fila in filas:
        s = {}
        s['nombre'] = fila['nombre']
        s['autor'] = fila['autor']
        s['year'] = fila['year']
        lista.append(s)
    consulta.close()
    db2.close()
    return(lista)

def menu():
   print("Bienvenido, porfavor lee las siguientes instrucciones:")
   print("Si deseas aniadir campos a la Base de Datos, digita 1")
   print("Si deseas consultar el contenido de la Base de Datos, digita 2")
   opcion = int(input("Tu accion es: "))

   if (opcion == 1):
       insertar()
       print(" ")
       menu()
   elif (opcion == 2):
      ListaNovelas = consultar()
      for novela in ListaNovelas:
         print(novela['nombre'] + " " + novela['autor'] + " " + str(novela['year']))
      print(" ")
      menu()
   else:
       print("Hasta luego :)")

menu()
