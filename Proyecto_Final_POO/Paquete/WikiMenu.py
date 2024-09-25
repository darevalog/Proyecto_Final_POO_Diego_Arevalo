import os # Importamos la librería os
from Paquete.PMenu import Menu # Importamos la clase Menu del archivo PMenu.py
from colorama import Fore, Style # Importamos las clases Fore y Style de la librería colorama

class WikiMenu(Menu): # Clase para mostrar el menú de webscrapping de una wiki
    def __init__(self): # Constructor de la clase
        super().__init__() # Llamamos al constructor de la clase padre

    def display_menu(self): # Método para mostrar el menú de webscrapping de una wiki
        os.system("cls") # Limpia la pantalla
        print(Fore.YELLOW + "Seleccione una opción para realizar webscrapping de una wiki:\n")
        print(Fore.GREEN + "1." + Fore.YELLOW + " Webscraping de Wiki de Python")
        print(Fore.GREEN + "2." + Fore.YELLOW + " Webscraping de Wiki de Hipopótamos")
        print(Fore.GREEN + "3." + Fore.YELLOW + " Webscraping de Wiki de Historia de la Humanidad")
        print(Fore.GREEN + "4." + Fore.RED + " Volver al menú principal\n" + Style.RESET_ALL)
