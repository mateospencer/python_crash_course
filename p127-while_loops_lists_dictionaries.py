#	Python Crash Course 2nd Edition
#	Page 127 (While Loops with Lists and Dictionaries)

#	Section 7-8: Deli
#	Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make
#	an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a 
#	message for each order, such as I made your tuna sandiwch. As each sandwich is made, move it to
#	the list list of finished sandwiches. After all the sandwiches have been made, print a message 
#	listing each sandwich that was made.

sandwich_orders = ['dagwood', 'mountaineer', 'popeye']
finished_sandwiches = []

while sandwich_orders: 
	current_order = sandwich_orders.pop()

	print(f"Making order: {current_order.title()}")
	finished_sandwiches.append(current_order)

#	Displaying finished orders
print("\nThe following sandiwch orders have been made:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())


#	Section 7-9: No Pastrami
#	Using the list sandwich_orders from Exercise 7-8, make sure the sandiwch 'pastrami' appears in
#	the list at least three times. Add code near the beginning of your program to print a message
#	saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of
#	'pastrami' from sandwich_orders. Make sure no pastrami sandwichesend up in finished_sandwiches.
