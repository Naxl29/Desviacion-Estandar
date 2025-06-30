from datetime import datetime
import numpy as np

class Desviacion:
    def __init__(self, datos: list):
        self.datos = datos
        self.media = float(np.mean(datos))
        self.desviacion_estandar = float(np.std(datos, ddof=1))  
        self.cantidad = len(datos)
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_insert_tuple(self):
        return (
            ",".join(map(str, self.datos)),  
            self.media,
            self.desviacion_estandar,
            self.cantidad,
            self.fecha
        )