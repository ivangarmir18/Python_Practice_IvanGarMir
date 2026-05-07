logs_servidor = [
    "10:00:01 | GET /api/users | 200",
    "10:00:05 | POST /api/login | 401",
    "10:01:12 | GET /api/products | 200",
    "10:02:00 | GET /api/users | 200",
    "10:02:15 | DELETE /api/products | 403",
    "10:03:00 | GET /api/orders | 500",
    "10:03:10 | GET /api/users | 200",
    "10:04:05 | POST /api/checkout | 200"
]

def analizar_logs(lista_logs):
    diccionario = {}
    
    for string in lista_logs:
        try:
            partes = string.split(" | ")
            if partes[2] == "200":
                ruta = partes[1].split()[-1]
                diccionario[ruta] = diccionario.get(ruta, 0) + 1
        except IndexError:
            print("la lista de logs tiene algún error en: ", string)
            continue
            
    return diccionario

# --- PRUEBA ---
resultado = analizar_logs(logs_servidor)
print(resultado)

# RESULTADO ESPERADO EXACTO:
# {'/api/users': 3, '/api/products': 1, '/api/checkout': 1}