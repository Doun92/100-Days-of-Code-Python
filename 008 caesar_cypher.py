message = "salut"
change = 7

liste_lettres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

empty_dict = {}
for i, lettre in enumerate(liste_lettres):
    empty_dict[lettre] = i+1

print(empty_dict)

def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key
    return "key doesn't exist"

def encodeMessage(m,c):
    
    encoded_message = ""
    for lettre in m:
        # print(empty_dict[lettre])
        # print(empty_dict[lettre]+c)
        if (empty_dict[lettre]+c) > len(empty_dict):
            new_result = empty_dict[lettre]+c - len(empty_dict)
            encoded_message += get_key(new_result,empty_dict)
        else:
          encoded_message += get_key(empty_dict[lettre]+c,empty_dict)

    return encoded_message

encoded_message = encodeMessage(message,change)

print(encoded_message)