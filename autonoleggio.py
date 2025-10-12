import csv
from automobile import Automobile
from noleggio import Noleggio

class Autonoleggio:
    def __init__(self, nome, responsabile):
        # nome e responsabile dell’autonoleggio
        self.nome = nome
        self.responsabile = responsabile
        # liste per auto e noleggi attivi
        self.automobili = []
        self.noleggi_attivi = []

    def carica_file_automobili(self, file_path):
        # carica le auto da un file CSV
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                lettore = csv.reader(file)
                for riga in lettore:
                    codice = riga[0]
                    marca = riga[1]
                    modello = riga[2]
                    anno_immatricolazione = riga[3]
                    posti = riga[4]
                    auto = Automobile(codice, marca, modello, anno_immatricolazione, posti)
                    self.automobili.append(auto)
            return self.automobili
        except FileNotFoundError:
            print('File non trovato')

    def aggiungi_automobile(self, codice, marca, modello, anno_immatricolazione, posti):
        # aggiunge una nuova auto se non è già presente
        for automobile in self.automobili:
            if automobile.codice == codice:
                return 'Automobile già presente'
        auto_nuova = Automobile(codice, marca, modello, anno_immatricolazione, posti)
        self.automobili.append(auto_nuova)
        return auto_nuova

    def automobili_ordinate_per_marca(self):
        # restituisce le auto ordinate per marca
        return sorted(self.automobili, key=lambda automobile: automobile.marca)

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        # crea un nuovo noleggio se l’auto è disponibile
        auto_trovata = None
        for auto in self.automobili:
            if auto.codice == id_automobile:
                auto_trovata = auto
                break

        if auto_trovata is None:
            raise Exception(f"Auto con codice {id_automobile} non trovata")

        for noleggio in self.noleggi_attivi:
            if noleggio.id_automobile == id_automobile:
                raise Exception(f"Auto {id_automobile} già noleggiata")

        codice_noleggio = f"N{len(self.noleggi_attivi) + 1}"
        nuovo_noleggio = Noleggio(codice_noleggio, data, id_automobile, cognome_cliente)
        self.noleggi_attivi.append(nuovo_noleggio)
        return nuovo_noleggio

    def termina_noleggio(self, id_noleggio):
        # chiude un noleggio attivo
        for noleggio in self.noleggi_attivi:
            if noleggio.id_noleggio == id_noleggio:
                self.noleggi_attivi.remove(noleggio)
                return f'Noleggio {id_noleggio} terminato'
        return f'Noleggio {id_noleggio} non trovato'
