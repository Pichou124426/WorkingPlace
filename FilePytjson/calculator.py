import json 

class transaction : 
    def __init__(self, date_transaction, pays, compte_emetteur,compte_recepteur,somme):
        self.date_transaction = date_transaction
        self.pays = pays 
        self.compte_emetteur = compte_emetteur
        self.compte_recepteur = compte_recepteur
        self.somme = somme
    def to_dict(self):
        return {
            "date_transaction" : self.date_transaction,
            "pays" : self.pays,
            "compte_emetteur" : self.compte_emetteur,
            "compte_recepteur" : self.compte_recepeteur,
            "somme" : self.somme
        }




def ajouter_transaction():
    new_date = input ("Veuillez inserer la date sous le format suivant JJ/MM/AAAA :")
    new_pays = input ("Renseigner le pays dans lequel vous vous trouvez :")
    new_compte_emetteur = input ("Inserez l'IBAN du compte emetteur :")
    new_compte_recepteur= input ("Inserez l'IBAN du compte recepteur :")
    new_somme = input ("Quel somme voulez-vous envoyer ($):")
    new_transaction = transaction (new_date,new_pays,new_compte_emetteur,new_compte_recepteur,new_somme)
    transaction.append(new_transaction.to_dict())


ajouter_transaction()
