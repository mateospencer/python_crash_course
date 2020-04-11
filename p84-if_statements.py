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
	prnt("You just earned 20 points.")

#	Section 5-4: Alient Colors #2
#	Choose a color for an alien as you did above and write an if-else chain. 
#	* If the alien's color is green, print that the player just earned 5 points for shooting
#		the alien. 
#	* If the alien's color isnt green, print that the player just earned 10 points. 
#	* Write one version of this program that runs the if block and another that runs the else block. 

#	Runs the if block
alien_color = ['green']

if 'green' in alien_color:
	print("You just earned 5 points for shooting the alien."
else: 
	print("You just earned 10 points.")

#	Runs the else block
alien_color = ['yellow']

if 'green' in alien_color:
	print("You just earned 5 points for shooting the alien."
else: 
	print("You just earned 10 points.")