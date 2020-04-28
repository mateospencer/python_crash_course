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


#	Section 8-7: Album
#	Write a function called make_album() that builds a dictionary describing a music album. The 
#	function should take in an artist name and an album title, and it should return a dictionary
#	containing these two pieces of information. Use the function to make three dictionaries
#	representing different albums. Print each return value to show that the dictionaries are storing
#	the album information correctly. 
#	Use None to add an optional parameter to make_album() that allows you to store the number of
#	songs on an album. If the calling line includes a value for the number of songs, add that value
#	to the album's dictionary. Make at least one new function call that includes the number of songs
#	on an album. 

