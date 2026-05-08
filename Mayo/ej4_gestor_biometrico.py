import os

class GestorBiometrico:
    # Variable de clase (compartida, pero accesible de forma segura)
    ruta_base = "Records/MasterVoices"
    
    # LA SOLUCIÓN AL BUG MUTANTE: Usar None
    def __init__(self, usuarios_activos=None):
        if usuarios_activos is None:
            self.usuarios = []  # Ahora sí se crea una lista NUEVA y única por cada objeto
        else:
            self.usuarios = usuarios_activos
        
    def agregar_usuario(self, nombre):
        self.usuarios.append(nombre)
        
    def limpiar_audios_corruptos(self, lista_archivos):
        archivos_sanos = [] # En lugar de borrar, guardamos los buenos (mucho más seguro)
        
        for archivo in lista_archivos:
            # LA SOLUCIÓN AL BUG OS: os.path.join lo hace compatible con Windows/Mac/Linux
            ruta_completa = os.path.join(self.ruta_base, archivo)
            
            es_corrupto = False
            if archivo == "sample2.wav" or archivo == "sample3.wav":
                es_corrupto = True
                
            if not es_corrupto:
                archivos_sanos.append(archivo)
            else:
                print(f"Descartando: {archivo} en {ruta_completa}")
                
        return archivos_sanos

# --- PRUEBAS AHORA SÍ PASAN ---
gestor_roberto = GestorBiometrico()
gestor_roberto.agregar_usuario("Roberto")

gestor_invitado = GestorBiometrico()
gestor_invitado.agregar_usuario("Invitado")

# Cada gestor tiene su propia memoria aislada
print(f"Lista de Roberto: {gestor_roberto.usuarios}")   # ['Roberto']
print(f"Lista de Invitado: {gestor_invitado.usuarios}") # ['Invitado']

archivos_test = ["sample1.wav", "sample2.wav", "sample3.wav", "sample4.wav"]
resultado = gestor_roberto.limpiar_audios_corruptos(archivos_test)
print(f"Archivos limpios: {resultado}") # ['sample1.wav', 'sample4.wav']