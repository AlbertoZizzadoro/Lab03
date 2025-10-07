class Car:
    def __init__(self, codiceUnivoco, marca, modello, annoImmatricolazione, numPosti):
         self.codiceUnivoco = codiceUnivoco
         self.marca = marca
         self.modello = modello
         self.annoImmatricolazione = annoImmatricolazione
         self.numPosti=numPosti

    def descriviti(self):
        return (f"Macchina: {self.codiceUnivoco} {self.marca} {self.modello} {self.annoImmatricolazione} {self.numPosti}")

    def __str__(self):
        return self.descriviti(sel)
