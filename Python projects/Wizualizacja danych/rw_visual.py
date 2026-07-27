import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny.
while True:
    # Przygotowanie danych błądzenia losowego.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Wyświetlenie punktów błądzenia losowego.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Podkreślenie pierwszego i ostatniego punktu błądzenia losowego.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Ukrycie osi.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n):")
    if keep_running == 'n':
        break