prompt = "Proszę podać wiek: "

while True:
    age = input(prompt)

    if age == 'koniec':
        break
    else:
        age = int(age)
        if age < 3:
            print("Bilet jest bezpłatny.")
        elif 3 <= age <= 12:
            print("Cena biletu wynosi 10 zł.")
        else:
            print("Cena biletu wynosi 15 zł.")