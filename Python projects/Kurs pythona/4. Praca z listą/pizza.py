pizza = ['pepperoni', 'margerita', 'hawajska']
for one_pizza in pizza:
	print(f"Lubię pizzę {one_pizza}.")

print(f"Naprawdę uwielbiam pizzę!")

friend_pizzas = pizza[:]

pizza.append('wiejska')
friend_pizzas.append('góralska')

print("Moje ulubione rodzaje pizzy to:")
for one_pizza in pizza:
	print(one_pizza.title())

print("\nUlubione rodzaje pizzy mojego przyjaciela to:")
for one_pizza in friend_pizzas:
	print(one_pizza.title())