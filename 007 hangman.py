from random import choice

liste_mots = ["souris", "lynx", "football", "sprint", "chat"]
mot = choice(liste_mots)

fin_jeu = False

print(mot)
display = []
longueur_mot = len(mot)
for lettre in mot:
    display += "_"
print(display)

vies = 6

while fin_jeu == False:
    choix = input("Choisis une lettre: ")

    #Vérification de la lettre
    for position in range(longueur_mot):
        lettre = mot[position]
        if choix == lettre:
            display[position] = lettre

    if choix not in mot:
        vies -= 1
        if vies == 0:
            fin_jeu = True
            print("Tu as perdu")

    print(display)
    if "_" not in display:
        fin_jeu = True
        print("Tu as deviné le mot")