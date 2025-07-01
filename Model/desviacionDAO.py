from Database.conexion import Database

class DesviacionDAO:
    def __init__(self):
        self.db = Database(host="localhost", user="root", password="", database="ds") 

    # Guarda un nuevo cálculo de desviación estándar
    def guardar(self, desviacion):
        query = """
            INSERT INTO estadisticas (datos, media, desviacion_estandar, cantidad, fecha)
            VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, desviacion.to_insert_tuple())

    # Obtiene el último cálculo guardado
    def obtener_ultimo(self):
        return self.db.fetch_one("SELECT * FROM estadisticas ORDER BY id DESC LIMIT 1")
    
    #obtiene todos los cálculos guardados en la base de datos
    def obtener_todos(self):
        return self.db.fetch_all("SELECT * FROM estadisticas ORDER BY id DESC")

    #elimina todos los cálculos guardados en la base de datos
    def eliminar_todos(self):
        return self.db.execute_query("DELETE FROM estadisticas")

