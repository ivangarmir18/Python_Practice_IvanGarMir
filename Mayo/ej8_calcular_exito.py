logs_biometria = [
    ("Roberto", "EXITO"),
    ("Laura", "FALLO"),
    ("Roberto", "FALLO"),
    ("Laura", "EXITO"),
    ("Laura", "EXITO"),
    ("Invitado", "FALLO")
]
def calcular_tasa_exito(intentos):
    salida={}
    temp={}
    for nombre, resultado in intentos:
        temp.setdefault(nombre, []).append(resultado)
    for nombre, resultados in temp.items():
        total=0
        total += resultados.count("EXITO")
        total=total/len(resultados)
        salida[nombre]=round(total,2)
    return salida
resultado = calcular_tasa_exito(logs_biometria)
print(resultado)