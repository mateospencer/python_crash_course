#	This is a temp work space to ensure that code runs and to pull up alongside other code. 

#	Section 9-15: Lottery Analysis
#	You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make
#	a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket 
#	wins. Print a message reporting how many tiems the loop had to run to give you a winning ticket.


from random import choice

#	need to break problem down into parts. 


#	Need to create a class for getting the winning numbers. Could reuse existing code but best to
#	approach this with a class to do the work

#	Need another class to generating a random entry ticket. 

#	Need a class to check the entry ticket against the winning numbers. 

def generate_winner(alphanumerics):
	"""Generates the winning numbers for the lottery"""
	#	First an empty list to store the numbers
	winning_alphanumerics = []
	
	#	Using a while loop to make sure it loops until we have four numbers. 
	while len(winning_alphanumerics) < 4:
		#	Randomly select out of our list of possible letters and numbers and assign it a variable
		drawn_digit = choice(alphanumerics)
		#	Next, will want to make sure that we don't repeat numbers
		if drawn_digit not in winning_alphanumerics:
			#	Add the digit to the list (if not a repeat)
			winning_alphanumerics.append(drawn_digit)
	#	Return the full list of the winning combination
	return winning_alphanumerics

def check_ticket(picked_alphanumerics, winning_alphanumerics):
	for pick in picked_alphanumerics:
		if pick not in winning_alphanumerics:
			return False

	return True

def generate_ticket(alphanumerics):
	picked_alphanumerics = []

	while len(picked_alphanumerics) <4:
		drawn_digit = choice(alphanumerics)
		if drawn_digit not in picked_alphanumerics:
			picked_alphanumerics.append(drawn_digit)
			
	return picked_alphanumerics

alphanumerics = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 'E', 'A', 'R', 'T', 'H']
winning_alphanumerics = generate_winner(alphanumerics)

tickets = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
	new_ticket = generate_ticket(alphanumerics)
	won = check_ticket(new_ticket, winning_alphanumerics)
	tickets += 1
	if tickets >= max_tries:
		break

if won:
	print("We have a winner!")
	print(f"Purchased ticket: {new_ticket}")
	print(f"Winning ticket: {winning_alphanumerics}")
	print(f"It took {tickets} tries to win!")
else:
    print(f"Tried {tickets} times, without pulling a winner. :(")
    print(f"Purchased ticket: {new_ticket}")
    print(f"Winning ticket: {winning_alphanumerics}")





