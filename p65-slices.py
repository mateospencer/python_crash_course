#	Python Crash Course 2nd Edition
#	Page 65 (Slices)

#	Section 4-10: Slices
#	Using one of the programs you wrote in this chapter, add several lines to the end of the program
#	that do the following:
#	*	Print the message The first three items in the list are:. Then use a slice to print the
#		first three items from that program's list.
#	*	Print the message Three items from the middle of the list are:. Use a slice to print three
#		items from the middle of the list. 
#	*	Print the message The last three items in the list are:. Use a slice to print the last three
#		items in the list. 

birds = ["tui", "fantail", "kakapo", "kiwi", "kaka"]

#	Print first three
print("The first three items in the list are:")
for bird in birds[:3]:
	print(bird.title())

#	Print middle three
#	Print middle three (theres probably a better way of doing this than manually calculating the 
#	three middle numbers in the range)
print("The middle three items in this list are:")
for bird in birds[1:4]:
	print(bird.title())

#	Print last three
print("The last three items in this list are:")
for bird in birds[-3:]:
	print(bird.title())

#	Section 4-11: My Pizzas, Your Pizzas
#	Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call
#	it friend_pizzas. Then, do the following:
#	*	Add a new pizza to the original list.
#	*	Add a different pizza to the list friend_pizzas.
#	*	Prove that you have two separate lists. Print the message My favorite pizzas are:, and then
#		use a for loop to print the first list. Print the message My friend's favorite pizzas are:,
#		and then use a for loop to print the second list. Make sure each new pizza is stored in the 
#		approprpiate list. 

pizzas = ["pepperoni", "sausage", "margherita", "veggie", "hawaiian"]
friend_pizzas = pizzas[:]

pizzas.append('meat lovers')
friend_pizzas.append('buffalo chicken')

for pizza in pizzas:
	print(f"I like {pizza} pizza.")

print(f"My favorite pizzas are: ")
for pizza in pizzas:
	print(pizza)

print(f"My friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
	print(friend_pizza)



# 4-12
my_foods = ['sushi', 'hopia baboy', 'xiao long bao', 'pho', 'korean bbq']
lisa_foods = ['sushi', 'pho', 'daikon soup', 'seaweed salad', 'ramen']

for my_food in my_foods:
	print(my_food)
for lisa_food in lisa_foods:
	print(lisa_food)