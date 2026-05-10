import numpy as np

def calcular_siguiente_generacion(tablero):

    filas, columnas = tablero.shape
    tablero_nuevo = np.zeros_like(tablero)
    
    for i in range(filas):
        for j in range(columnas): 
            fila_inicio = max(0, i-1)
            fila_fin = min(filas, i+2)

            col_inicio = max(0, j-1)
            col_fin = min(columnas, j+2)
            ventana = tablero[fila_inicio:fila_fin, col_inicio:col_fin]
            total = np.sum(ventana)
            vecinos = total - tablero[i, j]
            if tablero[i, j] == 1:
                if vecinos == 2 or vecinos == 3:
                    tablero_nuevo[i, j] = 1
                else:
                    tablero_nuevo[i, j] = 0
            else:
                if vecinos == 3:
                    tablero_nuevo[i, j] = 1
    
    return tablero_nuevo

if __name__ == "__main__":
    tablero_inicial = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    
    print("--- TURNO 0 (Inicial) ---")
    print(tablero_inicial)
    
    tablero_turno_1 = calcular_siguiente_generacion(tablero_inicial)
    
    print("\n--- TURNO 1 (Calculado por ti) ---")
    if tablero_turno_1 is not None:
        print(tablero_turno_1)
    else:
        print("Esperando tu código...")
        
    esperado_turno_1 = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    
    if tablero_turno_1 is not None and np.array_equal(tablero_turno_1, esperado_turno_1):
        print("\n✅ ¡PRUEBA SUPERADA! Has domado la lógica de la cuadrícula y los bordes.")
    else:
        print("\n❌ FALLO. Los nacimientos y muertes no cuadran.")