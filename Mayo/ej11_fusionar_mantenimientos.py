# Lista de mantenimientos programados por distintos técnicos (Desordenada)
# Fíjate bien en los números para hacerte el mapa mental
cortes_programados = [(8, 10), (1, 4), (3, 6), (15, 18), (5, 7)]

# Solución 1
"""
def fusionar_mantenimientos(horarios):
    horarios.sort()
    cortes = []
    temp=(0,0)
    for inicio, fin in horarios:
        if temp[1]>=inicio:
            temp=(temp[0],max(fin,temp[1]))
        if temp[1]<inicio :
            if temp!=(0,0): cortes.append(temp)
            temp=(inicio,fin)
    cortes.append(temp)
    return cortes
"""

# Solución 2
def fusionar_mantenimientos(horarios):
    horarios.sort()
    cortes = [horarios[0]]
    for inicio, fin in horarios[1:]:
        ultimo_corte=cortes[-1]
        if ultimo_corte[1]>=inicio:
            cortes[-1]=(ultimo_corte[0],max(fin,ultimo_corte[1]))
        else:
            cortes.append((inicio,fin))
    return cortes



        

        

# --- PRUEBAS ---
resultado = fusionar_mantenimientos(cortes_programados)
print(resultado)
# Resultado esperado exacto: [(1, 7), (8, 10), (15, 18)]

# Explicación mental:
# (1, 4), (3, 6) y (5, 7) se pisan y se encadenan. Se fusionan todos en un gran corte de (1, 7).
# (8, 10) está aislado.
# (15, 18) está aislado.