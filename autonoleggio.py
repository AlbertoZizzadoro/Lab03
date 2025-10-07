from automobile import Car
import csv

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.responsabile=responsabile

        # TODO

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
                lettore= csv.reader(infile, delimiter=',')
                for riga in lettore:
                    try:
                        codiceUnivoco = riga[0]
                        marca = riga[1]
                        modello = riga[2]
                        annoImmatricolazione = riga[2]
                        numPosti = riga[4]
                        macchina=Car(codiceUnivoco,marca,modello,annoImmatricolazione,numPosti)
                        lista_macchina.append(macchina)
                    except:

        except:





        # TODO

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

        nuova_macchina = Car(nuovo_codice, marca, modello, anno, num_posti)


    def automobili_ordinate_per_marca(self,lista_auto):
        """Ordina le automobili per marca in ordine alfabetico"""
        return sorted(lista_auto,key=lambda macchina:macchina.marca)

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
