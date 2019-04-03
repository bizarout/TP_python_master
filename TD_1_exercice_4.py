""" Exercice N: 4
    Auteur : Hamid.BEZZOUT 
"""    

# variable d'entrée :  nombre choisi par l'utilisateur 


n = int(input(" entrer un nombre "))

""" calcul si ce nombre est paire ou non """

modulo = n % 2 

if (modulo==0):
    print(" le nombre est paire ")
    
else : 
    print(" le nombre est impaire")
    