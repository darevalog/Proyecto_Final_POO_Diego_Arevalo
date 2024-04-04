import os # Importamos la librería os
from Paquete.PMenu import * # Importamos la clase Menu del archivo PMenu.py

class PersonalizedMenu(Menu): # Clase para mostrar el menú de webscrapping de una página personalizada
    def __init__(self): # Constructor de la clase
        super().__init__()

    def display_menu(self): # Método para mostrar el menú de webscrapping de una página personalizada
        os.system("cls")
        print(Fore.YELLOW + "Seleccione una opción para realizar webscrapping de una página personalizada:\n")
        print(Fore.GREEN + "1." + Fore.YELLOW + " Webscraping de Página Personalizada")
        print(Fore.GREEN + "2." + Fore.RED + " Volver al menú principal\n" + Style.RESET_ALL)