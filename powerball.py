from random import choice

winning_alphanumerics = []
winning_powerball = []
picked_alphanumerics = []
picked_powerball = []

def generate_winner(alphanumerics):
	while len(winning_alphanumerics) < 5:
		#	Randomly select out of our list of possible letters and numbers and assign it a variable
		drawn_digit = choice(alphanumerics)
		#	Next, will want to make sure that we don't repeat numbers
		if drawn_digit not in winning_alphanumerics:
			#	Add the digit to the list (if not a repeat)
			winning_alphanumerics.append(drawn_digit)
	#	Return the full list of the winning combination
	return winning_alphanumerics

def generate_winning_powerball(powerballs):
	while len(winning_powerball) < 1:
		select_winning_powerball = choice(powerballs)
		if select_winning_powerball not in winning_alphanumerics:
			winning_powerball.append(select_winning_powerball)

	return winning_powerball

def check_ticket(picked_alphanumerics, winning_alphanumerics):
	for pick in picked_alphanumerics:
		if pick not in winning_alphanumerics:
			return False
	return True

def check_powerball(picked_powerball, winning_powerball):
	for winner in picked_powerball:
		if winner not in winning_powerball:
			return False
	return True

def generate_ticket(alphanumerics):
	while len(picked_alphanumerics) < 5:
		drawn_digit = choice(alphanumerics)
		if drawn_digit not in picked_alphanumerics:
			picked_alphanumerics.append(drawn_digit)
			
	return picked_alphanumerics

def generate_powerball(powerballs, picked_alphanumerics):
	while len(picked_powerball) < 1:
		select_powerball = choice(powerballs)
		if select_powerball not in picked_alphanumerics:
			picked_powerball.append(select_powerball)

	return picked_powerball

alphanumerics = range(0, 70)
powerballs = range(0, 27)
winning_alphanumerics = generate_winner(alphanumerics)
winning_powerball = generate_winning_powerball(powerballs)

tickets = 0
won = False
hit_powerball = False

max_tries = 100_000_000

while not won:
	new_ticket = generate_ticket(alphanumerics)
	new_powerball = generate_powerball(powerballs, picked_alphanumerics)
	won = check_ticket(new_ticket, winning_alphanumerics)
	hit_powerball = check_powerball(picked_powerball, winning_powerball)
	tickets += 1
	if tickets >= max_tries:
		break

if won:
	print("We have a winner!")
	print(f"Purchased ticket: {new_ticket}")
	print(f"Purchased powerball: {new_powerball}")
	print(f"Winning ticket: {winning_alphanumerics}")
	print(f"Winning Powerball: {winning_powerball}")
	print(f"It took {tickets} tries to win!")
else:
    print(f"Tried {tickets} times, without pulling a winner. :(")
    print(f"Purchased ticket: {new_ticket}")
    print(f"Purchased powerball: {new_powerball}")
    print(f"Winning ticket: {winning_alphanumerics}")
    print(f"Winning powerball: {winning_powerball}")