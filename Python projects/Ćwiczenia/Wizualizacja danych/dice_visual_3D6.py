from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Utworzenie kości typu D6.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = [die_1.roll() + die_2.roll() + die_3.roll() for value in range(1000)]

# Analiza wyników.
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]

# Wizualizacja wyników.
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania trzema kośćmi D6 tysiąc razy', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')