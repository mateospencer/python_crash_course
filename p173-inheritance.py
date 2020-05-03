#	Python Crash Course 2nd Edition
#	Page 173 (Inheritance)

#	Section 9-6: Ice Cream Stand
#	An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that
#	inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4
#	(page 167). Either version of the class will work; just pick the one you like better. Add an 
#	attribute called flavors that stores a list of ice cream flavors. Write a method that displays
#	these flavors. Crate an instance of IceCreamStand, and call this method. 

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

	def set_number_served(self, customer_count):
		"""Allows updating the number of customers of the restaurant via a method"""
		self.number_served = customer_count

	def increment_number_served(self, additional_customers):
		"""Enables incrementing the number of customers of the restaurant via a method"""
		self.number_served += additional_customers