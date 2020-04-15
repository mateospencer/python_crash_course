#	Python Crash Course 2nd Edition
#	Page 89 (If Statements with Lists)

#	Section 3-8: Seeing the World
#	Think of at least five places int he world you'd like to visit. 
#	* Store the locations in a list. Make sure the list is not in alphabetical order.
#	* Print your list in its original order. Don't worry about printing the list neatly, just print
#		it as a raw Python list. 
#	* Use sorted() to print your list in alphabetical order without modifying the actual list.
#	* Show that your list is still in its original order by printing it. 
#	* Use sorted() to print your list in reverse alphabetical order without changing the order of
#		the original list. 
#	* Show that your list is still in its original order by printing it again. 
#	* Use reverse() to change the order of your list. Print the list to show that its order has 
#		changed. 
#	* Use reverse() to change the order of your list again. Print the list to show it's back to its 
#		original order
#	* Use sort() to change your list so it's stored in alphabetical order. Print the list to show
#		that its order has been changed. 
#	* Use sort() to change your list so it's stored in reverse alphabetical order. Print the list to
#	 	show that its order has changed."


#	Countries that I'd like to visit. 
locations = ["Vietnam", "Japan", "Cuba", "France", "Malaysia", "Fiji", "Indonesia"]

#	Printing list in original order
print(locations)

#	Printing with sorted() to print in alphabetical order w/o modifying original list
print(sorted(locations))

#	Showing that the original list did not change with sorted()
print(locations)

#	Reverse alphabetical order with sorted(). This was not in book but I got it work. 
print(sorted(locations, reverse=True))

#	Again showing that the original list did not change with sorted()
print(locations)

#	Using reverse to change the original order then printing to show the change. Worth remembering 
#		here the difference b/t functions and methods. Methods alter object states. Functions 
#		operate on them and return something. So things like sort() and reverse() are methods and 
#		sorted() is a function.
locations.reverse()
print(locations)

#	Reversing back again
locations.reverse()
print(locations)

#	Sorting list to alphabetical order (and changing original)
locations.sort()
print(locations)

#	Sorting in reverse alphabetical order
locations.sort(reverse=True)
print(locations)


#	Section 3-9: Dinner Guests
#	I switched up the exercise to use 3-8 instead of 3-4 thru 3-7 as directed. Did this to stay
#		related to code already here.
#	Use len() to print a message indicating the number of people you are inviting to dinner. 
print(f"There are " + {len(locations)} + " locations in my travel bucket list.")


#	Section 3-10: Every Function
#	Think of something you could store in a list. Write a program that creates a list containing
#		these items and then uses each function introduced in this chapter at least once. 

#	States where I've lived
states = ["West Virginia", "Maryland", "Virginia", "Wisconsin", "Pennslyvania"]

print("I have lived in " + {len(states)} + " states of the United States.")
print("States where I lived in, listed only in the order that I originally typed them:" + {states})
print("The states where I have lived in alphabetical order:" + {sorted(states)})
print("The states where I lived in reverse alphabetical order:" + {sorted(states, reverse=True)})
# Changing the original list to be permanently alphabetical.
states.sort()
print(states)
