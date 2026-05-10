import numpy as np


def distancia_euclidea(x1, x2, y1, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def asignar_camiones(paquetes, camiones): 
    
    #con bucles for
    '''
    asignaciones = np.zeros(len(paquetes), dtype=int)
    x2 = camiones[:, 0]
    y2 = camiones[:, 1]
    for i, paquete in enumerate(paquetes):
        distancias = distancia_euclidea(paquete[0], x2, paquete[1], y2)
        asignaciones[i] = np.argmin(distancias)
    '''
    #con newaxis
    paquetes_nuevo = paquetes[:, np.newaxis]
    diferencias = paquetes_nuevo - camiones
    suma_cuadrados = np.sum(diferencias**2, axis=2)
    asignaciones = np.argmin(suma_cuadrados, axis=1)
    return asignaciones
   

if __name__ == "__main__":

    matriz_camiones = np.array([
        [0.0, 0.0],
        [10.0, 10.0],
        [10.0, -10.0]
    ])
    
    matriz_paquetes = np.array([
        [1.0, 1.0],
        [9.0, 9.0],
        [8.0, -9.0],
        [-5.0, 0.0],
        [15.0, 15.0]
    ])
    
    print("--- INICIANDO ASIGNACIÓN LOGÍSTICA ---")
    resultados = asignar_camiones(matriz_paquetes, matriz_camiones)
    
    print("\nResultados obtenidos:", resultados)
    
    esperado = np.array([0, 1, 2, 0, 1])
    
    if resultados is not None and np.array_equal(resultados, esperado):
        print("✅ ¡PRUEBA SUPERADA! Has asignado la flota perfectamente.")
    else:
        print(f"❌ FALLO. Se esperaba {esperado} pero se obtuvo {resultados}")