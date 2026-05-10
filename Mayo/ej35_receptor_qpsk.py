import numpy as np
import matplotlib.pyplot as plt

def generar_bits(num_bits):
    return np.random.randint(0, 2, num_bits).astype(float)

def mapeador_qpsk(bits, voltaje=1.0):
    if len(bits) % 2 != 0:
        raise ValueError("El número de bits debe ser par")
    
    bits_I = bits[::2]
    bits_Q = bits[1::2]
    voltajes_I = (bits_I * 2 - 1) * voltaje
    voltajes_Q = (bits_Q * 2 - 1) * voltaje
    return voltajes_I + 1j * voltajes_Q


def aplicar_ruido_complejo(simbolos, std_dev):
    ruido_I = np.random.normal(0, std_dev, size=len(simbolos))
    ruido_Q = np.random.normal(0, std_dev, size=len(simbolos))
    ruido_complejo = (ruido_I + 1j * ruido_Q)
    return simbolos + ruido_complejo

def demapeador_qpsk(simbolos_rx):
    simbolos_I = simbolos_rx.real
    simbolos_Q = simbolos_rx.imag
    bits_recuperados = np.empty(len(simbolos_rx) * 2)
    bits_I = (simbolos_I > 0).astype(int)
    bits_Q = (simbolos_Q > 0).astype(int)
    bits_recuperados[0::2] = bits_I
    bits_recuperados[1::2] = bits_Q
    return bits_recuperados

# --- ORQUESTACIÓN Y ANÁLISIS ---
if __name__ == "__main__":
    NUM_BITS = 50000  # Subimos el volumen para ver bien la nube de ruido
    VOLTAJE = 1.0
    RUIDO_STD = 0.6   # Prueba a cambiar este valor luego (ej: 0.2, 0.9)
    
    # Transmisión
    bits_tx = generar_bits(NUM_BITS)
    simbolos_tx = mapeador_qpsk(bits_tx, VOLTAJE)
    
    # Canal
    simbolos_rx = aplicar_ruido_complejo(simbolos_tx, RUIDO_STD)
    
    # Recepción
    bits_rx = demapeador_qpsk(simbolos_rx)
    
    if bits_rx is not None:
        # Cálculo de Errores
        errores = np.sum(bits_tx != bits_rx)
        ber = errores / NUM_BITS
        print(f"Bits transmitidos: {NUM_BITS}")
        print(f"Errores: {errores}")
        print(f"BER: {ber:.4f}")
        
        # Ploteo de la constelación ruidosa (Solo mostramos 2000 para no saturar el gráfico)
        plt.figure(figsize=(7, 7))
        plt.scatter(simbolos_rx.real[:2000], simbolos_rx.imag[:2000], color='blue', alpha=0.3, marker='.', label='Símbolos Recibidos')
        plt.scatter(simbolos_tx.real[:4], simbolos_tx.imag[:4], color='red', marker='X', s=100, label='Ideales')
        
        plt.title(f"Constelación QPSK en Canal AWGN (Std: {RUIDO_STD})")
        plt.xlabel("I")
        plt.ylabel("Q")
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.grid(True, alpha=0.5)
        plt.legend()
        plt.xlim(-3, 3)
        plt.ylim(-3, 3)
        plt.show()
    else:
        print("Esperando la función del demapeador.")