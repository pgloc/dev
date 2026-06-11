filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Przepraszamy, ale plik {filename} nie istnieje.")
else:
    # Obliczenie przybliżonej liczby słów w pliku.
    words = contents.split()
    num_words = len(words)
    print(f"Plik {filename} zawiera {num_words} słów.")