import random

def roll_die():
    return random.randint(1, 6)

def get_option():
    options = ["No Play", "Ladder", "Snake"]
    return random.choice(options)

# Function to update position based on option
def player_move(position, die_roll, option):
    if option == "No Play":
        return position
    elif option == "Ladder":
        return position + die_roll
    elif option == "Snake":
        return position - die_roll

# UC 3: Simulate one move
position = 0
die_roll = roll_die()
option = get_option()
new_position = player_move(position, die_roll, option)
print(f"UC 3: Start Position = {position}, Die Roll = {die_roll}, Option = {option}, New Position = {new_position}")