import numpy as np

def calcular_puntos(distancias):
    puntos = np.zeros(len(distancias), dtype=int)
    
    puntos[distancias < 10] = 100
    puntos[(distancias >= 10) & (distancias < 20)] = 50
    puntos[(distancias >= 20) & (distancias < 50)] = 10

    return puntos


if __name__ == "__main__":
    # Simulamos 8 lanzamientos de dardos con estas distancias al centro:
    tiros = np.array([5.2, 15.0, 45.8, 80.1, 9.9, 10.0, 25.4, 1.1])
    
    resultados = calcular_puntos(tiros)
    
    print("Distancias registradas:", tiros)
    print("Puntuación asignada:   ", resultados)
    
    # El resultado final DEBERÍA SER exactamente este:
    # [100,  50,  10,   0, 100,  50,  10, 100]