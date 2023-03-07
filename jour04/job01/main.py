class Personne:
    def __init__(self, age : int = 14):
        self.age = age
    def afficherAge(self):print(self.age)
    def bonjour(self):print("Hello")
    def modifierAge(self, age : int):self.age = age

class Eleve:
    def __init__(self):self.ppl = Personne()
    def allerEnCour(self):print("Je vais en cours")
    def afficherAge(self):print("J'ai",self.ppl.afficherAge(),"ans")

class Professeur:
    def __init__(self, matiereEnseignee : str):self._matiereEnseignee = matiereEnseignee
    def enseigner(self):print("Le cours vas commencer")

ppl1 = Personne()
ppl2 = Eleve()
ppl2.afficherAge()
