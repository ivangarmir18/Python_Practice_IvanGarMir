registro={}
def registrar_intento(usuario:str,tiempo_segundos:int):
    registro.setdefault(usuario, [])
    registro[usuario].append(tiempo_segundos)
    contador=0
    indice = len(registro[usuario]) - 1

    for i in range(indice, -1, -1):
        tiempo = registro[usuario][i]
        
        if tiempo_segundos - tiempo <= 10:
            contador += 1
        else:
            del registro[usuario][i]
    if contador>=3:
        return "BLOQUEADO"
    else:
        return "PERMITIDO"
    



print(registrar_intento("Roberto", 1))  # Debe dar PERMITIDO
print(registrar_intento("Roberto", 5))  # Debe dar PERMITIDO
print(registrar_intento("Invitado", 6)) # Debe dar PERMITIDO (Es otro usuario)
print(registrar_intento("Roberto", 8))  # Debe dar BLOQUEADO (3 intentos en menos de 10s: el 1, el 5 y el 8)
print(registrar_intento("Roberto", 20)) # Debe dar PERMITIDO (Ya pasaron más de 10 segundos desde su primer intento)
