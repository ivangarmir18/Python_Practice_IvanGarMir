# Nuestros datos de entrenamiento
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

def entrenar_regresion_lineal(x, y, epocas=1000, tasa_aprendizaje=0.005):
    # 1. Inicializamos los pesos en 0
    m = 0.0
    b = 0.0

    for epoca in range(epocas):
        for xi, yi in zip(x, y):
            
            prediccion = m*xi + b
            error = yi - prediccion
            
            m = m + (error * xi * tasa_aprendizaje)
            b = b + (error * tasa_aprendizaje)   
    return m, b

# --- PRUEBA ---
m_final, b_final = entrenar_regresion_lineal(x, y)

print(f"La ecuación de la recta es: y = {m_final:.2f}x + {b_final:.2f}")

# Para comprobar si funciona, predecimos un valor nuevo. Si x=6, ¿cuánto valdrá y?
y_pred = m_final * 6 + b_final
print(f"Para x=6, la IA predice y={y_pred:.2f}")