import json
from datetime import datetime, timedelta

# Simulamos que "ahora" es exactamente este momento (Miércoles 6 de Mayo de 2026, a las 16:00)
ahora = datetime.fromisoformat("2026-05-06T16:00:00")
# Lo que llega por la red desde el sensor biométrico
datos_red = [
    '{"usuario": "Roberto", "estado": "ok", "timestamp": "2026-05-06T15:30:00"}', # Válido (hace 30 mins)
    '{"usuario": "Laura", "estado": "fail", "timestamp": "2026-05-05T10:00:00"}', # Válido (pero hace más de 24h)
    '{"usuario": "Carlos", "estado": "ok", "timestamp": "2026-05-06T09:00:00"}',  # Válido (hace 7 horas)
    '{usuario: Invitado, estado: error}', # CORRUPTO: Faltan comillas (Romperá el parser)
    '{"usuario": "Admin", "estado": "ok", "timestamp": "2026-05-06T14:20:00"'     # CORRUPTO: Falta la llave de cierre
]

def filtrar_alertas_recientes(payloads, momento_actual):
    alertas_validas = []
    for p_str in payloads:
        try:
            d = json.loads(p_str)
            user = d.get("usuario")
            status = d.get("estado")
            time = d.get("timestamp")
            time_compare = datetime.fromisoformat(time)
            if momento_actual <= time_compare + timedelta(hours=24):
                alertas_validas.append(d)
        except json.JSONDecodeError:
            continue
        
    return alertas_validas

# --- PRUEBA ---
resultado = filtrar_alertas_recientes(datos_red, ahora)

# Para verlo bonito en la consola
for r in resultado:
    print(r)

# Resultado esperado exacto (2 diccionarios):
# {'usuario': 'Roberto', 'estado': 'ok', 'timestamp': '2026-05-06T15:30:00'}
# {'usuario': 'Carlos', 'estado': 'ok', 'timestamp': '2026-05-06T09:00:00'}