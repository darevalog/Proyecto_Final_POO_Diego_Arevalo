import os
from Paquete.PMenu import *

class WikiMenu(Menu):
    def __init__(self):
        super().__init__()

    def display_menu(self):
        os.system("cls")
        print("Seleccione una opción para realizar webscrapping de una wiki:\n")
        print("1. Webscraping de Wiki de Python")
        print("2. Webscraping de Wiki de Hipopótamos")
        print("3. Webscraping de Wiki de Historia de la Humanidad")
        print("4. Volver al menú principal\n")