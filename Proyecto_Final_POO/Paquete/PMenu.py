import os

class Menu:
    def __init__(self):
        self.clear_screen()

    def clear_screen(self):
        os.system("cls")

    def display_menu(self):
        print("-------------- SISTEMA DE WEBSCRAPPING --------------\n")
        print("1. Webscraping de Wikis predeterminadas.")
        print("2. Webscraping de páginas de Retail.")
        print("3. Webscraping de páginas personalizadas.")
        print("4. Salir\n")

    def get_option(self):
        return input("Ingrese una opción: ")