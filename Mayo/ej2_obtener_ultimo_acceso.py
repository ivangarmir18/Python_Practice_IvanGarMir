# Simulamos la respuesta de la base de datos (JSON convertido a diccionario)
respuesta_api = {
    "status": "ok",
    "usuarios": [
        {
            "nombre": "Roberto",
            "rol": "admin",
            "accesos_exitosos": 15,
            "ultimos_logs": ["2026-05-01", "2026-05-03", "2026-05-05"]
        },
        {
            "nombre": "Invitado",
            "rol": "user",
            "accesos_exitosos": 2
            # Fíjate que este usuario NO tiene la clave "ultimos_logs" a propósito
        }
    ]
}

def obtener_ultimo_acceso(datos_api, nombre_usuario):
    
    # Comprobamos que la base de datos ha respondido bien
    if datos_api["status"] == "ok":
        lista_usuarios = datos_api["usuarios"]
        # Recorremos la lista de usuarios
        for i in range(len(lista_usuarios)):
            usuario = lista_usuarios[i]
            
            if usuario["nombre"] == nombre_usuario:
                # Extraemos la lista de fechas
                logs = usuario.get("ultimos_logs", [])
                
                # Cogemos la última fecha registrada
                ultimo_log = logs[-1] if logs else "No hay registros de acceso"
                
                return f"Último acceso de {nombre_usuario}: {ultimo_log}"
                
    return "Error o usuario no encontrado"

# Prueba de fuego
print(obtener_ultimo_acceso(respuesta_api, "Invitado"))