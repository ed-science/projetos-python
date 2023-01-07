from datetime import datetime

def today():
    return datetime.now()

def verify_date(date):
    try:
        return datetime.strptime(date, "%d-%m-%Y")
    except:
        raise Exception("Entrada inválida! Formato sugerido: D-M-Y. Exemplo: 01-09-2000")

def verify_due(date_ref):
    due_date = verify_date(date=date_ref)
    return "Data expirou..." if today() > due_date else "Data não expirou..."
