import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote

class DescargadorEBAU:
    user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 OPR/130.0.0.0"}
    
    def __init__(self, url_base, carpeta_destino="Examenes_EBAU"):
        self.url_base = url_base
        self.url_base_dominio = "https://universitats.gva.es" 
        self.carpeta_destino = carpeta_destino
        if not os.path.exists(carpeta_destino): os.mkdir(carpeta_destino)

    def obtener_sopa_html(self, user_agent=user_agent):
        """Descarga el HTML de la página principal y lo parsea."""
        respuesta=requests.get(self.url_base, headers=user_agent)
        if respuesta.status_code!=200:
            raise Exception(f"Error de web ({respuesta.status_code}): intentelo de nuevo más tarde o comprueba la red y la url")
        html = respuesta.text
        return BeautifulSoup(html,"lxml")
    
    def extraer_enlaces_pdf(self, sopa):
        """Busca en el HTML todos los enlaces que apunten a un PDF."""
        listas_carpetas = sopa.find_all("li", class_="folder")
        enlaces_validos=[]
        for lista in listas_carpetas:
            if lista.find("span", string=lambda t: t and "Exámenes" in t):
                enlaces_validos.extend(lista.find_all("a"))
        return enlaces_validos

    def extraer_nombre(self, respuesta, url_pdf):
        """Extrae y limpia el nombre del archivo desde la URL o las cabeceras."""
        content_disp = respuesta.headers.get('Content-Disposition')
        if content_disp and 'filename=' in content_disp:
            import re
            nombre = re.findall('filename="?([^";]+)"?', content_disp)[0]
            return nombre
        url_limpia = url_pdf.split("?")[0]
        partes = url_limpia.split("/")
        nombre_segmento = [p for p in partes if ".pdf" in p.lower()]
        
        if nombre_segmento:
            return unquote(nombre_segmento[0].replace("+", " "))

        return url_limpia.split("/")[-1]

    def descargar_archivo(self, url_pdf):
        if not url_pdf.startswith("http"):
            url_pdf = urljoin(self.url_base_dominio, url_pdf)
        
        respuesta = requests.get(url_pdf, headers=self.user_agent)
        
        if respuesta.status_code == 200:
            nombre_archivo = self.extraer_nombre(respuesta, url_pdf)

            ruta_final = os.path.join(self.carpeta_destino, nombre_archivo)
            
            with open(ruta_final, "wb") as f:
                f.write(respuesta.content)
                print(f"Archivo {nombre_archivo} descargado. ")

    def ejecutar(self):
        """Orquestador principal del pipeline."""
        print(f"Iniciando escaneo en: {self.url_base}")
        sopa = self.obtener_sopa_html()
        enlaces = self.extraer_enlaces_pdf(sopa)
        for e in enlaces:
            url_relativa = e.get("href")
            if url_relativa: 
                self.descargar_archivo(url_relativa)

        

# --- ZONA DE PRUEBAS ---
# URL de ejemplo (puedes buscar una real de tu comunidad autónoma)
url_objetivo = "https://universitats.gva.es/es/informacio-guies-i-examens-proves-acces-cursos-anteriors/-/documentos/qtiDktTa9HRG/folder/389340111"

# Instanciamos y arrancamos
bot = DescargadorEBAU(url_objetivo, "EXAMENES_EBAU_2023")
bot.ejecutar()