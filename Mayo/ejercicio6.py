logs_diarios = [
    ("Roberto", "ENTRADA", 100),
    ("Laura", "ENTRADA", 110),
    ("Roberto", "SALIDA", 150),   # Roberto sumaría 50 segs (150 - 100)
    ("Invitado", "SALIDA", 160),  # IGNORAR (No hay entrada previa de Invitado)
    ("Laura", "ENTRADA", 170),    # REEMPLAZA la entrada anterior de Laura (110) porque no salió.
    ("Laura", "SALIDA", 200),     # Laura sumaría 30 segs (200 - 170)
    ("Roberto", "ENTRADA", 210),
    ("Roberto", "SALIDA", 230),   # Roberto suma otros 20 segs (Total: 70)
    ("Carlos", "ENTRADA", 300)    # IGNORAR (El día acaba y Carlos nunca salió)
]

def calcular_tiempo_total(logs):
    indices_personas={}
    for i, (nombre,_,_) in enumerate(logs):
        indices_personas.setdefault(nombre, []).append(i)
    resultados={}

    for nombre, lista_indices in indices_personas.items():    
        tiempo_total=0
        ultima_entrada=None
        for idx in lista_indices:
            tipo=logs[idx][1]
            tiempo=logs[idx][2]
            if tipo=="ENTRADA":
                ultima_entrada=tiempo

            elif tipo=="SALIDA" and ultima_entrada is not None:
                tiempo_total += (tiempo-ultima_entrada)
                ultima_entrada = None
        if tiempo_total > 0:
            resultados[nombre] = tiempo_total
    return resultados

# Prueba
resultados = calcular_tiempo_total(logs_diarios)
print(resultados) 
# Debería imprimir exactamente: {'Roberto': 70, 'Laura': 30}