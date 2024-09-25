from Paquete.WebScraper import WebScraper # Importamos la clase WebScraper del archivo WebScraper.py

class RetailScraper(WebScraper): # Clase para hacer scraping de una página de Retail
    def __init__(self): # Constructor de la clase
        super().__init__()

    def scrape_mercado_libre(self): # Método para hacer scraping de Mercado Libre
        urls_and_filenames = [
    ("https://listado.mercadolibre.com.co/_Deal_promociones-colombia-electrodomesticos_Discount_5-100#deal_print_id=f114a860-f173-11ee-aa91-ad3d36ff2bf5&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=f114a860-f173-11ee-aa91-ad3d36ff2bf5", 'Electrodomésticos_de_Mercado_Libre.txt'),
    ("https://carros.mercadolibre.com.co/", 'Carros_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/_Deal_promociones-colombia-hogar_Discount_5-100#deal_print_id=7465c0f0-f174-11ee-b28a-f997347c76a9&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=7465c0f0-f174-11ee-b28a-f997347c76a9", 'Hogar_y_muebles_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/_Deal_promociones-colombia-deportes_Discount_5-100#deal_print_id=acff7ff0-f174-11ee-8807-49fb07fef16a&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=acff7ff0-f174-11ee-8807-49fb07fef16a", 'Deportes_y_fitness_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/_Deal_flagship-belleza#deal_print_id=c445c070-f174-11ee-8807-49fb07fef16a&c_id=header-normal&c_element_order=1&c_campaign=HEADER&c_uid=c445c070-f174-11ee-8807-49fb07fef16a", 'Belleza_y_cuidado_personal_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/_Deal_promociones-colombia-acc-vehiculos_Discount_5-100#deal_print_id=f6b54800-f174-11ee-a7aa-3d3b4f79cb59&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=f6b54800-f174-11ee-a7aa-3d3b4f79cb59", 'Accesorios_para_vehiculos_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/_Deal_promociones-colombia-herramientas_Discount_5-100#deal_print_id=140e4050-f175-11ee-aa91-ad3d36ff2bf5&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=140e4050-f175-11ee-aa91-ad3d36ff2bf5", 'Herramientas_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/construccion/_Deal_promociones-colombia_Discount_5-100#deal_print_id=30633620-f175-11ee-a697-af0b16b4eb58&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=30633620-f175-11ee-a697-af0b16b4eb58", 'Construccion_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/inmuebles/apartamentos/venta/", 'Apartamentos_en_venta_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/_Deal_promociones-colombia-juguetes_Discount_5-100#deal_print_id=2ac60700-f176-11ee-aa91-ad3d36ff2bf5&c_id=carousel&c_element_order=1&c_campaign=OFERTAS-IMPERDIBLES&c_uid=2ac60700-f176-11ee-aa91-ad3d36ff2bf5", 'Juguetes_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/_Deal_lunes-bebes-2022#deal_print_id=3e2bd900-f176-11ee-a7aa-3d3b4f79cb59&c_id=header-normal&c_element_order=1&c_campaign=HEADER&c_uid=3e2bd900-f176-11ee-a7aa-3d3b4f79cb59", 'Accesorios_para_bebes_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/_Container_cbt-always-on#DEAL_ID=MCO2638&S=landingHubalways-on-cbt&V=18&T=Button-normal&L=BOTVER-MAS&deal_print_id=e044ffb0-f175-11ee-9de2-dd782d5c452e&c_id=button-normal&c_element_order=1&c_campaign=BOTVER-MAS&c_uid=e044ffb0-f175-11ee-9de2-dd782d5c452e", 'Compras_internacionales_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/_Container_moda-mas-venta--fs#deal_print_id=150a3710-f176-11ee-b28a-f997347c76a9&c_id=carousel&c_element_order=1&c_campaign=CARTOP-MAS-VENDIDOS&c_uid=150a3710-f176-11ee-b28a-f997347c76a9", 'Moda_mas_vendida_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/salud-equipamiento-medico/_Tienda_all_BestSellers_YES#deal_print_id=b258f6e0-f195-11ee-9de2-dd782d5c452e&c_id=header-normal&c_element_order=1&c_campaign=SALUD_EQUIPAMIENTO_MEDICO&c_uid=b258f6e0-f195-11ee-9de2-dd782d5c452e", 'Salud_y_equipamiento_medico_de_Mercado_Libre.txt'),
    ("https://listado.mercadolibre.com.co/industrias-oficinas/equipamiento-oficinas/nuevo/_Tienda_all_BestSellers_YES#deal_print_id=c67b7a40-f176-11ee-b28a-f997347c76a9&c_id=header-normal&c_element_order=1&c_campaign=INDUSTRIAS_OFICINAS&c_uid=c67b7a40-f176-11ee-b28a-f997347c76a9", 'Equipamiento_de_oficinas_de_Mercado_Libre.txt')
]

        for url, filename in urls_and_filenames: # Iterar sobre cada URL y archivo
            self.scrape_website_ml(url, filename)

    def scrape_exito(self): # Método para hacer scraping de Éxito
        urls_and_filenames = [
    ("https://www.exito.com/mercado/aseo-del-hogar", 'Productos_Supermercado_de_Exito.txt'),
]

        for url, filename in urls_and_filenames:
            self.scrape_website_ex(url, filename)

    def scrape_alkosto(self): # Método para hacer scraping de Falabella
        urls_and_filenames = [
    ("https://www.alkosto.com/computadores-tablet/c/BI_COMP_ALKOS", 'Computadores_y_Tablets_de_Alkosto.txt'),
]

        for url, filename in urls_and_filenames:
            self.scrape_website_alk(url, filename)
        
    def scrape_jumbo(self): # Método para hacer scraping de Jumbo
        urls_and_filenames = [
    ("https://www.tiendasjumbo.co/tecnologia/informatica?layout=list", 'Tecnología_de_Jumbo.txt')
]

        for url, filename in urls_and_filenames:
            self.scrape_website_jm(url, filename)