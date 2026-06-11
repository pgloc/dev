requested_topping = 'pieczarki'

if requested_topping != 'anchois':
    print("Proszę o anchois!")

requested_topping = ['pieczarki', 'podwójny ser']

if 'pieczarki' in requested_topping:
    print("Dodaję pieczarki.")
if 'pepperoni' in requested_topping:
    print("Dodaję pepperoni.")
if 'podwójny ser' in requested_topping:
    print("Dodaję podwójny ser.")

print("\nTwoja pizza jest już gotowa!")

requested_topping = ['pieczarki', 'podwójny ser']

if 'pieczarki' in requested_topping:
    print("Dodaję pieczarki.")
elif 'pepperoni' in requested_topping:
    print("Dodaję pepperoni.")
elif 'podwójny ser' in requested_topping:
    print("Dodaję podwójny ser.")

print("\nTwoja pizza jest już gotowa!")

requested_toppings = ['pieczarki', 'boczek', 'podwójny ser']

for requested_topping in requested_toppings:
    if requested_topping == 'boczek':
        print("Przepraszamy, ale obecnie nie mamy boczku.")
    else:
        print(f"Dodaję {requested_topping}.")

print("\nTwoja pizza jest już gotowa!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Dodaję {requested_topping}.")
    print("\nTwoja pizza jest już gotowa!")
else:
    print("Czy jesteś pewien, że chcesz pizzę bez dodatków?")

available_toppings = ['pieczarki', 'oliwki', 'boczek', 'pepperoni', 'ananas',
                      'podwójny ser']

requested_toppings = ['pieczarki', 'frytki', 'podwójny ser']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Dodaję {requested_topping}.")
    else:
        print(f"Przepraszamy, ale obecnie nie mamy dodatku {requested_topping}.")

print("Twoja pizza jest już gotowa!")