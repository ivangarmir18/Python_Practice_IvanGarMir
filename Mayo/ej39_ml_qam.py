import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def modula_16qam_manual(bits_fuente):
    bits_fuente = np.asarray(bits_fuente)
    a = 1 / np.sqrt(10)
    b0, b1, b2, b3 = bits_fuente[0::4], bits_fuente[1::4], bits_fuente[2::4], bits_fuente[3::4]
    I, Q = np.empty(len(bits_fuente) // 4), np.empty(len(bits_fuente) // 4)
    
    I[(b0 == 0) & (b1 == 0)] = 3
    I[(b0 == 0) & (b1 == 1)] = 1
    I[(b0 == 1) & (b1 == 1)] = -1
    I[(b0 == 1) & (b1 == 0)] = -3
    
    Q[(b2 == 0) & (b3 == 0)] = 3
    Q[(b2 == 0) & (b3 == 1)] = 1
    Q[(b2 == 1) & (b3 == 1)] = -1
    Q[(b2 == 1) & (b3 == 0)] = -3
    return (I + 1j * Q) * a

if __name__ == "__main__":
    np.random.seed(42)

    bits_entrenamiento = np.array([
        0,0,0,0,  0,0,0,1,  0,0,1,0,  0,0,1,1,
        0,1,0,0,  0,1,0,1,  0,1,1,0,  0,1,1,1,
        1,0,0,0,  1,0,0,1,  1,0,1,0,  1,0,1,1,
        1,1,0,0,  1,1,0,1,  1,1,1,0,  1,1,1,1
    ])

    simbolos_ideales = modula_16qam_manual(bits_entrenamiento)
    
    NUM_BITS_TEST = 40000
    bits_test = np.random.randint(0, 2, NUM_BITS_TEST)
    simbolos_test = modula_16qam_manual(bits_test)
    
    ruido = (np.random.randn(len(simbolos_test)) + 1j * np.random.randn(len(simbolos_test))) * 0.15
    simbolos_ruidosos = simbolos_test + ruido
    X_train = np.stack((simbolos_ideales.real, simbolos_ideales.imag), axis = 1)
    Y_train = bits_entrenamiento.reshape(16, 4)
    
    X_test = np.stack((simbolos_ruidosos.real, simbolos_ruidosos.imag), axis = 1)
    
    model = KNeighborsClassifier(n_neighbors=1, weights='uniform', metric='euclidean')
    train = model.fit(X_train, Y_train)
    prediccion_matrices = model.predict(X_test)

    bits_predichos = prediccion_matrices.flatten()
    
    if 'bits_predichos' in locals() and bits_predichos is not None:
        errores = np.sum(bits_test != bits_predichos)
        ber = errores / NUM_BITS_TEST
        print(f"Total de bits evaluados: {NUM_BITS_TEST}")
        print(f"Errores cometidos por KNN: {errores}")
        print(f"Tasa de Error (BER): {ber:.4f}")
    else:
        print("Completa la lógica de Scikit-Learn para ver el resultado.")