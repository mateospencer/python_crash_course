#	Python Crash Course 2nd Edition
#	Page 123 (While Loops)

#	Section 7-4: Pizza Toppings
#	Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit'
#	value. As they enter each topping, print a message saying you'll add that topping to their 
#	pizza.

prompt = "\nEnter your choice of pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print(f"I'll add [topping] your pizza.")