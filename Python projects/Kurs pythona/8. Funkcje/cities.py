def city_country(city, country):
    formatted_name = f"{city}, {country}"
    return formatted_name.title()

cities = city_country('warszawa', 'polska')
print(cities)

cities = city_country('berlin', 'niemcy')
print(cities)

cities = city_country('paryż', 'francja')
print(cities)