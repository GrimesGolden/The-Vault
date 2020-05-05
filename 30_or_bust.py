import random
# Importing random for dice functionality. 

min = 1 # Final variables for dice range, (1-6 naturally)
max = 6
score = 0 # To hold the ongoing player score.
rolls = 0 # To hold number of dice rolls.
resets = 0 # To hold number of resets due to score > 30.

name = str(input("Hello, what player name do you prefer?\n"))
# Save user input as the string "name".

print("The goal of this game, " + name + ", is to accumulate a player score of exactly 30.\n")
intro = '''You will roll a pair of dice, then you must choose the score of one of the dice or the
total of the two dice. This value is added to your player score. If your score goes over 
30, the score is reset and you continue to roll and choose. You win when you accumulate a
score of exactly 30.\n'''
print(intro)

print("Here we go!" + "\n")

while True:
	print("\n")
	die_1 = random.randint(min, max)
	die_2 = random.randint(min, max)
	temp_total = die_1 + die_2

	if score == 0:
		print("Your score: " + str(score))
		rolls += 1
	elif score > 0 and score < 30:
		print("Your total: " + str(score) + ", keep going!\n")
		rolls += 1
	elif score > 30:
		print("Your total: " + str(score) + ", your score is now reset to 0. keep going!\n")
		rolls += 1
		resets +=1
		score = 0
	elif score == 30:
		print("Your total: " + str(score) + " Congratulations, you WIN!!\n")
		print("Total rolls of the dice pair: " + str(rolls) + "\n")
		print("Total times you started over at zero: " + str(resets) + "\n")
		break

	print("Your roll: " + "\n")
	print("Die 1: " + str(die_1) + "\n")
	print("Die 2: " + str(die_2) + "\n")
	print("Total: " + str(temp_total))

	user_choice = int(input("Do you wish to (1) Keep die 1, (2) Keep die 2, (3) Keep the total? (Respond with 1 or 2 or 3): "))

	if user_choice == 1:
		score += die_1
	elif user_choice == 2:
		score += die_2
	elif user_choice == 3:
		score += temp_total











