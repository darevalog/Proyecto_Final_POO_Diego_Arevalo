import os
from colorama import Fore, Style

class Menu:
    def __init__(self):
        self.clear_screen()

    def clear_screen(self):
        os.system("cls")

    def display_menu(self):
        print(Style.BRIGHT + Fore.MAGENTA + "-------------- SISTEMA DE WEBSCRAPPING --------------" + Style.RESET_ALL)
        print(Fore.GREEN + "\n1." + Fore.YELLOW + " Webscraping de Wikis predeterminadas.")
        print(Fore.GREEN + "2." + Fore.YELLOW + " Webscraping de páginas de Retail.")
        print(Fore.GREEN + "3." + Fore.YELLOW + " Webscraping de páginas personalizadas.")
        print(Fore.GREEN + "4." + Fore.RED + " Salir\n" + Style.RESET_ALL)

    def get_option(self):
        return input(Fore.CYAN + "Ingrese una opción: " + Style.RESET_ALL)
