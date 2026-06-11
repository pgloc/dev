alien_0 = {'color': 'zielony', 'points': 5}
alien_1 = {'color': 'żółty', 'points': 10}
alien_2 = {'color': 'czerwony', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Utworzenie pustej listy przeznaczonej do przechowywania obcych
aliens = []

# Utworzenie 30 zielonych obcych
for alien_number in range(30):
    new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'zielony':
        alien['color'] = 'żółty'
        alien['points'] = 10
        alien['speed'] = 'średnio'
    elif alien['color'] == 'żółty':
        alien['color'] = 'czerwony'
        alien['points'] = 15
        alien['speed']= 'szybko'

# Wyświetlenie pierwszych pięciu obcych
for alien in aliens[:5]:
    print(alien)
print("...")

# Wyświetlenie całkowitej liczby utworzonych obcych
print(f"Całkowita liczba obcych: {len(aliens)}")