""" Exercice N: 8
    Auteur : Hamid.BEZZOUT 
""" 


# ce programme permet de donner le tableau de multiplication d'un nombre 

nombreEntier = int(input(" Taper un nombre entier : "))

for i in range(1,11):
    res = i * nombreEntier
    print(i,"*", nombreEntier," = ",res)