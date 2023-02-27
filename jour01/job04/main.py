class Personne:
    def __init__(self, nom="John", prenom="Doe"):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print('Je suis ' + self.nom + " " + self.prenom)

Personne().SePresenter()
ppl = Personne("Jean","Dupond")
ppl.SePresenter()
