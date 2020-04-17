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

print("I'm not able to attend tomorrow. -" + guests[2])

invite_followup = "thank you for your RSVP. We can't wait to see you."
declined_invites = 'Elon Musk'
guests.remove(declined_invites)

print("Dear " + guests[0].title() + ", Thank you for your RSVP. We can't wait to see you.")
print("Dear " + guests[1].title() + ", Thank you for your RSVP. We can't wait to see you.")
print("Dear " + guests[2].title() + ", Thank you for your RSVP. We can't wait to see you.")
print("Dear " + guests[3].title() + ", Thank you for your RSVP. We can't wait to see you.")


#	3-6 More Guests

#	You just found a bigger dinner table, so now more space is available. Think of three more
#	guests to invite to dinner. 
#	*	Start with your program from 3-4 or 3-5. Add a print() call to the end of your program
#		informing people that you found a bigger dinner table. 
#	* 	Use insert() to add one new guest to the beginning of your list.
#	* 	Use insert() to add one new guest to the middle of your list. 
#	* 	Use append() to add one new guest to the end of your list. 
#	* 	Print a new set of invitation messages, one for each person in your list. 

print("Dear " + guests[0].title() + ", We found a bigger table! Expect a bigger party!")
print("Dear " + guests[1].title() + ", We found a bigger table! Expect a bigger party!")
print("Dear " + guests[2].title() + ", We found a bigger table! Expect a bigger party!")
print("Dear " + guests[3].title() + ", We found a bigger table! Expect a bigger party!")

#	A better way of doing this but with loops (covered later in book). 
for guest in guests:
	print("Dear " + guest.title() + ", We found a bigger table! Expect a bigger party!")

guests.insert(0, 'Gandhi')
#	Would like to find some sort of syntax to indicate the middle of a list. Cant find one yet so 
#	doing it manually here)
guests.insert(3, 'Fa Mulan')
guests.insert(-1, 'Heddy Lamarr')

#	New invites
for guest in guests:
	print("Dear " + guest.title() + ", This invite confirms the new location for tonight's dinner.")


#	Section 3-7: Shrinking Guest List
#	You just found out that your new dinner table won't arrive in time for the dinner, and you have
#	space for only two guests. 
#	* 	Start with your program from 3-6. Add a new line that prints a message saying that you can
#		invite only two people for dinner. 
#	* 	Use pop() to remove guests from your list one at a time until only two names remain in your
#		list. Each time you pop a name from your list, print a message to that person letting them
#		know you're sorry you can't invite them to dinner. 
#	* 	Print a message to each of the two people still on your list, letting them know they're still
#		invited.
#	* 	Use del to remove the last two names from your list, so you have an empty list. Print your
#		list to make sure you actually have an empty list at the end of your program. 

uninvited_guests = guests.pop(-1)
print("I'm sorry " + uninvited_guests.title() + ", our new table hasn't arrive yet and we will \
only have space for two guests.")

uninvited_guests = guests.pop(-1)
print("I'm sorry " + uninvited_guests.title() + ", our new table hasn't arrive yet and we will \
only have space for two guests.")

uninvited_guests = guests.pop(-1)
print("I'm sorry " + uninvited_guests.title() + ", our new table hasn't arrive yet and we will \
only have space for two guests.")

uninvited_guests = guests.pop(-1)
print("I'm sorry " + uninvited_guests.title() + ", our new table hasn't arrive yet and we will \
only have space for two guests.")

uninvited_guests = guests.pop(-1)
print("I'm sorry " + uninvited_guests.title() + ", our new table hasn't arrive yet and we will \
only have space for two guests.")

#	Updating remaining guests that they are still invited
print("Dear " + guests[0].title() + ", We have room for you tonight. See you there!")
print("Dear " + guests[1].title() + ", We have room for you tonight. See you there!")

#	Removing the remaining guests wiht del per instructions. Then printing out to ensure the list 
#	is empty. 
del guests[0]
del guests[0]
print guests