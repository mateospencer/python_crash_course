#	Python Crash Course 2nd Edition
#	Page 89 (If Statements with Lists)

#	Section 5-8: Hello Admin
#	Make a list of five or more usernames, including the name 'admin'. Imagine you are writing
#	code that will print a greeting to each user after they log in to a website. Loop through the
#	list, and print a greeting to each user:
#	* If username is 'admin', print a special greeting, such as Hello admin, would you like to see a
#		status report?
#	* Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again. 

#	Uncertain why I ran into errors using print(f"Hello, {username}") in last line. Will research
#		later.

usernames = ['admin', 'anguyen', 'bwong', 'csato', 'ddevi', 'emwangi', 'fibrahim']

for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello " + username + ", thank you for logging in again.")


#	Section 5-9: No Users
#	Add an if test to hello_admin.py to make sure the list of users is not empty. 
#	* If the list is empty, print the message 'We need to find some users!'
#	* Remove all of the usernames from your list, and make sure the correct message is printed. 

#	With usernames
usernames = ['admin', 'gtan', 'ksmith', 'lmoyo', 'mdejong', 'nchen', 'odelacruz']

if usernames: 
	for username in usernames:
		if username == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + username + ", thank you for logging in again.")
else:
	print("We need to find some users!")

#	Without usernames
usernames = []

if usernames: 
	for username in usernames:
		if username == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + username + ", thank you for logging in again.")
else:
	print("We need to find some users!")


#	Section 5-10: Checking Usernames
#	Do the following to create a program that simulates how websites ensure that everyone has a
#		unique username.
#	* Make a list of five or more usernames called current_users
#	* Make another list of five usernames called new_users. Make sure one or two of the new
#		usernames are also in the current_users list. 
#	* Loop through the new_users list to see if each new username has already been used. If it has, 
#		print a message that the person will need to enter a new username. If a username has not 
#		been used, print a message saying that the username is available. 
#	* Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be
#		accepted. (To do this, you'll need to make a copy of current_users containing the lowercase
#		versions of all existing users.)