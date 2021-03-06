#	Python Crash Course 2nd Edition
#	Page 162 (Creating and Using Classes)

#	Section 9-1: Restaurant
#	Make a class called Restaurant. The __init__() method for Restaurant should store two
#	attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant()
#	that prints these two pieces of information, and a method called open_restaurant() that prints
#	a message indicating that the restaurant is open. 
#	Make an instance called restaurant from your class. Print the two attributes individually, and
#	then call both methods. 

class Restaurant:
	"""A simple class representing restaurant details"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant name and cuisine type attributes"""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Prints info about the restaurant."""
		details = f"{self.restaurant_name} is a {self.cuisine_type} restaurant."
		print(f"\n{details}")

	def open_restaurant(self):
		"""Prints a message statin that the restaurant is open."""
		open = f"{self.restaurant_name} is now open."
		print(f"\n{open}")

restaurant1 = Restaurant('Daikoku','Japanese')
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()


#	Section 9-2: Three Restaurants
#	Start with your class from Exercise 9-1. Create three different instances from the class, and 
#	call describe_restaurant() for each instance. 

restaurant2 = Restaurant('Sikaku@Bubble', 'Boba Tea')
restaurant3 = Restaurant('Kenyan Cafe', 'Kenyan')
restaurant4 = Restaurant('Yama', 'Japanese')

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()


#	Section 9-3: Users
#	Make a class called User. Create two attributes called first_name and last_name, and then create
#	several other attributes that are typically stored in a user profile. Make a method called
#	describe_user() that prints a summary of the user's information. Make another method called 
#	greet_user() that prints a personalized greeting to the user. 
#	Create several instances representing different users, and call both methods for each user. 

class User:
	"""A class for simulated user profile details"""
	def __init__(self, first_name, last_name, email, title):
		"""Initializing attributes"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.email = email
		self.title = title.title()

	def describe_user(self):
		print(f"User's Name: {self.first_name} {self.last_name}")
		print(f"Email: {self.email}")
		print(f"Title: {self.title}")

	def greet_user(self):
		print(f"\nKia ora, {self.first_name}!")

user1 = User('Rt Hon Jacinda', 'Ardern', 'jacinda@beehive.govt.nz', 'Prime Minister')
user2 = User('Sir Edmund', 'Hillary', 'edmund@mountaintop.gov.nz', 'Explorer')
user3 = User('Tenzing', 'Norgay', 'tenzing@mountaintop.gov.nz', 'Explorer')

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
