class Ville:
    def __init__(self, nom, nbr):
        self._nom = nom
        self._nbr = nbr

class Personne:
    def __init__(self, name, age, ville):
        self.name = name
        self.age = age
        self.ville = ville
    
    def ajouterPopulation(self):
        self.ville._nbr += 1

Paris =  Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)
print(Paris._nbr)
print(Marseille._nbr)
John = Personne("John", 45, Paris)
John.ajouterPopulation()
Myrtille = Personne("Myrtilly", 4, Paris)
Myrtille.ajouterPopulation()
Chloé = Personne("Chloé", 18, Marseille)
Chloé.ajouterPopulation()
print(Paris._nbr)
print(Marseille._nbr)
