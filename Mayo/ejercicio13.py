# Base de datos del sensor local
import copy
edge_db = {
    "usr_001": {"nombre": "Roberto", "nivel": 2, "roles": ["puerta_principal", "servidores"]},
    "usr_002": {"nombre": "Laura_Local", "nivel": 1, "roles": ["recepcion"]},
    "usr_004": {"nombre": "Carlos_Nuevo", "nivel": 1, "roles": ["invitado"]} # Solo está aquí
}

# Base de datos del servidor central
cloud_db = {
    "usr_001": {"nombre": "Roberto_Gomez", "nivel": 1, "roles": ["puerta_principal", "admin"]},
    "usr_002": {"nombre": "Laura", "nivel": 3, "roles": ["recepcion"]},
    "usr_003": {"nombre": "Marta", "nivel": 5, "roles": ["master"]} # Solo está aquí
}

def sincronizar_bases(db_local, db_nube):
    db_maestra = copy.deepcopy(db_nube)
    for user, valores in db_local.items():
        if user not in db_maestra:
            db_maestra[user]=valores
        else:
            level = valores["nivel"]
            db_maestra[user]["nivel"] = max(db_maestra[user]["nivel"], level)

            roles = valores["roles"]
            actuales = set(db_maestra[user]["roles"])
            nuevos = set(roles)
            db_maestra[user]["roles"] = list(actuales | nuevos)

    return db_maestra

# --- PRUEBAS ---
resultado = sincronizar_bases(edge_db, cloud_db)

import json
print(json.dumps(resultado, indent=2))

"""
# Resultado esperado exacto:
{
  "usr_001": {
    "nombre": "Roberto_Gomez", 
    "nivel": 2, 
    "roles": ["puerta_principal", "servidores", "admin"] 
  },
  "usr_002": {
    "nombre": "Laura", 
    "nivel": 3, 
    "roles": ["recepcion"]
  },
  "usr_003": {
    "nombre": "Marta", 
    "nivel": 5, 
    "roles": ["master"]
  },
  "usr_004": {
    "nombre": "Carlos_Nuevo", 
    "nivel": 1, 
    "roles": ["invitado"]
  }
}
"""