class Personne:
    def __init__(self, age : int = 14):self.age = age
    def afficherAge(self):print(self.age)
    def bonjour(self):print("Hello")
    def modifierAge(self, age : int):self.age = age

class Eleve:
    def __init__(self, ppl):self.ppl = ppl
    def allerEnCour(self):print("Je vais en cours")
    def afficherAge(self):print("J'ai",self.ppl.afficherAge(),"ans")

class Professeur:
    def __init__(self, ppl, matiereEnseignee : str):self._matiereEnseignee, self.ppl = matiereEnseignee, ppl
    def enseigner(self):print("Le cours vas commencer")

ppl1 = Personne()
student = Eleve(ppl1)
student.ppl.modifierAge(15)
student.ppl.bonjour()
student.allerEnCour()

ppl2 = Personne()
teacher = Professeur(ppl2,"maths")
teacher.ppl.modifierAge(40)
teacher.ppl.bonjour()
teacher.enseigner()
