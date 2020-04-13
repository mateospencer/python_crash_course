#	Python Crash Course 2nd Edition
#	Page 42

# 	Section 3-4: Guest List
#	If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list
#		that includes at least three people that you'd like to invite to dinner. Then use your list
#		to print a message to each person, inviting them to dinner. 

#	List with guests
guests = ['Barack Obama', 'Siddhartha', 'Elon Musk', 'Trevor Noah', 'Ip Man']

name = guests[0].title()
print(name + ", It would be a pleasure if you can join us over dinner.")
name = guests[1].title()
print(name + ", It would be a pleasure if you can join us over dinner.")
name = guests[2].title()
print(name + ", It would be a pleasure if you can join us over dinner.")
name = guests[3].title()
print(name + ", It would be a pleasure if you can join us over dinner.")
name = guests[4].title()
print(name + ", It would be a pleasure if you can join us over dinner.")

#	Another way that this could work:
#invite = {guests[0].title()} + "It would be a pleasure if you can join us over dinner tomorrow."
#print(invite)


#	Section 3-5: Changing Guest List
#	You just heard that one of your guests cant make the dinner, so you need to send out a new set
#		of invitations. You'll have to think of someone else to invite. 
#	* Start with your program from Exercise 3-4. Add a print() call at the end of your program
#		stating the name of the guest who can't make it. 
#	* Modify your list, replacing the name of the guest who can't make it with the name of the new
#		person you are inviting. 
#	* Print a second set of invitation messages, one for each person who is still in your list. 

#print("I'm not able to attend tomorrow but I'll be sure to make the next dinner." + {guests[2]})

invite_followup = "thank you for your RSVP. We can't wait to see you."
declined_invites = 'Elon Musk'
guests.remove(declined_invites)
#print(f"Dear {guests[0]}, {invite_followup}")
#print(f"Dear {guests[1]}, {invite_followup}")
#print(f"Dear {guests[2]}, {invite_followup}")
#print(f"Dear {guests[3]}, {invite_followup}")


# 3-6 More Guests

# Printing each line manually because I dont know how to do loops yet. Using only guests[] puts the whole list on that line.
#print(f"Dear {guests[0]}, \nWe found a bigger dinner table! Expect the party to be even bigger!")
#print(f"Dear {guests[1]}, \nWe found a bigger dinner table! Expect the party to be even bigger!")
#print(f"Dear {guests[2]}, \nWe found a bigger dinner table! Expect the party to be even bigger!")
#print(f"Dear {guests[3]}, \nWe found a bigger dinner table! Expect the party to be even bigger!")

guests.insert(0, 'Gandhi')
# would like to find some sort of syntax to indicate the middle of a list. Cant find one yet so doing it manually here)
guests.insert(3, 'Fa Mulan')
guests.insert(-1, 'Heddy Lamarr')

# new invites
#print(f"Dear {guests[0]}, \nThis invite confirms the new location for tonight's dinner.")
#print(f"Dear {guests[1]}, \nThis invite confirms the new location for tonight's dinner.")
#print(f"Dear {guests[2]}, \nThis invite confirms the new location for tonight's dinner.")
#print(f"Dear {guests[3]}, \nThis invite confirms the new location for tonight's dinner.")
#print(f"Dear {guests[4]}, \nThis invite confirms the new location for tonight's dinner.")
#print(f"Dear {guests[5]}, \nThis invite confirms the new location for tonight's dinner.")
#print(f"Dear {guests[6]}, \nThis invite confirms the new location for tonight's dinner.")


# 3-7 Shrinking Guest List
oops_message = "This is embarrassing to admit but our new table hasn't arrived yet and we will only have space for two guests. We'll add you to the top of the list for next time."

# Checking the guests before popping out
#print(guests)
uninvited_guests = guests.pop(-1)
# Checking the guests after popping out (Ipman removed)
#print(guests)
# Testing that guest was added to uninvited guests. Note: This is not a list. Pop only keeps the last popped value. Running this later won't add an additional value to 
#print(uninvited_guests)

# Printing uninvite to removed guest per instructions
# Uninviting Ip Man
#print(f"I am sorry {uninvited_guests}. {oops_message}")

# Checking guest list before removing
#print(guests)
uninvited_guests = guests.pop(-1)
# Uninviting Heddy Lamarr
#print(f"I am sorry {uninvited_guests}. {oops_message}")
#print(guests)
#print(uninvited_guests)

# Checking guest list before removing
#print(guests)
uninvited_guests = guests.pop(-1)
#Uninviting Trevor Noah
#print(f"I am sorry {uninvited_guests}. {oops_message}")

# Checking guest list before removing
#print(guests)
uninvited_guests = guests.pop(-1)
# Uninviting Fa Mulan
#print(f"I am sorry {uninvited_guests}, {oops_message}")
#print(guests)

# Checking guest list before removing
#print(guests)
uninvited_guests = guests.pop(-1)
# Uninviting Siddhartha
#print(f"I am sorry {uninvited_guests}, {oops_message}")
#print(guests)

# Updating remaining guests that they are still invited
#print(f"Dear {guests[0]}, I am pleased to tell you that we still have a seat for you at tonights event.")
#print(f"Dear {guests[1]}, I am pleased to tell you that we still have a seat for you at tonights event.")

# Removing the remaining guests wiht del per instructions. Then printing out to ensure the list is empty. 
#Running this twice since I dont know how to do loops yet. 
del guests[0]
del guests[0]
print guests
