#	Python Crash Course 2nd Edition
#	Page 78 (Conditional Tests)


#	Section 5-1: Conditional Tests
#	Write series of conditional tests. Print a statement describing each test and yoru prediction 
#	for the results of each test. Create 10 tests and have five tests evaluate to True and five 
#	to False. 
astronaut = 'Armstrong'
print("Is Armstrong an Astronaut? The answer should be True.")
print(astronaut == 'Armstrong')

visited_countries = ['US', 'NZ', 'CA', 'MX', 'JM']
print("Is the US a country that I've visited? The answer should be True.")
print('US' in visited_countries)

family_members = ['isidro uy', 'isabella uy', 'lisa uy', 'mateo michael']
print("Is Isidro Uy a family member? The answer should be True.")
print('isidro uy' in family_members)

wife_age = 35
husband_age = 37
print("Is anyone old enough to be President? The answer should be True.")
print(wife_age >= 35 or husband_age >= 35)

delicious_foods = ['sushi', 'hopia baboy', 'boba tea', 'xiao long bao', 'korean bbq']
print("Is sushi a delicious food? The answer should be True.")
print('sushi' in delicious_foods)

daughter_age = 5
son_age = 1
print("Is either child old enough to vote? The answer should be False.")
print(daughter_age >= 18 or son_age >= 18)

print("Are all the children old enough for primary school? The answer should be False.")
print(daughter_age >= 5 and son_age >= 5)

print("Are any of the children old enough to drive? The answer should be False.")
print(daughter_age >= 16 or son_age >= 16)

print("Are any of the children teenagers? The answer should be False.")
print(daughter_age >= 13 or son_age >= 13)

print("Are any of the children considered infants? The answer should be False.")
print(daughter_age < 1 or son_age < 1)


#	Section 5-2: More Conditional Tests
