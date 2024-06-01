def player_validation(i):
    if i in ["s", "stone", "S"]:
        return "stone"
    elif i in ["p", "paper", "P"]:
        return "paper"
    elif i in ["s", "scissors", "S"]:
        return "scissors"
    else:
        return "none"

def choice():
    player_choice = input("(S)tone, (p)aper or (s)cissors ?")

    valid_choice = player_validation(player_choice)

    return valid_choice


valid_choice = "none"
while valid_choice == "none":
    valid_choice = choice()