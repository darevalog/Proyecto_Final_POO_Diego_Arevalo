# Proyecto Final POO (Webscraping) // Diego Arévalo

## `1. Analisis del problema`

Se propuso construir una aplicación que emule un un sistema de webs crapping utilizando Python, por lo cual vamos a iniciar hablando acerca de algunas bibliotecas que serán necesarias para hacer peticiones a las páginas web que querramos scrapear.
Lo que se buscará hacer es mediante estas bibliotecas y algo de conocimiento de HTML, una vez proporcionado un link, analizar el código fuente de la página para utilizar los identificadores de HTML para requerir todos aquellos objetos con esa misma identificación.

### *`Biblioteca "requests":`*
Es una biblioteca de software libre que permite realizar solicitudes HTTP de manera sencilla y eficiente. Con esta biblioteca, puedes enviar solicitudes a servidores web y recibir respuestas. Es ampliamente utilizada en el desarrollo web y en tareas de scraping (extracción de datos de sitios web), así como en aplicaciones que requieren comunicación con servidores a través de HTTP. 

Para utilizar la biblioteca "requests", primero debes instalarla mediante pip, el gestor de paquetes de Python, utilizando el siguiente comando en tu terminal:

```python
pip install requests
```

Una vez instalada, puedes comenzar a utilizarla en tu código Python importándola de la siguiente manera:

```python
import requests
```
A partir de ahí, podremos utilizar las funciones y métodos proporcionados por la biblioteca "requests" para interactuar con servidores web de manera fácil y efectiva.

### *`Biblioteca "bs4":`* 
La librería bs4 en Python se refiere a Beautiful Soup 4, que es una biblioteca de análisis HTML y XML. Es una herramienta útil para extraer información de páginas web y manipular datos en formatos HTML y XML de una manera sencilla y eficiente. La biblioteca bs4 es popular entre los desarrolladores web y los científicos de datos que necesitan extraer datos de páginas web para análisis y procesamiento posterior. Es una herramienta flexible y poderosa que facilita el trabajo con datos web en Python.

Para utilizar la biblioteca "bs4", primero debes instalarla mediante pip, el gestor de paquetes de Python, utilizando el siguiente comando en tu terminal:

```python
pip install beautifulsoup4
```

Una vez instalada, puedes comenzar a utilizarla en tu código Python importándola de la siguiente manera ya que utilizaremos una libreria dentro de esta biblioteca:

```python
from bs4 import BeautifulSoup
```

Además de instalar la librería, es posible que también necesites instalar un analizador HTML para que Beautiful Soup pueda analizar el código HTML, el cual se instala de la siguinete manera: 

```python
pip install lxml
```

## `2. Manejo del problema`
Una vez que hayamos instalado estas bibliotecas crearemos una carpeta llamda "Proyecto_Final_POO" la cual alojará todos nuestros archivos y estará compuesta de la siguiente manera:

```
/Proyecto_Final_POO/
├── paquete/
│   ├── __init__.py
│   ├── Controller.py
│   ├── PersonalizedMenu.py
│   ├── PMenu.py
│   ├── RetailMenu.py
│   ├── RetailScraper.py
│   ├── WebScraper.py
│   ├── WikiMenu.py
│   └── WikiScraper.py
└── main.py
```

La carperta paquete contiene algunos módulos que a su vez contienen clases, las cuales heredad algunos atributos de estos mismo módulos, lo cual se representa de mejor manera en el siguiente diagrama UML: 
```mermaid
classDiagram
    Main <.. Controler
    Controler <.. PMenu
    Controler <.. WebScraper
    PMenu <|-- WikiMenu
    PMenu <|-- RetailMenu
    PMenu <|-- PersonalizedMenu
    WebScraper <|-- WikiScraper
    WebScraper <|-- RetailScraper
    class Controler{
      +self
      +__init__(self)
      +run(self)
    }
    class PMenu{
        +self
        +__init__(self)
        +display_menu(self)
        +get_option(self)
    }
    class WikiMenu{
        +self
        +super().__init__()
        +display_menu(self)
    }
    class RetailMenu{
        +self
        +super().__init__()
        +display_menu(self)
    }
    class PersonalizedMenu{
        +self
        +super().__init__()
        +display_menu(self)
    }
    class WebScraper{
        +self
        +url
        +filename
        +__init__(self)
        +scrape_website_mle(self, url, filename)
        +scrape_website_ml(self, url, filename)
        +scrape_website(self, url, filename)
    }
    class WikiScraper{
        +self
        +super().__init__()
        +scrape_python_wiki(self)
        +scrape_hipopotamos_wiki(self)
        +scrape_historia_humanidad_wiki(self)
    }
    class RetailScraper{
        +self
        +super().__init__()
        +scrape_mercado_libre(self)
    }
```

El contenido y la función de cada módulo son los siguientes: 

### *`__init__.py`*
El archivo __init__.py en un módulo de Python es un archivo especial que se utiliza para indicar que el directorio que lo contiene debe ser tratado como un paquete. Estos archivos también pueden contener código Python que se ejecutará cuando el paquete sea importado por primera vez.

### *`Controller.py`*
Este archivo se encarga de importar todos los demás módulos y empaquetarlos para facilitar la interacción del usuario con el archivo main.py.

```python
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
                        print("Se ha creado un archivo .txt acerca de la wiki de Python.\n") 
                        os.system("pause")
                        os.system("cls")
                    elif option == "2": # Si la opción es 2, se hará scraping de la wiki de Hipopótamos
                        os.system("cls")
                        self.wiki_scraper.scrape_hipopotamos_wiki()
                        print("Se ha creado un archivo .txt acerca de la wiki de Hipopótamos.\n")
                        os.system("pause")
                        os.system("cls")
                    elif option == "3": # Si la opción es 3, se hará scraping de la wiki de la Historia de la Humanidad
                        os.system("cls")
                        self.wiki_scraper.scrape_historia_humanidad_wiki()
                        print("Se ha creado un archivo .txt acerca de la wiki de la Historia de la Humanidad.\n")
                        os.system("pause")
                        os.system("cls")
                    elif option == "4": # Si la opción es 4, se regresará al menú principal
                        break
                    else:
                        os.system("cls")
                        print("Opción inválida. Intente de nuevo.\n") # Si la opción no es válida, se mostrará un mensaje
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
                        print("Se han creado varios archivos .txt acerca de productos de Mercado Libre.\n")
                        os.system("pause")
                        os.system("cls")
                    elif option == "2": # Si la opción es 2, volverá al menú principal
                        break
                    else:
                        os.system("cls")
                        print("Opción inválida. Intente de nuevo.\n") # Si la opción no es válida, se mostrará un mensaje
                        os.system("pause")
                        os.system("cls")
            elif option == "3": # Si la opción es 3, se hará scraping de una página personalizada
                while True:
                    menu.clear_screen()
                    personalized_menu.display_menu()
                    option = personalized_menu.get_option()

                    if option == "1": # Si la opción es 1, se hará scraping de una página personalizada
                        os.system("cls")
                        url = input("Ingrese la URL de la página: ") # Se le pedirá al usuario que ingrese la URL de la página
                        os.system("cls")
                        self.wiki_scraper.scrape_website(url, "Página Personalizada.txt") # Se hará scraping de la página personalizada
                        print("Se ha creado un archivo .txt acerca de la página personalizada.\n") # Se mostrará un mensaje
                        os.system("pause")
                        os.system("cls")
                    elif option == "2": # Si la opción es 2, volverá al menú principal
                        break
                    else:
                        os.system("cls")
                        print("Opción inválida. Intente de nuevo.\n") # Si la opción no es válida, se mostrará un mensaje
                        os.system("pause")
                        os.system("cls")
            elif option == "4": # Si la opción es 4, se cerrará la aplicación
                os.system("cls")
                break
            else:
                os.system("cls")
                print("Opción inválida. Intente de nuevo.\n") # Si la opción no es válida, se mostrará un mensaje
                os.system("pause")
                os.system("cls")
```
### *`PMenu.py`*
Este archivo se encarga de la creación del menú inicial con el cual el usuario va a interactuar, ademas crea algunas funciones que luego serán heredadas por WikiMenu, RetailMenu y PersonalizedMenu.
```python
import os # Importamos la librería os

class Menu: # Clase para mostrar el menú principal
    def __init__(self): # Constructor de la clase
        self.clear_screen()

    def clear_screen(self): # Método para limpiar la pantalla
        os.system("cls")

    def display_menu(self): # Método para mostrar el menú principal
        print("-------------- SISTEMA DE WEBSCRAPPING --------------\n")
        print("1. Webscraping de Wikis predeterminadas.")
        print("2. Webscraping de páginas de Retail.")
        print("3. Webscraping de páginas personalizadas.")
        print("4. Salir\n")

    def get_option(self): # Método para obtener la opción seleccionada por el usuario
        return input("Ingrese una opción: ")
```

### *`WikiMenu.py`*
Este archivo se encarga de la creación del menú de interacción para hacer web scrapin de una web de tipo wiki y dará algunas opciones predeterminadas las cuales el usuario podrá elegir, este archivo hereda funciones de Pmenu.

```python
import os # Importamos la librería os
from Paquete.PMenu import * # Importamos la clase Menu del archivo PMenu.py

class WikiMenu(Menu): # Clase para mostrar el menú de webscrapping de una wiki
    def __init__(self): # Constructor de la clase
        super().__init__()

    def display_menu(self): # Método para mostrar el menú de webscrapping de una wiki
        os.system("cls")
        print("Seleccione una opción para realizar webscrapping de una wiki:\n")
        print("1. Webscraping de Wiki de Python")
        print("2. Webscraping de Wiki de Hipopótamos")
        print("3. Webscraping de Wiki de Historia de la Humanidad")
        print("4. Volver al menú principal\n")
```

### *`RetailMenu`*
Este archivo se encarga de la creación del menú de interacción para hacer web scrapin de una web de tipo retail y dará algunas opciones predeterminadas las cuales el usuario podrá elegir, este archivo hereda funciones de Pmenu.

```python
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
```

### *`PersonalizedMenu`*

Este archivo se encarga de la creación del menú de interacción para hacer web scrapin de una web que el usuario escoja y para ello le pedirá la introducción del link de la página la cual desea scrapear, este archivo hereda funciones de Pmenu.

```python
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
```
