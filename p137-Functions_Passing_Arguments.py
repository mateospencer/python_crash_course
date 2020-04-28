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