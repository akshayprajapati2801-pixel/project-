from dao.login_dao import LoginDAO
from config.db import DBConnection

class LoginDAOImpl(LoginDAO):

    def login(self, username, password):

        connection = DBConnection.get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT *
        FROM admin
        WHERE username=%s
        AND password=%s
        """

        cursor.execute(query, (username, password))

        admin = cursor.fetchone()

        cursor.close()
        DBConnection.close_connection(connection)

        return admin