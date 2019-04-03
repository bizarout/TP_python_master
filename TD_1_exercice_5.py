""" Exercice N: 5
    Auteur : Hamid.BEZZOUT 
"""    

# variable d'entrée :  note d'un étudiant  

note = float(input(" entrer la note d'un étudiant : "))

if ( note < 0 or note > 20 ):
    print(" la note est hors intervalle ")
else:
    if note < 10 :
        print(" ***insuffisant***")
    else:
        if note < 12:
            print(" ***passable*** ")
        else:
            if note < 14 :
                print(" ***Assez bien***")
            else :
                if note < 16 :
                    print(" ***Bien***")
                else:
                    print(" ***Très bien***")
                