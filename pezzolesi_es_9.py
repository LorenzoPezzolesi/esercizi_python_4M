class Libro:
    def __init__(self,titolo,autore,pagine):
        self._titolo = titolo
        self._autore = autore
        self._pagine = pagine
    @property
    def titolo (self) -> bool|str: 
        if self._titolo != None:
            
            return self._titolo
        return False
    @property
    def autore (self) -> bool|str:
        if self._autore != None:
            return self._autore
        return False
        
    @property
    def pagine (self) -> bool|int:
        if self._pagine != None:
            return self._pagine
        return False
        
    @titolo.setter
    def titolo (self,nuovo_titolo:str) -> bool:
        if self._titolo != '':
            self._titolo = nuovo_titolo
            return True
        return False
    @autore.setter
    def autore (self,nuovo_autore:str) -> bool:
        if self._autore != '':
            self._autore = nuovo_autore
            return True
        return False
    @pagine.setter
    def pagine (self,nuove_pagine:int) -> bool:
        if self._pagine > 0:
            self._pagine = nuove_pagine
            return True
        return False
                
# Esempio di utilizzo

libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
print(libro.titolo)  # Chiama automaticamente il getter
libro.titolo = "Lo Hobbit"  # Chiama automaticamente il setter
print(libro.titolo)