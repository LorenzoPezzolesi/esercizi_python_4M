from datetime import datetime

class Profilo:
    def __init__(self, immagine: str, biografia: str):
        self.immagine = immagine
        self.biografia = biografia

class Utente:
    def __init__(self, nome_utente: str, email: str, password: str, profilo: Profilo):
        self.nome_utente = nome_utente
        self.email = email
        self.password = password
        self.profilo = profilo
        self.foto = []
        self.album = []
        self.seguaci = []

    def carica_foto(self, foto: 'Foto') -> None:
        self.foto.append(foto)

    def crea_album(self, album: 'Album') -> None:
        self.album.append(album)

    def segui(self, utente: 'Utente') -> None:
        self.seguaci.append(utente)

class Foto:
    def __init__(self, id: int, titolo: str, descrizione: str, data_caricamento: datetime, utente: Utente, album: 'Album'):
        self.id = id
        self.titolo = titolo
        self.descrizione = descrizione
        self.data_caricamento = data_caricamento
        self.utente = utente
        self.album = album
        self.commenti = []

    def aggiungi_commento(self, commento: 'Commento') -> None:
        self.commenti.append(commento)

class Album:
    def __init__(self, titolo: str, descrizione: str, utente: Utente):
        self.titolo = titolo
        self.descrizione = descrizione
        self.utente = utente
        self.foto = []

    def aggiungi_foto(self, foto: Foto) -> None:
        self.foto.append(foto)

class Commento:
    def __init__(self, id: int, testo: str, data: datetime, utente: Utente, foto: Foto):
        self.id = id
        self.testo = testo
        self.data = data
        self.utente = utente
        self.foto = foto