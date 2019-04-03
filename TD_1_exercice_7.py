""" Exercice N: 7
    Auteur : Hamid.BEZZOUT 
""" 

# Ce programme permet de calculer le factorielle d'un nombre entier 

nombre = int(input(" Entrer un nombre pour calculer son factorielle: "))

fact = 1

""" Calcul du factorielle """
for i in range(1,nombre+1 ):
    fact = fact * i
    
print( " la factorielle de :",nombre,"est : ",fact)