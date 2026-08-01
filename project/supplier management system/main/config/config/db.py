import mysql.connector
from mysql.connector import Error

class DBConnection:

    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="your_mysql_password",   # Change this
                database="supplier_management"
            )

            if connection.is_connected():
                return connection

        except Error as e:
            print("Database Connection Error:", e)
            return None

    @staticmethod
    def close_connection(connection):
        if connection is not None and connection.is_connected():
            connection.close()