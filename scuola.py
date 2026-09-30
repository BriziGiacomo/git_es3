class Scuola:
    def __init__(self):
        self.studenti = []

    def aggiungi_studente(self, studente: Studente):
        self.studenti.append(studente)

    def cerca_per_cognome(self, cognome: str) -> list:
        """Restituisce una lista di studenti che corrispondono al cognome cercato."""
        cognome_lower = cognome.lower()
        return [s for s in self.studenti if s.cognome.lower() == cognome_lower]

    def cerca_per_eta(self, eta: int) -> list:
        """Restituisce una lista di studenti con una specifica età."""
        return [s for s in self.studenti if s.eta == eta]

    def conteggio(self) -> int:
        """Restituisce il numero totale degli studenti iscritti."""
        return len(self.studenti)