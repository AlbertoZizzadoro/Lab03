
class Automobile:


    def __init__(self, codice, marca, modello, anno_immatricolazione, posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno_immatricolazione = anno_immatricolazione
        self.num_posti = posti



    def __str__(self):

        posti = f"{self.num_posti} posti" if self.num_posti is not None else "N/D posti"
        return f"Auto: {self.codice} - {self.marca} {self.modello} ({self.anno_immatricolazione}), {posti}"

    def __repr__(self):

        return f"Automobile('{self.codice}', '{self.marca}', '{self.modello}', {self.anno_immatricolazione}, {self.num_posti})"