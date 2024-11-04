class Piatto:

    def __init__(self,nome: str,prezzo: float,disponibile:bool):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = disponibile















class Piatto:
    ...
    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'}"

# Esempio di utilizzo
antipasto = Antipasto("Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola")
primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

piatti_ordinati = [antipasto, primo, secondo, dolce]
conto_totale = calcola_conto(piatti_ordinati)
print(f"Il conto totale è: {conto_totale}€")  # Output: Il conto totale è: 48.0€

print("\nMenu del Ristorante:")
stampa_menu(piatti_ordinati)