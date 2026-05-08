transcripcion_sucia = "apagar apagar el servidor maldita sea apagar"
palabras_prohibidas = ["servidor", "maldita"]

def procesar_transcripcion(texto, prohibidas):
    palabras=texto.strip().split()
    resultado=[]
    for i, palabra in enumerate(palabras):
        if i>0 and palabra==palabras[i-1]:
            continue
        if palabra in prohibidas:
                resultado.append('*'*len(palabra))
                continue
        else:
            resultado.append(palabra)
    return " ".join(resultado)



# --- PRUEBAS ---
resultado1 = procesar_transcripcion(transcripcion_sucia, palabras_prohibidas)
print(resultado1) 
# Resultado esperado exacto: "apagar el *** *** sea apagar"
# Explicación: Quita un "apagar", censura "servidor" y "maldita", pero respeta el "apagar" del final.

resultado2 = procesar_transcripcion("hola hola hola que que tal", ["tal"])
print(resultado2)
# Resultado esperado exacto: "hola que ***"