import numpy as np

# Generamos 1000 puntos. 
# Etiqueta 0 = Símbolo "00" (Normal, centrado en 1, 1)
# Etiqueta 1 = Símbolo "01" (Defectuoso, centrado en -0.6, 0.6)
np.random.seed(42)
X_binario = []
y_binario = []

for _ in range(1000):
    if np.random.rand() > 0.5:
        # Símbolo 00
        X_binario.append([1.0 + np.random.normal(0, 0.2), 1.0 + np.random.normal(0, 0.2)])
        y_binario.append(0)
    else:
        # Símbolo 01 (El problemático)
        X_binario.append([-0.6 + np.random.normal(0, 0.5), 0.6 + np.random.normal(0, 0.5)])
        y_binario.append(1)

X_entrenamiento = np.array(X_binario)
y_entrenamiento = np.array(y_binario)

# Los puntos ambiguos de tu receptor
X_prueba = np.array([
    [-0.1, 0.8],  
    [0.2, 0.5],   
    [1.1, 0.9]    
])

def entrenar_neurona(X, y, epocas=100, tasa_aprendizaje=0.01):
    w1, w2, b = 0.0, 0.0, 0.0
    for _ in range(epocas):
        for (xi, yi), yreal in zip(X, y):
            z = (xi * w1) + (yi * w2) + b
            p = 1 / (1 + np.exp(-z))
            error = yreal - p
            w1 = w1 + tasa_aprendizaje * error * xi
            w2 = w2 + tasa_aprendizaje * error * yi
            b = b + tasa_aprendizaje * error
    return w1, w2, b
        

def predecir_probabilidad(X_nuevos, w1, w2, b):
    probabilidad_defecto = []
    for xi, yi in X_nuevos:
        z = (xi * w1) + (yi * w2) + b
        p = 1 / (1 + np.exp(-z))
        probabilidad_defecto.append(round(p, 4))
    return probabilidad_defecto

w1_final, w2_final, b_final = entrenar_neurona(X_entrenamiento, y_entrenamiento)
probabilidades = predecir_probabilidad(X_prueba, w1_final, w2_final, b_final)
print(probabilidades)