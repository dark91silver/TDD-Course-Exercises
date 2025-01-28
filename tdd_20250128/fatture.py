import datetime

from models import Fattura
import errors

required_fields = ["emitted", "recipient", "fiscal_code", "vat", "payment_4", "payment_10", "payment_22"]

def create(fattura: dict):
    pass

def update(fattura: dict):
    pass

def delete(id: int):
    pass

def read(id: int):
    pass
