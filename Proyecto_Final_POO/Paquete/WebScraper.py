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

    def scrape_website_ex(self, url, filename):
        try:
            response = requests.get(url) # Hacer la petición y parsear el contenido HTML
            response.raise_for_status()  # Lanza una excepción para errores HTTP
            html_text = response.text # Obtiene el contenido HTML de la página
            soup = BeautifulSoup(html_text, 'lxml') # Crea un objeto BeautifulSoup

            products = soup.find_all('div', class_='productCard_productInfo__yn2lK')  # Encuentra todos los productos en la página

            with open(filename, 'a', encoding='utf-8') as file: # Abrir el archivo en modo de escritura
                for product in products: # Intentar obtener el precio y nombre del producto       
                    try:
                        product_price = product.find('p', class_='ProductPrice_container__price__XmMWA').text.strip()  
                    except AttributeError:
                        product_price = 'Precio no disponible'
                    
                    try:
                        product_name = product.find('p', class_='styles_name__qQJiK').text.strip()  
                    except AttributeError:
                        product_name = 'Nombre no disponible'
                    
                    text = f"{product_name} - $ {product_price}\n" # Crear la línea de texto para el archivo
                      
                    file.write(text) # Escribir la línea en el archivo
                    
            print(f"Datos guardados en {filename}")

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")  

    def scrape_website_jm(self, url, filename):
        try:
            response = requests.get(url) # Hacer la petición y parsear el contenido HTML
            response.raise_for_status()  # Lanza una excepción para errores HTTP
            html_text = response.text # Obtiene el contenido HTML de la página
            soup = BeautifulSoup(html_text, 'lxml') # Crea un objeto BeautifulSoup

            products = soup.find_all('div', class_='flex mt0 mb0 pt0 pb0    justify-start vtex-flex-layout-0-x-flexRowContent vtex-flex-layout-0-x-flexRowContent--detailsproductDesktop items-stretch w-100')  # Encuentra todos los productos en la página

            with open(filename, 'a', encoding='utf-8') as file: # Abrir el archivo en modo de escritura
                for product in products: # Intentar obtener el precio y nombre del producto       
                    try:
                        product_price = product.find('div', class_='tiendasjumboqaio-jumbo-minicart-2-x-price').text.strip()  
                    except AttributeError:
                        product_price = 'Precio no disponible'
                    
                    try:
                        product_name = product.find('h3', class_='vtex-product-summary-2-x-productNameContainer vtex-product-summary-2-x-productNameContainer--nameListDesktop mv0 vtex-product-summary-2-x-nameWrapper vtex-product-summary-2-x-nameWrapper--nameListDesktop overflow-hidden c-on-base f5').text.strip()  
                    except AttributeError:
                        product_name = 'Nombre no disponible'
                    
                    text = f"{product_name} - $ {product_price}\n" # Crear la línea de texto para el archivo
                      
                    file.write(text) # Escribir la línea en el archivo
                    
            print(f"Datos guardados en {filename}")

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}") 

    def scrape_website_alk(self, url, filename):
        try:
            response = requests.get(url) # Hacer la petición y parsear el contenido HTML
            response.raise_for_status()  # Lanza una excepción para errores HTTP
            html_text = response.text # Obtiene el contenido HTML de la página
            soup = BeautifulSoup(html_text, 'lxml') # Crea un objeto BeautifulSoup

            products = soup.find_all('body', class_='page-cmsitem-00347107-algolia pageType-CategoryPage template-pages-category-algoliaCategoryPage smartedit-page-uid-cmsitem_00347107_algolia smartedit-page-uuid-eyJpdGVtSWQiOiJjbXNpdGVtXzAwMzQ3MTA3X2FsZ29saWEiLCJjYXRhbG9nSWQiOiJhbGtvc3RvQ29udGVudENhdGFsb2ciLCJjYXRhbG9nVmVyc2lvbiI6Ik9ubGluZSJ9 smartedit-catalog-version-uuid-alkostoContentCatalog/Online language-es site-alkosto js-sf-cmsitem_00347107_algolia')  # Encuentra todos los productos en la página

            with open(filename, 'a', encoding='utf-8') as file: # Abrir el archivo en modo de escritura
                for product in products: # Intentar obtener el precio y nombre del producto       
                    try:
                        product_price = product.find('span', class_='price').text.strip()  
                    except AttributeError:
                        product_price = 'Precio no disponible'
                    
                    try:
                        product_name = product.find('h3', class_='product__item__top__title js-algolia-product-click js-algolia-product-title').text.strip()  
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