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
        new_position = position + die_roll
        # UC 5: Stay at previous position if exceeding 100
        if new_position > 100:
            return position
        return new_position
    elif option == "Snake":
        new_position = position - die_roll
        if new_position < 0:
            return 0
        return new_position

# UC 5: Test near 100
position = 98
die_roll = roll_die()
option = "Ladder"  # Force ladder for testing
new_position = player_move(position, die_roll, option)
print(f"UC 5: Start Position = {position}, Die Roll = {die_roll}, Option = {option}, New Position = {new_position}")