#	Python Crash Course 2nd Edition
#	Page 167 (Working with Classes and Instances)

#	Section 9-4: Number Served
#	Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with
#	a default value of 0. Create an instance called restaurant from this class. Print the number of
#	customers the restaurant has served, and then change this value and print it again. 
#	Add a method called set_number_served() that lets you set the number of customers that have been
#	served. Call this method with a new number and print the value again. 
#	Add a method called increment_number_served() that lets you increment the number of customers
#	who've been served. Call this method with any number you like that could represent how many
#	customers were served in, say, a day of business. 

class Restaurant:
	"""A simple class representing restaurant details"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant name and cuisine type attributes"""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Prints info about the restaurant."""
		details = f"{self.restaurant_name} is a {self.cuisine_type} restaurant."
		print(f"\n{details}")

	def open_restaurant(self):
		"""Prints a message statin that the restaurant is open."""
		open = f"{self.restaurant_name} is now open."
		print(f"\n{open}")