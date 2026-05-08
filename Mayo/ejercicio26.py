import numpy as np
from collections import Counter

# Formato: (Coordenada X, Coordenada Y, "Símbolo Digital")
datos_entrenamiento = [
    (0.8, 0.9, "00"), (1.1, 0.7, "00"), (0.9, 1.2, "00"),    # Cuadrante 1
    (-0.9, 0.8, "01"), (-1.2, 1.1, "01"), (-0.8, 1.0, "01"), # Cuadrante 2
    (-1.0, -1.0, "11"), (-0.8, -1.2, "11"), (-1.1, -0.9, "11"),# Cuadrante 3
    (1.0, -0.8, "10"), (1.2, -1.1, "10"), (0.9, -0.9, "10")  # Cuadrante 4
]

# Una señal que el receptor no tiene muy clara
nueva_senal = (-0.1, 0.8) 

def d_euclideana(x1, x2, y1, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

def knn_decodificador(historial, punto_nuevo, k=3):
    nuevo1, nuevo2 = punto_nuevo
    distancias = []
    for d in datos_entrenamiento:
        valor1, valor2, etiqueta = d
        distancia = d_euclideana(nuevo1, valor1, nuevo2, valor2)
        distancias.append((distancia, etiqueta))
    top_k = sorted(distancias)[:k]
    etiquetas = [tupla[1] for tupla in top_k]
    conteo = Counter(etiquetas)
    ganador = conteo.most_common(1)[0][0]
    return ganador
    



# --- PRUEBA ---
simbolo_recibido = knn_decodificador(datos_entrenamiento, nueva_senal, k=3)
print(f"La señal {nueva_senal} ha sido decodificada como: {simbolo_recibido}")