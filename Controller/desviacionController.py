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
                self.predefinido()
            elif opcion == '3':
                self.mostrar_ultimo()
            elif opcion == '4':
                self.mostrar_todos()
            elif opcion == '5':
                resultados = self.dao.obtener_todos()
                if not resultados:
                    self.vista.mostrar_mensaje("No hay cálculos para eliminar.")
                else:
                    preguntar = self.vista.preguntar_eliminar()
                    if preguntar == True:
                        self.dao.eliminar_todos()
                        self.vista.mostrar_mensaje("Se eliminaron todos los cálculos.")
                    else:
                        self.vista.mostrar_mensaje("No se eliminaron los cálculos.")
            elif opcion == '6':
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

    def mostrar_todos(self):
        resultados = self.dao.obtener_todos()
        if resultados:
            for fila in resultados:
                self.vista.mostrar_resultados(fila)
        else:
            self.vista.mostrar_mensaje("No hay resultados disponibles.")
    
    def predefinido(self):
        speed= [86, 87, 88, 86, 87, 85, 86]
        desviacion = Desviacion(speed)
        self.dao.guardar(desviacion)
        self.vista.mostrar_calculo(desviacion)
         
        if self.vista.preguntar_grafico():
            self.vista.mostrar_grafico(desviacion.datos, desviacion.media, desviacion.desviacion_estandar)

        return desviacion
