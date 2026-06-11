# Przechowywanie informacji o pizzy zamawianej przez klienta
pizza = {
    'crust': 'grubym',
    'toppings': ['pieczarki', 'podwójny ser']
}

# Podsumowanie zamówienia
print(f"Zamówiłeś pizzę na {pizza['crust']} cieście "
    "wraz z następującymi dodatkami:")

for topping in pizza['toppings']:
    print(f"\t{topping}")