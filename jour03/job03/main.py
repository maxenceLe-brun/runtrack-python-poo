class Tache:
    def __init__(self, title, description, status = "a faire"):
        self.title = title
        self.description = description
        self.status = status
class ListeDeTaches:
    def __init__(self):self.liste = []
    def ajouterTache(self,tache):self.liste.append(tache)
    def supprimerTache(self,tache):self.liste.remove(tache)
    def marquerCommeFinie(self, tache):
        for a in range(len(self.liste)):
            if self.liste[a] == tache and self.liste[a].status == "a faire":
                self.liste[a].status = "terminer"
                break
            elif self.liste[a] == tache and self.liste[a].status != "a faire":
                print("la tache est deja en tant que 'terminer' ")
                break
    def afficherListe(self):[print("titre :", a.title, "  description :", a.description, "   status :", a.status,) for a in self.liste]
    def filtrerListe(self):
        temp = ""
        for a in self.liste:
            if a.status == "a faire":
                temp +="titre : "+a.title+ "   description : "+ a.description+"\n"
        return temp

tache1 = Tache("Reveil", "se lever avant 9h")
tache2 = Tache("dejeuner", "prendre un petit dejeuner correctement avant de partir")
tache3 = Tache("partir", "verifier que tout est eteint, sac pret, fenetres ferme")

tasklist = ListeDeTaches()
tasklist.ajouterTache(tache1)
tasklist.ajouterTache(tache2)
tasklist.ajouterTache(tache3)
tasklist.supprimerTache(tache2)
tasklist.marquerCommeFinie(tache1)
tasklist.afficherListe()
print(tasklist.filtrerListe())
