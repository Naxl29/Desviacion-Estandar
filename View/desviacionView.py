from colorama import Fore, Style
from tabulate import tabulate

class DesviacionView:

    @staticmethod
    def mostrar_menu():
        print(Fore.CYAN + "Menú de Desviación Estándar:" + Style.RESET_ALL)
        print("1. Crear manualmente")
        print("2. Mostrar último cálculo")
        print("3. Salir")

    @staticmethod
    def pedir_cantidad():
        try:
            cantidad = int(input(Fore.YELLOW + "Ingrese la cantidad de números a calcular: " + Style.RESET_ALL))
            return cantidad
        except ValueError:
            print(Fore.RED + "Error: Debe ingresar un número entero." + Style.RESET_ALL)
            return 0
    
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
    
    
    