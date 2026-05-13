def es_sintaxis_valida(cadena):
    tipos = {'{': '}', '[': ']', '(': ')'}
    pila = []
    
    for char in cadena:
        if char in tipos:  
            pila.append(char)
            
        elif char in tipos.values(): 
            if not pila or tipos[pila.pop()] != char:
                return False

    return not pila

if __name__ == "__main__":
    
    print("--- TEST DE RENDIMIENTO: VALIDADOR DE SINTAXIS ---")
    
    # CASOS DE PRUEBA
    casos = [
        ("()", True),            # Caso 1: Básico
        ("()[]{}", True),        # Caso 2: Secuencial
        ("(]", False),           # Caso 3: Cierre incorrecto
        ("([)]", False),         # Caso 4: Orden cruzado (Inválido)
        ("{[]}", True),          # Caso 5: Anidado correcto
        ("[", False),            # Caso 6: Falta cerrar
        ("}}", False)            # Caso 7: Cierre sin apertura previa
    ]
    
    exito_total = True
    
    for i, (cadena, resultado_esperado) in enumerate(casos):
        resultado_obtenido = es_sintaxis_valida(cadena)
        if resultado_obtenido == resultado_esperado:
            print(f"Caso {i+1} correcto: '{cadena}' -> {resultado_obtenido}")
        else:
            print(f"❌ Caso {i+1} FALLIDO: '{cadena}'. Esperado: {resultado_esperado} | Obtenido: {resultado_obtenido}")
            exito_total = False
            
    # VALIDACIÓN RRHH
    if exito_total:
        print("\n✅ ¡PRUEBA SUPERADA! Entiendes perfectamente el control de flujo y el estado LIFO.")
    else:
        print("\n❌ FALLO TÉCNICO. Revisa tu lógica para manejar los cierres o los elementos sobrantes.")