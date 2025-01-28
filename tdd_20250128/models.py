import datetime

class Fattura():
    id: int
    emitted: datetime
    recipient: str
    fiscal_code: str
    vat: str
    payment_4: float #imponibile 4%
    payment_10: float #imponibile 10%
    payment_22: float #imponibile 22%
    tax_4: float = 0.0 #imposta 4%
    tax_10: float = 0.0 #imposta 10%
    tax_22: float = 0.0 #imposta 22%
    total: float = 0.0 #totale

    def __init__(self, id: int, emitted: datetime, recipient: str, fiscal_code: str, vat: str,
                 payment_4: float, payment_10: float, payment_22: float):
        self.id = id
        self.emitted = emitted
        self.recipient = recipient
        self.fiscal_code = fiscal_code,
        self.vat = vat
        self.payment_4 = payment_4
        self.payment_10 = payment_10
        self.payment_22 = payment_22
        self.calculate_tax_4()
        self.calculate_tax_10()
        self.calculate_tax_22()
        self.calculate_total()

    def calculate_tax_4(self):
        if self.payment_4 > 0.0:
            self.tax_4 = self.payment_4 / 0.04
    
    def calculate_tax_10(self):
        if self.payment_10 > 0.0:
            self.tax_10 = self.payment_10 / 0.1
    
    def calculate_tax_22(self):
        if self.payment_22 > 0.0:
            self.tax_22 = self.payment_22 / 0.22

    def calculate_total(self):
        return sum([self.payment_4, self.tax_4, self.payment_10, self.tax_10, self.payment_22, self.tax_22])
    


