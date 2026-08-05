import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    index = 0
    for header in header_row:
        if header == 'NAME':
            name_index = index
        if header == 'DATE':
            date_index = index
        if header == 'TMAX':
            highs_index = index
        if header == 'TMIN':
            lows_index = index
        index += 1

    # Pobranie dat i najwyższych temperatur z pliku.
    dates, highs, lows = [], [], []
    for row in reader:
        station = row[name_index]
        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        high = int(row[highs_index])
        low = int(row[lows_index])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Dane wykresu.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatowanie wykresu.
ax.set_title(f"Najwyższa i najniższa temperatura dnia\nw {station} - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.set_ylim(20, 140)
ax.tick_params(axis='both', which='major', labelsize='16')

plt.show()