import os # Importamos la librería os
from Paquete.PMenu import * # Importamos la clase Menu del archivo PMenu.py

class PersonalizedMenu(Menu): # Clase para mostrar el menú de webscrapping de una página personalizada
    def __init__(self): # Constructor de la clase
        super().__init__()

    def display_menu(self): # Método para mostrar el menú de webscrapping de una página personalizada
        os.system("cls")
        print("Seleccione una opción para realizar webscrapping de una página personalizada:\n")
        print("1. Webscraping de Página Personalizada")
        print("2. Volver al menú principal\n")