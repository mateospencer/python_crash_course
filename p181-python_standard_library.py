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