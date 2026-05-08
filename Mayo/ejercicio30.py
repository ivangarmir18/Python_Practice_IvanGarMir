import sqlite3
import math
import numpy as np
# --- SETUP: MOCK DE LA BASE DE DATOS (No tocar) ---
def preparar_bd_prueba():
    conexion = sqlite3.connect(":memory:")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE registro_errores (timestamp TEXT, coord_x REAL, coord_y REAL, esperado TEXT, detectado TEXT)")
    
    # Insertamos errores simulados (El "01" va a ser el que más falle a propósito)
    errores_mock = [
        ("T1", 0.1, 0.9, "00", "01"), ("T2", -0.2, 0.8, "01", "00"),
        ("T3", -0.5, -0.1, "01", "11"), ("T4", 0.9, -0.2, "10", "11"),
        ("T5", -0.1, 0.7, "01", "00"), ("T6", -0.3, 0.2, "01", "10")
    ]
    cursor.executemany("INSERT INTO registro_errores VALUES (?,?,?,?,?)", errores_mock)
    conexion.commit()
    return conexion

# Diccionario de posiciones ideales para tus cálculos
IDEALES = {"00": (1.0, 1.0), "01": (-1.0, 1.0), "11": (-1.0, -1.0), "10": (1.0, -1.0)}

# =====================================================================
# TU MISIÓN: COMPLETAR ESTAS 3 FUNCIONES
# =====================================================================

def d_euclideana(x1, x2, y1, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

def simbolo_con_mas_errores(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT esperado, COUNT(esperado) as total FROM registro_errores GROUP BY esperado ORDER BY total DESC LIMIT 1;")
    resultado = cursor.fetchone()
    return resultado


def calcular_desviacion_media(conexion, simbolo_peor, IDEALES = IDEALES):
    cursor = conexion.cursor()
    cursor.execute("SELECT coord_X, coord_y FROM registro_errores WHERE esperado = ?;", (simbolo_peor[0],))
    coordenadas = cursor.fetchall()
    ideales = IDEALES.get(simbolo_peor[0])
    distancias = []
    for coordenada in coordenadas:
        distancia = d_euclideana(ideales[0], coordenada[0], ideales[1], coordenada[1])
        distancias.append(distancia)

    media_distancias = np.mean(distancias)
    return media_distancias

def generar_reporte(conexion):
    simbolo_erroneo = simbolo_con_mas_errores(conexion)
    if simbolo_erroneo:
        desviacion_media = calcular_desviacion_media(conexion, simbolo_erroneo)
        print(f"ALERTA: El símbolo {simbolo_erroneo[0]} es el más inestable con {simbolo_erroneo[1]} fallos registrados.")
        print(f"Desviación media de su posición ideal: {round(desviacion_media, 2)} unidades.")


# =====================================================================
# ZONA DE PRUEBAS
# =====================================================================
if __name__ == "__main__":
    conn = preparar_bd_prueba()
    print("Iniciando análisis de anomalías...\n")
    generar_reporte(conn)
    
    conn.close()