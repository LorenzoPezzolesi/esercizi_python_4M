class Persona:
    def __init__(self, nome, eta, citta) -> None:
        self.nome = nome
        self.eta = eta
        self.citta = citta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}.")

    def descrizione(self):
        print(f"Ho {self.eta} anni e vivo a {self.citta}.")

persona = Persona("Simona", 52, "Pisa") 
persona.saluta()
persona.descrizione()