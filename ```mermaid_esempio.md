```mermaid
classDiagram
    class Allenatore {
        +String nome
        +String cognome
        +String specializzazione
        +allena(membro: Membro)
    }

    class Membro {
        +String nome
        +String cognome
        +List~Corso~ corsi
        +SchedaAllenamento schedaAllenamento
        +set_allenatore(allenatore: Allenatore)
        +set_scheda_allenamento(scheda: SchedaAllenamento)
        +iscrivi_corso(corso: Corso)
    }

    class Corso {
        +String nome
        +String durata
        +Allenatore allenatore
        +List~Membro~ membri
    }

    class SchedaAllenamento {
        +Membro membro
        +List~String~ esercizi
    }

    Allenatore "1" -- "0..*" Membro : allena
    Membro "1" -- "0..*" Corso : iscrizione
    Membro "1" -- "1" SchedaAllenamento : ha
    Corso "1" -- "0..*" Membro : iscrizione
    Corso "1" -- "1" Allenatore : insegnato da

