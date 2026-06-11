number = input("Podaj dowolną liczbę: ")
number = int(number)

if number % 10 == 0:
    print(f"\nLiczba {number} jest podzielna przez 10.")
else:
    print(f"\nLiczba {number} nie jest podzielna przez 10.")