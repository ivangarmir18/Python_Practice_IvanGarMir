import sqlite3
import json
from datetime import datetime, timedelta

# --- SETUP INICIAL SQL ---
conexion = sqlite3.connect(":memory:") 
cursor = conexion.cursor()
# La tabla espera: usuario (texto), fecha (texto), exito (entero: 1 o 0)
cursor.execute("CREATE TABLE accesos (usuario TEXT, fecha TEXT, exito INTEGER)")
# -------------------------

# Simulación del tiempo actual en el servidor
ahora = datetime.fromisoformat("2026-05-06T20:00:00")

# Lote de datos crudos que llega por la red desde el sensor
payloads_red = [
    '{"user": "Roberto", "timestamp": "2026-05-06T19:30:00", "status": true}',   # Válido (Hoy)
    '{"user": "Laura", "timestamp": "2026-04-20T10:00:00", "status": false}',  # DESCARTAR: Hace más de 7 días
    '{user: "Fantasma", timestamp: "error", status: true}',                    # DESCARTAR: JSON Corrupto
    '{"user": "Carlos", "timestamp": "2026-05-05T08:00:00", "status": true}'     # Válido (Ayer)
]

class RegistroAcceso:
    def __init__(self, user, timestamp, status):
        self.user = user
        self.timestamp = timestamp
        self.status = 1 if status else 0
    def guardar(self, cursor_db):
        cursor_db.execute("INSERT INTO accesos (usuario, fecha, exito) VALUES (?, ?, ?)",
        (self.user, self.timestamp, self.status))
        cursor_db.connection.commit()

def procesar_lote(payloads, cursor_db, momento_actual):
    for registro in payloads:
        try:
            d = json.loads(registro)
            user = d.get("user")
            time = d.get("timestamp")
            status = d.get("status")
            time_compare = datetime.fromisoformat(time)
            if momento_actual <= time_compare + timedelta(days=7):
                log = RegistroAcceso(user, time, status)
                log.guardar(cursor_db)
        except (json.JSONDecodeError, ValueError, TypeError):
            continue

# --- PRUEBA ---
# Ejecutamos el orquestador
procesar_lote(payloads_red, cursor, ahora)

# Comprobamos la base de datos
cursor.execute("SELECT * FROM accesos")
resultados = cursor.fetchall()

print("Base de datos final:")
for fila in resultados:
    print(fila)

# Resultado esperado exacto en consola:
# Base de datos final:
# ('Roberto', '2026-05-06T19:30:00', 1)
# ('Carlos', '2026-05-05T08:00:00', 1)