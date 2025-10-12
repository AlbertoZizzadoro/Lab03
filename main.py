from autonoleggio import Autonoleggio
from datetime import datetime, date
import sys

def menu():                                                       # mostra il menu principale
    print("\n--- MENU AUTONOLEGGIO ---")
    print("1. Modifica nome del responsabile dell’autonoleggio")
    print("2. Carica automobili da file")
    print("3. Aggiungi nuova automobile (da tastiera)")
    print("4. Visualizza automobili ordinate per marca")
    print("5. Noleggia automobile")
    print("6. Termina noleggio automobile")
    print("7. Esci")
    return input("Scegli un'opzione >> ")

def main():                                                       # funzione principale
    autonoleggio = Autonoleggio("Polito Rent", "Alessandro Visconti")   # crea l'autonoleggio

    while True:                                                   # ciclo principale
        scelta = menu()                                           # mostra menu e legge scelta

        if scelta == "1":                                         # modifica responsabile
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ")
            autonoleggio.responsabile = nuovo_responsabile
            print(f"Responsabile aggiornato a: {autonoleggio.responsabile}")

        elif scelta == "2":                                       # carica automobili da file
            while True:
                try:
                    file_path = input("Inserisci il path del file da caricare: ").strip()
                    autonoleggio.carica_file_automobili(file_path)
                    print(f"Caricamento da {file_path} completato.")
                    break
                except FileNotFoundError:
                    print(f"Errore: file non trovato all'indirizzo '{file_path}'. Riprova.")
                except Exception as e:
                    print(f"Errore durante il caricamento: {e}")
                    break

        elif scelta == "3":                                       # aggiungi nuova automobile
            marca = input("Marca: ")
            modello = input("Modello: ")

            try:
                anno = input("Anno di immatricolazione: ").strip()
                posti = input("Numero di posti (lascia vuoto se N/D): ").strip()
            except Exception:
                print("Errore durante l'inserimento dei dati.")
                continue

            try:
                automobile = autonoleggio.aggiungi_automobile(marca, modello, anno, posti)
                print(f"Automobile aggiunta: {automobile}")
            except Exception as e:
                print(f"Errore durante l'aggiunta: {e}")

        elif scelta == "4":                                       # mostra auto ordinate per marca
            print("\n--- Lista Automobili per Marca ---")
            automobili_ordinate = autonoleggio.automobili_ordinate_per_marca()

            if not automobili_ordinate:
                print("Nessuna automobile nella flotta.")
            else:
                for a in automobili_ordinate:
                    print(f"-> {a}")

        elif scelta == "5":                                       # noleggia un'auto
            id_auto = input("ID automobile: ").strip().upper()
            cognome_cliente = input("Cognome cliente: ").strip()
            data = date.today().isoformat()

            try:
                noleggio = autonoleggio.nuovo_noleggio(data, id_auto, cognome_cliente)
                print(f"Noleggio andato a buon fine: {noleggio}")
            except Exception as e:
                print(f"Errore noleggio: {e}")

        elif scelta == "6":                                       # termina noleggio
            codice_noleggio = input("ID noleggio da terminare: ").strip().upper()
            try:
                autonoleggio.termina_noleggio(codice_noleggio)
                print(f"Noleggio {codice_noleggio} terminato con successo.")
            except Exception as e:
                print(f"Errore terminazione: {e}")

        elif scelta == "7":                                       # uscita
            print("Uscita dal programma...")
            sys.exit(0)

        else:                                                     # scelta non valida
            print("Opzione non valida!")

if __name__ == "__main__":                                        # avvio programma
    main()
