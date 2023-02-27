import math

class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        print(self.nombre1 + self.nombre2)


class Personne:
    def __init__(self, nom="John", prenom="Doe"):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print('Je suis ' + self.nom + " " + self.prenom)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self): print("x=", self.x, "y=", self.y)

    def afficherX(self): print(self.x)
    def afficherY(self): print(self.y)

    def changerX(self, x): self.x = x
    def changerY(self, y): self.y = y


class Animal:
    def __init__(self, age=0, prenom=''):
        self.age = age
        self.prenom = prenom

    def vieillir(self): self.age += 1

    def nommer(self, prenom): self.prenom = prenom


class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self): self.x -= 1
    def droite(self): self.x += 1
    def bas(self): self.y -= 1
    def haut(self): self.y += 1

    def position(self): return self.x, self.y


class Cercle:
    def __init__(self, rayon: int):
        self.rayon = rayon

    def changerRayon(self, rayon): self.rayon = rayon
    def afficherInfo(self): print('rayon :', self.rayon)
    def circonférence(self): print(2*math.pi*self.rayon)
    def aire(self): print(math.pi*self.rayon**2)
    def diametre(self): print(self.rayon*2)


class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * self.TVA + self.prixHT

    def afficher(self): print('nom :', self.nom, '\nprixHT :', self.prixHT, '\nTVA :', self.TVA)
