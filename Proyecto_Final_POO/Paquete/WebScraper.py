import requests # Instalación: pip install requests
from bs4 import BeautifulSoup # Instalación: pip install beautifulsoup4
import os # Importamos la librería os


class WebScraper: # Clase para hacer scraping de una página web
    def __init__(self): # Constructor de la clase
        pass
        
    def scrape_website_ml(self, url, filename): # Add 'self' and 'url' parameters
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        products = soup.find_all('div', class_='ui-search-result__content-wrapper')

        for product in products:
            product_price = product.find('span', class_='andes-money-amount__fraction').text
            product_name = product.find('h2', class_='ui-search-item__title').text

            text = product_name + " - " + "$ " + product_price + "\n"
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(text)
                
    def scrape_website(self, url, filename): # Método para hacer scraping de una página web
        page = requests.get(url) # Hace una petición a la página web
        content = page.text # Obtiene el contenido de la página web

        soup = BeautifulSoup(content, "lxml") # Crea un objeto BeautifulSoup

        text = soup.find("body").get_text() # Obtiene el texto de la página web

        with open(filename, "w", encoding="utf-8") as file:
            file.write(text) # Escribe el texto en un archivo .txt