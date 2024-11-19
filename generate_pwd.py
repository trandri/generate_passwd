import random
import string

char = string.ascii_letters
digit = string.digits
special = string.punctuation
characters = char + digit + special
password = ''

# Demander toujours à l'utilisateur tant qu'il n'a pas rentré un nombre valide
while True:
    try:
        length = int(input("Taille du mot de passe: "))
        break # sort de la boucle si c'est un nombre valide
    except ValueError:
        print("Veuillez entrer un nombre")

for i in range(length):
    password += random.choice(characters)

print("Le mots génerer est: ",password)