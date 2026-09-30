class Studente:
    def __init__(self, nome: str, cognome: str, eta: int, citta_residenza: str):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta_residenza = citta_residenza

    def classificazione(self) -> str:
        """Classifica lo studente in Biennio o Triennio in base all'età."""
        if self.eta <= 16:
            return "Biennio"
        else:
            return "Triennio"

    def __str__(self) -> str:
        return (f"Studente: {self.nome} {self.cognome}, "
                f"Età: {self.eta}, Città: {self.citta_residenza} "
                f"[{self.classificazione()}]")





