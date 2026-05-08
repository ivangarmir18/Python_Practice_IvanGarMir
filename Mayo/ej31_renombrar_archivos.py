import os
import ast
import re
from collections import Counter

# =====================================================================
# RETO 32: RENOMBRADO LOCAL EXTREMO (CERO APIs, CERO NUBE)
# =====================================================================

def generar_resumen_local(contenido):
    """
    Lee el código en local y extrae de qué va basándose en las funciones
    o las variables más repetidas.
    """
    # PLAN A: Intentar buscar nombres de funciones usando el compilador de Python
    try:
        arbol = ast.parse(contenido)
        funciones = [nodo.name for nodo in ast.walk(arbol) if isinstance(nodo, ast.FunctionDef)]
        
        if funciones:
            funcion_principal = max(funciones, key=len)
            palabras = funcion_principal.split('_')
            return "_".join(palabras[:2]).lower()
    except Exception:
        pass 

    stopwords = {'import', 'print', 'for', 'in', 'if', 'else', 'while', 'def', 'return', 
                 'numpy', 'np', 'from', 'range', 'len', 'append', 'true', 'false', 'list', 'math'}

    palabras = re.findall(r'[a-zA-Z]{4,}', contenido.lower())
    palabras_limpias = [p for p in palabras if p not in stopwords]

    if palabras_limpias:
        top_2 = [p[0] for p in Counter(palabras_limpias).most_common(2)]
        return "_".join(top_2)

    return "script_basico"


def formatear_nuevo_nombre(nombre_original, resumen):
    numero = nombre_original.replace("ejercicio", "").replace(".py", "")
    nuevo_formato = f"ej{numero}_{resumen}.py"
    return nuevo_formato


def orquestador_local(directorio_objetivo):
    archivos = os.listdir(directorio_objetivo)
    script_actual = os.path.basename(__file__)
    archivos_py = [i for i in archivos if i.endswith(".py") and i.startswith("ejercicio") and i != script_actual]

    if not archivos_py:
        print("No hay archivos 'ejercicioX.py' para procesar.")
        return

    print(f"Archivos encontrados: {len(archivos_py)}. Iniciando escaneo local ultrarrápido...")

    for archivo in archivos_py:
        ruta_vieja = os.path.join(directorio_objetivo, archivo)
        
        with open(ruta_vieja, "r", encoding="utf-8") as f:
            contenido = f.read()

        try:
            resumen = generar_resumen_local(contenido)
            nuevo_nombre = formatear_nuevo_nombre(archivo, resumen)

            ruta_nueva = os.path.join(directorio_objetivo, nuevo_nombre)
            
            os.rename(ruta_vieja, ruta_nueva)
            print(f"ÉXITO: {archivo} -> {nuevo_nombre}")
            
        except Exception as e:
            print(f"Error procesando {archivo}: {e}")

if __name__ == "__main__":
    carpeta_correcta = os.path.dirname(os.path.abspath(__file__))
    orquestador_local(carpeta_correcta)