#	Python Crash Course 2nd Edition
#	Page 68 (Tuples))

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
#
# would return a type error. Whereas, you can associate a new tuple with an existing variable name 
# because reassigning a variable is valid. 
#
# e.g. 	dimensions = (200, 100)
#		print(dimensions)
#		dimensions = (100, 300)
#		print(dimensions)
#
# would print just fine. 

#	Section 4-13: Buffet
#	A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store 
#	them in a tuple. 
#	*	Use a for loop to print each food the restaurant offers.
#	*	Try to modify one of the items, and make sure that Python rejects the change. 
#	*	The restaurant changes its menu, replacing two of the items with different foods. Add a line 
#		that rewrites the tuple, and then use a for loop to print each of the items on the revised 
#		menu. 

buffet_foods = ("crab legs", "rice", "lo mein", "shrimp", "soup")

#	Print each item in for loop
for food in buffet_foods:
	print(food)

#	Modify one of the items and make sure Python rejects change
# 	Commented out so rest of code runs ok afterwards.
# 	buffet_foods[0] = "sauteed beans"

#	Adding a line that rewrites the tuple to replace two items with different foods and then uses a
# 	for loop to print each of the items on a revised menu.

buffet_foods = ("crab legs", "fried rice", "bao", "shrimp", "soup")
for food in buffet_foods:
	print(food)
