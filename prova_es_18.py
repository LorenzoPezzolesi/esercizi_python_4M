from datetime import datetime
class Allenatore:
    def __init__(self,nome:str,cognome:str,specializzazione:str):
        self.nome= nome
        self.cognome= cognome
        self.specializzazione=specializzazione

class Membro:
    def __init__(self,nome:str,cognome:str,corsi:list[str]):
        self.nome = nome
        self.cognome=cognome
        self.corsi=corsi

class Corso:
    def __init__(self,nome:str,durata:datetime,iscritti_corsi:str):
        self.nome=nome
        self.durata=durata
        self.iscritti_corsi= iscritti_corsi
    
class Scheda_di_allenamento:
    def __init__(self,lista_esercizi:list[str],descrizione_esercizi:str):
        self.lista_esercizi= lista_esercizi
        self.descrizione_esercizi=descrizione_esercizi
    

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
    membro1.iscrivi_corso(corso1)
    membro1.iscrivi_corso(corso2)
    membro2.iscrivi_corso(corso3)

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