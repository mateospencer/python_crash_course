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