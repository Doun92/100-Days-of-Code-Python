from random import randint

def add_char(password):
    small_letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    capital_letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    numbers = ("1","2","3","4","5","6","7","8","9","0")
    special_caracters = ("+","-","@","#","%","&","/","(",")","=","?","!","{","}","$","<",">","\\","-","_")

    list_lists = (small_letters, capital_letters, numbers, special_caracters)

    random_nb = randint(1,4)
    
    print(list_lists[random_nb])

def generate_password(length=21, difficulty=4):
    final_password = []

    while len(final_password) < length:
        add_char(final_password)
        
    print(final_password)

username = input("Username: ")
url = input("URL: ")
need_of_password = input("Need to create a password ? (y/n)")
existing_password = input("Already created password: ")
mfa = input("The MFA code: ")

generate_password()