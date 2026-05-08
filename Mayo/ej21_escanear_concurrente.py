import sqlite3
import time
import concurrent.futures
import random

# --- SIMULADOR DE INTERNET (No tocar) ---
def extraer_oferta_web(id_pagina):
    """Simula que el ordenador tarda 1 segundo en descargar la web."""
    time.sleep(1) 
    # Simulamos que a veces la web da error 404 y no devuelve nada
    if random.random() > 0.8: 
        return None 
    
    roles = ["Junior Data Scientist", "Backend Developer Python", "DevOps Engineer"]
    empresas = ["TechCorp", "DataDynamics", "CloudSys"]
    return {
        "id": id_pagina, 
        "titulo": random.choice(roles), 
        "empresa": random.choice(empresas)
    }
# ----------------------------------------

class RadarEmpleo:
    def __init__(self):
        self.conexion = sqlite3.connect(':memory:')
        self.cursor_db = self.conexion.cursor()
        self.cursor_db.execute("CREATE TABLE IF NOT EXISTS ofertas (id INTEGER PRIMARY KEY, titulo TEXT, empresa TEXT);")
        self.conexion.commit()

    def oferta_existe(self, id_oferta):
        resultado = self.cursor_db.execute("SELECT * FROM ofertas WHERE id = ?;", (id_oferta,)).fetchone()
        if resultado is not None:
            return True   
        else:
            return False

    def guardar_oferta(self, oferta):
        id = oferta.get("id")
        titulo = oferta.get("titulo")
        empresa = oferta.get("empresa")
        self.cursor_db.execute("INSERT INTO ofertas (id, titulo, empresa) VALUES (?, ?, ?);", (id, titulo, empresa))
        self.conexion.commit()
        return [id, titulo, empresa]

    def procesar_pagina(self, id_pagina):
        """Esta función procesa UNA sola página. Será ejecutada por los hilos."""
        datos = extraer_oferta_web(id_pagina)
        if not datos:
            return
        if self.oferta_existe(id_pagina):
            return
        else:
            datos_lista = self.guardar_oferta(datos)
            print(f"AÑADIDO: {datos_lista[1]} en {datos_lista[2]}")

    def escanear_secuencial(self, paginas):
        """Bucle tradicional (Lento)"""
        print("Iniciando escaneo secuencial...")
        inicio = time.time()
        for pag in paginas:
            self.procesar_pagina(pag)
        print(f"-> Tiempo secuencial: {time.time() - inicio:.2f} segundos\n")

    def escanear_concurrente(self, paginas):
        """Procesamiento en paralelo (Rápido)"""
        print("Iniciando escaneo concurrente...")
        inicio = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ejecutor:
            inicio = time.time()
            ejecutor.map(self.procesar_pagina, paginas)
        
        print(f"-> Tiempo concurrente: {time.time() - inicio:.2f} segundos\n")

# --- ORQUESTACIÓN Y PRUEBAS ---
lista_paginas = list(range(1, 11)) #IDs del 1 al 10

bot = RadarEmpleo()

# 1. Inyectamos a mano la oferta con ID 3 para simular que la vimos ayer
bot.conexion.cursor().execute("INSERT INTO ofertas VALUES (3, 'Junior Antiguo', 'ViejaCorp')")
bot.conexion.commit()

# 2. Probamos el método lento
bot.escanear_secuencial(lista_paginas)

# 3. Probamos el método rápido (Verás que el ID 3 no se vuelve a notificar, y que es 5 veces más rápido)
bot.escanear_concurrente(lista_paginas)