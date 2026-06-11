filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("Uwielbiam programować.\n")
    file_object.write("Uwielbiam tworzyć nowe gry.\n")

with open(filename, 'a') as file_object:
    file_object.write("Uwielbiam odnajdywać elementy w ogromnych zbiorach danych.\n")
    file_object.write("Uwielbiam tworzyć aplikacje uruchamiane w przeglądarce internetowej.\n")