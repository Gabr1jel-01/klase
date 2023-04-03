import datetime


def create_invoice():
    pass

def print_invoice():
    pass

invoices = []
invoice = {
        'invoice_number': 'R/01/01/123456',
        'invoice_date' : datetime.datetime.now(),
        'invoice_items' : [
            ['Monitor', 9.99],
            ['Laptop', 19.99],
            ['Mis i Tipkovnica', 3.99],
            ['Torba', 6.99],
            ['Podloska za mis', 0.99],
            ['Slusalice', 4.99]
        ]
    }
    

invoices.append(invoice)

invoice['invoice_number'] = 'R/01/01/123457'

invoices.append(invoice)

#print(invoice_number)
#print(invoice_date)

#for item_name, item_price in invoice_items:
    #print(item_name, item_price)