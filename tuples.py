# Tuples
# Values that dont change are called immutables. Immutable lists are called Tuples. 
# 
# A list looked like this:     values = [1,20,5,6] etc. 
# A tuple looks similiar:      values = (4, 200)
# 
# Accessing values is the same regardless if a tuple or a list. e.g. print(values[0])
#
# A tuple of a single value requires a trailign comma. e.g. age = (28,)
#
# Immutable lists cant have values altered: 
# e.g.  dimensions = (200, 40)
#		dimensions[0] = 300
# would return a type error. Whereas, youc an associate a new tuple with an existing variable name because reassigning a variable is valid. 
# e.g. 	dimensions = (200, 100)
#		print(dimensions)
#		dimensions = (100, 300)
#		print(dimensions)
# would print just fine. 

# 4-13: Buffet


buffet_foods = ("crab legs", "rice", "lo mein", "shrimp", "soup")

# Q1 Print each item in for loop
for food in buffet_foods:
	print(food)

# Q2 Try to modify one of the items and make sure Python rejects change
# Commented out so rest of code runs ok afterwards.
# buffet_foods[0] = "sauteed beans"

# Q3 Add a line that rewrites the tuple to replace two items with different foods and then uses a for loop to print each of the items on a revised menu.
# This is quite simple and essentially the same code as before with different items assigned to variable. 

buffet_foods = ("crab legs", "fried rice", "bao", "shrimp", "soup")
for food in buffet_foods:
	print(food)
