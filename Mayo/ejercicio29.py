import sqlite3
import random
from datetime import datetime, timedelta


def generar_flujo_datos(cantidad=250):
    """
    Genera un flujo de datos simulando lecturas continuas.
    Formato de cada lectura: (timestamp, coordenada_x, coordenada_y, simbolo_esperado)
    """
    random.seed(42)
    flujo = []
    tiempo_actual = datetime.fromisoformat("2026-05-08T10:00:00")
    
    # Cuadrantes ideales: 00(+,+), 01(-,+), 11(-,-), 10(+,-)
    ideales = {"00": (1, 1), "01": (-1, 1), "11": (-1, -1), "10": (1, -1)}
    
    for _ in range(cantidad):
        simbolo = random.choice(list(ideales.keys()))
        x_ideal, y_ideal = ideales[simbolo]
        
        # El 15% de las veces generamos un error severo (cae en otro cuadrante)
        if random.random() < 0.15:
            x_real = x_ideal * -0.2 + random.uniform(-0.5, 0.5)
            y_real = y_ideal * -0.2 + random.uniform(-0.5, 0.5)
        else:
            # Lectura normal con ruido aceptable
            x_real = x_ideal + random.uniform(-0.4, 0.4)
            y_real = y_ideal + random.uniform(-0.4, 0.4)
            
        flujo.append((tiempo_actual.isoformat(), round(x_real, 2), round(y_real, 2), simbolo))
        tiempo_actual += timedelta(milliseconds=10)
        
    return flujo

datos_entrada = generar_flujo_datos()


# =====================================================================
# TU MISIÓN EMPIEZA AQUÍ: COMPLETAR LAS 4 FUNCIONES VACÍAS
# =====================================================================

def inicializar_base_datos(conexion):
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS registro_errores (timestamp TEXT, coord_x REAL, coord_y REAL, esperado TEXT, detectado TEXT);")
    conexion.commit()

def decodificador_basico(x, y):
    if x>0:
        if y>=0: return "00" 
        else: return "10"
    else:
        if y>=0: return "01" 
        else: return "11"

def guardar_errores_lote(conexion, lote_errores):
    if not lote_errores:
        return
    conexion.cursor().executemany("INSERT INTO registro_errores (timestamp, coord_x, coord_y, esperado, detectado) VALUES (?,?,?,?,?)", (lote_errores))
    conexion.commit()


def procesar_flujo(datos, conexion, tamano_lote=50):
    errores_totales = 0
    for i in range(0, len(datos), tamano_lote):  
        lista_errores = []
        datos_lote = datos[i : i + tamano_lote]
        for dato in datos_lote:
            detectado = decodificador_basico(dato[1], dato[2])
            dato+=(detectado,)
            if detectado != dato[3]:
                lista_errores.append(dato)
        guardar_errores_lote(conexion, lista_errores)
        errores_totales += len(lista_errores)
    return errores_totales

# =====================================================================
# ZONA DE PRUEBAS (NO TOCAR LA LÓGICA, SOLO EJECUTAR PARA COMPROBAR)
# =====================================================================
if __name__ == "__main__":
    # 1. Creamos conexión en memoria (RAM)
    conn = sqlite3.connect(":memory:")
    
    # 2. Inicializamos las tablas
    inicializar_base_datos(conn)
    
    # 3. Arrancamos el procesamiento por lotes
    total_errores = procesar_flujo(datos_entrada, conn, tamano_lote=50)
    
    print(f"--- PROCESAMIENTO FINALIZADO ---")
    print(f"Total de señales procesadas: {len(datos_entrada)}")
    print(f"Total de anomalías detectadas: {total_errores}")
    
    # 4. Verificación en Base de Datos
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registro_errores LIMIT 5")
    muestras = cursor.fetchall()
    
    print("\nPrimeros 5 errores guardados en SQL:")
    for m in muestras:
        print(f"[{m[0]}] X:{m[1]:.2f} Y:{m[2]:.2f} | Esperaba: {m[3]} -> Detectó: {m[4]}")
        
    conn.close()