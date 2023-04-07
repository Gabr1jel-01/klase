
def funkcija(parametar):
    print(parametar)






class Primjer:
    def metoda(self):
        print('Pozdrav')
        
        
        
primjer_objekt = Primjer()
#Primjer.metoda()

primjer_objekt.metoda() # ako koristimo self u def metoda onda ovako a ako ne onda samo Primjer.metoda()