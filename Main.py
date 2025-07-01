from Model.desviacion import Desviacion
from Controller.desviacionController import DesviacionController
from View.desviacionView import DesviacionView

# Punto de entrada del programa
if __name__ == "__main__":
    vista = DesviacionView()
    controlador = DesviacionController(vista)
    controlador.ejecutar()
    
