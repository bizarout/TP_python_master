""" Exercice N: 2 
    Auteur : H.BEZZOUT 
"""    

"""Déclaration des variables"""

duree    = 8000   # déclaration du variable contenant le nombre de secondes 
heures    = 0      # initialisation des trois variables , heures , minutes , secondes 
minutes  = 0
secondes = 0

""" programme principale """ 

print(" Entrer une durée : ")
duree    = float(input( " la durée "))
heures   = duree // 3600                # pour utiliser la division entiere il faut ustiliser l'opérateur : // 
duree    = duree % 3600 
minutes  = duree // 60 
secondes = duree % 60

print(str(heures)+" heure  "+str(minutes)+" minute  "+str(secondes)+" seconde")




 
