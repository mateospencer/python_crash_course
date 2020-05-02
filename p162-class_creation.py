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
