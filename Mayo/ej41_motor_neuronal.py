import numpy as np

# =====================================================================
# RETO 41: DEEP LEARNING DESDE CERO (Forward Propagation)
# =====================================================================

def relu(Z):
    return np.maximum(Z,0)


def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))


def motor_inferencia(X, W1, b1, W2, b2):

    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

    return A2


if __name__ == "__main__":
    X = np.array([
        [120.0, 14.0, 1.0],  # Transacción Normal
        [4500.0, 3.0, 5.0],  # Sospechosa (Madrugada, alto monto, muchos intentos)
        [15.0, 18.0, 1.0],   # Normal
        [3200.0, 2.0, 4.0]   # Sospechosa
    ])
    
    W1 = np.array([
        [ 0.1, -0.2,  0.5,  0.0],
        [ 0.0,  0.8, -0.1,  0.3],
        [-0.5,  0.9,  0.2, -0.4]
    ])
    b1 = np.array([0.1, -0.1, 0.0, 0.2])
    
    W2 = np.array([
        [-0.8],
        [ 0.9],
        [-0.5],
        [ 0.6]
    ])
    b2 = np.array([-0.5])
    
    print("--- INICIANDO MOTOR DE IA ---")
    probabilidades = motor_inferencia(X, W1, b1, W2, b2)
    
    print("\nProbabilidades de fraude obtenidas:")
    if probabilidades is not None:
        for i, p in enumerate(probabilidades):
            print(f"Transacción {i+1}: {p[0]:.4f} -> {'¡ALERTA FRAUDE!' if p[0] > 0.5 else 'Normal'}")
    else:
        print("Completa la lógica para ver los resultados.")
        
    if probabilidades is not None:
        esperado_t2 = 1.0 
        if probabilidades[1][0] > 0.9:
            print("\n✅ ¡PRUEBA SUPERADA! Has programado el motor matemático de una Red Neuronal.")
        else:
            print("\n❌ FALLO. Los cálculos matriciales no coinciden.")