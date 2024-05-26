import os

def write_file(band_name):
    cwd = os.getcwd()
    f = open(f"{cwd}\\01_band_names.txt", "a")
    f.write(f"{band_name}\n")
    f.close()

def try_again():
    try_again_question = input("Try again ?")
    if try_again_question in ["T", "t", "y", "yes", "true", "Yes", "o", "oui"]:
        create_group_name()
    elif try_again_question in ["F", "f", "n", "no", "false", "No", "non"]:
        exit()
    else:
        print("Please confirm with \"y\" or \"n\".")
        try_again()

def question_save_file(band_name):
    save_file = input("Do you want to save the name ? ")
    # if the answer is affirmative
    if save_file in ["T", "t", "y", "yes", "true", "Yes", "o", "oui"]:
        write_file(band_name)
    elif save_file in ["F", "f", "n", "no", "false", "No", "non"]:
        try_again()
    else:
        print("Please confirm with \"y\" or \"n\".")
        question_save_file(band_name)
    try_again()

def create_group_name():
    pet_name = input("Please, chose a pet name: ")
    city = input("Please, chose a city: ")

    band_name = f"{city} {pet_name}"
    print(f"Your band name is \"{band_name}\"")

    question_save_file(band_name)

create_group_name()