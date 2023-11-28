import mysql.connector

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'juego',
    'raise_on_warnings': True
}

# Conectar a la base de datos
try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        cursor = connection.cursor()

        # Ejecutar una consulta
        query = "SELECT * FROM puntuacion"
        cursor.execute(query)

        # Obtener resultados
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except mysql.connector.Error as error:
    print("Error al conectarse a la base de datos:", error)

finally:
    # Cerrar la conexión
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada")
