# Classi del sistema: utenti, video, playlist, abbonamenti e commenti

<<<<<<< HEAD
from datetime import *
from typing import Optional

class TipoAbbonamento:
    def __init__(self, nome: str, prezzo: float, durata: timedelta) -> None:
        self.nome = nome
        self.prezzo = prezzo
        self.durata = durata

class Utente:
    def __init__(self, nome: str, email: str, password: str) -> None:
        self.nome = nome
        self.email = email
        self.password = password
        self.abbonamento = None

    def acquista_abbonamento(self, tipo: TipoAbbonamento) -> None:
        self.abbonamento = AcquistoAbbonamento(tipo, datetime())

    def has_abbonamento_valido(self) -> bool:
        return self.abbonamento != None and self.abbonamento.is_attivo()

class Commento:
    def __init__(self, autore: Utente, testo: str) -> None:
        self.autore = autore
        self.testo = testo
        self.data = datetime()

class AcquistoAbbonamento:
    def __init__(self, tipo: TipoAbbonamento, inizio: datetime) -> None:
        self.tipo = tipo
        self.inizio = inizio

    def get_fine(self) -> datetime:
        return self.inizio + self.tipo.durata
    
    def is_attivo(self) -> bool:
        return datetime() <= self.get_fine()

class Video:
    def __init__(self, creatore: Utente, titolo: str, descrizione: str, url: str, durata: float, abbonamento_richiesto: Optional[TipoAbbonamento]) -> None:
        self.creatore = creatore
        self.titolo = titolo
        self.descrizione = descrizione
        self.url = url
        self.durata = durata
        self.abbonamento_richiesto = abbonamento_richiesto
        self.commenti = list[Commento]()

    def aggiungi_commento(self, commento: Commento) -> None:
        self.commenti.append(commento)

    def elimina_commento(self, commento: Commento) -> None:
        self.commenti.remove(commento)

class Playlist:
    def __init__(self, creatore: Utente, nome: str) -> None:
        self.creatore = creatore
        self.nome = nome
        self.video = list[Video]()

    def aggiungi_video(self, video: Video) -> None:
        self.video.append(video)

    def rimuovi_video(self, video: Video) -> None:
        self.video.remove(video)

def __main__() -> None:
    piero = Utente("Piero", "piero@gmail.com", "1234")
    luigi = Utente("Luigi", "luigi@gmail.com", "1234")

    video = Video(piero, "Test", "", "", 0, None)

    video.aggiungi_commento(Commento(luigi, "Ciao"))

    playlist = Playlist(luigi, "Preferiti")
    playlist.aggiungi_video(video)

    abbonamento_super = TipoAbbonamento("Super", 10, timedelta(days=30))
    print("Utente " + luigi.nome + " ha abbonamento " + luigi.abbonamento)
    luigi.acquista_abbonamento(abbonamento_super)
    print("Utente " + luigi.nome + " ha abbonamento " + luigi.abbonamento)

    video_2 = Video(piero, "Test 2", "", "", 0, abbonamento_super)

if __name__ == "__main__":
    __main__()
=======
from datetime import datetime, timedelta
from typing import Optional

class TipoAbbonamento:
    def __init__(self, nome: str, prezzo: float, durata: timedelta) -> None:
        self.nome = nome
        self.prezzo = prezzo
        self.durata = durata

class Utente:
    def __init__(self, nome: str, email: str, password: str) -> None:
        self.nome = nome
        self.email = email
        self.password = password
        self.abbonamento = None

    def acquista_abbonamento(self, tipo: TipoAbbonamento) -> None:
        self.abbonamento = AcquistoAbbonamento(tipo, datetime.now())

    def has_abbonamento_valido(self) -> bool:
        return self.abbonamento != None and self.abbonamento.is_attivo()

class Commento:
    def __init__(self, autore: Utente, testo: str) -> None:
        self.autore = autore
        self.testo = testo
        self.data = datetime.now()

class AcquistoAbbonamento:
    def __init__(self, tipo: TipoAbbonamento, inizio: datetime) -> None:
        self.tipo = tipo
        self.inizio = inizio

    def get_fine(self) -> datetime:
        return self.inizio + self.tipo.durata
    
    def is_attivo(self) -> bool:
        return datetime.now() <= self.get_fine()

class Video:
    def __init__(self, creatore: Utente, titolo: str, descrizione: str, url: str, durata: float, abbonamento_richiesto: Optional[TipoAbbonamento]) -> None:
        self.creatore = creatore
        self.titolo = titolo
        self.descrizione = descrizione
        self.url = url
        self.durata = durata
        self.abbonamento_richiesto = abbonamento_richiesto
        self.commenti = list[Commento]()

    def aggiungi_commento(self, commento: Commento) -> None:
        self.commenti.append(commento)

    def elimina_commento(self, commento: Commento) -> None:
        self.commenti.remove(commento)

class Playlist:
    def __init__(self, creatore: Utente, nome: str) -> None:
        self.creatore = creatore
        self.nome = nome
        self.video = list[Video]()

    def aggiungi_video(self, video: Video) -> None:
        self.video.append(video)

    def rimuovi_video(self, video: Video) -> None:
        self.video.remove(video)

def __main__() -> None:
    piero = Utente("Piero", "piero@gmail.com", "1234")
    luigi = Utente("Luigi", "luigi@gmail.com", "1234")

    video = Video(piero, "Test", "", "", 0, None)

    video.aggiungi_commento(Commento(luigi, "Ciao"))

    playlist = Playlist(luigi, "Preferiti")
    playlist.aggiungi_video(video)

    abbonamento_super = TipoAbbonamento("Super", 10, timedelta(days=30))
    print(f"Utente {luigi.nome} ha abbonamento {luigi.abbonamento}")
    luigi.acquista_abbonamento(abbonamento_super)
    print(f"Utente {luigi.nome} ha abbonamento {luigi.abbonamento}")

    video_2 = Video(piero, "Test 2", "", "", 0, abbonamento_super)

if __name__ == "__main__":
    __main__()