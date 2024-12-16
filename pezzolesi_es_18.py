class Allenatore:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.specializzazione})"


class Membro:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.allenatore = None
        self.corsi = []
        self.scheda_allenamento = None

    def set_allenatore(self, allenatore):
        self.allenatore = allenatore

    def set_scheda_allenamento(self, scheda):
        self.scheda_allenamento = scheda

    def iscrivi_corso(self, corso):
        self.corsi.append(corso)

    def __str__(self):
        corsi_nome = [corso.nome for corso in self.corsi]
        scheda = ", ".join(self.scheda_allenamento.esercizi) if self.scheda_allenamento else "Nessuna"
        return f"{self.nome} {self.cognome}, Allenatore: {self.allenatore}, Corsi: {', '.join(corsi_nome)}, Scheda: {scheda}"


class Corso:
    def __init__(self, nome, durata, allenatore):
        self.nome = nome
        self.durata = durata
        self.allenatore = allenatore
        self.membri = []

    def aggiungi_membro(self, membro):
        self.membri.append(membro)
        membro.iscrivi_corso(self)

    def __str__(self):
        return f"{self.nome} ({self.durata}), Insegnato da {self.allenatore}"


class SchedaAllenamento:
    def __init__(self, membro, esercizi):
        self.membro = membro
        self.esercizi = esercizi

    def __str__(self):
        return ", ".join(self.esercizi)


def main():
    # Creazione degli allenatori
    allenatore1 = Allenatore("Giovanni", "Rossi", "Fitness")
    allenatore2 = Allenatore("Luca", "Bianchi", "Yoga")

    # Creazione dei membri
    membro1 = Membro("Anna", "Verdi")
    membro2 = Membro("Marco", "Neri")

    # Assegnazione degli allenatori ai membri
    membro1.set_allenatore(allenatore1)
    membro2.set_allenatore(allenatore2)

    # Creazione dei corsi
    corso1 = Corso("Pilates", "3 mesi", allenatore1)
    corso2 = Corso("HIIT", "6 mesi", allenatore1)
    corso3 = Corso("Yoga Avanzato", "4 mesi", allenatore2)

    # Iscrizione dei membri ai corsi
    corso1.aggiungi_membro(membro1)
    corso2.aggiungi_membro(membro1)
    corso3.aggiungi_membro(membro2)

    # Creazione delle schede di allenamento
    scheda1 = SchedaAllenamento(membro1, ["Esercizio 1: Squat", "Esercizio 2: Push-up"])
    scheda2 = SchedaAllenamento(membro2, ["Esercizio 1: Plank", "Esercizio 2: Burpee"])

    # Assegnazione delle schede di allenamento ai membri
    membro1.set_scheda_allenamento(scheda1)
    membro2.set_scheda_allenamento(scheda2)

    # Stampa delle informazioni
    print(membro1)
    print(membro2)


if __name__ == "__main__":
    main()
