# Lista de tuplas (hora_entrada, hora_salida)
registro_accesos = [
    (9, 12),   # Roberto
    (10, 14),  # Laura
    (11, 13),  # Carlos
    (13, 15),  # Invitado 1
    (14, 16)   # Invitado 2
]
# Mi solución 1
'''def calcular_pico_ocupacion(sesiones):
    horas_acceso=[]
    repeticiones=[]
    nmin = float('inf')
    nmax = 0
    for entrada,salida in sesiones:
        horas_acceso.append(tuple(range(entrada, salida)))
        if entrada < nmin:
            nmin = entrada
        if salida > nmax:
            nmax = salida
    for i in range(nmin,nmax):
        
        repeticiones.append(sum(horas.count(i) for horas in horas_acceso))
        print(i, repeticiones)
    pico_max=max(repeticiones)
    return pico_max

'''
# Mi solución 2
def calcular_pico_ocupacion(sesiones):
    accesos=[]
    totales=[]
    total=0
    for entrada,salida in sesiones:
        accesos.append((entrada,1))
        accesos.append((salida,-1))
    accesos.sort()
    for _, suma in accesos:
        total += suma
        totales.append(total)
    maximo=max(totales)
    return maximo

# --- PRUEBA ---
pico_maximo = calcular_pico_ocupacion(registro_accesos)
print(f"El pico máximo de ocupación fue: {pico_maximo} personas.")
# Resultado esperado exacto: 3
# Explicación del ejemplo:
# A las 11:00 están Roberto, Laura y Carlos dentro (3 personas).
# A las 12:00 Roberto se va.
# A las 13:00 Carlos se va y entra Invitado 1. (Nunca superan los 3).