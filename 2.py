#Fatima Gómez Díaz
#951

# Desarrollar una clase llamada PaisMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre.
# Debe agregar los siguientes métodos:
# insertar(id, nombre): Método para insertar datos en la Tabla Pais, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# editar(nombre): Método para editar el nombre en la Tabla País. Validar que nombre no exista en la tabla.
# eliminar(id): Método para eliminar un elemento de la Tabla País. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
# consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla País. Ejemplo: “id = 1” , “nombre like %A%”

import mysql.connector

class MySQLConnect:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None

    def establecer_conexion(self):
        try:
            self._connection = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            return self._connection
        except mysql.connector.Error as err:
            print(f"Error al establecer conexión: {err}")
            return None

    def cerrar_conexion(self):
        if self._connection:
            self._connection.close()
            print("Conexión cerrada")

class PaisMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, nombre):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT COUNT(*) FROM Pais WHERE nombre = '{nombre}'")
                count = cursor.fetchone()[0]
                if count == 0:
                    cursor.execute(f"INSERT INTO Pais (id, nombre) VALUES ({id}, '{nombre}')")
                    connection.commit()
                    print("Inserción exitosa")
                    return True
                else:
                    print("Error: El nombre ya existe en la tabla")
                    return False
        finally:
            self.cerrar_conexion()

    def editar(self, id, nuevo_nombre):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT COUNT(*) FROM Pais WHERE nombre = '{nuevo_nombre}' AND id != {id}")
                count = cursor.fetchone()[0]
                if count == 0:
                    cursor.execute(f"UPDATE Pais SET nombre = '{nuevo_nombre}' WHERE id = {id}")
                    connection.commit()
                    print("Edición exitosa")
                    return True
                else:
                    print("Error: El nuevo nombre ya existe en la tabla")
                    return False
        finally:
            self.cerrar_conexion()

    def eliminar(self, id):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM Pais WHERE id = {id}")
                connection.commit()
                if cursor.rowcount > 0:
                    print("Eliminación exitosa")
                    return True
                else:
                    print("Error: No se encontró el país con el ID proporcionado")
                    return False
        finally:
            self.cerrar_conexion()

    def consultar(self, filtro):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(f"SELECT * FROM Pais WHERE {filtro}")
                results = cursor.fetchall()
                return results
        finally:
            self.cerrar_conexion()


pais_db = PaisMySQLconexion(host="127.0.0.1", user="root", password="12345678", database="olimpiadas")
pais_db.insertar(1, "Argentina")
pais_db.editar(1, "NuevoNombre")
pais_db.eliminar(1)
resultados = pais_db.consultar("id = 2")
print(resultados)
