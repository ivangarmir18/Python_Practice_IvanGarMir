import numpy as np
import matplotlib.pyplot as plt


def generar_bits(num_bits):
    bits = np.random.randint(0, 2, num_bits).astype(float)
    return bits


def mapear_a_simbolos_nrz(bits, voltaje=1.0):
    lista_voltajes = []
    simbolos = (bits * 2 - 1) * voltaje
    array_voltajes =np.array(lista_voltajes)
    return array_voltajes


def generar_forma_de_onda(simbolos, muestras_por_bit):
    return np.repeat(simbolos, muestras_por_bit)


if __name__ == "__main__":
    # --- ZONA DE ORQUESTACIÓN Y PRUEBAS ---
    
    # 1. Parámetros físicos del sistema
    NUM_BITS = 15
    MUESTRAS_POR_BIT = 100 # Frecuencia de muestreo / Tasa de bits
    VOLTAJE_PICO = 2.0     # Operaremos a +/- 2 Voltios
    
    # 2. Flujo de transmisión
    mis_bits = generar_bits(NUM_BITS)
    mis_simbolos = mapear_a_simbolos_nrz(mis_bits, voltaje=VOLTAJE_PICO)
    mi_onda = generar_forma_de_onda(mis_simbolos, MUESTRAS_POR_BIT)
    
    # 3. Análisis de Resultados (Solo visualización, no modificar)
    print(f"Bits originales: {mis_bits}")
    print(f"Símbolos NRZ:    {mis_simbolos}")
    
    # Comprobación de integridad
    if mi_onda is not None and len(mi_onda) == (NUM_BITS * MUESTRAS_POR_BIT):
        plt.figure(figsize=(12, 4))
        plt.plot(mi_onda, color='crimson', linewidth=2)
        plt.title("Onda Física a Transmitir (Código NRZ Polar)")
        plt.xlabel("Muestras (Resolución temporal)")
        plt.ylabel("Amplitud (Voltios)")
        
        # Líneas de referencia
        plt.axhline(0, color='black', linewidth=1)
        plt.axhline(VOLTAJE_PICO, color='gray', linestyle='--')
        plt.axhline(-VOLTAJE_PICO, color='gray', linestyle='--')
        plt.ylim(-VOLTAJE_PICO - 0.5, VOLTAJE_PICO + 0.5)
        plt.grid(True, alpha=0.3)
        plt.show()
    else:
        print("Error: La onda generada no tiene las dimensiones correctas.")