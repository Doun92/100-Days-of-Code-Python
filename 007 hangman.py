word = "bosquet"

used_letters = []


def get_user_choice():
    while True:
        user_choice = input("Choose a letter: ")

        if len(user_choice) == 0:
            continue
        elif len(user_choice) > 1:
            user_choice = user_choice[0]
            
        return user_choice

user_lettter = get_user_choice()
print(user_lettter)