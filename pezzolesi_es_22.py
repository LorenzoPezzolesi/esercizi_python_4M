class Automobile:
    def __init__(self, targa: str, modello: str, categoria: str, disponibile: bool):
        self.targa = targa
        self.modello = modello
        self.categoria = categoria
        self.disponibilita = disponibile

    def noleggia(self) -> bool:
        if self.disponibilita:
            self.disponibilita = False
            return True
        return False

    def restituisci(self) -> None:
        self.disponibilita = True

    def __str__(self) -> str:
        return f"Automobile {self.targa} ({self.modello}, {self.categoria}) - {'Disponibile' if self.disponibilita else 'Noleggiata'}"


class AgenziaNoleggio:
    def __init__(self):
        self.automobili = []
        self.noleggi = []

    def aggiungi_automobile(self, auto: Automobile) -> None:
        self.automobili.append(auto)

    def noleggia_automobile(self, targa: str) -> bool:
        for auto in self.automobili:
            if auto.targa == targa and auto.noleggia():
                self.noleggi.append(auto)
                return True
        return False

    def visualizza_automobili_disponibili(self) -> list:
        return [auto for auto in self.automobili if auto.disponibilita]

    def visualizza_noleggi(self) -> list:
        return self.noleggi