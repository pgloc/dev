from operator import itemgetter

import requests

from plotly.graph_objects import Bar
from plotly import offline

# Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Kod stanu: {r.status_code}")

# Przetworzenie informacji o każdym artykule.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Przygotowanie oddzielnego wywołania API dla każdego artykułu.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        # Utworzenie słownika dla każdego artykułu.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"<a href='http://news.ycombinator.com/item?id={submission_id}'>{response_dict['title']}</a>",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        print(f"Brak danych dla artykułu o ID: {submission_id}")

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Utworzenie wizualizacji.
data = [{
    'type': 'bar',
    'x': [submission_dict['hn_link'] for submission_dict in submission_dicts],
    'y': [submission_dict['comments'] for submission_dict in submission_dicts],
    'hovertext': [submission_dict['title'] for submission_dict in submission_dicts],
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': 'Najaktywniejsze dyskusje na Hacker News',
    'font': {'size': 28},
    'xaxis': {
        'title': 'Tytuł artykułu',
        #'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Liczba komentarzy',
        #'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='active_discussions.html')