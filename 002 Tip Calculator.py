print("Welcome to the tip calculator!")

def check_result(result, last_func):
    try:
        result = int(result)
        return result
    except:
        try:
            result = float(result)
            return result
        except:
            print("Please enter a number or a float")
            return last_func()

def calculate_bill():

    total_bill = input("What was the total bill? ")
    return check_result(total_bill, calculate_bill)

def calculate_tip():
    available_tip = ["0","5","10","12","15"]
    tip = input(f"How much tip would you like to give: {', '.join(available_tip)} ? ")
    try:
        result = int(tip)
        if tip in available_tip:
            return result
        else:
            confirmation_tip = input(f"Do you want to give this custom tip: {tip}? ")
            if confirmation_tip in ["yes", "y", "oui", "o"]:
                return result
            else:
                print("Please choose beetween a suggested tip.")
                calculate_tip()
    except:
        print("Please choose beetween a suggested tip.")
        calculate_tip()

def calculate_people():
    people = input("How many people to split the bill ? ")
    try:
        result = int(people)
        return result
    except:
        print("Please enter an integer.")
        calculate_people()

def calculate_total():
    result_bill = calculate_bill()

    result_tip = calculate_tip()

    result_people = calculate_people()

    total = (result_bill + (result_bill*(result_tip/100)))/result_people

    return round(total, 2)

pay_per_person = calculate_total()
print(f"Each person should pay: ${pay_per_person}.")