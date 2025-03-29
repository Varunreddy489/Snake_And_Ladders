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

# UC 7: Two-player game
player1_pos = 0
player2_pos = 0
dice_rolls = 0
player1_history = [player1_pos]
player2_history = [player2_pos]

print("UC 7: Two Player Game Starts!")
while player1_pos < 100 and player2_pos < 100:
    # Player 1's turn
    die_roll = roll_die()
    option = get_option()
    dice_rolls += 1
    old_pos1 = player1_pos
    player1_pos = player_move(player1_pos, die_roll, option)
    player1_history.append(player1_pos)
    print(f"Roll {dice_rolls} (P1): Dice = {die_roll}, Option = {option}, Position = {old_pos1} -> {player1_pos}")
    if player1_pos == 100:
        break
    
    # Player 2's turn
    die_roll = roll_die()
    option = get_option()
    dice_rolls += 1
    old_pos2 = player2_pos
    player2_pos = player_move(player2_pos, die_roll, option)
    player2_history.append(player2_pos)
    print(f"Roll {dice_rolls} (P2): Dice = {die_roll}, Option = {option}, Position = {old_pos2} -> {player2_pos}")
    if player2_pos == 100:
        break

# Report winner
winner = "Player 1" if player1_pos == 100 else "Player 2"
print(f"\nGame Over! {winner} wins in {dice_rolls} total rolls!")
print(f"Player 1 History: {player1_history}")
print(f"Player 2 History: {player2_history}")