# comprehension du randow dans le cas du generateur de mdp 
import random

mot = "abcdefg123"
alphabet = mot*3
nombre_aleatoire = random.randint(1,200)

liste = list(alphabet)        
random.shuffle(liste)    
melange = "".join(liste) 

print(alphabet)
print(melange)
print(type(alphabet))
print(type(melange))
print (melange[0])

motdepasse=melange[:5]
print (motdepasse)