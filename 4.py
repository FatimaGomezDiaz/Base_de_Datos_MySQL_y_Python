#Fatima Gómez Díaz
#951

#Desarrollar una clase llamada ResultadosMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre.
#Debe agregar los siguientes métodos:
#insertar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Método para insertar datos en la Tabla Resultados, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
#editar(oro, plata, bronce): Método para editar oro, plata, bronce en la Tabla Resultados. Validar que sean valores enteros positivos.
#eliminar(idOlimpiada, idPais, idGenero): Método para eliminar un elemento de la Tabla Resultados. Debe tener como parámetro la llave primaria compuesta, retorna True si logró eliminarse y False en caso contrario.
#consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Resultados. Ejemplo: “idPais = 1” , “idPais = 1 and idOlimpiada=2”


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

class ResultadosMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor()
                # Insertar los resultados
                cursor.execute(
                    f"INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) "
                    f"VALUES ({idOlimpiada}, {idPais}, {idGenero}, {oro}, {plata}, {bronce})"
                )
                connection.commit()
                print("Inserción exitosa")
                return True
        finally:
            self.cerrar_conexion()

    def editar(self, idOlimpiada, idPais, idGenero, nuevo_oro, nuevo_plata, nuevo_bronce):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor()
                if nuevo_oro >= 0 and nuevo_plata >= 0 and nuevo_bronce >= 0:
                    cursor.execute(
                        f"UPDATE Resultados SET oro = {nuevo_oro}, plata = {nuevo_plata}, bronce = {nuevo_bronce} "
                        f"WHERE idOlimpiada = {idOlimpiada} AND idPais = {idPais} AND idGenero = {idGenero}"
                    )
                    connection.commit()
                    print("Edición exitosa")
                    return True
                else:
                    print("Error: Los valores deben ser enteros positivos")
                    return False
        finally:
            self.cerrar_conexion()

    def eliminar(self, idOlimpiada, idPais, idGenero):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor()
                cursor.execute(
                    f"DELETE FROM Resultados WHERE idOlimpiada = {idOlimpiada} "
                    f"AND idPais = {idPais} AND idGenero = {idGenero}"
                )
                connection.commit()
                if cursor.rowcount > 0:
                    print("Eliminación exitosa")
                    return True
                else:
                    print("Error: No se encontraron resultados con las llaves proporcionadas")
                    return False
        finally:
            self.cerrar_conexion()

    def consultar(self, filtro):
        try:
            connection = self.establecer_conexion()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(f"SELECT * FROM Resultados WHERE {filtro}")
                results = cursor.fetchall()
                return results
        finally:
            self.cerrar_conexion()

resultados_db = ResultadosMySQL(host="127.0.0.1", user="root", password="12345678", database="olimpiadas")
resultados_db.insertar(1, 1, 1, 5, 3, 2)
resultados_db.editar(1, 1, 1, 6, 4, 2)
resultados_db.eliminar(1, 1, 1)
resultados = resultados_db.consultar("idPais = 1")
print(resultados)
