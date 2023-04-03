from datetime import datetime as dt


class Invoice:
    broj = 'R-2023-123456'
    datum = dt.now()
    stavke = []
    
    def print_invoice(self):
        print(self.broj, self.datum, self.stavke)
        
    def __str__(self) -> str:
        return f'{self.broj}, {self.datum}, {self.stavke}'
        
    
    #'invoice_number': 'R/01/01/123456',
        #'invoice_date' : datetime.datetime.now(),
       # 'invoice_items' : [
       #     ['Monitor', 9.99],
      #      ['Laptop', 19.99],
      ##      ['Mis i Tipkovnica', 3.99],
      #      ['Torba', 6.99],
      #      ['Podloska za mis', 0.99],
      #      ['Slusalice', 4.99]
      #  ]



invoices = []

invoice = Invoice()
invoices.append(invoice)
invoice = Invoice()
invoices.append(invoice)


while True:
    
    # new_invopice = Invoice()
    # invoices.append(new_invoice)
    
    invoices.append(Invoice())
    next = input('Novi racun?')
    if next.lower() != 'da':
        break


for invoice_element in invoices:
    #print(invoice_element.broj, invoice_element.datum, invoice_element.stavke)
    print(invoice_element)


