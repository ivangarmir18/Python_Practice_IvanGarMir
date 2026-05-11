import numpy as np

def funcion_coste(A, b, enjambre):

    costes = np.dot(enjambre, A.T) - b
    return np.linalg.norm(costes, axis = 1)



def optimizador_pso(A, b, num_particulas=50, iteraciones=100):

    dimensiones = A.shape[1]
    c1 = 1.2
    c2 = 2

    X = np.random.uniform(-10, 10, (num_particulas, dimensiones))
    V = np.zeros_like(X)

    P_best = X.copy()
    record_personales = funcion_coste(A, b, X)

    G_best = P_best[np.argmin(record_personales)].copy()
    
    for i in range(iteraciones):
        w = 0.9 - (0.5 * (i / iteraciones))

        R1 = np.random.rand(num_particulas, dimensiones)
        R2 = np.random.rand(num_particulas, dimensiones)

        
        V = w * V + c1 * R1 * (P_best - X) + c2 * R2 * (G_best - X)

        v_max = 0.1
        V = np.clip(V, -v_max, v_max)

        X = X + V

        errores = funcion_coste(A, b, X)
        mascara = errores < record_personales

        record_personales[mascara] = errores[mascara]
        P_best[mascara] = X[mascara]

        indice_mejor_global = np.argmin(record_personales)
        G_best = P_best[indice_mejor_global].copy()
     
    return G_best


if __name__ == "__main__":
    np.random.seed(42)

    DIMENSIONES = 10

    A = np.random.rand(DIMENSIONES, DIMENSIONES) * 10

    x_real = np.random.uniform(-10, 10, DIMENSIONES)
    
    b = A @ x_real
    
    print(f"--- INICIANDO TEST DE ESTRÉS: SISTEMA {DIMENSIONES}x{DIMENSIONES} ---")
    print("El enjambre tiene que volar por un espacio de 10 dimensiones...")
    
    mejor_solucion = optimizador_pso(A, b, num_particulas=1000, iteraciones=1000)
    
    if mejor_solucion is not None:
        error_absoluto = np.linalg.norm(mejor_solucion - x_real)
        
        print(f"\nError de distancia a la solución real: {error_absoluto:.4f}")
        
        if error_absoluto < 1.0:
            print("\n✅ ¡BRUTAL! Tu algoritmo base es una bestia. Ha resuelto 30 dimensiones.")
        else:
            print("\n❌ EL ENJAMBRE SE HA PERDIDO EN EL ESPACIO.")
            print("Las partículas no han tenido inercia suficiente para llegar a los números negativos.")
            print("Para arreglarlo, tendrías que tocar los parámetros 'w', 'c1' o 'c2' dentro de tu función.")
    else:
        print("\nEjecuta el código para ver el resultado.")