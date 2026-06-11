filename = 'guest.txt'
guest = input("Podaj swoje imię: ")

with open(filename, 'w') as file_object:
    file_object.write(f"{guest.title()}\n")

filename = 'guest_book.txt'
repeat = True
while repeat:
    guest = input("Podaj swoje imię (napisz 'koniec' aby zakończyć): ")

    if guest == 'koniec':
        repeat = False
    else:
        print(f"Witaj, {guest.title()}!")

        with open(filename, 'a') as file_object:
            file_object.write(f"{guest.title()}\n")