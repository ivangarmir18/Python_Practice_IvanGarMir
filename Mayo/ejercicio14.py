import sqlite3

# --- SETUP INICIAL (No tocar) ---
# Creamos una base de datos en la memoria RAM solo para esta prueba
conexion = sqlite3.connect(":memory:") 
cursor = conexion.cursor()
# Creamos la tabla con SQL
cursor.execute("CREATE TABLE sensores (id_sensor TEXT, ubicacion TEXT, activo INTEGER)")
# --------------------------------

class Sensor:
    def __init__(self, id_sensor, ubicacion, activo=True):
        # Estos son los atributos del objeto
        self.id_sensor = id_sensor
        self.ubicacion = ubicacion
        self.activo = 1 if activo else 0 # 1 si es True, 0 si es False

    def guardar_en_db(self, cursor_db):
        cursor_db.execute("INSERT INTO sensores (id_sensor, ubicacion, activo) VALUES (?, ?, ?);", 
    (self.id_sensor, self.ubicacion, self.activo))

# --- PRUEBAS ---
# 1. Instanciamos dos objetos de la clase Sensor
sensor1 = Sensor("SENS_001", "Puerta Principal", True)
sensor2 = Sensor("SENS_002", "Sala de Servidores", False)

# 2. Les pedimos a los objetos que se guarden a sí mismos
sensor1.guardar_en_db(cursor)
sensor2.guardar_en_db(cursor)

# 3. Comprobamos la base de datos directamente
cursor.execute("SELECT * FROM sensores")
resultados = cursor.fetchall()

print(resultados)
# Resultado esperado exacto: 
# [('SENS_001', 'Puerta Principal', 1), ('SENS_002', 'Sala de Servidores', 0)]