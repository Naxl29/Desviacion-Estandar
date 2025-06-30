from datetime import datetime
import statistics

class Desviacion:
    def __init__(self, datos: list):
        self.datos = datos
        self.media = statistics.mean(datos)
        self.desviacion_estandar = statistics.stdev(datos)
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