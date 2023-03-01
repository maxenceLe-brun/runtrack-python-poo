class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def change_longueur(self, longueur): self._longueur = longueur

    def change_largeur(self, largeur): self._largeur = largeur

    def get_longueur(self): return self._longueur

    def get_largeur(self): return self._largeur


class Livre:
    def __init__(self, titre, auteur, num_page):
        self._titre = titre
        self._auteur = auteur
        self._num_page = num_page

    def change_titre(self, titre):
        self._titre = titre

    def change_auteur(self, auteur):
        self._auteur = auteur

    def change_nombre_page(self, num_page):
        if num_page > 0:
            self._num_page = num_page
        else:
            print('Le nombre de page ne peut pas être négatif !')

    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nombre_page(self):
        return self._num_page


class Livre2:
    def __init__(self, titre, auteur, num_page):
        self._titre = titre
        self._auteur = auteur
        self._num_page = num_page
        self._disponible = True

    def change_titre(self, titre):
        self._titre = titre

    def change_auteur(self, auteur):
        self._auteur = auteur

    def change_nombre_page(self, num_page):
        if num_page > 0:
            self._num_page = num_page
        else:
            print('Le nombre de page ne peut pas être négatif !')

    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nombre_page(self):
        return self._num_page

    def vérification(self):
        return self._disponible

    def emprunter(self):
        if self.vérification():
            self._disponible = False
        else:
            print('Livre indisponible!')

    def rendre(self):
        if not self.vérification():
            self._disponible = True
        else:
            print('Livre deja disponible!')


class Student:
    def __init__(self, name, surname, student_number, credit=0):
        self._name = name
        self._surname = surname
        self._student_number = student_number
        self._credit = credit

    def add_credit(self, credit):
        if credit > 0:
            self._credit += credit
        else:
            print("Can't add negative credit number!")

    def studentEval(self):
        if self._credit >= 90:
            return 'Excellent'
        elif self._credit >= 80:
            return 'Très bien.'
        elif self._credit >= 70:
            return 'Bien'
        elif self._credit >= 60:
            return 'Passable'
        else:
            return 'Insuffisant'

    def studentInfo(self):
        print('Nom =', self._name, '\nPrénom =', self._surname, '\nid =', self._student_number, '\nNiveau =',
              self.studentEval())


class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = en_marche
        self._reservoir = reservoir

    def change_marque(self, marque): self._marque = marque

    def change_modele(self, modele): self._modele = modele

    def change_annee(self, annee): self._annee = annee

    def change_kilometrage(self, kilometrage): self._kilometrage = kilometrage

    def change_en_marche(self, en_marche): self._en_marche = en_marche

    def get_marque(self): return self._marque

    def get_modele(self): return self._modele

    def get_annee(self): return self._annee

    def get_kilometrage(self): return self._kilometrage

    def get_en_marche(self): return self._en_marche

    def demarrer(self):
        if self._verifier_plein() > 5:
            self._en_marche = True

    def arreter(self): self._en_marche = False

    def _verifier_plein(self): return self._reservoir


# plat = [{'name':'Nom du plat', 'prix': 10}, {'name':'Nom du plat2', 'prix': 15}]


class Commande:
    def __init__(self, commande_num, statut, list_plat=[]):
        self._commande_num = commande_num
        self._list_plat = list_plat
        self._statut = statut

    def ajouter_plat(self, plat):
        self._list_plat.append(plat)

    def cancel_commande(self):
        self._statut = 'annulée'

    def _prix_total(self):
        if self._list_plat:
            self.cost = 0
            for a in self._list_plat:
                self.cost += a['prix']
                print('===', a['name'])
            print('Le prix a payer est de', self.cost)
