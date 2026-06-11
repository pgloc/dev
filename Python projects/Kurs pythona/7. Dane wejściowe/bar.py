sandwich_orders = ['kanapka z tuńczykiem', 'kanapka z pastrami', 'kanapka z szynką', 'kanapka z pastrami', 'kanapka z serem', 'kanapka z pastrami']
finished_sandwiches = []

print("W barze skończyło się pastrami")
while 'kanapka z pastrami' in sandwich_orders:
    sandwich_orders.remove('kanapka z pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Przygotowano {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nZrobione kanapki:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())