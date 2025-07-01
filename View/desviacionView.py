from colorama import Fore, Style
from tabulate import tabulate
import matplotlib.pyplot as plt

class DesviacionView:

    # Muestra el menú principal 
    @staticmethod
    def mostrar_menu():
        print(Fore.CYAN + "Menú de Desviación Estándar:" + Style.RESET_ALL)
        print("1. Crear manualmente")
        print("2. Lista predeterminada")
        print("3. Mostrar último cálculo")
        print("4. Mostrar todos los cálculos")
        print("5. Eliminar todos los cálculos")
        print("6. Salir")

    # Se solicita la cantidad de números a calcular
    @staticmethod
    def pedir_cantidad():
        try:
            cantidad = int(input(Fore.YELLOW + "Ingrese la cantidad de números a calcular: " + Style.RESET_ALL))
            return cantidad
        except ValueError:
            print(Fore.RED + "Error: Debe ingresar un número entero." + Style.RESET_ALL)
            return 0
    
    # Se solicita los números a calcular
    @staticmethod
    def pedir_numeros(cantidad):
        numeros = []
        for i in range(cantidad):
            while True:
                try:
                    numero = float(input(Fore.YELLOW + f"Ingrese el número {i + 1}: " + Style.RESET_ALL))
                    numeros.append(numero)
                    break
                except ValueError:
                    print(Fore.RED + "Error: Debe ingresar un número válido." + Style.RESET_ALL)
        return numeros

    # Muestra el cálculo que se realizó
    @staticmethod
    def mostrar_calculo(modelo):
        print(Fore.GREEN + "Cálculo realizado:" + Style.RESET_ALL)
        print(f"Datos: {modelo.datos}")
        print(f"Media: {modelo.media}")
        print(f"Desviación estándar: {modelo.desviacion_estandar}")
        print(f"Fecha: {modelo.fecha}")
    
    # Muestra el último cálculo guardado 
    @staticmethod
    def mostrar_resultado(fila):
        if fila:
            datos_lista = list(map(float, fila['datos'].split(',')))
            print (Fore.GREEN + "Último cálculo guardado:" + Style.RESET_ALL)
            print(f"Datos: {datos_lista}")
            print(f"Media: {fila['media']}")
            print(f"Desviación estándar: {fila['desviacion_estandar']}")
            print(f"Fecha: {fila['fecha']}")
        else:
            print(Fore.RED + "No hay resultados disponibles." + Style.RESET_ALL)
    
    # Muestra todos los cálculos guardados en la base de datos
    @staticmethod
    def mostrar_todos(filas):
        if filas:
            tabla = []
            for fila in filas:
                datos = fila['datos']
                media = round(fila['media'], 2)
                desviacion = round(fila['desviacion_estandar'], 2)
                cantidad = fila['cantidad']
                fecha = fila['fecha']
                tabla.append([datos, media, desviacion, cantidad, fecha])

            headers = ["Datos", "Media", "Desviación Estándar", "Cantidad", "Fecha"]
            print(Fore.CYAN + "Historial de Cálculos:" + Style.RESET_ALL)
            print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
        else:
            print(Fore.RED + "No hay resultados disponibles." + Style.RESET_ALL)
    
    # Pregunta al usuario si desea ver el gráfico de los datos
    @staticmethod
    def preguntar_grafico():
        respuesta = input(Fore.YELLOW + "¿Desea ver un gráfico de los datos? (s/n): " + Style.RESET_ALL).strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print(Fore.RED + "Respuesta no válida. Por favor, ingrese 's' o 'n'." + Style.RESET_ALL)
            return DesviacionView.preguntar_grafico()
    
    # Muestra el gráfico de los datos de desviación estándar
    @staticmethod
    def mostrar_grafico(datos, media, desviacion):
        plt.figure(figsize=(8, 5))
        plt.plot(datos, marker='o', label='Datos')
        plt.axhline(media, color='green', linestyle='--', label='Media')
        plt.title(f'Desviación Estándar: {round(desviacion, 2)}')
        plt.xlabel('Índice')
        plt.ylabel('Valor')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # Muestra un mensaje personalizado según el tipo
    @staticmethod
    def mostrar_mensaje(mensaje, tipo="info"):
        if tipo == "ok":
            print(Fore.RED + mensaje + Style.RESET_ALL)
        elif tipo == "error":
            print(Fore.RED + mensaje + Style.RESET_ALL)
        else:
            print(mensaje)

    # Preguntar si esta seguro de que quieren eliminar todos los cálculos
    @staticmethod
    def preguntar_eliminar():
        respuesta = input(Fore.YELLOW + "¿Está seguro de que desea eliminar todos los cálculos? (s/n): " + Style.RESET_ALL).strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print(Fore.RED + "Respuesta no válida. Por favor, ingrese 's' o 'n'." + Style.RESET_ALL)
            return DesviacionView.preguntar_eliminar()