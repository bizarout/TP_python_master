""" Exercice N: 3 
    Auteur : H.BEZZOUT 
"""    
from math import sqrt

# variables d'entrée circle 1 

x1 = float(input(" entrer l'abscisse de la 1er circle x1 : ")) 
y1 = float(input(" entrer l'ordonée de la 1er circle y1 : "))
r1 = float(input(" entrer le rayon de la 1er circle x1 : "))

# variables d'entrée circle 2 

x2 = float(input(" entrer l'abscisse de la 2eme circle x2 : ")) 
y2 = float(input(" entrer l'ordonée de la 2eme circle y2 : "))
r2 = float(input(" entrer le rayon de la 2eme circle x2 : "))

# calcul de la distance : 

dist = sqrt((x1-x2)**2 + (y1-y2)**2)

if dist < (r1+r2):
    print(" les deux circles sont en collision")
else:
    print(" il n ya pas de collision entre les deux cicles ")
    




# programme principal 

""" Données 1er circle """

print(" Entrer l'abscisse x , l'ordonnée y et le rayon R de la première circle ")
x1 = float(input(" Entrer x1 : "))
y1 = float(input("Entrer y1 : "))
r1 = float(input("Entrer r1 : "))

""" Données 2ème circle """

print(" Entrer l'abscisse x , l'ordonnée y et le rayon R de la deuxième circle ")
x2 = float(input(" Entrer x2 : "))
y2 = float(input("Entrer y2 : "))
r2 = float(input("Entrer r2 : "))

distance = sqrt((x1-x2)**2 + (y1-y2)**2)     # permet de calculer la distance entre les deux centre des deux circles

if distance < r1 + r2 :                      
    print("les deux circles en collision ")
else:
    print(" il n ya pas de collision ")
