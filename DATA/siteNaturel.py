from DATA.siteTouristique import *


class siteNaturel(SiteTouristique):
    def __init__(self,nom,l,it):
        super().__init__(nom)
        self.lieu = l
        self.ineretTouristisue = it

    def afficheName(self):
        print("SiteTouristique { nom = ", self.name, " }")


