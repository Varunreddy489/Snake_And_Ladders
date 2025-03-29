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
        if new_position > 100:
            return position
        return new_position
    elif option == "Snake":
        new_position = position - die_roll
        if new_position < 0:
            return 0
        return new_position

# UC 6: Single-player game with reporting
position = 0
dice_rolls = 0
position_history = [position]

print("UC 6: Single Player Game Starts!")
while position < 100:
    die_roll = roll_die()
    option = get_option()
    dice_rolls += 1
    old_position = position
    position = player_move(position, die_roll, option)
    position_history.append(position)
    print(f"Roll {dice_rolls}: Dice = {die_roll}, Option = {option}, Position = {old_position} -> {position}")

print(f"\nGame Over! Reached 100 in {dice_rolls} rolls.")
print(f"Position History: {position_history}")