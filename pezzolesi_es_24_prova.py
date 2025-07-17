class Film:
    def __init__(self, titolo:str, regista:str, anno_di_uscita:int, genere:str, valutazione:float):
        self.titolo = titolo
        self.regista = regista
        self.anno_di_uscita = anno_di_uscita
        self.genere = genere
        self.valutazione = valutazione

    def __str__(self):
        return f"Titolo:{self.titolo} Regista:{self.regista} Data di uscita:{self.anno_di_uscita} Genere:{self.genere} Valutazione:{self.valutazione}"

    def get_valutazione(self):
        return self.valutazione

class Libreria:
    def __init__(self):
        #Iniziallizzo la lista dei film vuota perchè non c'è ancora nessun film
        self.film = []

    def aggiungi_film(self, film:Film):
        self.film.append(film)

    def cerca_film(self, titolo:str):
        pass
        
    def visualizza_film(self):
        pass

    def calcola_valutazione_media(self):
        pass

def main():
    libreria = Libreria()

if __name__ == "__main__":
    main()
    