import random

#Greetings
name = input("What is your name?")
print("Hello,"+ name + "!")

#Dice Game
roll_dice1 = random.randint(1,6)
roll_dice2 = random.randint(1,6)
total = roll_dice1 + roll_dice2
print("Rolling dice...")
print(f"Die 1: {(roll_dice1)}")
print(f"Die 2: {(roll_dice2)}")
print(f"Total value: {(total)}")

#Won/lost message added
if total > 7:
    print( name + " win")
else:
    print( name + " lost")
