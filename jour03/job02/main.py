class CompteBancaire:
    def __init__(self, num : int, nom : str, prenom : str, solde : float, découvert : bool):
        self._num = num
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._découvert = découvert
        
    def afficher(self):print("numéro de compte :", self.num, "\n", "nom :", self._nom, "\n", "prénom :", self._prenom, "\n", "solde du compte :", round(self._solde,2), "\n", "droit de découvert :", self._découvert)
    def afficherSolde(self):print("solde du compte :", round(self._solde,2))
    def versement(self, nbr : int):
        if nbr <= 0:
            print("Le versement n'a pas pu aboutir a terme")
            print("Annulation")
        else:            
            self.solde += nbr
            print("Le versement a bien été effectué")
            print("Fin de la transaction")
    def retrait(self, nbr : int):
        if self._découvert == True or self._solde - nbr >= 0:
            self._solde -= nbr
            print("Le retrait a bien été effectué")
            print("Fin de la transaction")
        else:
            print("Le retrait n'a pas pu aboutir a terme")
            print("Annulation")
    def agios(self):
        if self._solde < 0:
            self._solde -= self._solde*10*0.15/365
    def virement(self, ref, compte, nbr):
        if nbr <= 0 or ref != self._num or str(type(compte)) != "<class '__main__.CompteBancaire'>" or self._découvert == False:
            print("Le virement n'a pas pu aboutir a terme")
            print("Annulation")
        else:
            self._solde -= nbr
            compte._solde += nbr
            print("Le virement a bien été effectué")
            print("Fin de la transaction")
Account1 = CompteBancaire(49720397, "Doe", "John", 3581.59, True)
Account2 = CompteBancaire(49720314, "Blanchard", "Joe", -153.12, True)
Account1.virement(49720397, Account2, 150)
Account2.afficherSolde()
Account1.virement(49720397, Account2, 20)
Account2.afficherSolde()
