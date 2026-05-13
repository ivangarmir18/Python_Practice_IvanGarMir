import sqlite3

def auditar_ventas(datos_crudos):

    conexion = sqlite3.connect(':memory:')
    cursor = conexion.cursor()
    datos_limpios = []
    cursor.execute("CREATE TABLE ventas (order_id TEXT PRIMARY KEY, user_id TEXT, amount REAL, status TEXT);")
    
    for dato in datos_crudos:
        if not dato.get("order_id"):
            continue
        order_id = dato.get("order_id")
        user_id = dato.get("user_id") 
        status = str(dato.get("status", "")).upper().strip()
        amount = float(str(dato.get("amount") or "0.0").replace("$", "").replace("€", "").strip())
        datos_limpios.append((order_id, user_id, amount, status))
    
    cursor.executemany("INSERT INTO ventas (order_id, user_id, amount, status) VALUES (?, ?, ?, ?);", datos_limpios)
    conexion.commit()
    
    query = """
    SELECT user_id, SUM(amount) AS total_gastado
    FROM ventas
    WHERE status = 'DELIVERED'
    GROUP BY user_id
    HAVING total_gastado > 100
    ORDER BY total_gastado DESC;
"""

    cursor.execute(query)
    resultados = cursor.fetchall()
    
    conexion.close()
    return resultados

if __name__ == "__main__":
    
    # VOLCADO CRUDO DEL SERVIDOR
    volcado_pagos = [
        {"order_id": "A1", "user_id": "U_01", "amount": "€ 120.50", "status": "delivered "},
        {"order_id": "A2", "user_id": "U_02", "amount": "$45.00", "status": "DELIVERED"},
        {"order_id": None, "user_id": "U_01", "amount": "500.0", "status": "DELIVERED"}, # IGNORAR: Sin order_id
        {"order_id": "A3", "user_id": "U_03", "amount": "  200", "status": "pending"},
        {"order_id": "A4", "user_id": "U_01", "amount": "10.00", "status": "DELIVERED"},
        {"order_id": "A5", "user_id": "U_02", "amount": "€80.0", "status": "Delivered"},
        {"order_id": "A6", "user_id": "U_04", "status": "DELIVERED"}, # Sin amount, asume 0.0
        {"order_id": "A7", "user_id": "U_03", "amount": "50.0", "status": "DELIVERED"},
        {"order_id": "A8", "user_id": "U_02", "amount": "300.0", "status": "cancelled"}
    ]
    
    print("--- INICIANDO ETL Y AUDITORÍA ---")
    resultados_finales = auditar_ventas(volcado_pagos)
    
    print(f"\nResultados obtenidos: {resultados_finales}")
    
    esperado = [('U_01', 130.5), ('U_02', 125.0)]
    
    if resultados_finales == esperado:
        print("\n✅ ¡PRUEBA SUPERADA! Has integrado Python y SQL de forma impecable.")
    else:
        print("\n❌ FALLO TÉCNICO. Revisa la limpieza de strings o la lógica de tu query SQL.")