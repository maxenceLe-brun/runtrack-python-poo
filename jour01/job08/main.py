class Cercle:
    def __init__(self, rayon: int):
        self.rayon = rayon

    def changerRayon(self, rayon): self.rayon = rayon
    def afficherInfo(self): print('rayon :', self.rayon)
    def circonférence(self): print(2*math.pi*self.rayon)
    def aire(self): print(math.pi*self.rayon**2)
    def diametre(self): print(self.rayon*2)
