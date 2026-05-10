import numpy as np
import matplotlib.pyplot as plt

def generar_bits(num_bits):
    return np.random.randint(0, 2, num_bits).astype(float)

def mapeador_qpsk(bits, voltaje=1.0):
    if (len(bits) % 2) == 0:
        bits_I = bits[::2]
        bits_Q = bits[1::2]
        voltajes_I = (bits_I * 2 - 1) * voltaje
        voltajes_Q = (bits_Q * 2 - 1) * voltaje
        complejos = voltajes_I + 1j * voltajes_Q
        return complejos
    else: 
        raise ValueError("El número de bits debe ser par para QPSK")


if __name__ == "__main__":
    NUM_BITS = 1000  # 1000 bits se convertirán en 500 símbolos QPSK
    VOLTAJE = 1.0
    
    # 1. Generación y Mapeo
    mis_bits = generar_bits(NUM_BITS)
    simbolos_qpsk = mapeador_qpsk(mis_bits, voltaje=VOLTAJE)
    
    # 2. Comprobaciones y Visualización
    if simbolos_qpsk is not None:
        print(f"Número de bits originales: {len(mis_bits)}")
        print(f"Número de símbolos generados: {len(simbolos_qpsk)}")
        
        # Mostrar los primeros 4 bits y sus primeros 2 símbolos
        print(f"\nPrimeros 4 bits: {mis_bits[:4]}")
        print(f"Primeros 2 símbolos QPSK: {simbolos_qpsk[:2]}")
        
        # Ploteo de la Constelación (Plano Complejo)
        plt.figure(figsize=(6, 6))
        # Extraemos la parte real (I) y la imaginaria (Q) para pintar
        plt.scatter(simbolos_qpsk.real, simbolos_qpsk.imag, color='red', marker='o')
        
        plt.title("Constelación QPSK Ideal")
        plt.xlabel("Componente En Fase (I)")
        plt.ylabel("Componente en Cuadratura (Q)")
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        plt.grid(True, linestyle='--')
        
        # Ajustar ejes para ver la cruz perfectamente
        plt.xlim(-VOLTAJE - 0.5, VOLTAJE + 0.5)
        plt.ylim(-VOLTAJE - 0.5, VOLTAJE + 0.5)
        plt.show()
    else:
        print("Esperando a que completes la función mapeador_qpsk().")