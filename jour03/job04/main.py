class Player:
    def __init__(self, name : str, number : int, pos : str, nbr_goal: int, final_pass : int, yellow : int, red : int):
        self.name       = name
        self.number     = number
        self.pos        = pos
        self.nbr_goal   = nbr_goal
        self.final_pass = final_pass
        self.yellow     = yellow
        self.red        = red
    def marquerUnBut(self,n):self.nbr_goal += n
    def effectuerUnePasseDecisive(self,n):self.final_pass += n
    def recevoirUnCartonJaune(self,n):self.yellow += n
    def recevoirUnCartonRouge(self,n):self.red += n
    def afficherStatistiques(self):print(self.name, self.number, self.pos, self.nbr_goal, self.final_pass, self.yellow, self.red)
class Equipe:
    def __init__(self, nom : str, liste : list  = []):self.nom, self.liste = nom, liste
    def ajouterJoueur(self, joueur):self.liste.append(joueur)
    def AfficherStatistiquesJoueur(self):[self.liste[a].afficherStatistiques() for a in range(len(self.liste))]
    def mettreAJourStatistiques(self, joueur, but,  passes, jaune, rouge): self.liste.remove(joueur),joueur.marquerUnBut(but),joueur.effectuerUnePasseDecisive(passes),joueur.recevoirUnCartonJaune(jaune),joueur.recevoirUnCartonRouge(rouge),self.ajouterJoueur(joueur)
joueur1 = Player("clement", 1, "attaquant", 0, 0, 0, 0)
joueur2 = Player("erwan", 2, "attaquant", 0, 0, 0, 0)
joueur3 = Player("maxence", 3, "defenseur", 0, 0, 0, 0)
#flm de tt faire enft
