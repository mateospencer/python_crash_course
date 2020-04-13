#	Python Crash Course 2nd Edition
#	Page 84 (If Statements)

#	Section 5-3: Alien Colors #1
#	Create a variable called alien_color and assigned it a value of green, yellow, and red
#	* Write an if statement to test whether the alien's color is green. IF so, print a msg that the
#		player just earned 5 points. 

alien_color = ['green']

if 'green' in alien_color:
	print("You just earned 5 points.")

#	* Write a version of this program that passes the if test and another that fails (fails should
#	have no output.)

alien_color = ['red']

if 'red' in alien_color:
	print("You just earned 10 points.")

if 'yellow' in alien_color:
	print("You just earned 20 points.")


#	Section 5-4: Alien Colors #2
#	Choose a color for an alien as you did above and write an if-else chain. 
#	* If the alien's color is green, print that the player just earned 5 points for shooting
#		the alien. 
#	* If the alien's color isnt green, print that the player just earned 10 points. 
#	* Write one version of this program that runs the if block and another that runs the else block. 

#	Runs the if block
alien_color = ['green']

if 'green' in alien_color:
	print("You just earned 5 points for shooting the alien.")
else:
	print("You just earned 10 points.")


#	Runs the else block
alien_color = ['yellow']

if 'green' in alien_color:
	print("You just earned 5 points for shooting the alien.")
else: 
	print("You just earned 10 points.")


#	Section 5-5: Alien Colors #3
#	Turn if-else chain from 5-4 into an if-elif-else chain.
#	* If alien = green, print that player earned 5 pts. 
#	* If alien = yellow, print that player earned 10 pts.
#	* If alien = red, print that player earned 15 pts.
#	* Write three versions of program, making sure each message is printed for the appro color.

alien_color = ['red']
if 'green' in alien_color:
	print("You just earned 5 points.")
elif 'yellow' in alien_color:
	print("You just earned 10 points.")
else: 
	print("You just earned 15 points.")

alien_color = ['yellow']
if 'green' in alien_color:
	print("You just earned 5 points.")
elif 'yellow' in alien_color:
	print("You just earned 10 points.")
else: 
	print("You just earned 15 points.")

alien_color = ['green']
if 'green' in alien_color:
	print("You just earned 5 points.")
elif 'yellow' in alien_color:
	print("You just earned 10 points.")
else: 
	print("You just earned 15 points.")	


#	Section 5-6: Stages of Life
#	Write an if-elif-else chain that determines a person's stage of life. Set a value for the 
#		variable age, and then:
#	* If person is <2yo, print that the person is a baby.
#	* If >=2 but <4yo, person is a toddler
#	* If >=4 but <13yo, person is a kid
#	* If >=13 but <20yo, person is a teenager
#	* If >=20 but <65yo, person is an adult
#	* If >=65, person is an elder. 

#	Took awhile to figure out why age = 28 works but age = ['28'] does not work and it was because 
#	I wasn't writing if 'age' <2, etc. 
age = 28

if age <2 and age >0:
	print("This person is a baby.")
elif age >=2 and age <4:
	print("This person is a toddler.")
elif age >=4 and age <13:
	print("This person is a kid.")
elif age >=13 and age <20:
	print("This person is a teenager.")
elif age >=20 and age <65:
	print("This person is an adult.")
else:
	print("This person is an elder.")


#	Section 5-7: Favorite Fruit
#	Make list of favorite fruits and then write series of indepedent if statements that check for 
#	certain fruits in list. 
#	* Make list of three favorite fruits and call it favorite_fruits
#	* Write five if statements. Each should check whether a certain kind of fruit is in your list.
#		If the fruit is in your list, the if block should print a statement, such as "You really
#		like bananas!"

favorite_fruits = ['mango', 'feijoa', 'kiwi']

if 'mango' in favorite_fruits:
	print("You really like mango!")
if 'feijoa' in favorite_fruits:
	print("You really like feijoa!")
if 'kiwi' in favorite_fruits:
	print("You really like kiwi!")
if 'durian' in favorite_fruits:
	print("You really like durian.")
if 'pineapple' in favorite_fruits:
	print("You really like pineapple.")