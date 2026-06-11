for value in range(1, 21):
	print(value)

million_numbers = []
for value in range(1, 1000001):
	million_numbers.append(value)
	#print(value)
#print(million_numbers)

print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

not_even = []
for value in range(1, 20, 2):
	print(value)

power_numbers = []
for value in range(3, 31):
	power_number = value**3
	power_numbers.append(power_number)
	print(power_number)

power_numbers = [value**3 for value in range(1, 11)]
print(power_numbers)