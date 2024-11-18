class Piatto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = True
    
    def get_nome(self):
        return self.nome
    
    def get_prezzo(self):
        return self.prezzo
    
    def is_disponibile(self):
        return self.disponibile
    
    def ordina(self):
        if self.disponibile:
            self.disponibile = False
        else:
            print(f"{self.nome} , non è disponibile per l'ordinazione.")
    
    def disponi(self):
        if not self.disponibile:
            self.disponibile = True
        else:
            print(f"{self.nome} , è già disponibile.")
    
    @staticmethod
    def ricerca(piatti, nome=None, prezzo=None):
        risultati = []
        for piatto in piatti:
            if (nome and nome.lower() in piatto.get_nome().lower()) or (prezzo and prezzo == piatto.get_prezzo()):
                risultati.append(piatto)
        return risultati
    
    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'}"

class Antipasto(Piatto):
    def __init__(self, nome, prezzo, ingredienti, porzione):
        super().__init__(nome, prezzo)
        self.ingredienti = ingredienti
        self.porzione = porzione
    
    def get_ingredienti(self):
        return self.ingredienti
    
    def get_porzione(self):
        return self.porzione

class Primo(Piatto):
    def __init__(self, nome, prezzo, tipo_pasta, sugo):
        super().__init__(nome, prezzo)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo
    
    def get_tipo_pasta(self):
        return self.tipo_pasta
    
    def get_sugo(self):
        return self.sugo

class Secondo(Piatto):
    def __init__(self, nome, prezzo, tipo_carne, cottura):
        super().__init__(nome, prezzo)
        self.tipo_carne = tipo_carne
        self.cottura = cottura
    
    def get_tipo_carne(self):
        return self.tipo_carne
    
    def get_cottura(self):
        return self.cottura

class Dolce(Piatto):
    def __init__(self, nome, prezzo, tipo_dolce, calorie):
        super().__init__(nome, prezzo)
        self.tipo_dolce = tipo_dolce
        self.calorie = calorie
    
    def get_tipo_dolce(self):
        return self.tipo_dolce
    
    def get_calorie(self):
        return self.calorie

def calcola_conto(piatti_ordinati):
    totale = 0
    for piatto in piatti_ordinati:
        totale += piatto.get_prezzo()
    return totale

def stampa_menu(piatti):
    for piatto in piatti:
        print(piatto)


# Esempio di utilizzo

antipasto = Antipasto("Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola")
primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

piatti_ordinati = [antipasto, primo, secondo, dolce]

conto_totale = calcola_conto(piatti_ordinati)
print(f"Il conto totale è: {conto_totale}€")

print("\nMenu del Ristorante:")
stampa_menu(piatti_ordinati)
