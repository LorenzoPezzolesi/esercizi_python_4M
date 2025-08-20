```mermaid
classDiagram
    class Allenatore:
        -nome: str
        -cognome: str
        -specializzazione: str

    class Membro:
        -nome: str
        -cognome: str

    class Corso:
        -nome: str
        -durata: datetime
        -iscritti_corsi: str

    class Scheda_di_allenamento:
        -lista_esercizi: list
        -descrizione_esercizi: str

Allenatore "1" --> "*" Membro
Membro "*" --> "*" Corso
Allenatore "1" --> "*" Corso
Scheda_di_allenamento "*" --> "*" Membro
