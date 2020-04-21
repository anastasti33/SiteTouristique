from pip._vendor.distlib.compat import raw_input

from DATA.siteTouristique import *
from DATA.siteDeProduction import *
from DATA.zoneTouristique import *
from DATA.siteNaturel import *
from DATA.monumentHistorique import *
from SERVICE.userInteraction import *

from EXEC.creation import *
#fonction pour afficher tous les sites!
def afficheAll(dic):
    for x in dic.values():
        for y in x:
          y.afficheName()
#fonction pour l'affichage par catégorie!!
def afficheCat(dic,n):
    for k,v in dic.items():
        if k==n:
            for y in v:
                y.afficheName()
#affichage par theme!
def afficheTheme(b,dic,n):
    #pour la zone 1
    if b == '1':
        for k, x in dic.items():
            if k == '1' or k == '2' or k == '3':
                for y in x:
                    if n=='1' and y.theme == "Histoire":
                        y.afficheName()
                    if n=='2' and y.theme == "Artisanat":
                        y.afficheName()
                    if n=='3' and y.theme == "Art moderne":
                        y.afficheName()
                    if n=='4' and y.theme == "Ethnographie":
                        y.afficheName()
                    if n=='5' and y.theme == "Télécommunications":
                        y.afficheName()
    #pour la zone 2
    else:
        for k, x in dic.items():
            if k == '1' or k == '2' or k == '3':
                for y in x:
                    if n=='1' and y.theme == "Histoire":
                        y.afficheName()
                    if n=='2' and y.theme == "Art et culture":
                        y.afficheName()
                    if n=='3' and y.theme == "Jardin":
                        y.afficheName()
                    if n=='4' and y.theme == "Artisanat":
                        y.afficheName()


#affichage des sites qui possède une visite guidée!!
def afficheVisiteGuidee(dic):
    for k, x in dic.items():
        if k == '2' or k == '3':
            for y in x:
                if y.visiteguidee == "Oui":
                    y.afficheName()


#la fonction qui contiet tous le programme!
def prog():
    z = '0'
    while z != '1' and z != '2' and z != '3':
        menuZone()
        z = raw_input()
        if z == '1':
            print("**************** Vous avez choisi la zone de Rabat-Salé : *******************")
            print("-----------------------------------------------------------------------------")
            fonctionMenu(z,z1d,"matriceZ1.txt")
        elif  z == '2':
            print("**************** Vous avez choisi la zone de Marrakech :   ******************")
            print("-----------------------------------------------------------------------------")
            fonctionMenu(z,z2d,"matriceZ2.txt")
        elif z == '3':
            print("Fin du programme !!!!")
            return 0
        else:
                print("La valeur que vous avez choisi n'est pas valide !!")


def fonctionMenu(s,dict,file):

    c = '-1'
    while c !='7':
        meniPrincipal()
        c = raw_input()

        if c == '1':
            print("************************** Tous les sites **********************************")
            afficheAll(dict)
            print("\n")
        if c == '2':
            m = '-2'
            if s == '1':
                while m != '1' and m!= '2' and m != '3' and m != '4' and m !='5':
                    menuTheme()
                    m = raw_input()
                    if m not in ('1', '2', '3', '4', '5'):
                        print("Valeur non valide !!")
            else:
                while m != '1' and m != '2' and m != '3' and m != '4':
                    menuTheme2()
                    m = raw_input()
                    if m not in ('1', '2', '3', '4'):
                        print("Valeur non valide !!")
            print("*********************** Affichage par thème choisie ************************")
            afficheTheme(s,dict,m)
        if c == '3':
            n ='0'
            while n != '1' and n != '2' and n != '3' and n != '4':
                menuCategorie()
                n = raw_input()
            print("************************ Affichage par catégorie choisie ****************************")
            afficheCat(dict, n)
            print("\n")

        if c == '4':
            print("************** tous les sites qui proposent une visite guidée ***************")

            afficheVisiteGuidee(dict)

        if c == '5':
            n = '-1'
            while n not in ('1','2','3','4','5','6','7','8','9','10'):
                if s == '1':
                    menuDistance()
                else:
                    menuDistance2()
                n = raw_input("Donner le nombre totale de site : ")
                print("------------------------")
                if n not in ('1','2','3','4','5','6','7','8','9','10'):
                    print("Valeur non valide !!!")
            print("Veuillez donner les sites par l'ordre que vous voulez suivre !")
            distance(dict, n, file)
        if c == '6':
            prog()
        if c not in ('1', '2', '3', '4', '5', '6','7'):
            print("Valeur non valide !!!")

    print("fin!!!")
    return 0

def distance(dict,n,file):
    n=eval(n)
    dis=0
    fichier=open(file,'r')
    l=fichier.readlines()
    ll = []
    for x in l:
        ll.append(x.split())
    d = []

    while len(d) != n:
        elem = raw_input("Donner le numéro du site à visiter : ")
        if elem not in ('1','2','3','4','5','6','7','8','9','10'):
            print("Valeur non valide ! essayez à nouveau !")
        else:
            d.append(eval(elem))

    for i in range(n-1):

        dis = dis+eval(ll[d[i]-1][d[i+1]-1])

    print("La distance totale en suivant l'ordre que vous avez choisi est :",dis,"KM")







