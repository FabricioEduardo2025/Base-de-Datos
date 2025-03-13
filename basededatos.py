import mysql.connector

# Función para conectarse a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Edu@rdo15",
        database="escuela"
    )

# Función para insertar un alumno
def insertar_alumno(cursor):
    nombre = input("Ingrese el nombre del alumno: ")
    num_control = input("Ingrese el número de control del alumno: ")
    cursor.execute("INSERT INTO alumnos (nombre, num_control) VALUES (%s, %s)", (nombre, num_control))
    print("Alumno insertado correctamente.")

# Función para consultar todos los alumnos
def consultar_alumnos(cursor):
    cursor.execute("SELECT * FROM alumnos")
    result = cursor.fetchall()
    if result:
        for row in result:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Número de Control: {row[2]}")
    else:
        print("No hay alumnos registrados.")

# Función para actualizar un alumno
def actualizar_alumno(cursor):
    id_alumno = input("Ingrese el ID del alumno a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    cursor.execute("UPDATE alumnos SET nombre = %s WHERE id = %s", (nuevo_nombre, id_alumno))
    print("Alumno actualizado correctamente.")

# Función para eliminar un alumno
def eliminar_alumno(cursor):
    id_alumno = input("Ingrese el ID del alumno a eliminar: ")
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id_alumno,))
    print("Alumno eliminado correctamente.")

# Menú principal
def menu():
    conn = conectar_db()
    cursor = conn.cursor()

    while True:
        print("\n--- Menú de opciones ---")
        print("1. Insertar un alumno")
        print("2. Consultar todos los alumnos")
        print("3. Actualizar un alumno")
        print("4. Eliminar un alumno")
        print("5. Salir")
        
        opcion = input("Elija una opción (1-5): ")

        if opcion == "1":
            insertar_alumno(cursor)
        elif opcion == "2":
            consultar_alumnos(cursor)
        elif opcion == "3":
            actualizar_alumno(cursor)
        elif opcion == "4":
            eliminar_alumno(cursor)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        conn.commit()  # Confirmar los cambios realizados

    cursor.close()
    conn.close()

# Ejecutar el menú
if __name__ == "__main__":
    menu()
