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


def main():
    scuola = Scuola()
    
    # Aggiungiamo qualche studente di prova
    scuola.aggiungi_studente(Studente("Mario", "Rossi", 15, "Roma"))
    scuola.aggiungi_studente(Studente("Anna", "Bianchi", 17, "Milano"))
    scuola.aggiungi_studente(Studente("Luca", "Verdi", 16, "Torino"))

    while True:
        print("\n--- GESTIONE SCUOLA ---")
        print("1. Aggiungi studente")
        print("2. Cerca per cognome")
        print("3. Cerca per età")
        print("4. Mostra conteggio studenti")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione (1-5): ").strip()

        if scelta == "1":
            nome = input("Inserisci il nome: ").strip()
            cognome = input("Inserisci il cognome: ").strip()
            try:
                eta = int(input("Inserisci l'età: "))
                citta = input("Inserisci la città di residenza: ").strip()
                nuovo_studente = Studente(nome, cognome, eta, citta)
                scuola.aggiungi_studente(nuovo_studente)
                print("Studente aggiunto con successo!")
            except ValueError:
                print("Errore: L'età deve essere un numero intero valido.")

        elif scelta == "2":
            cognome_cercato = input("Inserisci il cognome da cercare: ").strip()
            risultati = scuola.cerca_per_cognome(cognome_cercato)
            if risultati:
                print(f"\nTrovati {len(risultati)} studenti:")
                for s in risultati:
                    print(f"- {s}")
            else:
                print("Nessuno studente trovato con questo cognome.")

        elif scelta == "3":
            try:
                eta_cercata = int(input("Inserisci l'età da cercare: "))
                risultati = scuola.cerca_per_eta(eta_cercata)
                if risultati:
                    print(f"\nTrovati {len(risultati)} studenti:")
                    for s in risultati:
                        print(f"- {s}")
                else:
                    print("Nessuno studente trovato con questa età.")
            except ValueError:
                print("Errore: Inserisci un numero valido per l'età.")

        elif scelta == "4":
            print(f"Numero totale studenti iscritti: {scuola.conteggio()}")

        elif scelta == "5":
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()