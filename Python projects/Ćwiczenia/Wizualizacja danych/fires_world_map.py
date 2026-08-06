import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pobranie danych o pożarach z pliku.
    lats, lons, brightnesses, hover_texts = [], [], [], []
    for row in reader:
        try:
            lat = float(row[0])
            lon = float(row[1])
            brightness = float(row[2])
        except ValueError:
            print(f"Brak danych dla wiersza: {row}.")
        else:
            lats.append(lat)
            lons.append(lon)
            brightnesses.append(brightness)
            hover_texts.append(f"Siła pożaru: {brightness}")

# Mapa pożarów.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/25 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Siła pożaru'},
    },
}]

my_layout = Layout(title="Pożary na świecie - dane z ostatnich 24 godzin")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')