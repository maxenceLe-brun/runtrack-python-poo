class Animal:
    def __init__(self, age=0, prenom=''):
        self.age = age
        self.prenom = prenom

    def vieillir(self): self.age += 1

    def nommer(self, prenom): self.prenom = prenom

pet = Animal()
print("L'age de l'animal",pet.age,"ans")
pet.vieillir()
print("L'age de l'animal",pet.age,"ans")
