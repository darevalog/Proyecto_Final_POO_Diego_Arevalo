from Paquete.WebScraper import * # Importamos la clase WebScraper del archivo WebScraper.py

class WikiScraper(WebScraper): # Clase para hacer scraping de una wiki
    def __init__(self): # Constructor de la clase
        super().__init__()

    def scrape_python_wiki(self): # Método para hacer scraping de la wiki de Python
        url = "https://aws.amazon.com/es/what-is/python/" # URL de la wiki de Python
        filename = "Wiki acerca de Python.txt" # Nombre del archivo de salida
        self.scrape_website(url, filename) # Llama al método scrape_website de la clase WebScraper

    def scrape_hipopotamos_wiki(self): # Método para hacer scraping de la wiki de Hipopótamos
        url = "https://www.oasysparquetematico.com/hipopotamos/amp/" # URL de la wiki de Hipopótamos
        filename = "Wiki acerca de Hipopótamos.txt" # Nombre del archivo de salida
        self.scrape_website(url, filename) # Llama al método scrape_website de la clase WebScraper

    def scrape_historia_humanidad_wiki(self): # Método para hacer scraping de la wiki de la Historia de la Humanidad
        url = "https://es.wikipedia.org/wiki/Historia_de_la_humanidad" # URL de la wiki de la Historia de la Humanidad
        filename = "Wiki acerca de la historia de la humanidad.txt" # Nombre del archivo de salida
        self.scrape_website(url, filename) # Llama al método scrape_website de la clase WebScraper