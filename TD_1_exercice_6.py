""" Exercice N: 6
    Auteur : Hamid.BEZZOUT 
"""    
from webbrowser import Opera

# programme permet de simuler une calcullete 

premierNombre  = float(input("entrer le 1er nombre  : "))
deuxiemeNombre = float(input("entrer le 2eme nombre : "))
operateur      = input("entrer une operation ")

if (operateur== "+"): 
    res = premierNombre + deuxiemeNombre 
if (operateur=="-"):
    res = premierNombre - deuxiemeNombre 
if ( operateur == "*"):
    res = premierNombre * deuxiemeNombre 
if ( operateur == "/"):
    res = premierNombre / deuxiemeNombre 
    
print("Le resultat de l'opreration est : ",res)
