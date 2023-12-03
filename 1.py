#Fatima Gómez Díaz
#951

#Desarrollar una clase llamada MySQLConnect que tenga como atributos: host, user, password, database. Debe crear sus métodos set y get (property, setters). Debe tener los siguientes métodos: conectar() : Debe conectarse a la base de datos usando los atributos, debe retornar el objeto de conexión. desconectar(): Debe desconectar la base de datos. No debe retornar nada. Investigar método close().

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

conexion = MySQLConnect(host="127.0.0.1", user="root", password="12345678", database="olimpiadas")
conexion.establecer_conexion()

conexion.cerrar_conexion()
