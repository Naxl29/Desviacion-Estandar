from datetime import datetime
import numpy as np

class Desviacion:
    def __init__(self, datos: list):
        self.datos = datos      # Guarda la lista de números
        self.media = float(np.mean(datos))      # Calcula la media y la guarda como float
        self.desviacion_estandar = float(np.std(datos, ddof=1))        # Calcula y guarda la desviación estándar como float
        self.cantidad = len(datos)      # Guarda la cantidad de números de la lista
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Convierte los datos a un formato adecuado para insertar en la base de datos
    def to_insert_tuple(self):
        return (
            ",".join(map(str, self.datos)), # Convierte la lista de datos en un string
            self.media,
            self.desviacion_estandar,
            self.cantidad,
            self.fecha
        )