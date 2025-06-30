from Model.desviacion import Desviacion
from Model.desviacionDAO import DesviacionDAO

class DesviacionController:
    def __init__(self):
        self.dao = DesviacionDAO()
    
    def crear_manual(self, lista):
        try:
            desviacion = Desviacion(lista)
            self.dao.guardar(desviacion)
            return desviacion
        except Exception as e:
            print(f"Error al calcular desviación: {e}")
            return None
        
    def mostrar_ultimo(self):
        return self.dao.obtener_ultimo()