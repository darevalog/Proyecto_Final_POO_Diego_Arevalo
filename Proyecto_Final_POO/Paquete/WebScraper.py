import requests # Instalación: pip install requests
from bs4 import BeautifulSoup # Instalación: pip install beautifulsoup4
import os # Importamos la librería os


class WebScraper: # Clase para hacer scraping de una página web
    def __init__(self): # Constructor de la clase
        pass
        
    def scrape_website_mle(self, url, filename): # Método para hacer scraping de la página web de MercadoLibre
        page = requests.get(url) # Hace una petición a la página web
        content = page.text # Obtiene el contenido de la página web

        soup = BeautifulSoup(content, "lxml") # Crea un objeto BeautifulSoup

        text = soup.find("section", class_="ui-search-results").get_text() # Obtiene el texto de la sección de la página web

        with open(filename, "w", encoding="utf-8") as file:
            file.write(text) # Escribe el texto en un archivo .txt

    def scrape_website_ml(self, url, filename): # Método para hacer scraping de la página web de MercadoLibre
        page = requests.get(url) # Hace una petición a la página web
        content = page.text # Obtiene el contenido de la página web

        soup = BeautifulSoup(content, "lxml") # Crea un objeto BeautifulSoup

        text = soup.find("section", class_="ui-search-results ui-search-results--without-disclaimer").get_text() # Obtiene el texto de la sección de la página web

        with open(filename, "w", encoding="utf-8") as file:
            file.write(text) # Escribe el texto en un archivo .txt

    def scrape_website(self, url, filename): # Método para hacer scraping de una página web
        page = requests.get(url) # Hace una petición a la página web
        content = page.text # Obtiene el contenido de la página web

        soup = BeautifulSoup(content, "lxml") # Crea un objeto BeautifulSoup

        text = soup.find("body").get_text() # Obtiene el texto de la página web

        with open(filename, "w", encoding="utf-8") as file:
            file.write(text) # Escribe el texto en un archivo .txt