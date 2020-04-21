from DATA.monumentHistorique import *
class siteDeProduction (monument):
    def __init__(self,nom,l,it,th,vg):
        super().__init__(nom,it,th)
        self.lieu=l
        self.visiteguidee = vg

    def afficheName(self):
        print("SiteTouristique { nom = ", self.name, " }")