```mermaid
classDiagram
    class Volo{
    -numeroVolo: int
    -destinazione: str
    -dataOraPartenza: str
    -numeroMassimoPasseggeri: int

    }

    class Prenotazione{
    -nomePasseggero : str
    -tipoClasse: str
    -volo: str
    
    }