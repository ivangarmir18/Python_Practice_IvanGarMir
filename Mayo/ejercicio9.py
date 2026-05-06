secuencia_normal = ["1", "2","a", "<", "3", "4", "5", "<", "<", "9"]
secuencia_trampa = ["<", "<", "7", "7", "<", "8"]

def procesar_pin(teclas):
    teclas_correctas=""
    for tecla in teclas:

        if tecla=="<":
                teclas_correctas = teclas_correctas[:-1]    
        elif tecla.isdigit():
            teclas_correctas+=tecla
        
    return teclas_correctas
        

# --- PRUEBAS ---
resultado1 = procesar_pin(secuencia_normal)
print(f"PIN 1: {resultado1}") 
# Resultado esperado exacto: "139"
# Explicación: 
# Mete 1, mete 2 (12). Borra 2 (1). Mete 3, 4, 5 (1345). 
# Borra 5 (134), borra 4 (13). Mete 9 (139).

resultado2 = procesar_pin(secuencia_trampa)
print(f"PIN 2: {resultado2}")
# Resultado esperado exacto: "78"
# Explicación: 
# Borra en vacío (nada), borra en vacío (nada). Mete 7, 7 (77). Borra 7 (7). Mete 8 (78).