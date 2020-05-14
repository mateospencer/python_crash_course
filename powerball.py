#	This simulates a Powerball Lottery drawing and ticket purchase. It was based off of an 
#	exercise within Python Crash Course 2nd Edition by Eric Matthes which simulated a simple
#	lottery drawing and analysis. There are probably better and more efficient ways of implementing
#	this but this was just a personal exercise expanding upon the original assignment. The main
#	difference here is that there is a powerball within a smaller number range than the other 
#	balls. 

#	Also note, this takes awhile to run. It's been limited to 100 million simulations so as not run
#	for too long so it may exit without a winning ticket. 

from random import choice

#	These had to be moved outside of the class definitions because at least one of them was used by
#	more than one class. They didn't all need to be here but it keeps it consistent.

#	Empty List to store the winning 
winning_numbers = []
winning_powerball = []
picked_numbers = []
picked_powerball = []

def generate_winner(numbers):
	"""Generates the winning numbers for the lottery"""
	while len(winning_numbers) < 5:
		#	Randomly select out of our list of possible letters and numbers and assign it a variable
		drawn_digit = choice(numbers)
		#	Next, will want to make sure that we don't repeat numbers
		if drawn_digit not in winning_numbers:
			#	Add the digit to the list (if not a repeat)
			winning_numbers.append(drawn_digit)
	#	Return the full list of the winning combination
	return winning_numbers

def generate_winning_powerball(powerballs):
	while len(winning_powerball) < 1:
		select_winning_powerball = choice(powerballs)
		if select_winning_powerball not in winning_numbers:
			winning_powerball.append(select_winning_powerball)

	return winning_powerball

def check_ticket(picked_numbers, winning_numbers):
	for pick in picked_numbers:
		if pick not in winning_numbers:
			return False
	return True

def check_powerball(picked_powerball, winning_powerball):
	for winner in picked_powerball:
		if winner not in winning_powerball:
			return False
	return True

def generate_ticket(numbers):
	while len(picked_numbers) < 5:
		drawn_digit = choice(numbers)
		if drawn_digit not in picked_numbers:
			picked_numbers.append(drawn_digit)
			
	return picked_numbers

def generate_powerball(powerballs, picked_numbers):
	while len(picked_powerball) < 1:
		select_powerball = choice(powerballs)
		if select_powerball not in picked_numbers:
			picked_powerball.append(select_powerball)

	return picked_powerball

numbers = range(0, 70)
powerballs = range(0, 27)
winning_numbers = generate_winner(numbers)
winning_powerball = generate_winning_powerball(powerballs)

tickets = 0
won = False
hit_powerball = False

max_tries = 100_000_000

while not won:
	new_ticket = generate_ticket(numbers)
	new_powerball = generate_powerball(powerballs, picked_numbers)
	won = check_ticket(new_ticket, winning_numbers)
	hit_powerball = check_powerball(picked_powerball, winning_powerball)
	tickets += 1
	if tickets >= max_tries:
		break

if won:
	print("We have a winner!")
	print(f"Purchased ticket: {new_ticket}")
	print(f"Purchased powerball: {new_powerball}")
	print(f"Winning ticket: {winning_numbers}")
	print(f"Winning Powerball: {winning_powerball}")
	print(f"It took {tickets} tries to win!")
else:
    print(f"Tried {tickets} times, without pulling a winner. :(")
    print(f"Purchased ticket: {new_ticket}")
    print(f"Purchased powerball: {new_powerball}")
    print(f"Winning ticket: {winning_numbers}")
    print(f"Winning powerball: {winning_powerball}")