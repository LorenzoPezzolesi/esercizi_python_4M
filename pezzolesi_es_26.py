class Veicolo:
    def __init__(self, marca, modello, carburante):
        self.marca = marca
        self.modello = modello
        self.carburante = carburante

    def __str__(self):
        return f"{self.marca} {self.modello} ({self.carburante})"

class Auto(Veicolo):
    pass

class Camion(Veicolo):
    pass

class Flotta:
    def __init__(self):
        self.veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self.veicoli.append(veicolo)

    def visualizza_veicoli(self):
        for veicolo in self.veicoli:
            print(veicolo)


def main():
    flotta = Flotta()

    while True:
        print("\nMenu Flotta Veicoli:")
        print("1. Aggiungi Veicolo")
        print("2. Visualizza Veicoli")
        print("3. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            tipo = input("Tipo di veicolo (auto/camion): ").lower()
            marca = input("Marca: ")
            modello = input("Modello: ")
            carburante = input("Carburante (benzina/diesel): ")

            if tipo == "auto":
                veicolo = Auto(marca, modello, carburante)
            elif tipo == "camion":
                veicolo = Camion(marca, modello, carburante)
            else:
                print("Tipo di veicolo non valido.")
                continue

            flotta.aggiungi_veicolo(veicolo)
            print("Veicolo aggiunto con successo.")

        elif scelta == "2":
            flotta.visualizza_veicoli()

        elif scelta == "3":
            break

        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
