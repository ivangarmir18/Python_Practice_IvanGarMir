import numpy as np
import matplotlib.pyplot as plt

# Funciones Ejercicio 32
def generar_bits(num_bits):
    return np.random.randint(0, 2, num_bits).astype(float)

def mapear_a_simbolos_nrz(bits, voltaje=1.0):
    return (bits * 2 - 1) * voltaje

def generar_forma_de_onda(simbolos, muestras_por_bit):
    return np.repeat(simbolos, muestras_por_bit)

# Nuevo
def aplicar_ruido_gaussiano(onda_limpia, desviacion_estandar=0.5):
    ruido = np.random.normal(0, desviacion_estandar, len(onda_limpia))
    onda_final = onda_limpia + ruido
    return onda_final

def receptor_muestreo(onda_recibida, muestras_por_bit):
    centros = np.arange(muestras_por_bit // 2, len(onda_recibida), muestras_por_bit)
    puntos_medios = onda_recibida[centros]
    voltajes = np.zeros_like(puntos_medios)
    voltajes[puntos_medios > 0] = 1.0
    return voltajes

# --- ZONA DE ORQUESTACIÓN Y PRUEBAS ---
if __name__ == "__main__":
    NUM_BITS = 1000
    MUESTRAS_POR_BIT = 100
    VOLTAJE_PICO = 1.0
    RUIDO_STD = 0.8 # Ruido deliberadamente alto para forzar algunos errores

    # 1. Transmisión
    bits_tx = generar_bits(NUM_BITS)
    simbolos_tx = mapear_a_simbolos_nrz(bits_tx, voltaje=VOLTAJE_PICO)
    onda_tx = generar_forma_de_onda(simbolos_tx, MUESTRAS_POR_BIT)

    # 2. Canal AWGN
    onda_rx = aplicar_ruido_gaussiano(onda_tx, desviacion_estandar=RUIDO_STD)

    # 3. Recepción
    bits_rx = receptor_muestreo(onda_rx, MUESTRAS_POR_BIT)

    # 4. Análisis de Rendimiento (Bit Error Rate - BER)
    if bits_rx is not None:
        errores = np.sum(bits_tx != bits_rx)
        tasa_error = errores / NUM_BITS
        print(f"--- REPORTE DEL SISTEMA ---")
        print(f"Bits transmitidos: {NUM_BITS}")
        print(f"Errores detectados: {errores}")
        print(f"Tasa de Error (BER): {tasa_error:.4f}")
        
        # Visualización de los primeros 5 bits
        plt.figure(figsize=(12, 4))
        plt.plot(onda_rx[:500], color='gray', alpha=0.7, label='Señal Recibida (Ruido AWGN)')
        plt.plot(onda_tx[:500], color='crimson', linewidth=2, label='Señal Transmitida Original')
        
        # Marcar los puntos de muestreo
        puntos_muestreo = np.arange(MUESTRAS_POR_BIT // 2, 500, MUESTRAS_POR_BIT)
        plt.scatter(puntos_muestreo, onda_rx[puntos_muestreo], color='blue', zorder=5, label='Instantes de Decisión')
        
        plt.title("Simulación de Transmisión (Primeros 5 bits)")
        plt.axhline(0, color='black', linewidth=1)
        plt.legend()
        plt.show()
    else:
        print("Esperando a que completes la función receptor_muestreo() para evaluar la señal.")