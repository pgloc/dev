guests = ['Marta Witkowska', 'Radosław Gloc', 'Barbara Gloc']
print(f"Zapraszam {guests[0]} na uroczysty obiad.")
print(f"Zapraszam {guests[1]} na uroczysty obiad.")
print(f"Zapraszam {guests[2]} na uroczysty obiad.")

print(f"Na obiad nie przyjdzie {guests[1]}.")
guests[1] = 'Magdalena Gloc'

print(f"Zapraszam {guests[0]} na uroczysty obiad.")
print(f"Zapraszam {guests[1]} na uroczysty obiad.")
print(f"Zapraszam {guests[2]} na uroczysty obiad.")

print(f"Znalazłem większy stół!")

guests.insert(0, 'Monika Gloc')
guests.insert(2, 'Andrzej Gloc')
guests.append('Damian Witkowski')

print(f"Zapraszam {guests[0]} na uroczysty obiad.")
print(f"Zapraszam {guests[1]} na uroczysty obiad.")
print(f"Zapraszam {guests[2]} na uroczysty obiad.")
print(f"Zapraszam {guests[3]} na uroczysty obiad.")
print(f"Zapraszam {guests[4]} na uroczysty obiad.")
print(f"Zapraszam {guests[5]} na uroczysty obiad.")

print(f"Zapraszam {len(guests)} osób.")

print(f"Mogę zaprosić tylko dwie osoby")

guest_minus = guests.pop()
print(f"Przepraszam nie mogę zaprosić {guest_minus} na obiad.")
guest_minus = guests.pop()
print(f"Przepraszam nie mogę zaprosić {guest_minus} na obiad.")
guest_minus = guests.pop()
print(f"Przepraszam nie mogę zaprosić {guest_minus} na obiad.")
guest_minus = guests.pop()
print(f"Przepraszam nie mogę zaprosić {guest_minus} na obiad.")

print(f"Zapraszam {guests[0]} na uroczysty obiad.")
print(f"Zapraszam {guests[1]} na uroczysty obiad.")

del guests[0]
del guests[0]

print(guests)
