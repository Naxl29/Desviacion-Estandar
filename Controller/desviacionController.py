from Model.desviacion import Desviacion
from Model.desviacionDAO import DesviacionDAO

class DesviacionController:
    def __init__(self, vista):
        self.vista = vista
        self.dao = DesviacionDAO()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                cantidad = self.vista.pedir_cantidad()
                if cantidad > 0:
                    numeros = self.vista.pedir_numeros(cantidad)
                    self.crear_manual(numeros)
            elif opcion == '2':
                self.mostrar_ultimo()
            elif opcion == '3':
                print("Saliendo del programa.")
                break
            else:
                self.vista.mostrar_mensaje("Error: Opción no válida. Intente de nuevo.")
    
    def crear_manual(self, lista):
        try:
            desviacion = Desviacion(lista)
            self.dao.guardar(desviacion)
            self.vista.mostrar_calculo(desviacion)

            if self.vista.preguntar_grafico():
                self.vista.mostrar_grafico(desviacion.datos, desviacion.media, desviacion.desviacion_estandar)

            return desviacion
        except Exception as e:
            print(f"Error al calcular desviación: {e}")
            return None
        
    def mostrar_ultimo(self):
        resultado = self.dao.obtener_ultimo()
        if resultado:
            self.vista.mostrar_resultado(resultado)
        else:
            self.vista.mostrar_mensaje("No hay resultados disponibles.")