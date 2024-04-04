import requests # Instalación: pip install requests
from bs4 import BeautifulSoup # Instalación: pip install beautifulsoup4
import os # Importamos la librería os


class WebScraper: # Clase para hacer scraping de una página web
    def __init__(self): # Constructor de la clase
        pass
        
    def scrape_website_ml(self, url, filename): # Método para hacer scraping de una página web de Mercado Libre
        html_text = requests.get(url).text # Hace una petición a la página web y obtiene el contenido de la página web
        soup = BeautifulSoup(html_text, 'lxml') # Crea un objeto BeautifulSoup
        products = soup.find_all('div', class_='ui-search-result__content-wrapper') # Obtiene todos los productos de la página web

        for product in products: # Recorre todos los productos de la página web
            product_price = product.find('span', class_='andes-money-amount__fraction').text # Obtiene el precio del producto
            product_name = product.find('h2', class_='ui-search-item__title').text # Obtiene el nombre del producto

            text = product_name + " - " + "$ " + product_price + "\n" # Concatena el nombre y el precio del producto
            with open(filename, 'a', encoding='utf-8') as file: # Abre el archivo .txt en modo de escritura
                file.write(text) # Escribe el texto en el archivo .txt
                
    def scrape_website(self, url, filename): # Método para hacer scraping de una página web
        page = requests.get(url) # Hace una petición a la página web
        content = page.text # Obtiene el contenido de la página web

        soup = BeautifulSoup(content, "lxml") # Crea un objeto BeautifulSoup

        text = soup.find("body").get_text() # Obtiene el texto de la página web

        with open(filename, "w", encoding="utf-8") as file:
            file.write(text) # Escribe el texto en un archivo .txt