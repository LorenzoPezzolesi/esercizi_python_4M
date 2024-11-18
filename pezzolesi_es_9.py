class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    @property
    def titolo(self):
        return self._titolo
    
    @titolo.setter
    def titolo(self, valore):
        if not valore or not isinstance(valore, str):
            raise ValueError("Il titolo non può essere vuoto e deve essere una stringa.")
        self._titolo = valore
    
    @property
    def autore(self):
        return self._autore
    
    @autore.setter
    def autore(self, valore):
        if not valore or not isinstance(valore, str):
            raise ValueError("L'autore non può essere vuoto e deve essere una stringa.")
        self._autore = valore
    
    @property
    def pagine(self):
        return self._pagine
    
    @pagine.setter
    def pagine(self, valore):
        if not isinstance(valore, int) or valore <= 0:
            raise ValueError("Il numero di pagine deve essere un numero positivo.")
        self._pagine = valore


# Esempio di utilizzo

libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
print(libro.titolo)
libro.titolo = "Lo Hobbit"
print(libro.titolo)
