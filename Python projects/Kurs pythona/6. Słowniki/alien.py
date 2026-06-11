alien_0 = {'color': 'zielony', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"Zdobyłeś {new_points} punktów!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'zielony'
alien_0['point'] = 5
print(alien_0)

print(f"Obcy ma kolor {alien_0['color']}.")
alien_0['color'] = 'żółty'
print(f"Obcy ma teraz kolor {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'średnio'}
print(f"Początkowa wartość x-position: {alien_0['x_position']}")

# Przesunięcie obcego w prawo
# Ustalenie odległości, jaką powinien pokonać obcy poruszający się z daną szybkością

if alien_0['speed'] == 'wolno':
    x_increment = 1
elif alien_0['speed'] == 'średnio':
    x_increment = 2
else:
    # To musi być szybki obcy
    x_increment = 3

# Nowe położenie to suma dotychczasowego położenia i wartości x_increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Nowa wartość x-position: {alien_0['x_position']}")

alien_0 = {'color': 'zielony', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)