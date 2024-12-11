class Studente: pass

class Corso:
    def __init__(self,nome:str,superficie:float):
        self.studenti = set[Studente]()

    def aggiungi_studente(self,studente: Studente):
        if not studente in self.studenti:
            self.studenti.add(studente)
            studente.aggiungi_corso(self)

class Studente:
    def __init__(self,):
        self.corsi = set[Corso]()

    def aggiungi_corso(self,corso: Corso):
        if not corso in self.corsi:
            self.corsi.add(corso)
            corso.aggiungi_studente(self)