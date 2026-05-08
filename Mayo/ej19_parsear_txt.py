from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. DATOS EN CRUDO (Simulando el asignaturas.txt)
# Formato: Nombre | Descripción | Sector
datos_txt = """Matematicas I|Fundamentos de algebra lineal, matrices, calculo diferencial y su aplicacion en la ingenieria para resolver problemas fisicos.|general
Programacion 1|Introduccion a la logica algoritmica, estructuras de control, bucles y programacion orientada a objetos usando Python y Java.|informatica
Señales y Sistemas|Analisis matematico de señales continuas y discretas, uso de transformadas de Fourier y diseño de filtros analogicos y digitales.|teleco
Diseño de Interfaces|Creacion de experiencias de usuario (UX/UI), prototipado interactivo en Figma y psicologia del color para el diseño de aplicaciones.|tecnologias creativas
Fisica Basica|Estudio de la mecanica clasica, electromagnetismo y termodinamica aplicada al comportamiento de los materiales y la tecnologia.|general
Bases de Datos|Modelado entidad-relacion, lenguaje SQL avanzado, normalizacion y diseño de arquitecturas de almacenamiento seguras y robustas.|informatica
Antenas y Propagacion|Estudio de ondas electromagneticas, diseño de antenas dipolo y sistemas de microondas para comunicaciones inalambricas a larga distancia.|teleco
Animacion 3D|Modelado poligonal, rigging de personajes y renderizado de iluminacion utilizando herramientas estandar de la industria como Blender y Unity.|tecnologias creativas
Sistemas Operativos|Gestion de memoria, procesos y concurrencia. Administracion de servidores Linux, scripting en bash y control de permisos de usuario.|informatica
Redes de Computadores|Protocolos TCP/IP, enrutamiento, creacion de APIs para comunicacion entre servicios y arquitecturas de red en la nube.|informatica
Desarrollo Web|Creacion de aplicaciones frontend y backend, uso de frameworks como React, Node.js y despliegue de servicios en la nube.|informatica
Ingenieria de Software|Patrones de diseño, metodologias agiles (Scrum), control de versiones con Git y despliegue de contenedores Docker en produccion.|informatica
Inteligencia Artificial|Fundamentos de Machine Learning, redes neuronales, procesamiento de datos y creacion de modelos predictivos usando Python.|informatica
Seguridad Informatica|Criptografia, hacking etico, analisis de vulnerabilidades en servidores y proteccion de datos contra ataques ciberneticos.|informatica
Comunicaciones Opticas|Estudio de la luz como medio de informacion, despliegue de redes de fibra optica y componentes optoelectronicos avanzados.|teleco
Sistemas de Radiocomunicacion|Modulacion de radiofrecuencia, transmisores, receptores y protocolos de transmision de datos por satelite y telefonia movil.|teleco
Acustica y Audio|Procesamiento digital de sonido, diseño de salas acusticas, transduccion y captura de audio para sistemas de telecomunicacion.|teleco
Teletrafico|Analisis estadistico de redes de telecomunicacion, dimensionado de canales de voz y datos, y gestion de calidad de servicio (QoS).|teleco
Sistemas Empotrados|Programacion de microcontroladores, diseño de placas PCB, hardware de bajo nivel y sistemas de tiempo real para el Internet de las Cosas (IoT).|teleco
Redes Inalambricas|Estandares Wi-Fi, Bluetooth, 5G, planificacion celular y analisis de interferencias en entornos de alta densidad de usuarios.|teleco
Diseño de Videojuegos|Mecanicas de juego, narrativa interactiva, desarrollo de videojuegos usando motores graficos e inteligencia artificial para NPCs.|tecnologias creativas
Arte Concept y Storyboard|Dibujo digital, conceptualizacion de personajes, teoria de la composicion y creacion de guiones graficos para cine y animacion.|tecnologias creativas
Realidad Virtual y Aumentada|Desarrollo de entornos virtuales inmersivos, interaccion en 3D, programacion de shaders y visores de realidad mixta.|tecnologias creativas
Produccion Audiovisual|Edicion de video no lineal, etalonaje, postproduccion de efectos visuales (VFX) y composicion digital por nodos.|tecnologias creativas
Diseño de Sonido|Sintesis de audio, Foley, mezcla y masterizacion de bandas sonoras para medios interactivos y productos audiovisuales.|tecnologias creativas
Modelado y Escultura Digital|Esculpido de mallas de alta resolucion en ZBrush, retopologia, mapeado UV y texturizado avanzado para personajes y props 3D.|tecnologias creativas
Estadistica Aplicada|Estadistica avanzada, calculo de probabilidades, contraste de hipotesis y distribuciones numericas para el analisis cuantitativo de datos.|general
Calculo Multivariable|Derivadas parciales, integrales multiples, teoremas vectoriales y su aplicacion en el modelado de fenomenos fisicos y geometricos.|general
Quimica de Materiales|Estructura atomica, enlaces quimicos, propiedades de semiconductores, polimeros y su uso en la fabricacion de componentes tecnologicos.|general
Gestion de Empresas|Fundamentos de economia, organizacion empresarial, contabilidad, marketing y gestion de proyectos tecnologicos orientados al mercado.|general
Etica Profesional|Legislacion tecnologica, proteccion de datos (RGPD), propiedad intelectual y dilemas morales en el desarrollo de inteligencia artificial.|general
Expresion Grafica|Dibujo tecnico, geometria descriptiva, diseño asistido por ordenador (CAD) e interpretacion de planos de ingenieria.|general"""

# 2. DATOS NUEVOS A CLASIFICAR (Descripciones del nuevo Máster)
nuevas_descripciones = [
    "Desarrollo de videojuegos usando motores graficos, texturizado de entornos virtuales y programacion de shaders.",
    "Creacion de APIs RESTful en la nube, despliegue de contenedores Docker y gestion de servidores Linux.",
    "Estudio de fibra optica, modulacion de radiofrecuencia y protocolos de transmision de datos por satelite.",
    "Estadistica avanzada, calculo de probabilidades y distribuciones numericas para el analisis cuantitativo."
]

# --- 1. TU FUNCIÓN DE EXTRACCIÓN ---
def parsear_txt(texto_crudo):
    descripciones = []
    sectores = []
    for linea in datos_txt.splitlines():
        _, descripcion, sector = linea.split("|")
        descripciones.append(descripcion)
        sectores.append(sector)
    
    return descripciones, sectores

# --- 2. TU CLASE DE INTELIGENCIA ARTIFICIAL ---
class ClasificadorAsignaturas:
    def __init__(self):
        self.vectorizador=CountVectorizer()
        self.model=MultinomialNB()

    def entrenar(self, descripciones, etiquetas):
        X = self.vectorizador.fit_transform(descripciones)
        self.model.fit(X, etiquetas)
        

    def predecir(self, nuevas_descripciones):
        X_nuevo = self.vectorizador.transform(nuevas_descripciones)
        return self.model.predict(X_nuevo)


# --- ORQUESTACIÓN (No tocar) ---
# 1. Preparamos los datos
X_train, y_train = parsear_txt(datos_txt.strip())

# 2. Entrenamos
ia_universidad = ClasificadorAsignaturas()
ia_universidad.entrenar(X_train, y_train)

# 3. Predecimos
resultados = ia_universidad.predecir(nuevas_descripciones)

print("--- CLASIFICACIÓN DEL MÁSTER ---")
for desc, sector in zip(nuevas_descripciones, resultados):
    print(f"[{sector.upper()}] -> {desc[:40]}...")

# RESULTADO ESPERADO MENTALMENTE:
# La 1ª debería ser TECNOLOGIAS CREATIVAS (habla de videojuegos, motores, shaders)
# La 2ª debería ser INFORMATICA (APIs, Docker, Linux)
# La 3ª debería ser TELECO (Fibra optica, modulacion, satelite)
# La 4ª debería ser GENERAL (Estadistica, probabilidades, calculo)