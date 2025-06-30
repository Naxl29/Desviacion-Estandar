from Database.conexion import Database

class DesviacionDAO:
    def __init__(self):
        self.db = Database(host="localhost", user="root", password="", database="ds") 

    def guardar(self, desviacion):
        query = """
            INSERT INTO desviacion_estandar (datos, media, desviacion_estandar, fecha)
            VALUES (%s, %s, %s, %s)
        """
        self.db.execute_query(query, desviacion.to_insert_tuple())

    def obtener_ultimo(self):
        return self.db.fetch_one("SELECT * FROM desviacion_estandar ORDER BY id DESC LIMIT 1")
