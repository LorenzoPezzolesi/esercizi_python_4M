class Veicolo:
    """Classe base per tutti i veicoli della flotta"""
    
    def __init__(self, marca, modello, carburante):
        """
        Inizializza un veicolo con marca, modello e tipo di carburante
        
        Args:
            marca (str): La marca del veicolo
            modello (str): Il modello del veicolo
            carburante (str): Il tipo di carburante (benzina o diesel)
        """
        self._marca = marca
        self._modello = modello
        self._carburante = carburante
    
    def get_marca(self):
        """Restituisce la marca del veicolo"""
        return self._marca
    
    def get_modello(self):
        """Restituisce il modello del veicolo"""
        return self._modello
    
    def get_carburante(self):
        """Restituisce il tipo di carburante del veicolo"""
        return self._carburante
    
    def __str__(self):
        """Restituisce una rappresentazione string del veicolo"""
        return f"Veicolo: {self._marca} {self._modello} - Carburante: {self._carburante}"


class Auto(Veicolo):
    """Classe per le automobili della flotta"""
    
    def __init__(self, marca, modello, carburante):
        """
        Inizializza un'automobile
        
        Args:
            marca (str): La marca dell'auto
            modello (str): Il modello dell'auto
            carburante (str): Il tipo di carburante (benzina o diesel)
        """
        super().__init__(marca, modello, carburante)
    
    def __str__(self):
        """Restituisce una rappresentazione string dell'auto"""
        return f"Auto: {self._marca} {self._modello} - Carburante: {self._carburante}"


class Camion(Veicolo):
    """Classe per i camion della flotta"""
    
    def __init__(self, marca, modello, carburante):
        """
        Inizializza un camion
        
        Args:
            marca (str): La marca del camion
            modello (str): Il modello del camion
            carburante (str): Il tipo di carburante (benzina o diesel)
        """
        super().__init__(marca, modello, carburante)
    
    def __str__(self):
        """Restituisce una rappresentazione string del camion"""
        return f"Camion: {self._marca} {self._modello} - Carburante: {self._carburante}"


class Flotta:
    """Classe per gestire la flotta aziendale di veicoli"""
    
    def __init__(self):
        """Inizializza una flotta vuota"""
        self._veicoli = []
    
    def aggiungi_veicolo(self, veicolo):
        """
        Aggiunge un veicolo alla flotta
        
        Args:
            veicolo (Veicolo): Il veicolo da aggiungere alla flotta
        """
        if isinstance(veicolo, Veicolo):
            self._veicoli.append(veicolo)
            print(f"Veicolo aggiunto alla flotta: {veicolo}")
        else:
            print("Errore: Il veicolo deve essere un'istanza della classe Veicolo")
    
    def visualizza_flotta(self):
        """Visualizza tutti i veicoli presenti nella flotta"""
        if not self._veicoli:
            print("La flotta è vuota")
            return
        
        print("\n=== FLOTTA AZIENDALE ===")
        print(f"Numero totale di veicoli: {len(self._veicoli)}")
        print("-" * 50)
        
        for i, veicolo in enumerate(self._veicoli, 1):
            print(f"{i}. {veicolo}")
        
        print("-" * 50)
    
    def get_numero_veicoli(self):
        """Restituisce il numero totale di veicoli nella flotta"""
        return len(self._veicoli)
    
    def get_veicoli_per_tipo(self, tipo):
        """
        Restituisce una lista di veicoli di un determinato tipo
        
        Args:
            tipo (str): Il tipo di veicolo ('Auto' o 'Camion')
            
        Returns:
            list: Lista dei veicoli del tipo specificato
        """
        veicoli_tipo = []
        for veicolo in self._veicoli:
            if veicolo.__class__.__name__ == tipo:
                veicoli_tipo.append(veicolo)
        return veicoli_tipo


# Esempio di utilizzo del sistema
if __name__ == "__main__":
    # Creazione della flotta
    flotta_aziendale = Flotta()
    
    # Creazione di alcuni veicoli
    auto1 = Auto("Toyota", "Corolla", "benzina")
    auto2 = Auto("Volkswagen", "Golf", "diesel")
    auto3 = Auto("BMW", "Serie 3", "benzina")
    
    camion1 = Camion("Mercedes", "Actros", "diesel")
    camion2 = Camion("Iveco", "Daily", "diesel")
    
    # Aggiunta dei veicoli alla flotta
    print("=== AGGIUNTA VEICOLI ALLA FLOTTA ===")
    flotta_aziendale.aggiungi_veicolo(auto1)
    flotta_aziendale.aggiungi_veicolo(auto2)
    flotta_aziendale.aggiungi_veicolo(auto3)
    flotta_aziendale.aggiungi_veicolo(camion1)
    flotta_aziendale.aggiungi_veicolo(camion2)
    
    # Visualizzazione della flotta completa
    flotta_aziendale.visualizza_flotta()
    
    # Statistiche della flotta
    print(f"\nNumero totale di veicoli: {flotta_aziendale.get_numero_veicoli()}")
    
    # Visualizzazione per tipo di veicolo
    auto_in_flotta = flotta_aziendale.get_veicoli_per_tipo("Auto")
    camion_in_flotta = flotta_aziendale.get_veicoli_per_tipo("Camion")
    
    print(f"\nNumero di auto: {len(auto_in_flotta)}")
    print(f"Numero di camion: {len(camion_in_flotta)}")
    
    print("\n=== DETTAGLI AUTO ===")
    for auto in auto_in_flotta:
        print(f"- {auto}")
    
    print("\n=== DETTAGLI CAMION ===")
    for camion in camion_in_flotta:
        print(f"- {camion}")