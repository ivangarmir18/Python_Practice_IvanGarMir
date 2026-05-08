import copy
capital_inicial = 10000.0

senales_ia = [
    {"ticker": "AAPL", "precio": 150.0, "stop_loss": 140.0, "ai_score": 0.85},
    {"ticker": "TSLA", "precio": 200.0, "stop_loss": 180.0, "ai_score": 0.92},
    {"ticker": "AMZN", "precio": 100.0, "stop_loss": 95.0,  "ai_score": 0.78},
    {"ticker": "MSFT", "precio": 300.0, "stop_loss": 280.0, "ai_score": 0.88},
    {"ticker": "GOOG", "precio": 120.0, "stop_loss": 118.0, "ai_score": 0.95}
]

def gestor_de_cartera(capital:int, senales:list, risk_pct = 1, acciones_fraccionadas = True):
    risk = capital * (risk_pct / 100)
    capital_total = copy.copy(capital)
    scores_ia = [(senal.get("ai_score"),i) for i, senal in enumerate(senales)]
    scores_ia.sort(reverse = True)
    
    for _, index in scores_ia:
        ticker = senales[index].get("ticker")
        precio = senales[index].get("precio")
        stop_loss = senales[index].get("stop_loss")
        try:
            acciones = round(risk / (precio - stop_loss), 2) if acciones_fraccionadas else risk // (precio - stop_loss) 
            coste_total = acciones * precio
            if capital_total >= coste_total:
                capital_total = capital_total - coste_total
                print(f"Compra {acciones} Acciones de la empresa {ticker}.", f"Quedan {capital_total}€ disponibles.")
            else: 
                print(f"Saldo Insuficiente. La acción {ticker} tiene un coste de {coste_total}€ y te qquedan {capital_total} en la cuenta.")
        except TypeError:
            print(f"Error de tipo en los datos de la {index+1} fila, revisa los datos, saltando fila.")
            continue
        
    
        
        

# --- PRUEBA ---
print(gestor_de_cartera(capital_inicial, senales_ia))