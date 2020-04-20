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

numbers = list(range(1, 21))
#	Print first three

print(f"The first three numbers are {numbers[0:3]}")
#	Print middle three (theres probably a better way of doing this than manually calculating the 
#	three middle numbers in the range)

print(f"The three middle numbers are {numbers[9:12]}")

#	Print last three
print(f"The last three numbers are {numbers[-3:]}")
