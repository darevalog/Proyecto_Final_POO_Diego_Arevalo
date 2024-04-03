# Proyecto Final POO (Webscraping) // Diego Arévalo

## `1. Analisis del problema`

Se propuso construir una aplicación que emule un un sistema de webscrapping utilizando Python, por lo cual vamos a iniciar hablando acerca de algunas bibliotecas que serán necesarias para hacer peticiones a las páginas web que querramos scrapear.
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
