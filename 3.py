#Fatima Gómez Díaz
#951

#Desarrollar una clase llamada OlimpiadaMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre.
#Debe agregar los siguientes métodos:
#insertar(id, year): Método para insertar datos en la Tabla Olimpiada, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
##editar(year): Método para editar el año en la Tabla Olimpiada. Validar que el año no exista en la tabla.
#eliminar(id): Método para eliminar un elemento de la Tabla Olimpiada. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
#consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Olimpiada. Ejemplo: “id = 1” , “year > 1990”


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

class OlimpiadaMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, year):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT COUNT(*) FROM Olimpiada WHERE year = {year}")
                count = cursor.fetchone()[0]
                if count == 0:
                    cursor.execute(f"INSERT INTO Olimpiada (id, year) VALUES ({id}, {year})")
                    connection.commit()
                    print("Inserción exitosa")
                    return True
                else:
                    print("Error: El año ya existe en la tabla")
                    return False
        finally:
            self.cerrar_conexion()

    def editar(self, id, nuevo_year):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT COUNT(*) FROM Olimpiada WHERE year = {nuevo_year} AND id != {id}")
                count = cursor.fetchone()[0]
                if count == 0:
                    cursor.execute(f"UPDATE Olimpiada SET year = {nuevo_year} WHERE id = {id}")
                    connection.commit()
                    print("Edición exitosa")
                    return True
                else:
                    print("Error: El nuevo año ya existe en la tabla")
                    return False
        finally:
            self.cerrar_conexion()

    def eliminar(self, id):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM Olimpiada WHERE id = {id}")
                connection.commit()
                if cursor.rowcount > 0:
                    print("Eliminación exitosa")
                    return True
                else:
                    print("Error: No se encontró la olimpiada con el ID proporcionado")
                    return False
        finally:
            self.cerrar_conexion()

    def consultar(self, filtro):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(f"SELECT * FROM Olimpiada WHERE {filtro}")
                results = cursor.fetchall()
                return results
        finally:
            self.cerrar_conexion()


olimpiada_db = OlimpiadaMySQLconexion(host="127.0.0.1", user="root", password="12345678", database="olimpiadas")
olimpiada_db.insertar(1, 2024)
olimpiada_db.editar(1, 2025)
olimpiada_db.eliminar(1)
resultados = olimpiada_db.consultar("id = 2")
print(resultados)
