class Rectangle:
    def __init__(self, longueur, largeur):self._longueur, self._largeur = longueur, largeur
    def perimetre(self):print(2*self._longueur + 2*self._largeur)
    def surface(self):print(self._longueur*self._largeur)
    def modifierLongueur(self, longueur):self._longueur = longueur
    def modifierLargeur(self, largeur):self._largeur = largeur
    
class Parallelepipede:
    def __init__(self, rct, hauteur):self.rct, self.hauteur = rct, hauteur
    def volume(self):print(self.rct._longueur*self.rct._largeur*self.hauteur)
    
rct1 = Rectangle(10,8)
rct1.perimetre()
rct1.surface()
rct1.modifierLargeur(7)
rct1.modifierLongueur(11)    
rct1.perimetre()
rct1.surface()

para = Parallelepipede(rct1, 8)
para.volume()
