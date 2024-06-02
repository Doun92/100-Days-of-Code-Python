from random import randint

def battle(player, opponent):
    loose_message = "You loose !"
    win_message = "You won !"
    draw_message = "It is a draw !"
    
    print(f"You chose: {player}")
    print(f"Your opponent chose: {opponent}")

    if player == "stone":
        if opponent == "paper":
            return loose_message
        elif opponent == "scissors":
            return win_message
        else:
            return draw_message
    elif player == "paper":
        if opponent == "paper":
            return draw_message
        elif opponent == "scissors":
            return loose_message
        else:
            return win_message
    elif player == "scissors":
        if opponent == "paper":
            return win_message
        elif opponent == "scissors":
            return draw_message
        else:
            return loose_message


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

def get_random_choice():
    random_nb = randint(1,3)
    if random_nb == 1:
        return "stone"
    elif random_nb == 2:
        return "stone"
    elif random_nb == 3:
        return "scissors"

valid_choice = "none"
while valid_choice == "none":
    valid_choice = choice()

random_choice = get_random_choice()

result_battle = battle(valid_choice, random_choice)
print(result_battle)