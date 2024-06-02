from random import randint

def player_validation(i):
    if i in ["s", "stone", "S"]:
        return "stone"
    elif i in ["p", "paper", "P"]:
        return "paper"
    elif i in ["c", "scissors", "C"]:
        return "scissors"
    else:
        return "none"

def choice():
    player_choice = input("(S)tone, (p)aper or s(c)issors ?")

    valid_choice = player_validation(player_choice)

    return valid_choice

def random_choice():
    random_nb = randint(1,3)
    print(random_nb)

valid_choice = "none"
while valid_choice == "none":
    valid_choice = choice()

print(valid_choice)
random_choice()