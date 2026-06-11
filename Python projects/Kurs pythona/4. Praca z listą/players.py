players = ['karol', 'martyna', 'michał', 'florian', 'ela']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Oto trzech pierwszych graczy naszej drużyny:")
for player in players[:3]:
	print(player.title())

print("Pierwsze trzy elementy listy to:")
for player in players[:3]:
	print(player.title())

print("Trzy elementy w środku listy to:")
for player in players[1:4]:
	print(player.title())

print("Ostatnie trzy elementy listy to:")
for player in players[-3:]:
	print(player.title())