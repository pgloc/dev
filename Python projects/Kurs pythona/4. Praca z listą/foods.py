my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
friend_foods = my_foods[:]

my_foods.append('cannolo')
friend_foods.append('lody')

print("Moje ulubione potrawy to:")
print(my_foods)

print("\nUlubione potrawy mojego przyjaciela to:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
#Poniższe rozwiązanie nie działa.
friend_foods = my_foods

my_foods.append('cannolo')
friend_foods.append('lody')

print("Moje ulubione potrawy to:")
for food in my_foods:
	print(food)

print("\nUlubione potrawy mojego przyjaciela to:")
for food in friend_foods:
	print(food)