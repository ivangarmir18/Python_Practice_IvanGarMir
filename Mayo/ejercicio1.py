import numpy as np

def extraer_energia_voz(audio_array, umbral_energia):
    tramos_validos = []
    estado_hablando = False
    
    for i in range(len(audio_array)):
        # Calculamos la suma de las 3 muestras actuales
        if i + 2 < len(audio_array):  # Aseguramos que no se salga del rango
            energia_ventana = audio_array[i] + audio_array[i+1] + audio_array[i+2]
            print(energia_ventana)
            if energia_ventana > umbral_energia:
                estado_hablando = True
                tramos_validos.append(round(energia_ventana,2))  # Guardamos la energía redondeada a 2 decimales
            else:
                estado_hablando = False
                
    return tramos_validos

# Datos de prueba simulados (7 muestras)
audio_test = [0.1, 0.2, 0.8, 0.9, 0.7, 0.1, 0.05]
resultado = extraer_energia_voz(audio_test, 1.5)

print("Tramos detectados:", resultado)