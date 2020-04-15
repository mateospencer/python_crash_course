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

current_users = ['pgonzalez', 'qquispe', 'rmori', 'sinthavong', 'tali']
new_users = ['rmori', 'tali', 'ujonsdottir', 'vborg', 'wrossi']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user in current_users:
		print("Sorry, the username '" + new_user + "' is unavailable. Please enter a new username.")
	else:
		print("The username '" + new_user + "' is avaiable. Thank you for your registering.")


#	Section 5-11: Ordinal Numbers
#	Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end
#		in th, expect 1, 2, and 3. 
#	* Store the numbers 1 through 9 in a list.
#	* Loop through the list
#	* Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
#		Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on 
#		a separate line.

list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in list:
	if number == '1':
		print("1st")
		#If the goal was to append the ending on every value, could use print(list[0] + "st").
	elif number == '2':
		print("2nd")
	elif number == '3':
		print("3rd")
	else:
		print(number + "th")