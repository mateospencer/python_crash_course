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

def make_album(artist_name, album_title, tracks=None):
	"""Returns neatly formatted information about a music album"""
	album = {'artist': artist_name, 'album': album_title}
	if tracks:
		album['tracks'] = tracks
	return album

album1 = make_album('The Roots', 'The Roots Come Alive')
album2 = make_album('A Tribe Called Quest', 'Midnight Marauders')
album3 = make_album('Mos Def', 'Black on Both Sides')
album4 = make_album('Nas', 'Illmatic', '10')
print(album1)
print(album2)
print(album3)
print(album4)


#	Section 8-8: User Albums
#	Start with your program from Exercise 8-7. Write a while loop that allows uers to enter an 
#	album's artist and title. Once you have that information, call make_album() with the user's
#	input and print the dictionary that's created. Be sure to include a quit value in the while
#	loop. 

def make_album(artist_name, album_title, tracks=None):
	"""Returns neatly formatted information about a music album"""
	album = {'artist': artist_name, 'album': album_title}
	if tracks:
		album['tracks'] = tracks
	return album

while True:
	print("\nEnter an artist's name:")
	print("(enter 'q' at any time to quit)")

	musician = input("Artist's name: ")
	if musician == 'q':
		break
	record = input("Album Name: ")
	if record == 'q':
		break

	make_album = make_album(musician, record)
	print(f"\n {make_album}")
