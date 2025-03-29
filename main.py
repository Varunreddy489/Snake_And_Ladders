import random

def roll_die():
    return random.randint(1, 6)

position = 0
die_roll = roll_die()
print(f"UC 1: Starting Position = {position}, Die Roll = {die_roll}")