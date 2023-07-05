import mysql.connector

def conectar():
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost", #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
            user="root", #/////////////////////// Se cambian las credenciales ya que estas las uso para mi ambinte lcoal /////////////////////
            password="!B4rc3l0n4$", #/////////////// Puedes poner las tuyas, en este caso se hizo este CRUD con MYSQL ////////////////////////
            database="curso" #////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        )
        
        if conexion.is_connected():
            print("\n",'Conexion exitosa a MySQL',"\n")
        
        # Retornar la conexión
        return conexion
    
    except mysql.connector.Error as error:
        print(f'Error al conectar a MySQL: {error}')