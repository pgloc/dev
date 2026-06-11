def greet_user(username):
    """Wyświetla proste powitanie."""
    print(f"Witaj, {username.title()}!")

greet_user('janek')

def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowane pełne imię i nazwisko."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nProszę podać imię i nazwisko:")
    print("(wpisz 'q', aby zakończyć pracę programu w dowolnym momencie)")
    f_name = input("Imię: ")
    if f_name == 'q':
        break
    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nWitaj, {formatted_name}!")