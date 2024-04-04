from Paquete.WebScraper import * # Importamos la clase WebScraper del archivo WebScraper.py

class RetailScraper(WebScraper): # Clase para hacer scraping de una página de Retail
    def __init__(self): # Constructor de la clase
        super().__init__()

    def scrape_mercado_libre(self): # Método para hacer scraping de Mercado Libre
        url = "https://listado.mercadolibre.com.co/supermercado/_Deal_cpg-ofertas_Discount_5-100#DEAL_ID=https://listado.mercadolibre.com.co/supermercado/_Deal_cpg-ofertas_Discount_5-100&S=landingHubsupermercado&V=11&T=CarouselDynamic-home&L=VER-MAS&deal_print_id=fd590720-f172-11ee-a697-af0b16b4eb58&c_id=carouseldynamic-home&c_element_order=undefined&c_campaign=VER-MAS&c_uid=fd590720-f172-11ee-a697-af0b16b4eb58" # URL de la página de Supermercado de Mercado Libre
        filename = "Supermercado de Mercado Libre.txt" # Nombre del archivo de salida 
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/_Deal_promociones-colombia-electrodomesticos_Discount_5-100#deal_print_id=f114a860-f173-11ee-aa91-ad3d36ff2bf5&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=f114a860-f173-11ee-aa91-ad3d36ff2bf5" # URL de la página de Electrodomésticos de Mercado Libre
        filename = "Electrodomésticos de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/carros.mercadolibre.com.co/" # URL de la página de Carros de Mercado Libre
        filename = "Carros de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_mle de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/_Deal_promociones-colombia-hogar_Discount_5-100#deal_print_id=7465c0f0-f174-11ee-b28a-f997347c76a9&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=7465c0f0-f174-11ee-b28a-f997347c76a9" # URL de la página de Hogar y muebles de Mercado Libre
        filename = "Hogar y muebles de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/_Deal_promociones-colombia-deportes_Discount_5-100#deal_print_id=acff7ff0-f174-11ee-8807-49fb07fef16a&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=acff7ff0-f174-11ee-8807-49fb07fef16a" # URL de la página de Deportes y fitness de Mercado Libre
        filename = "Deportes y fitness de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/_Deal_flagship-belleza#deal_print_id=c445c070-f174-11ee-8807-49fb07fef16a&c_id=header-normal&c_element_order=1&c_campaign=HEADER&c_uid=c445c070-f174-11ee-8807-49fb07fef16a" # URL de la página de Belleza y cuidado personal de Mercado Libre
        filename = "Belleza y cuidado personal de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/_Deal_promociones-colombia-acc-vehiculos_Discount_5-100#deal_print_id=f6b54800-f174-11ee-a7aa-3d3b4f79cb59&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=f6b54800-f174-11ee-a7aa-3d3b4f79cb59" # URL de la página de Accesorios para vehículos de Mercado Libre
        filename = "Accesorios para vehículos de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/_Deal_promociones-colombia-herramientas_Discount_5-100#deal_print_id=140e4050-f175-11ee-aa91-ad3d36ff2bf5&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=140e4050-f175-11ee-aa91-ad3d36ff2bf5" # URL de la página de Herramientas de Mercado Libre
        filename = "Herramientas de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/construccion/_Deal_promociones-colombia_Discount_5-100#deal_print_id=30633620-f175-11ee-a697-af0b16b4eb58&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=30633620-f175-11ee-a697-af0b16b4eb58" # URL de la página de Construcción de Mercado Libre
        filename = "Construcción de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/" # URL de la página de Apartamentos en venta de Mercado Libre
        filename = "Apartamentos en venta de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_mle de la clase WebScraper 

        url = "https://listado.mercadolibre.com.co/_Deal_promociones-colombia-juguetes_Discount_5-100#deal_print_id=2ac60700-f176-11ee-aa91-ad3d36ff2bf5&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=2ac60700-f176-11ee-aa91-ad3d36ff2bf5" # URL de la página de Juguetes de Mercado Libre
        filename = "Juguetes de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml

        url = "https://listado.mercadolibre.com.co/_Deal_lunes-bebes-2022#deal_print_id=3e2bd900-f176-11ee-a7aa-3d3b4f79cb59&c_id=header-normal&c_element_order=1&c_campaign=HEADER&c_uid=3e2bd900-f176-11ee-a7aa-3d3b4f79cb59" # URL de la página de Accesorios para bebés de Mercado Libre
        filename = "Accesorios para bebés de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml

        url = "https://listado.mercadolibre.com.co/_Container_cbt-always-on#DEAL_ID=MCO2638&S=landingHubalways-on-cbt&V=18&T=Button-normal&L=BOTVER-MAS&deal_print_id=e044ffb0-f175-11ee-9de2-dd782d5c452e&c_id=button-normal&c_element_order=1&c_campaign=BOTVER-MAS&c_uid=e044ffb0-f175-11ee-9de2-dd782d5c452e" # URL de la página de Compras internacionales de Mercado Libre
        filename = "Compras internacionales de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/_Container_moda-mas-venta--fs#deal_print_id=150a3710-f176-11ee-b28a-f997347c76a9&c_id=carousel&c_element_order=1&c_campaign=CARTOP-MAS-VENDIDOS&c_uid=150a3710-f176-11ee-b28a-f997347c76a9" # URL de la página de Moda más vendida de Mercado Libre
        filename = "Moda más vendida de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/salud-equipamiento-medico/_Tienda_all_BestSellers_YES#deal_print_id=b258f6e0-f195-11ee-9de2-dd782d5c452e&c_id=header-normal&c_element_order=1&c_campaign=SALUD_EQUIPAMIENTO_MEDICO&c_uid=b258f6e0-f195-11ee-9de2-dd782d5c452e" # URL de la página de Salud y equipamiento médico de Mercado Libre
        filename = "Salud y equipamiento médico de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/industrias-oficinas/equipamiento-oficinas/nuevo/_Tienda_all_BestSellers_YES#deal_print_id=c67b7a40-f176-11ee-b28a-f997347c76a9&c_id=header-normal&c_element_order=1&c_campaign=INDUSTRIAS_OFICINAS&c_uid=c67b7a40-f176-11ee-b28a-f997347c76a9" # URL de la página de Equipamiento de oficinas de Mercado Libre
        filename = "Equipamiento de oficinas de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper

        url = "https://listado.mercadolibre.com.co/servicios.mercadolibre.com.co/#deal_print_id=e006c8c0-f176-11ee-a7aa-3d3b4f79cb59&c_id=header-normal&c_element_order=1&c_campaign=TRACKING&c_uid=e006c8c0-f176-11ee-a7aa-3d3b4f79cb59" # URL de la página de Servicios de Mercado Libre
        filename = "Servicios de Mercado Libre.txt" # Nombre del archivo de salida
        self.scrape_website_ml(url, filename) # Llama al método scrape_website_ml de la clase WebScraper