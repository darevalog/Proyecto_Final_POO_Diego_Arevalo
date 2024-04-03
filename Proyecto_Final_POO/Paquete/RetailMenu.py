import os # Importamos la librería os
from Paquete.PMenu import * # Importamos la clase Menu del archivo PMenu.py

class RetailMenu(Menu): # Clase para mostrar el menú de webscrapping de una página de Retail
    def __init__(self): # Constructor de la clase
        super().__init__()

    def display_menu(self): # Método para mostrar el menú de webscrapping de una página de Retail
        os.system("cls")
        print("Seleccione una opción para realizar webscrapping de Mercado Libre:\n")
        print("1. Webscraping de Mercado Libre")
        print("2. Volver al menú principal\n")