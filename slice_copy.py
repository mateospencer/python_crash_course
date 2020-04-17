#page 65.  
#4-11

pizzas = ["pepperoni", "sausage", "margherita", "veggie", "hawaiian"]
friend_pizzas = pizzas[:]

pizzas.append('meat lovers')
friend_pizzas.append('buffalo chicken')

for pizza in pizzas:
	print(f"I like {pizza} pizza.")

print(f"My favorite pizzas are: ")
for pizza in pizzas:
	print(pizza)

print(f"My friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
	print(friend_pizza)



# 4-12
my_foods = ['sushi', 'hopia baboy', 'xiao long bao', 'pho', 'korean bbq']
lisa_foods = ['sushi', 'pho', 'daikon soup', 'seaweed salad', 'ramen']

for my_food in my_foods:
	print(my_food)
for lisa_food in lisa_foods:
	print(lisa_food)