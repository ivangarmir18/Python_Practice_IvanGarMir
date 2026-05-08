# IMPORTANTE: pip install scikit-learn

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# --- TUS DATOS DE ENTRENAMIENTO (El conocimiento histórico) ---
movimientos_historicos = [
    "CARGO UBER EATS MADRID", "COMPRA MERCADONA TICKET 123", 
    "RECIBO LUZ IBERDROLA", "AMAZON PRIME VIDEO", 
    "CARGO GLOVO BARCELONA", "COMPRA CARREFOUR EXPRES",
    "PAGO NETFLIX", "FACTURA AGUA CANAL", 
    "UBER TRIP MADRID", "COMPRA DIA SUPERMERCADO"
]

# Las etiquetas correspondientes a cada frase de arriba
etiquetas = [
    "COMIDA", "SUPERMERCADO", 
    "SUMINISTROS", "OCIO", 
    "COMIDA", "SUPERMERCADO",
    "OCIO", "SUMINISTROS", 
    "COMIDA", "SUPERMERCADO"
]

# --- LOS DATOS NUEVOS (Lo que la IA tiene que adivinar hoy) ---
nuevos_movimientos = [
    "COMPRA EN EL MERCADONA SUR 45",
    "CARGO MENSUAL NETFLIX.COM",
    "PEDIDO DE GLOVO",
    "RECIBO IBERDROLA FEBRERO"
]

class CategorizadorGastos:
    def __init__(self):
        self.vectorizador=CountVectorizer()
        self.model=MultinomialNB()

    def entrenar(self, textos, categorias):
        X = self.vectorizador.fit_transform(textos)
        self.model.fit(X, categorias)
        

    def predecir(self, nuevos_textos):
        X_nuevo = self.vectorizador.transform(nuevos_textos)
        return self.model.predict(X_nuevo)
        
# --- ORQUESTACIÓN Y PRUEBA ---
# Instanciamos nuestra IA
mi_ia = CategorizadorGastos()

# Le damos clases de contabilidad
mi_ia.entrenar(movimientos_historicos, etiquetas)

# Le pedimos que trabaje
predicciones = mi_ia.predecir(nuevos_movimientos)

# Mostramos los resultados
print("Resultados de la IA Contable:")
for movimiento, categoria in zip(nuevos_movimientos, predicciones):
    print(f"[{categoria}] <- {movimiento}")
    
# RESULTADO ESPERADO EXACTO:
# [SUPERMERCADO] <- COMPRA EN EL MERCADONA SUR 45
# [OCIO] <- CARGO MENSUAL NETFLIX.COM
# [COMIDA] <- PEDIDO DE GLOVO
# [SUMINISTROS] <- RECIBO IBERDROLA FEBRERO