#	Python Crash Course 2nd Edition
#	Page 99 (Dictionaries)

#	Section 6-1: Person
#	Use a dictionary to store information about a person you know. Store their first name, last
#		name, age, and the city in which tye live. You should have keys such as first_name, 
#		last_name, age, and city. Print each piece of information stored in your dictionary

person_0 = {'first_name': 'Jacinda', 'last_name': 'Ardern', 'age': '39', 'city': 'Wellington',}

print(person_0['first_name'])
print(person_0['last_name'])
print(person_0['age'])
print(person_0['city'])


#	Section 6-2: Favorite Numbers
#	Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys
#		in your dictionary. Think of a favorite number for each person, and store each as a value in
#		your dictionary. Print each person's name and their favorite number.

fav_numbers = {'Bella': '5', 'Sid': '2', 'Lisa': '6', 'Matt': '11', 'Kelen': '14',}

print("Bella's favorite number is " + fav_numbers['Bella'] + ".")
print("Sid's favorite number is " + fav_numbers['Sid'] + ".")
print("Lisa's favorite number is " + fav_numbers['Lisa'] + ".")
print("Matt's favorite number is " + fav_numbers['Matt'] + ".")
print("Kelen's favorite number is " + fav_numbers['Kelen'] + ".")

