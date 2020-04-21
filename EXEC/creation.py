from DATA.siteTouristique import *
from DATA.musee import *
from DATA.siteDeProduction import *
from DATA.siteNaturel import *
from DATA.monumentHistorique import *




########################################### Zone 1 #####################################################################
mon1=monument("Tour Hassan","Découvrir l’histoire et le patrimoine de la ville de Rabat", "Histoire")
mon2=monument("Oudaya","Découvrir l’histoire et le patrimoine de la ville de Rabat", "Histoire")
mon3=monument("Chellah","Découvrir l’histoire et le patrimoine de la ville de Rabat", "Histoire")

mus1=musee("Le Musée Mohammed VI","Rabat centre-ville","Découvrir des œuvres artistiques modernes marocains et étrangers","Art moderne","Oui","20 DH")
mus2=musee("Musée Belghazi","Sidi Bouknadel, Salé","Découvrir la culture marocaine traditionnelle","Ethnographie","Oui","50 DH")
mus3=musee("Musée Maroc Télécom","Hay Riad, Rabat","Avoir une idée sur l’évolution des Télécoms au Maroc","Télécommunications","Non","0 DH")

sdp1=siteDeProduction("Village de poterie Oulja","Oulja, Salé","Découvrir et acheter des produits de poterie marocains","Artisanat","Non")
sdp2=siteDeProduction("Ancienne Médina Rabat","Rabat ville","Acheter des produits d'artisanat","Artisanat","Non")

sn1=siteNaturel("Oued Bouregreg","Entre Rabat et Salé","Faire une balade fluviale en « Flouka »")
sn2=siteNaturel("Jardin exotique","Sidi Bouknadel, Salé","Faire une balade dans un jardin qui abrite des plantes des cinq coins du monde.")
z1d={'1':[mon1,mon2,mon3],'2':[mus1,mus2,mus3],'3':[sdp1,sdp2],'4':[sn1,sn2]}
########################################################################################################################

############################################ ZONE 2 ####################################################################
z2mon1=monument("Le Palais el Badi","*", "Histoire")
z2mon2=monument("Koutoubia","*", "Histoire")
z2mon3=monument("Palais de la Bahia","*","Histoire")
z2mus1=musee("Musée Orientaliste de Marrakech","*","*","Art et culture","Oui","*")
z2mus2=musee("Musée Boucharouite","*","*","Art et culture","Oui","*")
z2mus3=musee("Musée de Marrakech","*","*","Art et culture","Oui","*")
z2sdp1=siteDeProduction("Jardins de la Ménara","*","","Jardin","Oui")
z2sdp2=siteDeProduction("Jamaa el Fna","*","*","Artisanat","Non")
z2sn1=siteNaturel("Ourika","*","*")
z2sn2=siteNaturel("Oukaimeden","*","*")
z2d={'1':[z2mon1,z2mon2,z2mon3,],'2':[z2mus1,z2mus2,z2mus3],'3':[z2sdp1,z2sdp2],'4':[z2sn1,z2sn2]}
