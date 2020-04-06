# 3-8 Seeing the world

# Countries that I'd like to visit. 
locations = ["Vietnam", "Japan", "Cuba", "France", "Malaysia", "Fiji", "Indonesia"]

# Printing list in original order
print(locations)

# Printing with sorted() to print in alphabetical order w/o modifying original list
print(sorted(locations))

# Showing that the original list did not change with sorted()
print(locations)

# Reverse alphabetical order with sorted(). This was not in book but I got it work. 
print(sorted(locations, reverse=True))

# Again showing that the original list did not change with sorted()
print(locations)

# Using reverse to change the original order then printing to show the change
# Worth remembering here the difference b/t functions and methods. Methods alter object states. Functions operate on them and return something. So things like sort() and reverse() are methods and sorted() is a function.
locations.reverse()
print(locations)

# now reversing back again
locations.reverse()
print(locations)

# Sorting list to alphabetical order (and changing original)
locations.sort()
print(locations)

# Sorting in reverse alphabetical order
locations.sort(reverse=True)
print(locations)

# 3-9 Switching up the exercise to use on this problem.
print(f"There are {len(locations)} locations in my travel bucket list.")

# 3-10 Every Function
# States where I've lived
states = ["West Virginia", "Maryland", "Virginia", "Wisconsin", "Pennslyvania"]
print(f"I have lived in {len(states)} states of the United States.")
print(f"States where I lived in, listed only in the order that I originally typed them: {states}")
print(f"The states where I have lived in alphabetical order: {sorted(states)}")
print(f"The states where I lived in reverse alphabetical order {sorted(states, reverse=True)}")
# Changing the original list to be permanently alphabetical.
states.sort()
print(states)
