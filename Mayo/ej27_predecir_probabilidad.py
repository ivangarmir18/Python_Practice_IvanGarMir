import numpy as np
from sklearn.ensemble import RandomForestClassifier
# Los 4 símbolos ideales de QPSK
simbolos_ideales = {"00": (1.0, 1.0), "01": (-1.0, 1.0), "11": (-1.0, -1.0), "10": (1.0, -1.0)}

np.random.seed(42)
X_historico = []
y_historico = []

for _ in range(5000):
    etiqueta = np.random.choice(list(simbolos_ideales.keys()))
    x_ideal, y_ideal = simbolos_ideales[etiqueta]
    
    if etiqueta == "01":
        x_ruido = x_ideal + np.random.normal(0.4, 0.5) 
        y_ruido = y_ideal + np.random.normal(-0.4, 0.5) 
    else:
        x_ruido = x_ideal + np.random.normal(0, 0.2) 
        y_ruido = y_ideal + np.random.normal(0, 0.2) 
        
    X_historico.append([x_ruido, y_ruido])
    y_historico.append(etiqueta)

X_historico = np.array(X_historico)
y_historico = np.array(y_historico)

modelo = RandomForestClassifier()
modelo.fit(X_historico, y_historico)

X_prueba = np.array([
    [-0.1, 0.8],
    [-0.2, 0.1],
    [0.1, 0.9]
])

probabilidades = modelo.predict_proba(X_prueba)
print(probabilidades)