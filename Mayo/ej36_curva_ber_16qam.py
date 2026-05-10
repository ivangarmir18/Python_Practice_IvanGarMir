import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# RETO 36: SIMULADOR DE CURVA BER PARA 16-QAM (Basado en P3-Entrega)
# =====================================================================

def modula_16qam(bits_fuente):
    a = 1 / np.sqrt(10)
    mapping_4pam = {(0, 0): 3*a, (0, 1): 1*a, (1, 1): -1*a, (1, 0): -3*a}
    
    bits_agrupados = np.reshape(bits_fuente, (-1, 4))
    simbolos = []
    for fila in bits_agrupados:
        bits_I = tuple(fila[:2])
        bits_Q = tuple(fila[2:])
        simbolo = mapping_4pam[bits_I] + 1j * mapping_4pam[bits_Q]
        simbolos.append(simbolo)
    return np.array(simbolos)

# --- TU MISIÓN: COMPLETAR ESTAS DOS FUNCIONES ---

def canal_awgn_ebn0(x, EbN0_dB, M):
    k = np.log2(M)
    snr_db = EbN0_dB + 10 * np.log10(k)
    potencia_senal = np.mean(np.abs(x) ** 2)
    snr_lineal = 10 ** (snr_db / 10)
    potencia_ruido = potencia_senal / snr_lineal
    
    ruido_real = np.random.standard_normal(len(x)) * np.sqrt(potencia_ruido / 2)
    ruido_imag = np.random.standard_normal(len(x)) * np.sqrt(potencia_ruido / 2)
    
    canal_awgn = x + (ruido_real + 1j * ruido_imag)
    
    return canal_awgn

def demapeador_16qam(y_16QAM):
    a = 1 / np.sqrt(10)
    bits_rx_I = y_16QAM.real
    bits_rx_Q = y_16QAM.imag
    bits_rx = np.empty(len(y_16QAM) * 4, dtype=int)
    
    mI1 = (bits_rx_I >= 2 * a)
    mI2 = (bits_rx_I < 2 * a) & (bits_rx_I >= 0)
    mI3 = (bits_rx_I < 0) & (bits_rx_I >= -2 * a)
    mI4 = (bits_rx_I < -2 * a)
    
    bits_rx[0::4][mI1 | mI2] = 0
    bits_rx[0::4][mI3 | mI4] = 1
    
    bits_rx[1::4][mI1 | mI4] = 0
    bits_rx[1::4][mI2 | mI3] = 1
    
    mQ1 = (bits_rx_Q >= 2 * a)
    mQ2 = (bits_rx_Q < 2 * a) & (bits_rx_Q >= 0)
    mQ3 = (bits_rx_Q < 0) & (bits_rx_Q >= -2 * a)
    mQ4 = (bits_rx_Q < -2 * a)
    
    bits_rx[2::4][mQ1 | mQ2] = 0
    bits_rx[2::4][mQ3 | mQ4] = 1
    
    bits_rx[3::4][mQ1 | mQ4] = 0
    bits_rx[3::4][mQ2 | mQ3] = 1
    
    return bits_rx

# --- ORQUESTACIÓN (Bucle generador de la Curva BER) ---
if __name__ == "__main__":
    np.random.seed(34)
    NUM_BITS = 100000
    M = 16
    
    # 1. Generamos los bits y modulamos (Solo se hace una vez)
    bits_tx = np.random.randint(0, 2, NUM_BITS)
    x_16QAM = modula_16qam(bits_tx)
    
    # 2. Array de ruidos a evaluar (De -3 dB a 9 dB)
    array_EbN0 = np.arange(-3, 10)
    array_BER = np.zeros(len(array_EbN0))
    
    print("Iniciando barrido de ruidos en el canal AWGN...")
    
    # 3. Bucle principal de la práctica
    for i, ratio in enumerate(array_EbN0):
        # Pasamos por el canal
        y_16QAM = canal_awgn_ebn0(x_16QAM, ratio, M)
        
        # Demodulamos
        if y_16QAM is not None:
            bits_rx = demapeador_16qam(y_16QAM)
            
            # Calculamos Errores
            n_e = np.sum(bits_tx != bits_rx)
            array_BER[i] = n_e / len(bits_tx)
            
            print(f"16-QAM | Eb/N0 = {ratio:2d} dB | Errores = {n_e:5d} | BER = {array_BER[i]:.6f}")
    
    # 4. Ploteo de la curva si todo fue bien
    if array_BER[-1] < array_BER[0]: # El BER debe bajar al subir el Eb/N0
        plt.figure(figsize=(10, 6))
        plt.plot(array_EbN0, array_BER, 'r-*', linewidth=2, markersize=8)
        plt.yscale('log')
        plt.xlabel('Eb/N0 (dB)', fontsize=12)
        plt.ylabel('Bit Error Rate (BER)', fontsize=12)
        plt.title('Curva BER teórica para Modulación 16-QAM', fontsize=14)
        plt.grid(True, which="both", ls="--", alpha=0.7)
        plt.show()