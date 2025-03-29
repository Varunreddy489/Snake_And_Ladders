import random

def roll_die():
    return random.randint(1, 6)

def get_option():
    options = ["No Play", "Ladder", "Snake"]
    return random.choice(options)

def player_move(position, die_roll, option):
    if option == "No Play":
        return position
    elif option == "Ladder":
        return position + die_roll
    elif option == "Snake":
        new_position = position - die_roll
        # UC 4: Restart from 0 if below 0
        if new_position < 0:
            return 0
        return new_position

position = 2
die_roll = roll_die()
option = "Snake"  
new_position = player_move(position, die_roll, option)
print(f"UC 4: Start Position = {position}, Die Roll = {die_roll}, Option = {option}, New Position = {new_position}")