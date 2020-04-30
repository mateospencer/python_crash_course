#	Python Crash Course 2nd Edition
#	Page 150 (Arbitrary Number of Arguments)

#	Section 8-12: Sandwiches
#	Write a function that accepts a list of items a person wants on a sandwich. The function should
#	have one parameter that collects as many items as the function call provides, and it should
#	print a summary of the sandwich that's being ordered. Call the function three times, using a 
#	different number of arguments each time. 

def make_sandwich(*toppings):
	print(toppings)

make_sandwich('bacon', 'lettuce', 'tomato',)
make_sandwich('peanut butter', 'jelly',)
make_sandwich('cheese')


#	Section 8-13: User Profiles
#	Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling
#	build_profile(), using your first and last names and three other key-value pairs that describe
#	you. 

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('mateo', 'spencer', city='wellington', country='new zealand', 
	title='lead data scientist')
print(user_profile)


#	Section 8-14: Cars
#	Write a function that stores information about a car in a dictonary. The function should always
#	receive a manufacturer and a model name. It should then accept an arbitrary number of keyword
#	arguments. Call the function with the required information and two other name-value pairs, such
#	as a color or an option feature. Your function should work for a call like this one:
#		car = make_car('subaru', 'outback', color='blue', tow_package=True)
#	Print the dictionary that's returned to make sure all the information was stored correctly. 

def cars(make, model, **car_info):
	return car_info
	car_info['manufacturer'] = make
	car_info['model_name'] = model
car_details = cars('Tesla', 'Model S', color='Black', package='Long Range')

print(car_details)