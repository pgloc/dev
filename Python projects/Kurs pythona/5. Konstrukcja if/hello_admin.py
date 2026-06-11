users = ['Przemek', 'Artur', 'Monika', 'admin', 'Amelia']

if users:
    for user in users:
        if user == 'admin':
            print(f"Witaj, {user}! Czy chcesz przejrzeć dzisiejszy raport?")
        else:
            print(f"Witaj, {user}! Dziękujemy, że ponownie się zalogowałeś.")
else:
    print("Musimy znaleźć jakichś użytkowników!")

current_users = ['Przemek', 'Artur', 'Monika', 'admin', 'Amelia']
new_users = ['Radek', 'Marta', 'Przemek', 'Magda', 'Damian']

for new_user in new_users:
    if new_user in current_users:
        print("Wybrana nazwa użytkownika już istnieje.")
    else:
        print("Możesz wykorzystać wybraną nazwę użytkownika.")
        