#	Python Crash Course 2nd Edition
#	Page 60 (For Loops)

#	Section 4-3: Counting to Twenty
#	Use a for loop to print the numbers from 1 to 20, inclusive. 

numbers = list(range(1, 21))
print(numbers)


#	Section 4-4: One Million
#	Make a list of the numbers from one to one million, and then use a for loop to print the 
#	numbers. (If the output is taking too long, stop it.)

bignumbers = list(range(1, 1000001))
for bignumber in bignumbers:
	print(bignumber)

#	Section 4-5: Summing a Million
#	Make a list of the numbers from one to one million, and then use min() and max() to make sure
#	your list actually starts at one and ends at one million. Also, use the sum() function to see
#	how quickly Python can add a million numbers. 

print("The lowest number in the million number list is:")
print(min(bignumbers))

print("The highest number in the million number list is:")
print(max(bignumbers))

print("The sum of all the numbers in the million number list is:")
print(sum(bignumbers))


#	Section 4-6: Odd Numbers
#	Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#	Use a for loop to print each number. 

oddnums = list(range(1, 20, 2))
for oddnum in oddnums:
	print(oddnum)


#	Section 4-7: Threes
#	Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your
#	list. 

threes = list(range(3, 30, 3))
for three in threes:
	print(three)

#	Section 4-8: Cubes
#	A number raised to the third power is called a cube. For example, the cube of 2 is written as 
#	2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1
#	through 10), and use a for loop to print out the value of each cube. 

cubeies = []
for value in range(1, 11):
	cube = value ** 3
	cubeies.append(cube)
print(cubeies)


#	Section 4-9: Cube Comprehension
#	Use a list comprehension to generate a list of the first 10 cubes. 

cubes = [value**3 for value in range(1, 11)]
print(cubes)