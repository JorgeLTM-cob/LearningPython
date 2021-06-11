import sqlite3

def consultar():
   db2 = sqlite3.connect('novelas.db')
   print("Estas en la funcion consultar")
   db2.row_factory = sqlite3.Row
   consulta = db2.cursor()
   consulta.execute("SELECT * FROM tabla;")
   filas = consulta.fetchall()
   lista = []
   for fila in filas:
      s = {}
      s['nombre'] = fila['nombre']
      s['autor'] = fila['autor']
      s['year'] = str(fila['year'])
      lista.append(s)
   consulta.close()
   db2.close()
   return(lista)

ListaNovelas = consultar()
for novela in ListaNovelas:
    print(novela['nombre'],novela['autor'],novela['year'])


