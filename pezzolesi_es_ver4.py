from datetime import datetime

class Animale:
    def __init__(self, codiceIdentificativo, nome, eta, peso):
        self.codiceIdentificativo = codiceIdentificativo
        self.nome = nome
        self.eta = eta
        self.peso = peso
        self.habitat = None

class Mammifero(Animale):
    def __init__(self, codiceIdentificativo, nome, eta, peso, tipoPelliccia, temperaturaCorpo, periodoGestazione):
        super().__init__(codiceIdentificativo, nome, eta, peso)
        self.tipoPelliccia = tipoPelliccia
        self.temperaturaCorpo = temperaturaCorpo
        self.periodoGestazione = periodoGestazione

class Rettile(Animale):
    def __init__(self, codiceIdentificativo, nome, eta, peso, velenoso):
        super().__init__(codiceIdentificativo, nome, eta, peso)
        self.velenoso = velenoso

class Habitat:
    def __init__(self, codiceArea, nome, dimensione):
        self.codiceArea = codiceArea
        self.nome = nome
        self.dimensione = dimensione
        self.animali = []

class Veterinario:
    def __init__(self, matricola, nome, cognome, specializzazione, anniEsperienza):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione
        self.anniEsperienza = anniEsperienza

    def effettua_visita(self, animale, diagnosi, trattamentoProposto):
        return VisitaVeterinaria(datetime.now(), self, animale, diagnosi, trattamentoProposto)

class VisitaVeterinaria:
    def __init__(self, data, veterinario, animale, diagnosi, trattamentoProposto):
        self.data = data
        self.veterinario = veterinario
        self.animale = animale
        self.diagnosi = diagnosi
        self.trattamentoProposto = trattamentoProposto

class SistemaGestioneZoo:
    def __init__(self):
        self.animali = []
        self.habitats = []
        self.veterinari = []
        self.visiteVeterinarie = []

    def aggiungi_animale(self, animale):
        self.animali.append(animale)

    def rimuovi_animale(self, animale):
        if animale in self.animali:
            self.animali.remove(animale)
            if animale.habitat:
                animale.habitat.animali.remove(animale)

    def assegna_habitat(self, animale, habitat):
        if animale.habitat is not None:
            return False
        if len(habitat.animali) == 0 or all(type(a) == type(animale) for a in habitat.animali):
            habitat.animali.append(animale)
            animale.habitat = habitat
            return True
        return False

    def registra_visita(self, visita):
        self.visiteVeterinarie.append(visita)

    def get_animali_habitat(self, habitat):
        return habitat.animali

    def get_storico_visite(self, animale):
        return [visita for visita in self.visiteVeterinarie if visita.animale == animale]

    def calcola_eta_media_per_habitat(self):
        eta_media_per_habitat = {}
        for habitat in self.habitats:
            if len(habitat.animali) > 0:
                eta_media_per_habitat[habitat.nome] = sum(animale.eta for animale in habitat.animali) / len(habitat.animali)
            else:
                eta_media_per_habitat[habitat.nome] = 0
        return eta_media_per_habitat

def main():
    # Creazione del sistema
    zoo = SistemaGestioneZoo()

    # Creazione degli habitat
    savana = Habitat("Habitat001", "Savana Africana", 1000.0)
    rettilario = Habitat("Habitat002", "Rettilario", 500.0)
    zoo.habitats.extend([savana, rettilario])

    # Creazione dei veterinari
    vet1 = Veterinario("Veterinario001", "Mario", "Rossi", "Mammiferi", 10)
    vet2 = Veterinario("Veterinario002", "Laura", "Bianchi", "Rettili", 8)
    zoo.veterinari.extend([vet1, vet2])

    # Creazione degli animali
    leone = Mammifero("Mammifero001", "Simba", 5, 180.0, "Folta", 38.5, 110)
    serpente = Rettile("Rettile001", "Kaa", 3, 5.0, True)
    giraffa = Mammifero("Mammifero002", "Melman", 7, 800.0, "Maculata", 38.0, 450)

    # Aggiunta degli animali al sistema
    for animale in [leone, serpente, giraffa]:
        zoo.aggiungi_animale(animale)

    # Assegnazione degli habitat
    zoo.assegna_habitat(leone, savana)
    zoo.assegna_habitat(giraffa, savana)
    success = zoo.assegna_habitat(serpente, savana)
    print("\nTentativo di mettere serpente in savana:", "Riuscito" if success else "Fallito")
    zoo.assegna_habitat(serpente, rettilario)

    # Effettuazione delle visite veterinarie
    visita1 = vet1.effettua_visita(leone, "Controllo di routine", "Somministrazione vaccino annuale")
    zoo.registra_visita(visita1)

    visita2 = vet2.effettua_visita(serpente, "Infezione batterica", "Antibiotico per 7 giorni")
    zoo.registra_visita(visita2)

    # Stampa delle informazioni
    print("\n=== Stato dello Zoo ===")

    print("\nAnimali nella Savana:")
    for animale in zoo.get_animali_habitat(savana):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nAnimali nel Rettilario:")
    for animale in zoo.get_animali_habitat(rettilario):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nEtà media per habitat:")
    for habitat, eta_media in zoo.calcola_eta_media_per_habitat().items():
        print(f"- {habitat.nome}: {eta_media:.1f} anni")

    print("\nStorico visite di Simba:")
    for visita in zoo.get_storico_visite(leone):
        print(f"- Data: {visita.data}")
        print(f"  Veterinario: {visita.veterinario.nome} {visita.veterinario.cognome}")
        print(f"  Diagnosi: {visita.diagnosi}")
        print(f"  Trattamento: {visita.trattamentoProposto}")

if __name__ == "__main__":
    main()