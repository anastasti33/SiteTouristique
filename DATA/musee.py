from DATA.siteDeProduction import *

class musee(siteDeProduction):
    def __init__(self,nom,l,it,th,vg,tar):
        super().__init__(nom,l,it,th,vg)
        self.tarif=tar
    def afficheName(self):
        print("SiteTouristique { nom = ", self.name, " }")