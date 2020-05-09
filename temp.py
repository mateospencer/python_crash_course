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
	while len(winning_alphanumerics) <4:
		#	Randomly select out of our list of possible letters and numbers and assign it a variable
		drawn_digit = choice(alphanumerics)
		#	Next, will want to make sure that we don't repeat numbers
		if drawn_digit not in winning_alphanumerics:
			#	Add the digit to the list (if not a repeat)
			winning_alphanumerics.append(winning_alphanumerics)
	#	Return the full list of the winning combination
	return(winning_alphanumerics)



