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
        print ("La saisie renseigné n'est pas correcte !.")
        print()
        print ("--- Réesayer s'il vous plait ---")
        return choix_longueur_mot_de_passe ()
        
        


#Fonction qui permet de choisir les symboles disponibles pour constituer le mot de passe : 

def difficulté_mot_de_passe ():
    print()
    print ("Choissisez les caractéres souhaités dans le mot de passe :")
    print()
    minuscule = input ("Utiliser des lettres minuscules ? (o/n) : ").lower()=="o"
    majuscule = input ("Utiliser des lettres majuscules ? (o/n) : ").lower()=="o"
    chiffre = input ("Utiliser des chiffres ? (o/n) : ").lower()=="o"
    special_caractere = input ("Utiliser des caractéres spéciaux ? (o/n) : ").lower()=="o"


    import string
    alphabet = ""

    if minuscule : 
        alphabet += string.ascii_lowercase
    if majuscule : 
        alphabet += string.ascii_uppercase
    if chiffre :
        alphabet += string.digits
    if special_caractere :
        alphabet += string.punctuation
    
    if alphabet == "" :
        print()
        print ("Aucun type de caractére a été selectionné, veuillez en selectionner au moins un.")
        return difficulté_mot_de_passe ()

    return alphabet


# Fonction qui utiliser les deux parametres longueur et caractere pour generer le mot de passe. 
def construction_mot_de_passe (longueur,caractere) :
    import random

    nombre_de_catactere = longueur
    nombre_aleatoire = random.randint(1,200)
    choix_caractere = caractere*nombre_aleatoire
    liste_lettre = list(choix_caractere)
    random.shuffle(liste_lettre)
    melange="".join(liste_lettre)

    mot_de_passe = melange[:nombre_de_catactere]

    return mot_de_passe
    

 


longueur_du_mot_de_passe =  choix_longueur_mot_de_passe()
caractere_disponible_mot_de_passe = difficulté_mot_de_passe ()
mot_de_passe = construction_mot_de_passe (longueur_du_mot_de_passe,caractere_disponible_mot_de_passe)
print()
print(f"Voici votre mot de passe sécurisé : {mot_de_passe}")
print()