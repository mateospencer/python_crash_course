#	Python Crash Course 2nd Edition
#	Page 30 (Adding Comments)
#	Page 36 (Names, Greetings, Lists)

#	Section 3-1: Names
#	Store names of a few friends into a list, print each person's name by accessing each element
#	in the list, one at a time. 
friends = ['Lisa', 'Kelen', 'Bob', 'Vinnie']
print(friends[0])
print(friends[1])
print(friends[-1])
print(friends[-2])

#	Section 3-2: Greetings
#	Reuse list from above but instead of printing each person's name, print a message to them.
#	Text should be the same in each message but each message should be personalized. 
friends = ['Lisa', 'Kelen', 'Bob', 'Vinnie']
message = "where do you want to eat today?"
print(f"Hey, {friends[0]}, {message}")
print(f"Hey, {friends[1]}, {message}")
print(f"Hey, {friends[-2]}, {message}")
print(f"Hey, {friends[-1]}, {message}")

#	Section 3-3: Your Own List/Transportation
#	Make a list that stores several modes types of your favorite mode of transport. Use list to 
#	print a series of statements about these items. 
auto = ['Tesla Roadster', 'Tesla Model S', 'Tesla Model X', 'Tesla CyberTruck', 'Tesla Model 3', 'Tesla Model Y']
print(f"I'd like to own a {auto[0]} some day")
print(f"I'd like to own a {auto[1]} some day")
print(f"I'd like to own a {auto[2]} some day")
print(f"I'd like to own a {auto[3]} some day")
print(f"I'd like to own a {auto[4]} some day")
print(f"I'd like to own a {auto[5]} some day")