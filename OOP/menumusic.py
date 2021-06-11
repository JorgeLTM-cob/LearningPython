import sqlite3

def insertar():

    db1 = sqlite3.connect('musica.db')
    print("Estas en la funcion INSERTAR")
    print(" ")
    cancion1 = input("Escribe el nombre de la cancion: ")
    artista1 = input("Escribe el nombre del artista: ")
    album1 = input("Escribe el nombre del album: ")
    print(" ")
    
    insercion = db1.cursor()
    strInsercion = "INSERT INTO music(cancion,artista,album) values('" \
                   + cancion1 + "','" + artista1 + "','" + album1 + "')"
    print(strInsercion)
    insercion.execute(strInsercion)
    insercion.close()
    db1.commit()
    db1.close()
    print(" ")

def consultar():

    db2 = sqlite3.connect('musica.db')
    print("Estas en la funcion CONSULTAR")
    print(" ")
    db2.row_factory = sqlite3.Row
    consulta = db2.cursor()
    consulta.execute("SELECT * FROM music")
    filas = consulta.fetchall()
    lista = []
    for fila in filas:
        s = {}
        s['cancion'] = fila['cancion']
        s['artista'] = fila['artista']
        s['album'] = fila['album']
        lista.append(s)
    consulta.close()
    db2.close()
    print(" ")
    return(lista)

def menu():

    print("Bienvenido al sistema que gestiona la BD musica, porfavor lee las siguientes instrucciones")
    print("Para ingresar datos, digite 1")
    print("Para consultar la informacion, digite 2")
    opcion = int(input())
    if (opcion == 1):
        insertar()
        print(" ")
        menu()
    elif (opcion == 2):
        ListaCanciones = consultar()
        for cancion in ListaCanciones:
            print(cancion['cancion'] + " " + cancion['artista'] + " " + cancion['album'])
        print(" ")
        menu()
    else:
        print("Hasta luego :)")

menu()
    
