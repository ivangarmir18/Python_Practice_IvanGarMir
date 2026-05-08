import os
from google import genai

# =====================================================================
# RETO 32: AUTOMATIZACIÓN DE REPOSITORIOS CON LLM
# =====================================================================

# 1. Configura tu API Key (Puedes conseguirla gratis en Google AI Studio)
# CUIDADO: En un entorno real esto va en un archivo .env, pero por hoy 
# la pondremos aquí.
API_KEY = "AIzaSyBrYjFSAvHSZ6JwNd5HGwwl8FmNgvRvSes"
client = genai.Client(api_key=API_KEY)

# Instanciamos el modelo básico y rápido

def resumir_codigo_llm(codigo_python):
    prompt = f"""Lee este código, y resume en 2 líneas un título para ponerle a cada ejercicio para que quede
    en el formato ejX_tus_2_palabras.py para poder buscarlos rápidamente, te inserto todo el código, 
    por favor, solo 2 palabras separadas por _ tipo 'hola_mundo' {codigo_python}. """

    respuesta = client.models.generate_content(model = 'gemini-2.0-flash', contents=prompt)
    resultado_limpio = respuesta.text.strip()
    return resultado_limpio

def formatear_nuevo_nombre(nombre_original, resumen):
    numero = nombre_original.replace("ejercicio", "").replace(".py", "")
    nuevo_formato = "ej" + numero + "_" + resumen + ".py"
    return nuevo_formato

def orquestador_renombrado(directorio_objetivo):
    archivos = os.listdir(directorio_objetivo)
    script_actual = os.path.basename(__file__)
    archivos_py = [i for i in archivos if i.endswith(".py") and i.startswith("ejercicio") and i != script_actual]

    for archivo in archivos_py:
        ruta_vieja = os.path.join(directorio_objetivo, archivo)
        with open(ruta_vieja, "r", encoding="utf-8") as f:
            contenido = f.read()
        resumen_llm = resumir_codigo_llm(contenido)
        ruta_nueva = formatear_nuevo_nombre(archivo, resumen_llm)
        os.rename(archivo, ruta_nueva)
        print(f" Cambiando {archivo} -> {ruta_nueva}")

# --- ZONA DE PRUEBAS ---
if __name__ == "__main__":
    carpeta_correcta = os.path.dirname(os.path.abspath(__file__))
    orquestador_renombrado(carpeta_correcta)