#	Python Crash Course 2nd Edition
#	Page 181 (Python Standard Library)

#	Section 9-13: Dice
#	Make a class Die with one attribute called sides, which has a default value of 6. Write a method
#	called roll_die() that prints a random number between 1 and the number of sides the die has. 
#	Make a 6-sided die and roll it 10 times.
#	Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

#	Different sided Dice
d6 = Die()
d10 = Die(sides=10)
d20 = Die(sides=20)

#	Rolling different sided dice once
d6roll = d6.roll_die()
d10roll = d10.roll_die()
d20roll = d20.roll_die()

print("Rolling a six sided die once: " + str(d6roll))
print("Rolling a ten sided die once: " + str(d10roll))
print("Rolling a twenty sided die once: " + str(d20roll))

#	Rolling a d6 ten times
results6 = []
for roll_num in range(10):
	result = d6.roll_die()
	results6.append(result)
print("\nRolling a six sided die ten times:")
print(results6)

#	Rolling a d10 ten times
results10 = []
for roll_num in range(10):
	result = d10.roll_die()
	results10.append(result)
print("\nRolling a ten sided die ten tiems:")
print(results10)

#	Rolling a d20 ten times
results20 = []
for roll_num in range(10):
	result = d20.roll_die()
	results20.append(result)
print("\nRolling a twenty sided die ten times:")
print(results20)


#	Section 9-14: Lottery
#	Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four 
#	numbers or letters from the list and print a message saying that any ticket matching these four
#	numbers or letters wins a prize. 

from random import choice

alphanumerics = ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29", "E", "A", "R", "T", "H"]

#	This way works but doesn't ensure that repeats do not happen.
draw1 = choice(alphanumerics)
draw2 = choice(alphanumerics)
draw3 = choice(alphanumerics)
draw4 = choice(alphanumerics)
print("\nAny ticket matching the following four numbers or letters wins a prize:")
print(f"{draw1} : {draw2} : {draw3} : {draw4}")

#	A better way would be with a while loop
winning_alphanumerics = []

print("\nNow drawing tonight's lottery...")
while len(winning_alphanumerics) < 4:
	selected_alphanumeric = choice(alphanumerics)
	if selected_alphanumeric not in winning_alphanumerics:
		winning_alphanumerics.append(selected_alphanumeric)
		print(f"A {selected_alphanumeric} is drawn.")
print("The four winning selections are:" ,winning_alphanumerics)


#	Section 9-15: Lottery Analysis
#	You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make
#	a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket 
#	wins. Print a message reporting how many tiems the loop had to run to give you a winning ticket.

#	Need to admit that I went about this in a very inefficient way and had to finally look up
#	the solution in the book and follow its format. My initial approach worked very differently and 
#	needlessly complicated and messy.

from random import choice

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


#	Section 9-16: Python Module of the Week
#	One excellent resource for exploring the PYthon standard library is a site called Python Module
#	of the Week. Go to https://pymotw.com/ and look at the table of contents. Find a module that 
#	looks interesting to you and read about it, perhaps starting with the random module.