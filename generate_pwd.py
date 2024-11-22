import random
import string
import tkinter as tk

def generate_password():
    try:
        char = string.ascii_letters
        digit = string.digits
        special = string.punctuation
        characters = char + digit + special # Concaténation des letres, chiffres et caractères spéciaux
        password = ''
        lenght = int(entrer.get()) # Récuperez la saisie de l'utilisateur

        if lenght <= 0: # Lever une erreur si lenght est inféreur ou égal à 0
            raise ValueError
        
        for x in range(lenght): #itération du chiffre
            password += random.choice(characters) # Mélange de chraters de manière aléatoire
        label_password.config(text=f"Mots de passe génerer est: {password}", fg="green") # Affiche dans label_password

    except ValueError: #Lever une errer si c'est pas un nombre
        label_password.config(text="Veullez entrer un nombre valide", fg="red") # Affiche dans label_password

#Configuration
root = tk.Tk()  #fenetre racine
root.title("Generate Password")

label_entry = tk.Label(root, text="La taille du mots de passe", font=("Arial", 10)) # Texte à l'interieur de root
label_entry.grid(row=0, column=0, padx=10, pady=10)

entrer = tk.Entry(root, width=20) # Entrez saisi de l'utilisateur à l'intérieur de root
entrer.grid(row=0, column=1, padx=10, pady=10)

bouton = tk.Button(root, text="Génerer", command=generate_password) # Bouton à l'intérieur de root
bouton.grid(row=0, column=2, padx=10, pady=10)

label_password = tk.Label(root, text="", font=("Arial", 12), fg="green") # Texte de reussie ou erreur
label_password.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

root.mainloop() # Boucle