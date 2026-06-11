#Wielkość liter w imionach
first_name = "eryk"
print(f"Witaj, {first_name.title()}! Czy chcesz dzisiaj poznawać Pythona?")

first_name = "monika"
print(first_name.upper())
print(first_name.lower())
print(first_name.title())

first_name = "albert"
last_name = "einstein"
famous_person = f"{first_name.title()} {last_name.title()}"
quote = '"Osoba, która nigdy nie popełniła błędu, jest kimś, kto nigdy nie próbował niczego nowego"'
message = f"{famous_person} powiedział kiedyś: {quote}."
print(message)

first_name = "\tMonika\n"
print(first_name)
print(first_name.rstrip())
print(first_name.lstrip())
print(first_name.strip())