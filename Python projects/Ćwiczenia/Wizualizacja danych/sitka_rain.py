import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pobranie dat i najwyższych temperatur z pliku.
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        rain = float(row[3])
        dates.append(current_date)
        rains.append(rain)

# Dane wykresu.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='blue')

# Formatowanie wykresu.
ax.set_title("Wielkość dziennych opadów - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Wielkość (cm)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize='16')

plt.show()