import sqlite3

def insertar():

    db1 = sqlite3.connect('novelas.db')
    print ("Estas en la funcion insertar")

    nombre1=input("Escribe el titulo de la novela: ")
    autor1=input("Escribe el autor de la novela: ")
    year1=str(input("Digita el anio de la novela: "))

    consulta = db1.cursor()
    strConsulta = "insert into tabla(nombre,autor,year) values('" \
            + nombre1 + "','" + autor1 + "'," + year1 + ")"
    print(strConsulta)
    consulta.execute(strConsulta)
    consulta.close()
    db1.commit()
    db1.close()

insertar()
