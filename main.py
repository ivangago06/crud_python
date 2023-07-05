# Realizar un CRUD (SELECT, UPDATE, INSERT Y DELETE) con menú selecionable con opción de salir, puede ser con MYSQL, SLQ o SQLITE3, se debe de entregar a mas tardar el 10 de julio

from conexion import *

# Función para mostrar el menú y obtener la opción seleccionada
def mostrar_menu():
    print("\n--- MENU ---\n")
    print("1. Seleccionar registros")
    print("2. Actualizar registro")
    print("3. Insertar registro")
    print("4. Eliminar registro")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
    return opcion

# Función para seleccionar registros
def seleccionar_registros():
    conexion = conectar()
    db = conexion.cursor()
    db.execute("SELECT * FROM personas")
    registros = db.fetchall()
    for registro in registros:
        print(registro)
    conexion.close()

# Función para actualizar un registro
def actualizar_registro():
    conexion = conectar()
    db = conexion.cursor()
    db.execute("SELECT * FROM personas")
    registros = db.fetchall()
    for registro in registros:
        print(registro) # Se pinta en pantalla los registros existentes para poder elegir cual actualizar
    
    id = input("Ingrese el ID del registro a actualizar: ")
    nombre = input("Ingrese el nuevo valor para el nombre: ")
    edad = input("Ingrese el nuevo valor para la edad: ")
    curp = input("Ingrese el nuevo valor para el CURP: ")
    db.execute("UPDATE personas SET nombre = %s, edad = %s, curp = %s WHERE id = %s", (nombre, edad, curp, id))
    conexion.commit()
    print("Registro actualizado exitosamente.")
    conexion.close()

# Función para insertar un registro
def insertar_registro():
    conexion = conectar()
    db = conexion.cursor()
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    curp = input("Ingrese el CURP: ")
    db.execute("INSERT INTO personas (nombre, edad, curp) VALUES (%s, %s, %s)", (nombre, edad, curp))
    conexion.commit()
    print("Registro insertado exitosamente.")
    conexion.close()

# Función para eliminar un registro
def eliminar_registro():
    conexion = conectar()
    db = conexion.cursor()
    db.execute("SELECT * FROM personas")
    registros = db.fetchall()
    for registro in registros:
        print(registro) # Se pinta en pantalla los registros existentes para poder elegir cual eliminar

    id = input("Ingrese el ID del registro a eliminar: ")
    db.execute("DELETE FROM personas WHERE id = %s", (id,))
    conexion.commit()
    print("Registro eliminado exitosamente.")
    conexion.close()

# Función principal para ejecutar el programa
def ejecutar_programa():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            seleccionar_registros()
        elif opcion == "2":
            actualizar_registro()
        elif opcion == "3":
            insertar_registro()
        elif opcion == "4":
            eliminar_registro()
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Opcion invalida. Por favor, seleccione otra opcion.")

# Ejecutar el programa
ejecutar_programa()