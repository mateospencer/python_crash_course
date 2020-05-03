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

class IceCreamStand(Restaurant):
	"""Represents a Ice Cream Stand"""

	def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
		"""Initialize attributes of parent class and those specific to Ice Cream Stands"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def display_flavors(self):
		"""Displays the flavor of ice cream at the Ice Cream Stand"""
		print("\nThe following ice cream flavors are available:")
		for flavor in self.flavors:
			print(f"{flavor.title()}")

icecreamstand1 = IceCreamStand('The Hyppo')
icecreamstand1.flavors = ['horchata', 'coffee', 'caramel', 'dulce de leche', 'thai tea']

icecreamstand1.describe_restaurant()
icecreamstand1.display_flavors()


#	Section 9-7: Admin
#	An administrator is a special kind of user. Write a class called Admin that inherits from the
#	User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute,
#	privileges, that stores a list of strings like "can add post", "can delete post", 
#	"can ban user", and so on. Write a method called show_privileges() that lists the
#	administrator's set of privileges. Create an instance of Admin, and call your method. 

class User:
	"""A class for simulated user profile details"""
	def __init__(self, first_name, last_name, email, title):
		"""Initializing attributes"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.email = email
		self.title = title.title()
		self.login_attempts = 0

	def describe_user(self):
		print(f"User's Name: {self.first_name} {self.last_name}")
		print(f"Email: {self.email}")
		print(f"Title: {self.title}")

	def greet_user(self):
		"""Greets user by username"""
		print(f"\nKia ora, {self.first_name}!")

	def increment_login_attempts(self):
		"""Enables incrementing the number of login attempts by the user via a method"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Resets login attempts back to zero"""
		self.login_attempts = 0

class Admin(User):
	"""A class for admin profile attributes"""
	def __init__(self, first_name, last_name, email, title):
		"""Initializing attributes of parent class and those for Admin"""
		super().__init__(first_name, last_name, email, title)
		self.privileges = []

	def show_privileges(self):
		"""Lists the administrator's set of privileges."""
		print("\nThe Administrator has the following privileges:")
		for privilege in self.privileges:
			print(f"{privilege}")

admin_user = Admin('Admin', 'Istrator', 'admin@website.co.nz', 'Admin')
admin_user.privileges = ['create user', 'delete user', 'reset password', 'ban user']

admin_user.describe_user()
admin_user.show_privileges()


#	Section 9-8: Privileges
#	Write a separate Privileges class. The class should have one attribute, privileges, that stores
#	a list of strings as described in Exercise 9-7. Move teh show_privileges() method to this class.
#	Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin 
#	and use your method to show its privileges.