responses = []

polling_active = True

while polling_active:
    response = input("Jeżeli mógłbyś odwiedzić jedno dowolne miejsce na świecie, gdzie byś pojechał? ")
    responses.append(response.title())

    repeat = input("Czy ktokolwiek inny chce wziąć udział w ankiecie? (tak / nie) ")
    if repeat == 'nie':
        polling_active = False

print("\n--- Wyniki ankiety ---")
for response in responses:
    print(response.title())