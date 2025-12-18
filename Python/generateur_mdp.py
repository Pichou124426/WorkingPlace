# Fonction qui permet de choisir la longueur du mots de passe généré. En verifiant que la longueur du mot de passe soit logique et que la saisie soit un entier. 
def choix_longueur_mot_de_passe ():
    saisie= input ("Entrer la longueur souhaité (Min : 8 - Max : 100):")
    try : 
        nombre_caractere = int(saisie)
        if nombre_caractere <8 :
            print ("-------------------")
            print()
            print (f"Une longueur de {nombre_caractere}  caractére(s) est trop court pour un mot de passe sécuriser !")
            print ()
            print ("--- Réesayer s'il vous plait ---")
            choix_longueur_mot_de_passe ()
        elif nombre_caractere >100 : 
            print()
            print (f"Une longueur de {nombre_caractere} caractéres(s) est trop long !")
            print()
            print ("--- Réesayer s'il vous plait ---")

            choix_longueur_mot_de_passe ()
        else :
            print()
            print (f"La longueur du mot de passe sera de {nombre_caractere} caractères.")
            return nombre_caractere    
    except ValueError:
        print()
        print ("La saisie renseigné n'est pas un entier.")
        print()
        print ("--- Réesayer s'il vous plait ---")
        return choix_longueur_mot_de_passe ()
        
        
longueur_du_mot_de_passe =  choix_longueur_mot_de_passe()






#Fonction qui permet de choisir les symboles disponibles pour constituer le mot de passe : 

def difficulté_mot_de_passe ():
    print ("Quel(s) type(s) de caractére(s) voulez-vous dans votre mot de passe : (1 = Lettre et chiffre uniquement, 2 = Lettre, Chiffre et Characteres spéciaux ) ?")
    saisie = input ("Choix fortement conseillé '2' :")

    try : 
        niveau_difficulté = int(saisie)
        if niveau_difficulté == 1 : 
            print ("TEST 1")
        if niveau_difficulté == 2 :
            print ("TEST 2")
        
        else : 
            print ("La saisie n'est pas la bonne. ")
            return difficulté_mot_de_passe ()
    
    except ValueError:
        print ("La saisie n'est pas la bonne. ")
        return  difficulté_mot_de_passe()
    

difficulté_mot_de_passe ()