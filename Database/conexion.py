import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="ds"
            )
            self.cursor = self.connection.cursor(dictrionary=True)
            self.create_database(database)
            self.connection.database = database
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
        
    def create_database(self, database):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        self.cursor.execute(f"USE {database}")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS desviacion_estandar (
                id INT AUTO_INCREMENT PRIMARY KEY,
                datos VARCHAR(100) NOT NULL,
                media FLOAT NOT NULL,
                desviacion_estandar FLOAT NOT NULL,
                fecha DATETIME NOT NULL
                );
            """)
        self.connection.commit()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()