#	Python Crash Course 2nd Edition
#	Page 56 (For Loops)

#	Section 4-1: Pizzas
#	Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and
#	then use a for loop to print the name of each pizza. 
#	*	Modify your for loop to print a sentence using the name of the pizza instead of printing
#		just the name of the pizza. For each pizza you should have one line of output containing a
#		simple statement like I like pepperoni pizza. 
#	*	Add a line at the end of your program, outside the for loop, that states how much you like 
#		pizza. The output shoudl consist of three or more lines about the kinds of pizza you like
#		and then add an additional sentence, such as I really like pizza!

pizzas = ["pepperoni", "sausage", "margherita", "veggie", "hawaiian"]
for pizza in pizzas:
	print("I like " + pizza + " pizza.")

print("\nPizza is pretty tasty.")
print("But I cant eat it too often.")
print("Its unhealthy and painful.")
print("But, " + pizzas[0] + " pizza is my favorite even if its the most basic.\n")


# 	Section 4-2: Animals
#	Think of at least three different animals that have a common characteristic. Store the naems of 
#	these animals in a list, and then use a for loop to print out the name of each animal. 
#	*	Modify your program to print a statement about each animal, such as A dog would make a great
#		pet.
#	*	Add a line at the end of your program stating what these animals have in common. You could
#		print a sentence such as Any of these aniamls would make a great pet!

birds = ["tui", "fantail", "kakapo", "kiwi"]
for bird in birds:
	print("The " + bird + " is native to New Zealand.")
print("All of these birds are not found elsewhere.")
