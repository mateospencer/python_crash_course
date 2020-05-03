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

	def set_number_served(self, customer_count):
		"""Allows updating the number of customers of the restaurant via a method"""
		self.number_served = customer_count

	def increment_number_served(self, additional_customers):
		"""Enables incrementing the number of customers of the restaurant via a method"""
		self.number_served += additional_customers

restaurant = Restaurant('La Tapatia', 'Mexican')
print(restaurant.number_served)

restaurant.number_served = 314
print(restaurant.number_served)


#	Section 9-5: Login Attempts
#	Add an attribute called login_attempts to your User calss from Exercise 9-3 (page 162). Write a 
#	method called increment_login_attempts() that increments the value of login_attempts by 1. 
#	Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
#	Make an instance of the User class  and call increment_login_attempts() several times. Print 
#	the value of login_attempts to make sure it was incremented properly, and then call
#	reset_login_attempts(). Print login_attempts again to make sure it was reset to 0. 

class User:
	"""A class for simulated user profile details"""
	def __init__(self, first_name, last_name):
		"""Initializing first and last name attributes"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()

	def describe_user(self):
		user_details = f"User's Name: {self.first_name} {self.last_name}"
		print(f"\n{user_details}")

	def greet_user(self):
		print(f"\nKia ora, {self.first_name}!")

restaurant.set_number_served(592)
print(restaurant.number_served)

restaurant.increment_number_served(65)
print(restaurant.number_served)
