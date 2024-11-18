class MaterialeBiblioteca:
    def __init__(self, titolo, anno_pubblicazione):
        self.titolo = titolo
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = True  
    
    def get_titolo(self):
        return self.titolo
    
    def get_anno_pubblicazione(self):
        return self.anno_pubblicazione
    
    def is_disponibile(self):
        return self.disponibile
    
    def prestito(self):
        if self.disponibile:
            self.disponibile = False
        else:
            print(f"{self.titolo} , non è disponibile per il prestito.")
    
    def restituzione(self):
        if not self.disponibile:
            self.disponibile = True
        else:
            print(f"{self.titolo} , è già disponibile.")
    
    @staticmethod
    def ricerca(materiali, titolo):
        for materiale in materiali:
            if materiale.get_titolo().lower() == titolo.lower():
                return materiale
        return None

class Libro(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, autore, numero_pagine):
        super().__init__(titolo, anno_pubblicazione)
        self.autore = autore
        self.numero_pagine = numero_pagine
    
    # Metodi specifici per il libro
    def get_autore(self):
        return self.autore
    
    def get_numero_pagine(self):
        return self.numero_pagine

class Rivista(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, numero_edizione, mese_pubblicazione):
        super().__init__(titolo, anno_pubblicazione)
        self.numero_edizione = numero_edizione
        self.mese_pubblicazione = mese_pubblicazione
    
    # Metodi specifici per la rivista
    def get_numero_edizione(self):
        return self.numero_edizione
    
    def get_mese_pubblicazione(self):
        return self.mese_pubblicazione

class DVD(MaterialeBiblioteca):
    def __init__(self, titolo, anno_pubblicazione, regista, durata):
        super().__init__(titolo, anno_pubblicazione)
        self.regista = regista
        self.durata = durata

    def get_regista(self):
        return self.regista
    
    def get_durata(self):
        return self.durata

# Esempio di utilizzo

libro = Libro("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1178)
print(libro.get_titolo())  
print(libro.get_autore())  
libro.prestito()
print(libro.is_disponibile())
libro.restituzione()
print(libro.is_disponibile())

rivista = Rivista("National Geographic", 2023, 5, "Maggio")
print(rivista.get_titolo())
print(rivista.get_numero_edizione())

dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
print(dvd.get_titolo())
print(dvd.get_regista())

materiali = [libro, rivista, dvd]
risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
print(risultato.get_titolo())
