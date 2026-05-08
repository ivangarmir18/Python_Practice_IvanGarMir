import sqlite3

# --- SETUP (Simulamos que la base de datos ya tiene datos) ---
conexion = sqlite3.connect(":memory:") 
cursor = conexion.cursor()
cursor.execute("CREATE TABLE accesos (usuario TEXT, fecha TEXT, exito INTEGER)")
cursor.execute("INSERT INTO accesos VALUES ('Roberto', '2026-05-06T19:30:00', 1)")
cursor.execute("INSERT INTO accesos VALUES ('Roberto', '2026-05-06T08:00:00', 0)")
cursor.execute("INSERT INTO accesos VALUES ('Laura', '2026-05-06T09:00:00', 1)")
# -----------------------------------------------------------

class RegistroAcceso:
    def __init__(self, user, timestamp, status):
        self.user = user
        self.timestamp = timestamp
        # Si status viene de SQL como 1/0, lo mantenemos. Si viene como bool, lo convertimos.
        self.status = 1 if status else 0 

    @classmethod
    def obtener_historial(cls, cursor_db, nombre_usuario):
        objetos_revividos = []
        cursor_db.execute("SELECT * FROM accesos WHERE usuario = ?;", (nombre_usuario,))
        for user, time, status in cursor_db.fetchall():
            objetos_revividos.append(cls(user, time, status))

        return objetos_revividos


# --- PRUEBA ---
# Pedimos a la clase que nos fabrique el historial de Roberto
historial_roberto = RegistroAcceso.obtener_historial(cursor, "Roberto")

# Comprobamos que efectivamente nos ha devuelto OBJETOS y no tuplas
print(f"Se han encontrado {len(historial_roberto)} registros para Roberto:")
for registro in historial_roberto:
    # Fíjate que accedemos a los datos usando los atributos del objeto (.user, .timestamp)
    estado = "Éxito" if registro.status == 1 else "Fallo"
    print(f"-> Objeto en RAM: {registro.user} intentó acceder el {registro.timestamp} [{estado}]")