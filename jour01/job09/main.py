class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * self.TVA + self.prixHT

    def afficher(self): print('nom :', self.nom, '\nprixHT :', self.prixHT, '\nTVA :', self.TVA)
