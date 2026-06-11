favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python'
}

language = favorite_languages['sara'].title()
print(f"Ulubiony język programowania Sary to {language}.")

for name, language in favorite_languages.items():
    print(f"Ulubiony język programowania użytkownika {name.title()} to {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

friends = ['paweł', 'sara']
for name in favorite_languages.keys():
    print(f"Witaj, {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tWitaj, {name.title()}! Widzę, że Twoim ulubionym językiem programowania jest {language}!")

if 'elżbieta' not in favorite_languages.keys():
    print("Elżbieta, proszę, weź udział w naszej ankiecie!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, dziękujemy za udział w ankiecie.")

print("W ankiecie zostały wymienione następujące języki programowania:")
for language in favorite_languages.values():
    print(language.title())

print("W ankiecie zostały wymienione następujące języki programowania:")
for language in set(favorite_languages.values()):
    print(language.title())

people = ['paweł', 'sara', 'elżbieta', 'urszula']

for name in favorite_languages.keys():
    if name in people:
        print(f"{name.title()}, dziękujemy za zaangażowanie!")
    else:
        print(f"{name.title()}, proszę, weź udział w ankiecie.")

favorite_languages = {
    'janek': ['python', 'ruby'],
    'sara': ['c'],
    'edward': ['ruby', 'go'],
    'paweł': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\nUlubione języki programowania użutkownika {name.title()} to:")
    for language in languages:
        print(f"\t{language.title()}")