```mermaid
classDiagram    
    class SistemaTrading {
    - rischio: float
    - lista_crypto: list
    - saldo: float 
    - aggiorna_il_saldo()
    + compra_crypto(crypto, rischio)
    + vendi_crypto(crypto, rischio)
    + leggi_api() crypto
    }

    class RiskManager {
    + take_profit: float
    + stop_loss: float
    - calcola_rischio(take_profit, stop_loos) rischio_calcolato
    
    }

    class Strategy {
    - nome: str 
    - logiche: dict
    + analizza_i_dati()

    }



