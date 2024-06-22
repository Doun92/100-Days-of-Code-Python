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

while fin_jeu == False:
    choix = input("Choisis une lettre: ")

    for position in range(longueur_mot):
        lettre = mot[position]
        if choix == lettre:
            display[position] = lettre
        else:
            # print("Non")
            pass

    print(display)
    if "_" not in display:
        fin_jeu = True