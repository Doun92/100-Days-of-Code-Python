user_position = [0,0]
# steps_done = []
position_history = {}

found_treasure = False

def calculation(u, m):
    size = (10,10,-10,-10)
    # Ajouter map pour montrer la liste position_history
    if m in ["up", "u"]:
        u[1] += 1
    elif m in ["right", "r"]:
        u[0] += 1
    elif m in ["back", "b"]:
        u[1] -= 1
    elif m in ["left", "l"]:
        u[0] -= 1
    else:
        print("Please chose one of the directions")
    u = check_position(u, size)
    return u,m

def action_choice(user):
    mouvement = input("Please chose a direction to move: (u)p, (r)ight, (b)ack, (l)eft: ")
    new_place = calculation(user, mouvement)
    return new_place

def map_route(u, a, treasure_position):
    if a in ["up", "u", "back", "b"]:
        result = u[1] - treasure_position[1]
    elif a in ["right", "r", "left", "l"]:
        result = u[0] - treasure_position[0]
    distance_from_zero = abs(result)

def hint(u, a):
    treasure_position = [-5,5]
    print(f"Your position is {u}")

    my_map = map_route(u, a, treasure_position)
    print(f"The map: {my_map}")
    
    if u == treasure_position:
        print("You found the treasure !")
        print("Congratulations !")
        exit()

def check_position(user, position):
    if user[0] > position[1]:
        print("You're out of the map\n")
        user[0] -= 1
    elif user[0] < position[3]:
        print("You're out of the map")
        user[0] += 1
    elif user[1] > position[0]:
        print("You're out of the map")
        user[1] -= 1
    elif user[1] < position[2]:
        print("You're out of the map")
        user[0] += 1
    return user

while found_treasure == False:
    action = action_choice(user_position)
    user_position = action[0]
    action = action[1]
    hint(user_position, action)
    
# Ce qu'il faut faire, c'est calculer la distance entre le user et le trésor.
# Il faut enregistrer cette distance (pourquoi pas dans une liste)
#