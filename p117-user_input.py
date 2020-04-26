#	Python Crash Course 2nd Edition
#	Page 117 (User Input)

#	Section 7-1: Rental Car
#	Write a program that asks the user what kind of rental car they would like. Print a message
#	about that car, such as "Let me see if I can find you a Subaru."

#car_choice = input("What type of rental car would you like? ")
#print("I'll see if we have a " + car_choice +  " available.")

car_choice = input("What type of rental car would you like? ")
print(f"\nI'll see if we have a {car_choice} available.")


#	Section 7-2: Restaurant Seating
#	Write a program that asks the user how many people are in their dinner group. If the answer is
#	more than eight, print a message saying they'll have to wait for a table. Otherwise, report that
#	their table is ready. 

dinner_group = input("\nHow many people are in your dinner group? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
	print("I'm sorry. You will have to wait for a table.")
else:
	print(f"\nYour table for {dinner_group} guests is ready.")


#	Section 7-3: Multiples of Ten
#	Ask the user for a number, and then report whether the number is a multiple of 10 or not. 
