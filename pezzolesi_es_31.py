# Domanda composta da testo, opzioni e risposta corretta
class Domanda:
    def __init__(self, testo: str, opzioni: list[str], indice_risposta_corretta: int) -> None:
        self.testo = testo
        self.opzioni = opzioni
        self.indice_risposta_corretta = indice_risposta_corretta

# Quiz composto da domande
class Quiz:
    def __init__(self, domande: list[Domanda], punteggio_minimo: int) -> None:
        self.domande = domande
        self.punteggio_minimo = punteggio_minimo

class Persona:
    def __init__(self, nome: str, cognome: str) -> None:
        self.nome = nome
        self.cognome = cognome

class Docente(Persona):
    def __init__(self, nome: str, cognome: str) -> None:
        super().__init__(nome, cognome)
        self.corsi = list[Corso]()

class Studente(Persona):
    def __init__(self, nome: str, cognome: str) -> None:
        super().__init__(nome, cognome)
        self.corsi = list[Corso]()

# Corso composto da studenti, docente, titolo, descrizione e quiz finale
class Corso:
    def __init__(self, docente: Docente, titolo: str, descrizione: str, quiz: Quiz) -> None:
        self.studenti = list[Studente]()
        self.docente = docente
        self.docente.corsi.append(self)
        self.titolo = titolo
        self.descrizione = descrizione
        self.quiz = quiz

class TentativoQuiz:
    def __init__(self, corso: Corso, studente: Studente, indici_risposte_date: list[int]) -> None:
        self.corso = corso
        self.studente = studente
        self.indici_risposte_date = indici_risposte_date

    def valuta_risposte(self) -> int:
        numero_risposte_corrette = 0
        for indice_domanda in range(len(self.corso.quiz.domande)):
            domanda = self.corso.quiz.domande[indice_domanda]
            if domanda.indice_risposta_corretta == self.indici_risposte_date[indice_domanda]:
                numero_risposte_corrette += 1
        return numero_risposte_corrette
    
    def verifica_superamento(self) -> bool:
        return self.valuta_risposte() >= self.corso.quiz.punteggio_minimo
    
def main():
    pass

if __name__ == "__main__":
    main()
