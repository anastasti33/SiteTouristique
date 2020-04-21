from DATA.siteTouristique import *

class monument(SiteTouristique):
    def __init__(self, nom, it, th):
        super().__init__(nom)
        self.interetTouristique = it
        self.theme = th
    def afficheName(self):
        print("SiteTouristique { nom = ", self.name, " }")
