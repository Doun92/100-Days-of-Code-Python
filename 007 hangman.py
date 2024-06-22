word = "libraire"
used_letters = []
correct_letters = []

# Cette liste servira à la vérification si tous les caractères sont bons ou pas.
def word_to_letters(word):
    # On transforme la string en liste
    # Transforme la liste en dictionnaire pour supprimer les duplicats
    # Reforme la liste sans les duplicats
    word = list(dict.fromkeys(list(word)))
    # TODO: Mettre en ordre les lettres
    return word

def get_user_choice():
    while True:
        user_choice = input("Choose a letter: ")

        if len(user_choice) == 0:
            continue
        elif len(user_choice) > 1:
            user_choice = user_choice[0]
            
        return user_choice

def check_right(user, word, correct_letters):
    if user in list(word):
        correct_letters.append(user)



def check_letter_used(user,used_letters):
    if user in used_letters:
        print("Letter already used.")
        print(f"Here are the letters used: \n ***\n{used_letters}\n***")
    else:
        used_letters.append(user)
    check_right(user, word, correct_letters)

cleaned_word = word_to_letters(word)

while correct_letters != cleaned_word:

    user_lettter = get_user_choice()

    check_letter_used(user_lettter, used_letters)