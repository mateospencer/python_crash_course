page60

# Commented out all prints and loops that are not in use. 
# 4-3. Counting to Twenty: rint all numbers between 1 and 20 inclusive.
numbers = list(range(1, 21))
#print(numbers)

# 4-4. One Million: Make a list of numbers from 1 to 1mil then use a for loop to print the numbers. 
bignumbers = list(range(1, 1000001))
#for bignumber in bignumbers:
#	print(bignumber)

# 4-5. Summing a Million
#print(f"The lowest number in the million number list is {min(bignumbers)}")
#print(f"The higehst number in the million number list is {max(bignumbers)}")
# Sum is 500000500000 and takes .2 seconds. 
#print(f"Now I will add the sum of a million numbers {sum(bignumbers)}")

# 4-6. Odd Numbers
oddnums = list(range(1, 20, 2))
for oddnum in oddnums:
	print(oddnum)

# 4-7. Threes
threes = list(range(3, 30, 3))
for three in threes:
	print(three)

# 4-8. Cubes
cubeys = []
for value in range(1, 11):
	cube = value ** 3
	cubeys.append(cube)
print(cubeys)

# 4-9. Cube Comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)