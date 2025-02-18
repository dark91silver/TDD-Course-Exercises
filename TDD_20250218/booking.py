from datetime import datetime
import json

class Prenotazione():
    arrivo: datetime
    partenza: datetime
    nome: str
    cognome: str
    telefono: str
    cf: str

def check_availability(a: datetime, p: datetime, camera: str):
    pass

def search(arrivo: str, partenza: str, filename: str | None = "hotel.json"):
    pass

def book(prenotazione: dict, camera: str, filename: str | None = "hotel.json"):
    pass
