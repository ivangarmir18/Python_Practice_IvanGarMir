def detectar_fraude(transacciones):
    
    bloqueados = set()
    historial = {}
    for log in transacciones:
        
        id = log.get("id")
        importe = log.get("importe")
        minuto = log.get("min")

        if id in bloqueados: 
            continue

        if id not in historial:
            historial[id] = {"importes" : 0, "minutos" : [minuto]} 
        else:
            historial[id]["importes"] += importe
            historial[id]["minutos"].append(minuto)

        minutos_usuario = historial[id]["minutos"]

        if importe > 500 or historial[id]["importes"] > 1000:
            bloqueados.add(id)

        if len(minutos_usuario) >= 3:
            if minutos_usuario[-1] - minutos_usuario[-3] <= 10:
                bloqueados.add(id)

    return sorted(list(bloqueados))

if __name__ == "__main__":
    
    print("--- TEST DE RENDIMIENTO: MOTOR ANTIFRAUDE ---")
    
    # DATOS DEL DÍA (Cronológicos)
    logs_bancarios = [
        {"id": "U1", "importe": 50, "min": 1},
        {"id": "U2", "importe": 600, "min": 2},  # BLOQUEADO: Regla 1 (>500)
        {"id": "U1", "importe": 100, "min": 3},
        {"id": "U3", "importe": 400, "min": 4},
        {"id": "U1", "importe": 20, "min": 9},   # BLOQUEADO: Regla 3 (3 compras en min 1, 3, 9. Diferencia: 8 mins)
        {"id": "U3", "importe": 400, "min": 15},
        {"id": "U4", "importe": 100, "min": 20},
        {"id": "U3", "importe": 300, "min": 25}, # BLOQUEADO: Regla 2 (Suma: 400+400+300 = 1100)
        {"id": "U1", "importe": 5000, "min": 30},# Ignorar: Ya estaba bloqueado
        {"id": "U4", "importe": 100, "min": 35},
        {"id": "U4", "importe": 100, "min": 40}  # OK: 3 compras en min 20, 35, 40. Diferencia: 20 mins.
    ]
    
    res = detectar_fraude(logs_bancarios)
    esperado = ["U1", "U2", "U3"]
    
    print(f"Resultado obtenido: {res}")
    
    if res == esperado:
        print("\n🏆 ¡RETO 50 SUPERADO! Has integrado toda la lógica de backend.")
        print("La empresa está a salvo. Tu lógica es producción-ready.")
    else:
        print(f"\n❌ FALLO TÉCNICO. Esperábamos {esperado}.")