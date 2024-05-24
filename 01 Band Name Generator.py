

#TODO Ask a pet nam
pet_name = input("Please, chose a pet name: ")

#TODO: Ask a city
city = input("Please, chose a city: ")

#TODO: Display the result
print(f"Your band name is \"{city} {pet_name}\"")

#TODO: Create or incremente the file
def write_file():
    pass

#TODO: Ask if start again or not
def try_again():
    pass

#TODO: Ask to save the name in a txt file
def question_save_file():
    save_file = input("Do you want to save the name ?")
    # if the answer is affirmative
    if save_file in ["T", "t", "y", "yes", "true", "Yes", "o", "oui"]:
        write_file()
    if save_file in ["F", "f", "n", "no", "false", "No", "non"]:
        try_again()


#TODO: Begin by asking if the want to take a random input from the file