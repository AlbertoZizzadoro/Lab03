
class Noleggio:

    def __init__(self, codice_noleggio, data, id_automobile, cognome_cliente):
        self.codice = codice_noleggio
        self.data = data
        self.id_automobile = id_automobile
        self.cognome_cliente = cognome_cliente

    def __str__(self):

        return f"Noleggio: {self.codice} - Cliente: {self.cognome_cliente}, Auto: {self.id_automobile}, Data: {self.data}"

    def __repr__(self):

        return f"Noleggio('{self.codice}', '{self.data}', '{self.id_automobile}', '{self.cognome_cliente}')"