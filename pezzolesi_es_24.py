class Libreria:

    def __init__(self):
        pass

class Film:

    def __init__(self, titolo, regista, anno, genere):
        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.genere = genere

    def __str__(self):
        return f"{self.titolo} ({self.anno}) di {self.regista} - {self.genere}"

