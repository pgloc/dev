rivers = {
    'nil': 'egipt',
    'amazonka': 'brazylia',
    'wisła': 'polska'
}

for river, country in rivers.items():
    print(f"{river.title()} przepływa przez kraj {country.title()}")

for river in rivers:
    print(river.title())

for country in rivers.values():
    print(country.title())