from random import randint

small_letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
capital_letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
numbers = ("1","2","3","4","5","6","7","8","9","0")
special_caracters = ("+","-","@","#","%","&","/","(",")","=","?","!","{","}","$","<",">","-","_")


def add_char(password):

    list_lists = (small_letters, capital_letters, numbers, special_caracters)

    random_nb = randint(0,3)
    
    chosen_list = list_lists[random_nb]
    char_index = randint(0,len(list_lists[random_nb])-1)
    
    new_character = chosen_list[char_index]

    password.append(new_character)
    
    return password

def generate_password(length=20, difficulty=4):
    final_password = []

    while len(final_password) < length:
        add_char(final_password)
    
    final_password = "".join(final_password)
    return final_password

def check_password(password):
    check_list = []
    if any(ext in password for ext in small_letters):
        check_list.append("+")
    else:
        pass
    if any(ext in password for ext in capital_letters):
        check_list.append("+")
    else:
        pass
    if any(ext in password for ext in numbers):
        check_list.append("+")
    else:
        pass
    
    if len(check_list) == 3:
        check = "ok"
    else:
        check = "notok"
        
    return check


# username = input("Username: ")
# url = input("URL: ")
# need_of_password = input("Need to create a password ? (y/n)")
# existing_password = input("Already created password: ")
# mfa = input("The MFA code: ")

checked = "notok"

while checked == "notok":
    generated_password = generate_password()
    checked = check_password(generated_password)

print(generated_password)