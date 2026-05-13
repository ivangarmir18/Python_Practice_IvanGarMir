# =====================================================================
# RETO 49: PRUEBA TÉCNICA (Fusión de Intervalos Temporales)
# Tiempo límite sugerido: 40 minutos
# =====================================================================

def consolidar_reservas(intervalos):
    
    if not intervalos:
        return []
    intervalos.sort()
    resultado = [intervalos[0]]
    for intervalo in intervalos[1:]:
        if intervalo[1] < resultado[-1][1]:
            continue
        else:
            if intervalo[0] <= resultado[-1][1]:
                resultado[-1][1] = intervalo[1]
            else:
                resultado.append(intervalo)
                
    return resultado

if __name__ == "__main__":
    
    print("--- TEST DE RENDIMIENTO: MOTOR DE DISPONIBILIDAD ---")
    
    # CASO 1: Solapamiento básico y desordenado
    # El [1, 3] y [2, 6] se fusionan en [1, 6]. El [8, 10] queda libre.
    inv_1 = [[2, 6], [1, 3], [8, 10]]
    res_1 = consolidar_reservas(inv_1)
    print(f"Caso 1 - Esperado: [[1, 6], [8, 10]] | Obtenido: {res_1}")
    
    # CASO 2: Cadena de solapamientos (Efecto dominó)
    inv_2 = [[1, 4], [4, 5], [5, 9]]
    res_2 = consolidar_reservas(inv_2)
    print(f"Caso 2 - Esperado: [[1, 9]] | Obtenido: {res_2}")
    
    # CASO 3: Un intervalo "traga" a otros más pequeños
    inv_3 = [[1, 10], [2, 3], [4, 8], [11, 12]]
    res_3 = consolidar_reservas(inv_3)
    print(f"Caso 3 - Esperado: [[1, 10], [11, 12]] | Obtenido: {res_3}")
    
    # CASO 4: Totalmente separados
    inv_4 = [[1, 2], [5, 6], [9, 10]]
    res_4 = consolidar_reservas(inv_4)
    print(f"Caso 4 - Esperado: [[1, 2], [5, 6], [9, 10]] | Obtenido: {res_4}")
    
    # VALIDACIÓN RRHH
    if res_1 == [[1, 6], [8, 10]] and res_2 == [[1, 9]] and res_3 == [[1, 10], [11, 12]] and res_4 == inv_4:
        print("\n✅ ¡PRUEBA SUPERADA! Visión espacial y ordenamiento impecables.")
    else:
        print("\n❌ FALLO TÉCNICO. Los rangos no se han fusionado correctamente.")