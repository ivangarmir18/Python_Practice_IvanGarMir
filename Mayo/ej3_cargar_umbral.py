import json

def cargar_umbral_dtw():
    try:
        # 'with' gestiona la apertura y cierre automáticamente
        with open("config.json", "r") as archivo:
            diccionario_config = json.load(archivo) # Lee y parsea en un solo paso
            
        return diccionario_config["threshold_dtw"]
        
    except FileNotFoundError:
        return "Error: El archivo 'config.json' no existe."
    except json.JSONDecodeError:
        return "Error: El archivo 'config.json' tiene un formato JSON inválido."
    except KeyError:
        return "Error: No se encontró la clave 'threshold_dtw'."

# Prueba de ejecución
resultado = cargar_umbral_dtw()
print(f"Resultado: {resultado}")