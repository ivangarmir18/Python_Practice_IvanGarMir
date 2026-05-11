from datetime import datetime

# =====================================================================
# RETO 44: PRUEBA TÉCNICA DE ACCESO (Backend & Data)
# Tiempo límite sugerido: 45 minutos
# =====================================================================

def analizar_logs(logs_crudos):

    logs = sorted(logs_crudos, key=lambda x: x["time"])

    sesiones_finalizadas = []
    estado_usuarios = {}
    checkouts = 0

    for log in logs:
        user = log["user"]
        action = log["action"]
        current_time = datetime.strptime(log["time"], "%Y-%m-%dT%H:%M:%S")
        
        if user in estado_usuarios:
            ultimo_evento = estado_usuarios[user]["ultimo"]
            inicio_sesion = estado_usuarios[user]["inicio"]
            diff_minutos = (current_time - ultimo_evento).total_seconds() / 60
            
            if diff_minutos >= 30 or action == "login":
                duracion = (ultimo_evento - inicio_sesion).total_seconds()
                sesiones_finalizadas.append(duracion)
                del estado_usuarios[user]
            
        if user not in estado_usuarios:
            estado_usuarios[user] = {"inicio": current_time, "ultimo": current_time, "checkout": False}
        else:
            estado_usuarios[user]["ultimo"] = current_time
            
        if action == "checkout":
            checkouts += 1
            duracion = (current_time - estado_usuarios[user]["inicio"]).total_seconds()
            sesiones_finalizadas.append(duracion)
            del estado_usuarios[user]
        
        elif action == "logout":
            duracion = (current_time - estado_usuarios[user]["inicio"]).total_seconds()
            sesiones_finalizadas.append(duracion)
            del estado_usuarios[user]

    
    total_s = len(sesiones_finalizadas)
    duracion_media = (sum(sesiones_finalizadas) / 60) / total_s if total_s > 0 else 0
    tasa_conv = (checkouts / total_s) * 100 if total_s > 0 else 0
    
    for user, datos in estado_usuarios.items():
        duracion = (datos["ultimo"] - datos["inicio"]).total_seconds()
        sesiones_finalizadas.append(duracion)
        
    return {
        "total_sesiones": total_s,
        "duracion_media_minutos": round(duracion_media, 2),
        "tasa_conversion_porcentaje": round(tasa_conv, 2)
    }

if __name__ == "__main__":
    logs_servidor = [
        {"time": "2023-10-01T10:05:00", "user": "u1", "action": "view_item"},
        {"time": "2023-10-01T10:00:00", "user": "u1", "action": "login"},
        {"time": "2023-10-01T10:50:00", "user": "u1", "action": "checkout"}, # Han pasado 45 min, ¡es sesión nueva!
        {"time": "2023-10-01T10:10:00", "user": "u2", "action": "login"},
        {"time": "2023-10-01T10:12:00", "user": "u2", "action": "logout"},  # Sesión cerrada explícitamente
        {"time": "2023-10-01T10:15:00", "user": "u2", "action": "view_item"}, # Sesión nueva (la anterior se cerró)
        {"time": "2023-10-01T10:18:00", "user": "u2", "action": "checkout"},
        {"time": "2023-10-01T10:08:00", "user": "u1", "action": "add_to_cart"}
    ]
    
    print("--- PROCESANDO LOGS DEL SERVIDOR ---")
    resultados = analizar_logs(logs_servidor)
    
    print("\nResultados obtenidos:")
    print(resultados)
  
    if (resultados.get("total_sesiones") == 4 and 
        resultados.get("duracion_media_minutos") == 3.25 and 
        resultados.get("tasa_conversion_porcentaje") == 50.0):
        print("\n✅ ¡CONTRATADO! Lógica de negocio impecable y buen manejo de datos.")
    else:
        print("\n❌ FALLO TÉCNICO. Las métricas no cuadran con la realidad de los datos.")