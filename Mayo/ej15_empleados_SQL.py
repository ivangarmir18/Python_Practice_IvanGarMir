import sqlite3

# --- SETUP INICIAL ---
conexion = sqlite3.connect(":memory:") 
cursor = conexion.cursor()
cursor.execute("CREATE TABLE empleados (dni TEXT, nombre TEXT, sede TEXT)")
# ---------------------

class Empleado:
    def __init__(self, dni, nombre, sede):
        self.dni = dni
        self.nombre = nombre
        self.sede = sede
    def guardar(self, cursor_db):
        cursor_db.execute("INSERT INTO empleados (dni, nombre, sede) VALUES (?, ?, ?);",
        (self.dni, self.nombre, self.sede))
        cursor_db.connection.commit()
    def cambiar_sede(self, cursor_db, nueva_sede):
        self.sede = nueva_sede
        cursor_db.execute("UPDATE empleados SET sede = ? WHERE dni = ?;",(self.sede, self.dni))
        cursor_db.connection.commit()
# --- PRUEBAS (Descomenta esto para probar tu código) ---
# 1. Creamos el empleado y lo guardamos
trabajador = Empleado("12345678A", "Marta", "Sede Central")
trabajador.guardar(cursor)

# 2. Comprobamos que se guardó bien
cursor.execute("SELECT * FROM empleados")
print(f"Primera inserción: {cursor.fetchall()}") 
# Esperado: [('12345678A', 'Marta', 'Sede Central')]

# 3. La empresa traslada a Marta a la Sede Norte
trabajador.cambiar_sede(cursor, "Sede Norte")

# 4. Comprobamos que la base de datos se ha actualizado
cursor.execute("SELECT * FROM empleados")
print(f"Tras el update: {cursor.fetchall()}")
# Esperado: [('12345678A', 'Marta', 'Sede Norte')]