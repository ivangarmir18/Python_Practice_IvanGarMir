def encontrar_transacciones(transacciones, objetivo):

    diccionario = {}
    for i, transaccion in enumerate(transacciones):
        busqueda = [[i, indice] for indice, dato in diccionario.items() if dato + transaccion == objetivo]
        
        if busqueda:
            indices_objetivo = busqueda[0]
            break
        diccionario[i] = transaccion

    return sorted(indices_objetivo) if indices_objetivo else []

if __name__ == "__main__":
    
    print("--- TEST DE RENDIMIENTO: CONCILIACIÓN BANCARIA ---")
    
    # CASO 1: Básico. 2 + 7 = 9. Índices: 0 y 1.
    t_1 = [2, 7, 11, 15]
    obj_1 = 9
    res_1 = encontrar_transacciones(t_1, obj_1)
    print(f"Caso 1 - Esperado: [0, 1] o [1, 0] | Obtenido: {res_1}")
    
    # CASO 2: Elementos desordenados. 2 + 4 = 6. Índices: 1 y 2.
    t_2 = [3, 2, 4]
    obj_2 = 6
    res_2 = encontrar_transacciones(t_2, obj_2)
    print(f"Caso 2 - Esperado: [1, 2] o [2, 1] | Obtenido: {res_2}")
    
    # CASO 3: Números repetidos. 3 + 3 = 6. Índices: 0 y 1.
    t_3 = [3, 3]
    obj_3 = 6
    res_3 = encontrar_transacciones(t_3, obj_3)
    print(f"Caso 3 - Esperado: [0, 1] o [1, 0] | Obtenido: {res_3}")
    
    # VALIDACIÓN RRHH
    def validar(resultado, esperado):
        # Comprueba si el resultado es correcto independientemente del orden
        return isinstance(resultado, list) and sorted(resultado) == sorted(esperado)

    if validar(res_1, [0, 1]) and validar(res_2, [1, 2]) and validar(res_3, [0, 1]):
        print("\n✅ ¡PRUEBA SUPERADA! Has demostrado dominio total sobre la eficiencia algorítmica.")
    else:
        print("\n❌ FALLO TÉCNICO. Los índices devueltos no suman el objetivo o el formato no es una lista.")