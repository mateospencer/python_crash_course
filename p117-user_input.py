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