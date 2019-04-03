""" Exercice N: 8
    Auteur : Hamid.BEZZOUT 
""" 

compteAhmed = 0

ageAhmed = int(input(" entrer l'age de Ahmed : "))

for i in range(2,ageAhmed+1):
    
    compteAhmed = compteAhmed + 2*i + 100
    
print(" Le compte de Ahmed est de somme egale à : ",compteAhmed)
