import requests # Instalación: pip install requests
from bs4 import BeautifulSoup # Instalación: pip install beautifulsoup4
import os # Importamos la librería os


class WebScraper: # Clase para hacer scraping de una página web
    def __init__(self): # Constructor de la clase
        pass
        
    def scrape_website_ml(self, url, filename):
        try:
            response = requests.get(url) # Hacer la petición y parsear el contenido HTML
            response.raise_for_status()  # Lanza una excepción para errores HTTP
            html_text = response.text # Obtiene el contenido HTML de la página
            soup = BeautifulSoup(html_text, 'lxml') # Crea un objeto BeautifulSoup

            products = soup.find_all('div', class_='poly-card__content')  # Encuentra todos los productos en la página

            with open(filename, 'a', encoding='utf-8') as file: # Abrir el archivo en modo de escritura
                for product in products: # Intentar obtener el precio y nombre del producto       
                    try:
                        product_price = product.find('span', class_='andes-money-amount__fraction').text.strip()  
                    except AttributeError:
                        product_price = 'Precio no disponible'
                    
                    try:
                        product_name = product.find('h2', class_='poly-box').text.strip()  
                    except AttributeError:
                        product_name = 'Nombre no disponible'
                    
                    text = f"{product_name} - $ {product_price}\n" # Crear la línea de texto para el archivo
                      
                    file.write(text) # Escribir la línea en el archivo
                    
            print(f"Datos guardados en {filename}")

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")
                
    def scrape_website(self, url, filename): # Método para hacer scraping de una página web
        page = requests.get(url) # Hace una petición a la página web
        content = page.text # Obtiene el contenido de la página web

        soup = BeautifulSoup(content, "lxml") # Crea un objeto BeautifulSoup

        text = soup.find("body").get_text() # Obtiene el texto de la página web

        with open(filename, "w", encoding="utf-8") as file:
            file.write(text) # Escribe el texto en un archivo .txt