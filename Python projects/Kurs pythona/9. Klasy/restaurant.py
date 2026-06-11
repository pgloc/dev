class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurację {self.restaurant_name.title()} charakteryzuje kuchnia {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"Godziny otwarcia restauracji {self.restaurant_name.title()} to 11:00 - 22:00")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant('gurin', 'japońska')
restaurant2 = Restaurant('chicago', 'amerykańska')
restaurant3 = Restaurant('chinkali', 'gruzińska')

print(f"Restauracja: {restaurant.restaurant_name.title()}.")
print(f"Kuchnia: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

print(f"Restauracja {restaurant.restaurant_name.title()} obsłużyła {restaurant.number_served} gości.")
restaurant.set_number_served(5)
print(f"Restauracja {restaurant.restaurant_name.title()} obsłużyła {restaurant.number_served} gości.")
restaurant.increment_number_served(2)
print(f"Restauracja {restaurant.restaurant_name.title()} obsłużyła {restaurant.number_served} gości.")