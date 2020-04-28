#	Python Crash Course 2nd Edition
#	Page 137 (Functions and Passing Arguments)

#	Section 8-3: T-Shirt
#	Write a function called make_shirt() that accepts a size and the text of a message that should
#	be printed on the shirt. The function should print a sentence summarizing the size of the shirt
#	and the message printed on it. 
#	Call the funciton once using positional arguments to make a shirt. Call the function a second
#	time using keyword arguments. 

def make_shirt(size, text):
	"""Accepts a size and text of a message to print on a shirt."""
	print(f"\nThe size of the shirt is {size} and the printed text reads: {text}.")

#	Calling function with positional arguments
make_shirt('XL', 'supreme')

#	Calling functon using keyword arguments
make_shirt(text='All Blacks Rugby', size='large')


#	Section 8-4: Large Shirts
#	Modify the make_shirt() function so that shirts are large by default with a message that reads
#	I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of
#	any size with a different message.

def make_shirt(text='I love Python', size='large'):
	"""Accepts a size and text of a message to print on a shirt. Defaults to size large."""	
	print(f"\nThe size of the shirt is {size} and the printed text reads: {text}.")

make_shirt()
make_shirt(size='medium')
make_shirt(text='Coding in Parseltongue.')


#	Section 8-5: Cities
#	Write a function called describe_city() that accepts the name of a city and its country. The 
#	function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for
#	the country a default value. Call your function for three different cities, at least one of
#	which is not in the default country. 