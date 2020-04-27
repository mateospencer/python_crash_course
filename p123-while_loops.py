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


#	Section 7-5: Movie Tickets
#	A movie theatre charges different ticket prices depending on a person's age. If a person is
#	under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and
#	if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and
#	then tell them the cost of their movie ticket. 

prompt = "\nEnter your age and I will calculate your movie ticket price."
prompt += "\n(Enter 'quit' when you are finished.)"

age = ""
while True:
	age = input(prompt)
	if age == 'quit':
		break
	age = int(age)
	if age >= 3 and age <=12:
		print("$10")
	if age > 12:
		print("$15")
	if age <3:
		print("$0")


#	Section 7-6: Three Exits
#	Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at
#	least once:
#	*	Use a conditional test in the while statement to stop the loop. 
#	*	Use an active variable to control how long the loop runs. 
#	*	Use a break statement to exit the loop when the user enters a 'quit' value.

