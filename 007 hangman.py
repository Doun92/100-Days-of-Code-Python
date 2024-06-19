word = "bosquet"
used_letters = []
correct_letters = []

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
    # print(used_letters)
    check_right(user, word, correct_letters)

user_lettter = get_user_choice()
# print(user_lettter)

check_letter_used(user_lettter, used_letters)