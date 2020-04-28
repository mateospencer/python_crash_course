#	Python Crash Course 2nd Edition
#	Page 142 (Functions and Returning Values)

#	Section 8-6: City Names
#	Write a function called city_country() that takes in the name of a city and its country. The
#	function should return a string formatted like this:
#		"Santiago, Chile"
#	Call your function with at least three city-country pairs, and print the values that are 
#	returned.

def city_country(city, country):
	"""Returns a city and country neatly formatted"""
	place_names = f"{city}, {country}"
	return place_names.title()

locale1 = city_country('Wellington', 'New Zealand')
locale2 = city_country('Bali', 'Indonesia')
locale3 = city_country('Mexico City', 'Mexico')
print(locale1)
print(locale2)
print(locale3)




