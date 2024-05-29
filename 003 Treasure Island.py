user_position = [0,0]
steps_done = []

found_treasure = False

def calculation(u, m):
    size = (10,10,-10,-10)
    if m in ["up", "u"]:
        u[1] += 1
        u = check_position(u, size)
    elif m in ["right", "r"]:
        u[0] += 1
        check_position(u, size)
    elif m in ["back", "b"]:
        u[1] -= 1
        check_position(u, size)
    elif m in ["left", "l"]:
        u[0] -= 1
        check_position(u, size)
    else:
        print("Please chose one of the directions")
        check_position(u, size)
    return u,m

def action_choice(user):
    mouvement = input("Please chose a direction to move: (u)p, (r)ight, (b)ack, (l)eft: ")
    new_place = calculation(user, mouvement)
    return new_place

def map_route(a):
    steps_done.append(a)
    try:
        previous_action = steps_done[-2]
    except:
        previous_action = steps_done[-1]
    return previous_action

def set_direction(action, last_action):
    pass

def hint(u, a):
    last_action = map_route(a)
    treasure_position = [-5,5]
    print(f"Your position is {u}")
    
    set_direction(a, last_action)
    
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