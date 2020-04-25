#	Python Crash Course 2nd Edition
#	Page 112 (Nesting)

#	Section 6-7: People
#	Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries
#	representing different people, and store all three dictionaries in a list called people. Loop
#	through your list of people. As you loop through the list, print everything you know about each
#	person. 

person_0 = {'first_name': 'Jacinda', 'last_name': 'Ardern', 'age': '39', 'city': 'Wellington',}
person_1 = {'first_name': 'Barack', 'last_name': 'Obama', 'age': '58', 'city': 'Washington',}
person_2 = {'first_name': 'Justin', 'last_name': 'Trudeau', 'age': '48', 'city': 'Ottawa',}

people = [person_0, person_1, person_2]

for person in people:
	print("\nFull Name: " + person['first_name'] + " " + person['last_name'])
	print("Age: " + person['age'])
	print("City: " + person['city'])


#	Section 6-8: Pets
#	Make several dictionaries, where each dictionary respresents a different pet. In each
#	dictionary include the kind of animal and the owner's name. Store these dictionaries in a list 
#	called pets. Next, loop through your list and as you do, print everything you know about each 
#	pet. 

pet_0 = {'type': 'dog', 'pet_name': 'Bo', 'owner': 'Barack',}
pet_1 = {'type': 'cat', 'pet_name': 'Socks', 'owner': 'Chelsea',}
pet_2 = {'type': 'dog', 'pet_name': 'Sunny', 'owner': 'Michelle',}

pets = [pet_0, pet_1, pet_2]

print("\nPresidential Pets")
for pet in pets:
	print("Pet Name: " + pet['pet_name'])
	print("Animal Type: " + pet['type'])
	print("Owner: " + pet['owner'] + "\n")


#	Section 6-9: Favorite Places
#	Make a dicontary called favorite_places. Think of three names to use as keys in the dictonary, 
#	and store one to three favorite places for each person. To make this exercise a bit more
#	interesting, ask some friends to name a few of their favorite places. Loop through the
#	dictionary, and print each person's name and their favorite places. 

favorite_places = {
	'matt': ['maui', 'new zealand',],
	'kelen': ['jamaica', 'miami',],
	'awori': ['kenya', 'ireland', 'paris',],
	}

for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")


#	Section 6-10: Favorite Numbers
#	Modify our program from Exercise 6-2 (page 99) so each person can have more than one favorite
#	number. Then print each person's name along with their favorite number. 

fav_numbers = {
	'Bella': ['5','3'], 
	'Sid': ['2', '1',], 
	'Lisa': ['6', '7',],
	'Matt': ['11','7',], 
	'Kelen': ['14','23',],
	}

for person, numbers in fav_numbers.items():
	print(f"\n{person.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")


#	Section 6-11: Cities
#	Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
#	Create a dictionary of information about each city and include the country that the city is in,
#	its approximate population, and one fact about that city. The keys for each city's dictionary
#	should be something like country, population, and fact. Print the name of each city and all of
#	the information you have stored about it. 

