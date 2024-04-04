from Paquete.PMenu import * # Importamos la clase Menu del archivo PMenu.py
from Paquete.WikiScraper import * # Importamos la clase WikiScraper del archivo WikiScraper.py
from Paquete.RetailScraper import * # Importamos la clase RetailScraper del archivo RetailScraper.py
from Paquete.WikiMenu import * # Importamos la clase WikiMenu del archivo WikiMenu.py
from Paquete.RetailMenu import * # Importamos la clase RetailMenu del archivo RetailMenu.py
from Paquete.PersonalizedMenu import * # Importamos la clase PersonalizedMenu del archivo PersonalizedMenu.py


class Controller: # Clase para controlar el flujo de la aplicación
    def __init__(self): # Constructor de la clase
        self.wiki_scraper = WikiScraper() 
        self.retail_scraper = RetailScraper() 

    def run(self): # Método para ejecutar la aplicación
        menu = Menu() 
        wiki_menu = WikiMenu() 
        retail_menu = RetailMenu()
        personalized_menu = PersonalizedMenu()

        while True: # Ciclo para mostrar el menú principal
            menu.clear_screen() 
            menu.display_menu()
            option = menu.get_option() # Obtiene la opción seleccionada por el usuario

            if option == "1": # Si la opción es 1, se hará scraping de una wiki
                while True:
                    menu.clear_screen()
                    wiki_menu.display_menu()
                    option = wiki_menu.get_option()

                    if option == "1": # Si la opción es 1, se hará scraping de la wiki de Python
                        os.system("cls")
                        self.wiki_scraper.scrape_python_wiki()
                        print(Fore.GREEN + "Se ha creado un archivo .txt acerca de la wiki de Python.\n" + Style.RESET_ALL) 
                        os.system("pause")
                        os.system("cls")
                    elif option == "2": # Si la opción es 2, se hará scraping de la wiki de Hipopótamos
                        os.system("cls")
                        self.wiki_scraper.scrape_hipopotamos_wiki()
                        print(Fore.GREEN + "Se ha creado un archivo .txt acerca de la wiki de Hipopótamos.\n" + Style.RESET_ALL)
                        os.system("pause")
                        os.system("cls")
                    elif option == "3": # Si la opción es 3, se hará scraping de la wiki de la Historia de la Humanidad
                        os.system("cls")
                        self.wiki_scraper.scrape_historia_humanidad_wiki()
                        print(Fore.GREEN + "Se ha creado un archivo .txt acerca de la wiki de la Historia de la Humanidad.\n" + Style.RESET_ALL)
                        os.system("pause")
                        os.system("cls")
                    elif option == "4": # Si la opción es 4, se regresará al menú principal
                        break
                    else:
                        os.system("cls")
                        print(Fore.RED + "Opción inválida. Intente de nuevo.\n" + Style.RESET_ALL) # Si la opción no es válida, se mostrará un mensaje
                        os.system("pause")
                        os.system("cls")
            elif option == "2": # Si la opción es 2, se hará scraping páginas de retail
                while True:
                    menu.clear_screen()
                    retail_menu.display_menu()
                    option = retail_menu.get_option()

                    if option == "1": # Si la opción es 1, se hará scraping de Mercado Libre
                        os.system("cls")
                        self.retail_scraper.scrape_mercado_libre()
                        print(Fore.GREEN + "Se han creado varios archivos .txt acerca de productos de Mercado Libre.\n" + Style.RESET_ALL)
                        os.system("pause")
                        os.system("cls")
                    elif option == "2": # Si la opción es 2, volverá al menú principal
                        break
                    else:
                        os.system("cls")
                        print(Fore.RED + "Opción inválida. Intente de nuevo.\n" + Style.RESET_ALL) # Si la opción no es válida, se mostrará un mensaje
                        os.system("pause")
                        os.system("cls")
            elif option == "3": # Si la opción es 3, se hará scraping de una página personalizada
                while True:
                    menu.clear_screen()
                    personalized_menu.display_menu()
                    option = personalized_menu.get_option()

                    if option == "1": # Si la opción es 1, se hará scraping de una página personalizada
                        os.system("cls")
                        url = input(Fore.CYAN + "Ingrese la URL de la página: " + Style.RESET_ALL) # Se le pedirá al usuario que ingrese la URL de la página
                        os.system("cls")
                        self.wiki_scraper.scrape_website(url, "Página Personalizada.txt") # Se hará scraping de la página personalizada
                        print(Fore.GREEN + "Se ha creado un archivo .txt acerca de la página personalizada.\n" + Style.RESET_ALL) # Se mostrará un mensaje
                        os.system("pause")
                        os.system("cls")
                    elif option == "2": # Si la opción es 2, volverá al menú principal
                        break
                    else:
                        os.system("cls")
                        print(Fore.RED + "Opción inválida. Intente de nuevo.\n" + Style.RESET_ALL) # Si la opción no es válida, se mostrará un mensaje
                        os.system("pause")
                        os.system("cls")
            elif option == "4": # Si la opción es 4, se cerrará la aplicación
                os.system("cls")
                break
            else:
                os.system("cls")
                print(Fore.RED + "Opción inválida. Intente de nuevo.\n" + Style.RESET_ALL) # Si la opción no es válida, se mostrará un mensaje
                os.system("pause")
                os.system("cls")