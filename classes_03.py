from datetime import datetime as dt


class Invoice:
    def __init__(self,number, date, vat_rate) -> None:
        self.number = number
        self.date = date
        self.vat_rate = vat_rate
        
    def __str__(self) -> str:
        return f'Broj racuna: {self.number}; datum: {self.date}; PDV: {self.vat_rate}'
    
invoices = []

while True:
    invoice_number = input('Upisite broj racuna: ')
    invoice_date = dt.now()
    invoice_vat_rate = input('Upisite stopu PDV-a: ')
    
    invoice = Invoice()
        

