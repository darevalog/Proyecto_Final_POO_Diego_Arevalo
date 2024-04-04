import os
from Paquete.PMenu import *

class WikiMenu(Menu):
    def __init__(self):
        super().__init__()

    def display_menu(self):
        os.system("cls")
        print(Fore.YELLOW + "Seleccione una opción para realizar webscrapping de una wiki:\n")
        print(Fore.GREEN + "1." + Fore.YELLOW + " Webscraping de Wiki de Python")
        print(Fore.GREEN + "2." + Fore.YELLOW + " Webscraping de Wiki de Hipopótamos")
        print(Fore.GREEN + "3." + Fore.YELLOW + " Webscraping de Wiki de Historia de la Humanidad")
        print(Fore.GREEN + "4." + Fore.RED + " Volver al menú principal\n" + Style.RESET_ALL)
